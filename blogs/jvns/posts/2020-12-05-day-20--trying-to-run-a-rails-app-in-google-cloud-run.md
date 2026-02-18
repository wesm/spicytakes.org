---
title: "Day 20: trying to figure out how Google Cloud IAM works"
date: 2020-12-05
url: https://jvns.ca/blog/2020/12/05/day-20--trying-to-run-a-rails-app-in-google-cloud-run/
slug: day-20--trying-to-run-a-rails-app-in-google-cloud-run
word_count: 921
---


Hello! I spent all day on Friday trying to run a Rails app in Google Cloud run
and I partially succeeded, so I wanted to write down the main points I found
confusing.


### Google Cloud’s IAM is different from AWS IAM


I’ve worked with AWS IAM a lot, and GCP’s IAM seems pretty different. The way
I’m used to IAM working in AWS is:

1. You create an IAM role for a service/machine/whatever
2. You give permissions to that IAM role (like “this role can access this S3 bucket”)
3. That’s it


As far as I can tell, with Google Cloud both the terminology used in IAM and
the way it works is different.


Here are the mappings (as far as I can tell) from GCP IAM concepts to AWS IAM concepts

- an “IAM role” in Google Cloud is like a “permission” in AWS (NOT like an AWS
IAM role). So for example `roles/cloudsql.client` lets you access SQL instances
- a “service account” in Google Cloud is kiiiind of like a “IAM role” in AWS –
it’s the identity of a service. I think there are some pretty significant
differences though.


So “IAM role” in GCP and “IAM role” in AWS have completely different meanings.
Cool, that’s fine, we can work with that.


### how to assign a GCP IAM role to a service account


Like I said before, assigning an AWS permission to an AWS IAM role is pretty
simple ([here’s the terraform to do
it](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy).


I thought it would be the same in GCP (“just assign a role to a service
account”), but it’s completely different.


Instead of there being 1 single way to assign a permission to an identity (like
“this service can do X and Y and Z”), the way you give a service
account access to a resource is different depending on the kind of resource.


For example. Let’s say I want to give my service account access to a secret.
Here’s the command line incantation to do that:


```
gcloud beta secrets add-iam-policy-binding rails-master-key
--member=serviceAccount:refrigerator-poetry@refrigerator-poetry.iam.gserviceaccount.com
--role=roles/secretmanager.secretAccessor ```

```


or in Terraform:


```
resource "google_secret_manager_secret_iam_binding" "binding" {
  project   = "refrigerator-poetry"
  secret_id = google_secret_manager_secret.railsmaster.secret_id
  role      = "roles/secretmanager.secretAccessor"
  members = [
    "serviceAccount:${google_service_account.fridge.email}"
  ]
}

```


The general gcloud command line rule here seems to be (from [the GCP documentation on granting access](https://cloud.google.com/iam/docs/granting-changing-revoking-access#granting-gcloud-manual)):


```
gcloud GROUP add-iam-policy-binding RESOURCE --member=MEMBER --role=ROLE-ID

```


Okay, this isn’t what I’d hoped for (a single JSON file or something where I
can specify everything my service account can access), but at least there’s a
pattern. We can work with that!


### ok, so what if we want to give a service account access to a SQL database?


I used the above approach to give my service account access to the secrets it
needed access to. Hooray!


Next I wanted to give a service account access to a SQL database. The pattern from before is:


```
gcloud GROUP add-iam-policy-binding RESOURCE --member=MEMBER --role=ROLE-ID

```


which seems like it should translate to something like


```
gcloud sql instances add-iam-policy-binding my-db --member=serviceAccount:my-account@whatever --role=roles/cloudsql.client

```


But it doesn’t. `gcloud sql instances add-iam-policy-binding` doesn’t exist,
and `gcloud sql add-iam-policy-binding` doesn’t exist either. So it seems like
if you want to give access to a SQL instance, you need to do something
different.


At this point it was like 11:30PM so I gave up and granted my service account
very broad permissions on the project (`roles/editor`) because I just wanted to
get something to work.


Here’s what I ran:


```
gcloud projects add-iam-policy-binding  PROJECT_NAME \
                              --member=serviceAccount:account-email@whatever --role=roles/editor

```


and that worked! I still don’t know the correct way to grant access to a SQL
instance but that’s a fight for another day. At least I know you need to do
something different than for other types of resources.


### the terraform IAM resources are apparently generated with ERB


I spent many hours with Kamal trying to understand how this works, and  he went
and figured out how the Terraform resources that assign roles to service
accounts work. I was really surprised by this so here it is!


In the GCP Terraform provider, there are dozens of different resources to
assign a role to an identity, one for each different kind of GCP resource. (in
contract with AWS, where it’s just `aws_iam_role`, `aws_iam_policy`, `aws_iam_role_policy`).


Here are just a few.


```
google_folder_iam_binding
google_healthcare_dataset_iam_binding
google_healthcare_dicom_store_iam_binding
google_healthcare_fhir_store_iam_binding
google_iap_tunnel_iam_binding
google_iap_tunnel_instance_iam_binding
google_iap_web_backend_service_iam_binding
google_iap_web_iam_binding
google_iap_web_type_compute_iam_binding
google_kms_crypto_key_iam_binding
google_kms_key_ring_iam_binding
google_project_iam_binding

```


So if you want to give a service account access to a `google_iap_web_backend`
(whatever that is), you use a `google_iap_web_backend_service_iam_binding`.
Okay!


But there are all of these almost identical things, so how are they generated?
As promised in the section heading, it seems to be a bunch of Go code templated
with ERB.


Kamal did a bunch of digging and found [this ERB
template](https://github.com/GoogleCloudPlatform/magic-modules/blob/22a8a466e091d76deddccbd363717635a7264cf0/third_party/terraform/utils/provider.go.erb#L314-L321)
which generates a giant Go program that defines all these resources. So I guess
that’s how they generate a lot of resources that are very similar.


### I still don’t really understand how this works


My guess is that there are some upsides to the GCP approach to identity
management that I don’t understand yet – I’ve only used it for like 4 hours
and I’ve spent a LOT more time using AWS IAM.


But I still don’t really understand how to use it – I feel like there should
be a way to define “here are all the things this service account is allowed to
do” in a single place, but I haven’t found it yet. Maybe I’ll figure it out
soon!
