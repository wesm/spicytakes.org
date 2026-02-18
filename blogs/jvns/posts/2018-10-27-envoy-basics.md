---
title: "Some Envoy basics"
date: 2018-10-27
url: https://jvns.ca/blog/2018/10/27/envoy-basics/
slug: envoy-basics
word_count: 1743
---


[Envoy](https://www.envoyproxy.io/) is a newish network proxy/webserver in the same universe as HAProxy and nginx. When I first
learned about it around last fall, I was pretty confused by it.


There are a few kinds of questions one might have about any piece of software:

- how does do you use it?
- why is it useful?
- how does it work internally?


I’m going to spend most of my time in this post on “how do you use it?”, because I found a lot of
the basics about how to configure Envoy very confusing when I started. I’ll explain some of the
Envoy jargon that I was initially confused by (what’s an SDS? XDS? CDS? EDS?  ADS? filter? cluster?
listener? help!)


There will also be a little bit of “why is it useful?” and nothing at all about the internals.


### What’s Envoy?


Envoy is a network proxy. You compile it, you put it on the server that you want the, you tell it
which configuration file to use it, and away you go!


Here’s probably the simplest possible example of using Envoy. The configuration file is [a gist](https://gist.githubusercontent.com/jvns/340e4d20c83b16576c02efc08487ed54/raw/1ddc3038ed11c31ddc70be038fd23dddfa13f5d3/envoy_config.json).
This example starts a webserver on port 7777 that proxies to another HTTP server on port 8000.


If you have Docker, you can try it now – just download the configuration, start the Envoy docker
image, and away you go!


```
python -mSimpleHTTPServer & # Start a HTTP server on port 8000
wget https://gist.githubusercontent.com/jvns/340e4d20c83b16576c02efc08487ed54/raw/1ddc3038ed11c31ddc70be038fd23dddfa13f5d3/envoy_config.json
docker run --rm --net host -v=$PWD:/config envoyproxy/envoy /usr/local/bin/envoy -c /config/envoy_config.json

```


This will start an Envoy HTTP server, and then you can make a request to Envoy! Just `curl localhost:7777` and it’ll proxy the request to `localhost:8000`.


### Envoy basic concepts: clusters, listeners, routes, and filters


This small tiny
[envoy_config.json](https://gist.githubusercontent.com/jvns/340e4d20c83b16576c02efc08487ed54/raw/1ddc3038ed11c31ddc70be038fd23dddfa13f5d3/envoy_config.json)
we just ran contains all the basic Envoy concepts!


First, there’s a **listener**. This tells Envoy to bind to a port, in this case 7777:


```
"listeners": [{
  "address": { 
     "socket_address": { "address": "127.0.0.1", "port_value": 7777 } 

```


Next up, the listener has **filters**. Filters tell the listener what to do with the requests it receives,
and you give Envoy an array of filters. If you’re doing something complicated typically you’ll apply
several filters to every requests coming in.


There are a few different kinds of filters ([see list of TCP filters](https://www.envoyproxy.io/docs/envoy/v1.8.0/api-v2/api/v2/listener/listener.proto#listener-filter)), but the most important filter is probably the `envoy.http_connection_manager` filter, which is used for proxying HTTP requests. The HTTP connection manager has a further list of HTTP filters that it applies ([see list of HTTP filters](https://www.envoyproxy.io/docs/envoy/v1.8.0/api-v2/config/filter/network/http_connection_manager/v2/http_connection_manager.proto#envoy-api-msg-config-filter-network-http-connection-manager-v2-httpfilter)). The most important of those is the `envoy.router` filter which routes requests to the right backend.


In our example, here’s how we’ve configured our filters. There’s one TCP filter
(`envoy.http_connection_manager`) which uses 1 HTTP filter (`envoy.router`)


```
"filters": [
 {
   "name": "envoy.http_connection_manager",
   "config": {
     "stat_prefix": "ingress_http",
     "http_filters": [{ "name": "envoy.router", "config": {} }],
....

```


Next, let’s talk about **routes**. You’ll notice that so far we haven’t explained to the
`envoy.router` filter what to **do** with the requests it receives. Where should it proxy them? What
paths should it match? In our case, the answer to that question is going to be “proxy all requests
to localhost:8000”.


The `envoy.router` filter is configured with an array of routes. Here’s how they’re configured in
our test configuration. In our case there’s just one route.


```
"route_config": {
  "virtual_hosts": [
    {
      "name": "blah",
      "domains": "*",
      "routes": [
        {
          "match": { "prefix": "/" },
          "route": { "cluster": "banana" }

```


This gives a list of domains to match (these are matched against the requests Host header).  If we
changed `"domains": "*"` to `"domains": "my.cool.service"`, then we’d need to pass the header `Host: my.cool.service` to get a response.


If you’re paying attention to the ongoing saga of this configuration, you’ll notice that the port
`8000` hasn’t been mentioned anywhere. There’s just `"cluster": "banana"`. What’s a cluster?


Well, a **cluster** is a collection of address (IP address / port) that are the backend for a
service. For example, if you have 8 machines running a HTTP service, then you might have 8 hosts in
your cluster. Every service needs its own cluster. This example cluster is really simple: it’s just
a single IP/port, running on localhost.


```
  "clusters":[
    {
      "name": "banana",
      "type": "STRICT_DNS",
      "connect_timeout": "1s",
      "hosts": [
        { "socket_address": { "address": "127.0.0.1", "port_value": 8000 } }
      ]
    }
  ]

```


### tips for writing Envoy configuration by hand


I find writing Envoy configurations from scratch pretty time consuming – there are some examples in
the Envoy repository ([https://github.com/envoyproxy/envoy)](https://github.com/envoyproxy/envoy)), but even after using Envoy for a year
this basic configuration actually took me 45 minutes to get right. Here are a few tips:

- Envoy has 2 different APIs: the v1 and the v2 API. Many newer features are only available in the
v2 API, and I find its documentation a little easier to navigate because it’s automatically
generated from protocol buffers. (eg the Cluster docs are generated from [cds.proto](https://github.com/envoyproxy/envoy/blob/master/api/envoy/api/v2/cds.proto))
- A few good starting points in the Envoy API docs: [Listener](https://www.envoyproxy.io/docs/envoy/v1.8.0/api-v2/api/v2/lds.proto#envoy-api-msg-listener), [Cluster](https://www.envoyproxy.io/docs/envoy/v1.8.0/api-v2/api/v2/cds.proto#cluster), [Filter](https://www.envoyproxy.io/docs/envoy/v1.8.0/api-v2/api/v2/listener/listener.proto#envoy-api-msg-listener-filter),  [Virtual Host](https://www.envoyproxy.io/docs/envoy/v1.8.0/api-v2/api/v2/route/route.proto#envoy-api-msg-route-virtualhost). To get all the information you need you need to click a lot (for example to see how to configure the cluster for a route you need to start at “Virtual Host” and click route_config -> virtual_hosts -> routes -> route -> cluster), but it works.
- The [architecture overview docs](https://www.envoyproxy.io/docs/envoy/v1.8.0/intro/arch_overview/arch_overview) are useful and give an overall explanation of how some Envoy things are configured.
- You can use either json or yaml to configure Envoy. Above I’ve used JSON.


### You can configure Envoy with a server


Even though we started with a configuration file on disk, one thing that makes Envoy really
different from HAProxy or nginx is that Envoy often **isn’t configured with a configuration file**.
Instead, you can configure Envoy with one or several configuration **servers** which dynamically
change your configuration.


To get an idea of why this might be useful: imagine that you’re using Envoy to load balance requests
to 50ish backend servers, which are EC2 instances that you periodically rotate out. So
[http://your-website.com](http://your-website.com) requests go to Envoy, and get routed to an Envoy *cluster*, which needs to
be a list of the 50 IP addresses and ports of those servers.


But what if those servers change over time? Maybe you’re launching new ones or they’re getting
terminated. You could handle this by periodically changing the Envoy configuration file and
restarting Envoy. Or!! You could set up a “cluster discovery service” (or “CDS”), which for example
could query the AWS API and return all the IPs of your backend servers to Envoy.


I’m not going to get into the details of how to configure a discovery service, but basically it
looks like this (from [this template](https://github.com/envoyproxy/envoy/blob/master/configs/envoy_service_to_service_v2.template.yaml)). You tell it how often to refresh and what the address of the server is.


```
dynamic_resources:
  cds_config:
    api_config_source:
      cluster_names:
      - cds_cluster
      refresh_delay: 30s
...
  - name: cds_cluster
    connect_timeout: 0.25s
    type: STRICT_DNS
    lb_policy: ROUND_ROBIN
    hosts:
    - socket_address:
        protocol: TCP
        address: cds.yourcompany.net
        port_value: 80

```


### 4 kinds of Envoy discovery services


There are 4 kinds of resources you can set up discovery services for Envoy – routes (“what cluster
should requests with this HTTP header go to”), clusters (“what backends does this service have?”),
listener (the filters for a port), and endpoints. These are called RDS, CDS, LDS, and EDS
respectively. [XDS](https://github.com/envoyproxy/data-plane-api/blob/master/XDS_PROTOCOL.md) is the
overall protocol.


The easiest way to write a discovery service from scratch is probably in Go using the
[go-control-plane](https://github.com/envoyproxy/go-control-plane) library.


### some Envoy discovery services


It’s definitely possible to write Envoy configuration services from scratch, but there are some
other open source projects that implement Envoy discovery services. Here are the ones I know about,
though I’m sure there are more:

- There’s an open source Envoy discovery service called [rotor](https://github.com/turbinelabs/rotor) which looks interesting. The company that built it just [shut down](https://blog.turbinelabs.io/turbine-labs-is-shutting-down-and-our-team-is-joining-slack-2ad41554920c) a couple weeks ago.
- [Istio](https://istio.io/) (as far as I understand it) is  basically an Envoy discovery service
that uses information from the Kubernetes API (eg the services in your cluster) to configure Envoy
clusters/routes. It has its own configuration language.
- consul might be adding support for Envoy (see [this blog post](https://www.hashicorp.com/blog/consul-1-2-service-mesh)), though I don’t fully understand
the status there


### what’s a service mesh?


Another term that I hear a lot is “service mesh”. Basically a “service mesh” is where you install
Envoy on the same machine as every one of your applications, and proxy all your network requests
through Envoy.


Basically it gives you more easily control how a bunch of different applications (maybe written in
different programming languages) communicate with each other.


### why is Envoy interesting?


I think these discovery services are really the exciting thing about Envoy. If all of your network
traffic is proxied through Envoy and you control all Envoy configuration from a central server, then
you can potentially:

- use [circuit breaking](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/circuit_breaking)
- route requests to [only close instances](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/load_balancing#zone-aware-routing)
- encrypt network traffic end-to-end
- run controlled code rollouts (want to send only 20% of traffic to the new server you spun up? okay!)


all without having to change any application code anywhere. Basically it’s a very powerful/flexible
decentralized load balancer.


Obviously setting up a bunch of discovery services and operating them and using them to configure
your internal network infrastructure in complicated ways is a lot more work than just “write an
nginx configuration file and leave it alone”, and it’s probably more complexity than is appropriate
for most people. I’m not going to venture into telling you who should or should not use Envoy, but
my experience has been that, like Kubernetes, it’s both very powerful and very complicated.


### other exciting things about Envoy: timeout headers and metrics


One of the things I really like about Envoy is that you can pass it a HTTP header to tell it how to
retry/timeout your requests!! This is amazing because implementing timeout / retry logic correctly
works differently in every programming language and people get it wrong ALL THE TIME. So being able
to just pass a header is great.


The timeout & retry headers are documented [here](https://www.envoyproxy.io/docs/envoy/latest/configuration/http_filters/router_filter#http-headers-consumed), and here are my favourites:

- `x-envoy-max-retries`: how many times to retry
- `x-envoy-retry-on`: which failures to retry (eg `5xx` or `connect-failure`)
- `x-envoy-upstream-rq-timeout-ms`: total timeout
- `x-envoy-upstream-rq-per-try-timeout-ms`: timeout per retry


### that’s all for now


I have a lot of thoughts about Envoy (too many to write in one blog post!), so maybe I’ll say more
later!
