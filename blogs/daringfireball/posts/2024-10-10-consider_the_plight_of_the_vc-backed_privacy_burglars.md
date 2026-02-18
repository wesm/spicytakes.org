---
title: "Consider the Plight of the VC-Backed Privacy Burglars"
date: 2024-10-10
url: https://daringfireball.net/2024/10/consider_the_plight_of_the_vc-backed_privacy_burglars
slug: consider_the_plight_of_the_vc-backed_privacy_burglars
word_count: 1454
---


Kevin Roose wrote a column for The New York Times last week under the headline “[Did Apple Just Kill Social Apps?](https://www.nytimes.com/2024/10/02/technology/apple-social-apps-contacts-change.html)”, about which [Jason Snell quipped](https://sixcolors.com/link/2024/10/did-godzilla-just-step-on-a-bad-idea/), “It’s rare that a story is worse than its provocative headline, but this one manages it.” The gist of it is Roose positing that Apple’s new fine-grained controls over contact-sharing in iOS 18 are somehow controversial. Roose himself writes:


> For years now, the way contact sharing has worked on iOS devices
> is that an app can trigger a message called a “data access
> prompt,” asking for access to a user’s contacts.
> If the user agreed, the app developer got a list of all the
> contacts in that user’s address book, along with other information
> stored in the user’s contact cards, such as phone numbers and
> email addresses. App developers could then use that information to
> build out a user’s social graph, or suggest other accounts for the
> user to follow.
> In iOS 18, however, users who agree to give an app access to their
> contacts are shown a second message, allowing them to select which
> contacts to share. Users can opt to share just a handful of
> contacts by selecting them one by one, rather than forking over
> their entire address book.
> Apple’s stated rationale for these changes is simple: Users
> shouldn’t be forced to make an all-or-nothing choice. Many users
> have hundreds or thousands of contacts on their iPhones, including
> some they’d rather not share. (A therapist, an ex, a random person
> they met in a bar in 2013.) iOS has allowed users to give apps
> selective access to their photos for years; shouldn’t the same
> principle apply to their contacts?


The obvious answer is yes, the same principle should of course apply to contacts. But Roose presents the change as controversial and anticompetitive, on the grounds that burgeoning social networks have, over the last 15 years, used that all-or-nothing access to users’ contacts to great effect building out their social graphs, and pointing out that Apple’s own first-party apps like Messages and Mail aren’t faced with these restrictions.


Nick Heer wrote a splendid response to Roose’s piece at Pixel Envy — “[I Do Not Care About Impediments to a Creepy Growth Hacking Technique](https://pxlnv.com/blog/growth-hack/)” — the entirety of which is worth your full attention, but this paragraph sums up my first thought:


> The surprise is not that Apple is allowing more granular contacts
> access, it is that it has taken this long for the company to do
> so. Developers big and small have abused this feature to a
> shocking degree. [Facebook ingested](https://www.businessinsider.com/facebook-uploaded-1-5-million-users-email-contacts-without-permission-2019-4) the contact lists of
> a million and a half users unintentionally — and millions of
> users [intentionally](https://www.adweek.com/performance-marketing/facebook-now-suggesting-friends-found-in-imported-contact-lists/) — a massive collection of data
> which was used to inform its [People You May Know
> feature](https://gizmodo.com/people-you-may-know-a-controversial-facebook-features-1827981959). LinkedIn is [famously creepy](https://www.washingtonpost.com/technology/2022/07/26/linkedin-privacy-guide/) and does
> basically the same thing. Clubhouse borrowed from the TBH playbook
> by [slurping up contacts](https://onezero.medium.com/clubhouse-is-suggesting-users-invite-their-drug-dealers-and-therapists-a8161b3062fc) before you could use the app.
> This has [real consequences](https://www.splinter.com/facebook-recommended-that-this-psychiatrists-patients-f-1793861472) in surfacing hidden
> connections many people would want to *stay* hidden.


My other thought is that new restrictions are inevitably resented by those who were abusing the newly-restricted resource. Polluters resent new regulations that force them to cease dumping chemicals into rivers and lakes, or pumping them into the air. Coal mines and factories [resented child labor laws](https://www.everycrsreport.com/reports/RL31501.html) a century ago (and some [still resent them today](https://www.epi.org/publication/child-labor-laws-under-attack/)). If iOS had debuted in 2007 with per-contact sharing controls exactly like those in iOS 18 today, no one serious would ever have complained that this was wrong or unfair.1 But Apple adding these controls only now makes it different. They’re not just giving users control they previously didn’t have, they’re taking something away from companies that seek to exploit, as Heer aptly describes it, a creepy growth-hacking technique. Writ large, this psychology explains why granting social equality to minority groups feels to some in the majority group, the small-minded and bigoted, like a *loss* of privilege and a *downgrade* in status.2


As for Roose’s contention that it’s even somewhat controversial that Apple’s own apps aren’t subject to these address book restrictions:


> Some developers also pointed out that the iOS 18 changes don’t
> apply to Apple’s own services. For example, iMessage doesn’t have
> to ask for permission for access to users’ contacts the way
> WhatsApp, Signal, WeChat and other third-party messaging apps do.
> They see that as fundamentally anticompetitive — a clear-cut
> example of the kind of self-preferencing that antitrust regulators
> [have objected to](https://www.nytimes.com/2024/03/21/technology/apple-doj-lawsuit-antitrust.html) in other contexts.


To the first party go the first-party spoils. It’s absurd to consider a cell phone that doesn’t make the user’s full address book available to the built-in phone-call and messaging apps. All phones offer similar system-level integration between such core apps. But for Apple in particular, broad and deep integration is the company’s modus operandi. People choose to use Apple platforms *because* of the integration, not despite it. As I wrote last month in “[The iOS Continental Drift Widens](https://daringfireball.net/2024/09/the_ios_continental_drift_widens)”:


> Safari isn’t just *a* web browser that just happens to be Apple’s.
> It’s *the* web browser designed by Apple to do things *the iOS
> way* on iOS (and *the Macintosh way* on MacOS). If, as a user, you
> do things the Apple way — owning multiple Apple devices, using
> iCloud for sync, using Safari as your web browser — you get an
> integrated experience, with access on device A to the tabs open on
> device B, shared browsing history and bookmarks between all
> devices, and support for systemwide services and features. The
> default apps from Apple on a factory fresh iPhone are designed to
> work together and present themselves consistently. That’s not to
> say no one should use third-party apps that are alternatives to
> Apple’s own. Of course not. Surely almost every reader of Daring
> Fireball uses one or more third-party apps that are alternatives
> to Apple’s. I use several. But the built-in Apple apps, taken
> together, constitute the Apple-defined experience. Those really
> are the apps most non-expert users should use. And the best
> third-party alternatives — like [Fantastical](https://flexibits.com/fantastical) (calendar),
> [Cardhop](https://flexibits.com/cardhop) (contacts), [Overcast](https://overcast.fm/) (podcasts), and [Bear](https://bear.app/) (notes) — fit seamlessly within that overall Apple experience. They’re
> third-party apps that feel integrated with the first-party
> experience.


Cardhop is a particularly apt example, as its entire purpose is to serve as a full alternative to the system Contacts app. It wouldn’t be able to do so if it needed per-entry permission to each contact, so it asks the user for full address book read/write access, which Cardhop users grant because, duh, the entire point of the app is that it’s a full address book. A new social media network is not an address book — and users know it.


Also, even putting aside the fact that first-party apps necessarily have certain advantages third-party apps do not (otherwise, there’d be no distinction), apps from the same developer have broad permission to share data and resources [via app groups](https://help.apple.com/xcode/mac/current/#/dev8dd3880fe). Gmail can talk to Google Calendar, and Google Calendar has full access to Gmail’s address book. It’s no more “fundamentally anticompetitive” for Messages and Apple Mail to have full access to your Contacts address book than it was for Meta to launch Threads by piggybacking on the existing accounts and social graph of Instagram. If it’s unfair, it’s only unfair in the way that life in general is unfair.


The question to ask is, “Is this what users want and expect?” Sometimes it really is that simple. I’m not sure it’s ever worth asking “Is this what growth-hacking VC-backed social-media app makers want?”


---

1. This is hard to believe now, but [until iOS 6 in 2012](https://www.macrumors.com/2012/06/14/apple-requires-user-permission-before-apps-can-access-personal-data-in-ios-6/), there were no access restrictions on address book data at all. All apps simply had unfettered access to all of your contact data, with no permission prompt nor any indication that they were accessing it. This [came to a head](https://daringfireball.net/linked/2012/02/08/path-right) with [a massive controversy over the defunct social app Path’s uploading to its servers](https://www.techmeme.com/120208/p50#a120208p50) the entire address books of all its users. ↩︎︎
2. This sentiment has never been described more searingly than by Gene Hackman [in this scene from the great film *Mississippi Burning*](https://www.youtube.com/watch?v=UlzaBi_QxPw). A 1988 film about 1964 murders that, alas, captures our political moment today. ↩︎



| **Previous:** | [A Few Brief Thoughts on Meta Connect 2024](https://daringfireball.net/2024/09/a_few_brief_thoughts_on_meta_connect_2024) |
| **Next:** | [The Sordid Tale of Rudy Giuliani’s Yankees World Series Rings](https://daringfireball.net/2024/10/the_sordid_tale_of_rudy_giulianis_yankees_world_series_rings) |


PreviousNext