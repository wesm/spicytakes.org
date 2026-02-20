---
title: "Security Lessons Learned From The Diaspora Launch"
date: 2010-09-22
url: https://www.kalzumeus.com/2010/09/22/security-lessons-learned-from-the-diaspora-launch/
slug: security-lessons-learned-from-the-diaspora-launch
word_count: 2616
---


Last week, [Diaspora](http://www.joindiaspora.com) — the OSS privacy-respecting social network — released a “pre-alpha developer preview” of their [source code](http://www.github.com/diaspora/diaspora).  I took a look out it, mostly out of curiosity, and was struck by numerous severe security errors.  I then spent the next day digging through their code locally and trying to get in touch with the team to address them, privately.  In the course of this, I mentioned obliquely that the errors existed on Hacker News, and subsequently was interviewed by [The Register](http://www.theregister.co.uk/2010/09/16/diaspora_pre_alpha_landmines/) and got quoted in a couple of hundred places.


The money quote most outlets went for was:


> The bottom line is currently there is nothing that you cannot do to someone’s Diaspora account, absolutely nothing.


I’d like to back up that contention, now that it is safe(r) to do so.


Reporting security bugs is a funny business: any description of the error sufficient to resolve it is probably sufficient to create exploit code.  This is why I was fairly circumspect about the exact mechanism for the errors, and why Steve Klabnik also mostly [declined to give specifics](http://blog.steveklabnik.com/trouble-with-diaspora) when describing the state of the codebase.  Since the specific errors I reported are now patched, I’m going to disclose what they were, so that budding Rails developers who care about security do not inadvertently give attackers the ability to do anything they want.


By the way, if you’re looking for Rails security advice, I recommend the [official guide](http://guides.rubyonrails.org/security.html) and the [OWASP list of web application vulnerabilities](http://www.owasp.org/index.php/Top_10_2007), which would have helped catch all of these.  Web application security is a **very deep topic**, and often involves unforeseen circumstances caused by the interaction of complicated parts which are not totally under the developers’ control.  That said, **nobody** should be making errors like these.  It hurts us as developers, it hurts our ecosystem, and it endangers our users in spite of the trust they have put in us.


I found somewhere in the ballpark of a half-dozen critical errors — it depends on how you count pervasive mistakes that undermined virtually every class in the system.  There were three main genres.  All code samples are pulled from Diaspora’s source at launch, were reported to the Diaspora team immediately, and have been reported to me as fixed.


## Authentication != Authorization: The User Cannot Be Trusted


**Code**:


This basic pattern was repeated several times in Diaspora’s code base: security-sensitive actions on the server used the params hash to identify pieces of data they were to operate on, without checking that the logged in user was actually authorized to view or operate on that data. For example, if you were logged in to a Diaspora seed and knew the ID of any photo on the server, changing the URL of any destroy action from the ID of a photo you own to an ID of any other photo would let you delete that second photo. Rails makes exploits like this child’s play, since URLs to actions are trivially easy to guess and object IDs “leak” all over the place. **Do not assume** than an object ID is private.


(There is a second error here, by the way: the code doesn’t check to see if the destroy action is called by an HTTP POST or not. This means that an overenthusiastic browser might follow all links from a page, including the GET link to a delete action, and nuke the photo without any user action telling it to do so.)


You might think “Surely Diaspora checks to see if you’re logged in, right?” You’re right: they use Devise, a library which handles **authentication**, to verify that you can only get to the destroy action if you’re logged in. However, Devise does not handle **authorization** — checking to see that you are, in fact, permitted to do the action you are trying to do.


**Impact:**


When Diaspora shipped, an attacker with a free account on any Diaspora node had, essentially, full access to any feature of the software vis-a-vis someone else’s account. That’s **pretty bad**, but it gets even better when you combine it with other errors.


**How to avoid this:**


Check authorization prior to sensitive actions. The easiest way to do this (aside from using a library to handle it for you) is to take your notion of a logged in user and only access members through that. For example, in my software, any action past a login screen has access to a @user variable. If an action needs to access one of their print_jobs, it calls @user.print_jobs.find(params[:id]). If they have subverted the params hash, that will find no print_job (because of how associations scope to the user_id) and they’ll instantly generate an ActiveRecord exception, stopping any potential nastiness before it starts.


## Mass Assignment Will Ruin Your Day


**Code**:


Alright, so we know that if we forget authorization then we can do arbitrary bad things to people. In this case, since the user update method is insecured, we can meddle with their profiles. But is that all we can do?


Unseasoned developers might assume that an update method can only update things on the web form prior to it. For example, this form is fairly benign, so maybe all someone can do with this bug is deface my profile name and email address:


This is **catastrophically wrong**.


Rails by default uses something called “mass update”, where update_attributes and similar messages accept a hash as input and sequentially call all accessors for symbols in the hash. Objects will update both database columns (or their MongoDB analogues) and also call parameter_name= for any :parameter_name in the hash that has that method defined.


Let’s take a look at the Person object to see what mischief this lets us do. (Right, instead of updating the profile, update_profile updates the Person: Diaspora’s internal notion of the data associated with one human being, as opposed to the login associated with one email address (the User). Calling something update_profile when it is really update_person is a good way to hide the security implications of code like this from a reviewer. Names matter — make sure they’re accurate.) What methods and fields do you expose…


This is painful: by changing a Person’s owner_id, I can reassign the Person from one account (User) to another, allowing me to both deny arbitrary victims from their use of the service and also take over their account, allowing me to impersonate them, access their data at will, etc etc. This works because *one* in MongoDB picks the first matching entry in the DB it can find, meaning that if two Person have the same owner_id, your account will non-deterministically control one of them. So I’ll assign your Person#owner_id to be my #owner_id, which gives me a fifty-fifty shot at owning your account. If that is annoying for me, I can always assign my Person#owner_id to have some nonsense string, de-linking them and making sure current_user.person finds *your* data when I’m logged in.


**But wait, there is more!**: Note the serialized_key column. Can you guess what that is for? Well, if you follow some spaghetti in the User class, that is their serialized public/private encryption key pair. You might have heard that Diaspora seeds use encryption when talking between each other so that the prying eyes of Mark Zuckerberg can’t read your status updates. Well, bad news bears: the attacker can **silently overwrite your key pair**, replacing it with one he generated. Since he now knows your private key, regardless of how well-implemented your cryptography is, he can read your messages at will.


**This is what kills most encryption systems in real life.** You don’t have to beat encryption to beat the system, you just have to beat the weakest link in the chain around it. That almost certainly isn’t the encryption algorithm — it is some inadequacy in the larger system added by a developer who barely understands crypto but who trusts that sprinkling it in magically makes it better. Crypto is not soy sauce for security.


Is this a hard attack? **No.** You can do it with no tool more complicated than Firefox with Firebug installed: add an extra parameter to the form, switch the submit URL, own any account you like. It took me **two minutes** to find this vulnerability (I looked at the users controller first, figuring it was a likely place for bad stuff to happen if there was bad stuff to be found), and started trying to get the word to the Diaspora team immediately. It literally took longer to get Diaspora running than it took to create a script weaponizing this.


**Steps to avoid**: First, fix the authentication. That won’t prevent this attack, though — I can still screw up *my* Person by changing it’s owner_id to be yours (and do this an arbitrary number of times), virtually guaranteeing that I can successfully disassociate your account from your person.


After you fix authentication, you need to start locking down write access to sensitive data. Start by disabling mass assignment, which should be off in an public-facing Rails app. The Rails team keeps it in because it saves lines of code and makes the 15 minute blog demo nicer, but it is an easy security hole virtually anywhere it exists. Consider it guilty until proven innocent.


Second, if your data store allows it, you should explicitly make as much as feasible unwritable. ActiveRecord lets you do this with attr_readonly — I’m not sure whether you can do it with MongoMapper or not. There is almost certainly **no legitimate reason** for owner_id to be reassignable.


## NoSQL Doesn’t Mean No SQL Injection


**Code:**


Diaspora uses MongoDB, one of the new sexy NoSQL database options. I use a few myself. They have a few decades less experience getting exploited than the old relational databases you know and love, so let’s start: I claim this above code snippet gives me full read access to the database, including to serialized encryption keys.


What the heck?!


Well, observe that due to the magic of string interpolation I can cause the string including the Javascript to evaluate to virtually anything I want. For example, I could inject a carefully constructed Javascript string to cause the first regular expression to terminate without any results, then execute arbitrary code, then comment out the rest of the Javascript.


We can get one bit of data about any particular person out of this function: whether they are in the result set or not. However, since we can construct the result set at will, we can make that a **very significant bit** indeed. One thing Javascript can do is take a string and convert it to a number. I’ll elide the code for this because it is boring, but it is fairly straightforward. After I have that Javascript, I can run a binary search to get someone’s serialized_key. “Return Patrick if his serialized key is more than 2^512. OK, he isn’t in the result set? Alright, return Patrick if is key is more than 2^256. He is in the result set? Return him if his key is more than 2^256 + 2^255. …”


If their key has 1,024 bits (wow, so secure), it will take me roughly 1,024 and change accesses to find it. That will take me, hmm, a minute? Two? I can now read your messages at will.


I think MongoDB will let me do all sorts of nastiness here aside from just reading parts of the person object: for example, I strongly suspect that I can execute state-changing Javascript (though I didn’t have any luck making a Lil Bobby Tables to drop the database, but I only spent about two minutes on it) or join the Person document with other documents to read out anything I want from the database, such as User password hashes. That might be a fun project for someone who is not a complete amateur.


Code injection: **fun stuff** for attackers, not quite so fun.


**How to avoid this:**


Don’t interpolate strings in queries sent to your database! Use the MongoDB equivalent of prepared statements. If MongoDB doesn’t have prepared statements, **don’t use it for your security-critical projects** until it does, because you *will* be exploited.


## Take Care With Releasing Software To End Users


Since making my public comments, I have heard — over and over again — that none of the above matters because Diaspora is in secret squirrel double-plus alpha unrelease and early adopters know not to put any data in it. **False.** As a highly anticipated project, Diaspora was guaranteed to (and did) have publicly accessible nodes available within literally hours of the code being available.


People who set up nodes might be intelligent enough to evaluate the security consequences of running them. That is actually false, because there are public nodes available, but we’ll run with it. *Even if* the node operators understand what they are doing, their users and their users’ friends who are invited to join The New Secure Facebook are not capable of evaluating their security on Diaspora. They trust that, since it is on their browser and endorsed by a friend, it must be safe and secure. (This is essentially the same process by which they joined facebook — the zuckers.)


How would I have handled the Diaspora release? Well, candidly, I wouldn’t have released the code in the current state, and instead would have devoted non-trivial effort to securing it prior to release. If you put a gun to my head and said “Our donations came from 6,000 people who want to see progress, give me **something** to show them”, I would have released the code that they had with the registration pages elided, forcing people to only add new users via Rake tasks or the console. That preserves 100% of the ability of developers to work on the project, and for news outlets to take screenshots, without allowing technically unsophisticated people to successfully sign up to the Diaspora seed sites.


I don’t know if the Diaspora community understands how bad their current security posture is right now. Looking at the public [list of public Diaspora seeds](http://github.com/diaspora/diaspora/wiki/Community-supported-seeds), while the team has put a bold disclaimer that the software is insecure (which no one will read because no one reads on the Internet — welcome to software, guys), many of the nodes are explicitly appealing as safer options which won’t reset their DB, so you won’t lose your work if you start on them today. That is irresponsible.


## Is Diaspora Secure After The Patches?


**No.** The team is manifestly out of their depth with regards to web application security, and it is almost certainly impossible for them to gather the required expertise and still hit their timetable for public release in a month. You might believe in the powers of OSS to gather experts (or at least folks who have shipped a Rails app, like myself) to Diaspora’s banner and ferret out all the issues. You might also believe in magic code-fixing fairies. Personally, I’d be praying for the fairies because if Diaspora is dependent on the OSS community **their users are screwed**. There are, almost certainly, exploits as severe as the above ones left in the app, and there almost certainly will be zero-day attacks by hackers who would like to make the headline news. “Facebook Competitor Diaspora Launches; All Users Data Compromised Immediately” makes for a smashing headline in the New York Times, wouldn’t you say?


Include here the disclaimer that I like OSS, think the Diaspora team is really cool, and don’t mean to crush their spirits when I say that their code is unprofessional and not ready to be exposed to dedicated attackers any time soon.
