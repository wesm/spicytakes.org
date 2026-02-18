---
title: "A Spectacularly Bad Washington Post Story on Apple and Google’s Exposure Notification Project"
date: 2020-05-15
url: https://daringfireball.net/2020/05/washington_post_exposure_notification_story
slug: washington_post_exposure_notification_story
word_count: 2081
---


A Washington Post story today [on Apple and Google’s joint effort on COVID-19 exposure notification project](https://www.washingtonpost.com/technology/2020/05/15/app-apple-google-virus/), from reporters Reed Albergotti and Drew Harwell, is the worst story I’ve seen in the Post in memory. It’s so atrociously bad — factually wrong and one-sided in opinion — that it should be retracted.


Start with the headline: “[Apple and Google Are Building a Virus-Tracking System. Health Officials Say It Will Be Practically Useless.](https://www.washingtonpost.com/technology/2020/05/15/app-apple-google-virus/)” It’s not a “virus-tracking system”, and the health officials the Post talked to don’t know what they’re talking about.


> But as the tech giants have revealed more details, officials now
> say the software will be of little use. Due to strict rules
> imposed by the companies, the system will notify smartphone users
> if they’ve potentially come into contact with an infected person,
> but it won’t share any data with health officials or reveal where
> those meetings took place.


Notifying people when they’ve potentially come into contact with an infected person sounds useful to me. It’s true that by design, Apple and Google’s system does not track location. It’s true that location information would be potentially useful to health officials. But the exposure notifications alone are inherently useful, even without location data attached.


The gist of Apple and Google’s project is that it attempts to balance privacy with the usefulness of tracking potential exposure. It’s right there in the name of the project: “[Privacy-Protecting Contact Tracing](https://www.apple.com/covid19/contacttracing/)”. The Post’s sources for this story seemingly want a system with no regard for privacy at all. I wish that were an exaggeration.


> But Apple and Google have refused, arguing that letting the apps
> collect location data or loosening other smartphone rules would
> undermine people’s privacy. The companies are also concerned that
> easing the restrictions around apps’ Bluetooth use would drain
> phone battery life, which could irritate customers. That unbending
> stance has led some health authorities to abandon hopes of
> building a fully functioning contact-tracing app.


“Unbending stance” is a rather harsh description of Apple and Google’s desire not to “undermine people’s privacy” or “drain phone battery life”. This isn’t an “unbending stance”. It’s table stakes for designing a system that people will actually install and use. Imagine trying to sell the public on a system that undermines their privacy or unduly drains their phone batteries — let alone a system that does both.


> But Helen Nissenbaum, a professor of information science and
> director of the [Digital Life Initiative](https://www.dli.tech.cornell.edu/) at Cornell
> University, called Apple and Google’s use of privacy to defend
> their refusal to allow public health officials access to
> smartphone technology a “flamboyant smokescreen.” She said it was
> ironic that the two companies had for years tolerated the mass
> collection of people’s data but were now preventing its use for a
> purpose that is “critical to public health.”
> “If it’s between Google and Apple having the data, I would far
> prefer my physician and the public health authorities to have the
> data about my health status,” she said. “At least they’re
> constrained by laws.”


Nissenbaum obviously has no idea whatsoever how this system is designed to work, despite the fact that Apple and Google have published [a succinct 7-page FAQ](https://covid19-static.cdn-apple.com/applications/covid19/current/static/contact-tracing/pdf/ExposureNotification-FAQv1.1.pdf) that explains it in simple, easy-to-understand terms. It seems clear that neither the reporters from the Post nor Nissenbaum have read that FAQ, or if they did, that they don’t understand it. (Or willfully ignored it.)


Google and Apple will not “have the data”. It is stored entirely and only on each user’s own device. We, the users, will have the data, and we, the users, can share that data with our doctors.


And how in the world did “At least they’re constrained by laws” make it into this story? Nissenbaum believes Apple and Google are *not* constrained by laws? That will be news to both companies’ legal compliance departments, who I presume will soon be laid off.


> The Apple-Google system uses the short-range Bluetooth antennas in
> people’s smartphones to log when two people come into contact for
> a short period of time, but not where that contact took place. An
> alert is sent if one of the people tests positive for a
> coronavirus infection, but that information is not shared with
> public health officials or contact-tracing teams.


That’s close to an accurate description — sort of, if you squint your eyes — but what the Post omits is essential. The information is not shared *automatically* with health officials, but if you opt into the system and get a notification that you’ve potentially been in contact with someone who has tested positive, you can then share that information with your doctor. Only doctors and registered health officials can confirm that a user in this system has tested positive for COVID-19 — otherwise, it would be open season for pranksters.


> The tension over virus-tracking apps reflects a major power
> imbalance between the tech giants and state and local health
> officials, who argue that Apple and Google’s technical decisions
> have undermined their response to a global health emergency. It
> also highlights the tech giants’ ability to exert unfettered
> control over how billions of smartphones work.


This is nonsense. Smartphones comply with a veritable mountain of regulations and laws around the world. If you use an iPhone just look in Settings → General → Legal & Regulatory.


> “They are exercising sovereign power. It’s just crazy,” said Matt
> Stoller, the director of research at the American Economic
> Liberties Project, a Washington think tank devoted to reducing the
> power of monopolies. Apple and Google have “decided for the whole
> world,” he added, “that it’s not a decision for the public to
> make. … You have a private government that is making choices over
> your society instead of democratic governments being able to make
> those choices.”


This quote is what’s crazy. Again, Matt Stoller clearly has no idea what he’s talking about here. Apple and Google deciding how their operating systems work, in compliance with all existing laws, all around the world, is not “exercising sovereign power”. No one here is alleging that Apple or Google are doing anything even vaguely illegal. They’re not toeing some sort of line, they’re not taking advantage of any sort of loopholes.


And if Apple and Google did what Stoller and Nissenbaum seem to want them to do — track location data of every person you’re in contact with and report that data automatically to government health officials, they almost certainly *would* be breaking all sorts of laws around the world. The whole point of Europe’s well-intentioned but overzealous GDPR law — [88 dense pages in PDF](https://eur-lex.europa.eu/eli/reg/2016/679/oj) — is, quoting from its preamble, “Natural persons should have control of their own personal data.” That’s exactly the point of Apple and Google’s system — and seemingly exactly the opposite of what every source in this Post story thinks Apple and Google should do.


Also, regarding Stoller’s advocacy for democracy, good luck finding public support for a system that turns phones into surveillance devices that report anything at all automatically to the government, let alone something as sensitive as who we’ve been in contact with and where we’ve been. I’ll grant that one can make a case that a system where government health officials have access to such data from our phones, automatically, could be useful in tracking COVID-19 infections. But try getting popular support for it. And no one I’ve seen has made the case that such a system is *necessary* for using phones in the aid of contact tracing.


There is not much overlap between (a) people who have thought long and hard about the very complicated ways smartphones can be used to abuse personal privacy with tracking and data collection; and (b) public health officials admirably trying to track COVID-19. None of the few people in the intersection of those two groups were quoted in this story.


> The companies have argued that limiting the data the apps use
> could bolster their adoption rate, because people may not trust or
> use an app that logs their location for later use by public health
> authorities.


You think so?


> But some parts of the U.S., including Apple and Google’s home
> state, say the restrictions have rendered the apps effectively
> useless.


None of these apps are out yet, because the APIs in iOS and Android aren’t out yet.


> Contact tracers today use phone calls and interviews to track people’s movements, and rely almost entirely on people’s memory. Minute-by-minute location logs recorded by people’s phones, some officials have argued, could ease that burden by providing a more precise and automated way to track new outbreaks.


In what other context would the above paragraph pass the sniff test? “Some officials” — unnamed, unsourced — are arguing that the government should enjoy “minute-by-minute location logs recorded by people’s phones” and this is given *zero pushback* in a news story. No pushback at all on this argument, describing a scenario that is the very definition of a potential privacy fiasco.


> “The limitations of those kind of apps are extensive,” said Mike
> Reid, an assistant professor of medicine at University of
> California, San Francisco, who’s leading the effort to train
> contact tracers in the state. “I don’t think they have an
> important role to play for most of the population.”
> The contact tracers, he said, will be using software made by
> Salesforce and Accenture to help reach patients by phone and are
> trained on how to protect sensitive patient information.
> “We go to pains to minimize the amount of data we take from people
> and we ask consent from people we’re talking to on the phone. We
> go to considerable lengths to ensure there are strong technical
> controls to ensure the anonymization of our platforms,” he said.
> “Can you say the same thing about these big tech companies? I’m
> not sure.”


Yeah, so it would be better if Apple and Google minimized the data and stored it only on the devices themselves, rather than collecting it on their servers. And they should explain in detail how their system protects privacy and ensures anonymity from start to finish.


[Wait](https://covid19-static.cdn-apple.com/applications/covid19/current/static/contact-tracing/pdf/ExposureNotification-CryptographySpecificationv1.2.pdf).


Also — also! — we now have someone who will be training contact tracers in California, who voluntarily went on the record that Salesforce and Accenture are more worthy of trust for contract-tracing privacy protection (with detailed location data!) than the Apple/Google proposal. Goddamn.


> With the Apple and Google approach, “we’ve overcompensated for
> privacy and still created other risks and not solved the problem,”
> said Ashkan Soltani, the former chief technologist of the Federal
> Trade Commission. “I’d personally be more comfortable if it were a
> health agency that I trusted and there were legal protections in
> place over the use of the data and I knew it was operated by a
> dedicated security team.”


It is legit amazing to see [Ashkan Soltani](https://www.eff.org/deeplinks/2020/03/user-privacy-champion-ashkan-soltani-joins-eff-advisory-board), of all people, say “we’ve overcompensated for privacy.”


> Tom Frieden, the former director of the Centers for Disease
> Control and Prevention now working with the health organization
> Vital Strategies, said the proximity-tracing system as proposed by
> Apple and Google has “been largely a distraction.”
> “There are very serious questions about its feasibility and its
> ability to be done with adequate respect for privacy, and it has
> muddied the water for what actually needs to happen,” Frieden said
> in an interview Wednesday. “This was an approach that was done
> with not much understanding and a lot of overpromising.”


[Here is Apple and Google’s joint announcement](https://www.apple.com/newsroom/2020/04/apple-and-google-partner-on-covid-19-contact-tracing-technology/). What exactly did either company overpromise? Did a bunch of idiots who weren’t involved, didn’t read the specs, and don’t even understand the proposal jump to overpromise-y conclusions? Sure. But how is that Apple or Google’s fault?


> The proximity-tracing systems are “a bright shiny object,” he
> said, “but right now they’re doing nothing to stop the pandemic.”


Maybe because they’re *not fucking out yet*? Hallelujah, holy shit — where’s the Tylenol?



| **Previous:** | [More on Dithering](https://daringfireball.net/2020/05/more_on_dithering) |
| **Next:** | [Department of Justice Reopens Spat With Apple Over iPhone Encryption](https://daringfireball.net/2020/05/doj_apple_iphone_encryption) |


PreviousNext