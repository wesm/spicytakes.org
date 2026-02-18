---
title: "‘Changes to U.K. Surveillance Regime May Violate International Law’"
date: 2023-08-23
url: https://daringfireball.net/2023/08/kouvakas_uk_surveillance
slug: kouvakas_uk_surveillance
word_count: 599
---


[Ioannis Kouvakas, writing for Just Security](https://www.justsecurity.org/87615/changes-to-uk-surveillance-regime-may-violate-international-law/):


> While the proposal does not specify what technical changes would
> require notification, these may include changes in the
> architecture of software that would [interfere](https://www.gov.uk/government/consultations/revised-investigatory-powers-act-notices-regimes-consultation/consultation-on-revised-notices-regimes-in-the-investigatory-powers-act-2016-accessible-version#proposed-changes) with the
> U.K.’s current surveillance powers. As a result, an operator of a
> messaging service wishing to introduce an advanced security
> feature would now have to first let the Home Office know in
> advance. Device manufacturers would likely also have to notify the
> government before making available important [security
> updates](https://www.bbc.co.uk/news/technology-66256081) that fix known vulnerabilities and [keep devices
> secure](https://www.ncsc.gov.uk/collection/device-security-guidance/managing-deployed-devices/keeping-devices-and-software-up-to-date). Accordingly, the Secretary of State, upon receiving
> such an advance notice, could now request operators to, for
> instance, abstain from patching security gaps to allow the
> government to maintain access for surveillance purposes.


This is exactly where I’ve thought, for months, that the United Kingdom is heading with this legislation, but it’s still shocking to see it described so starkly. It’s like watching someone drive toward a cliff, and warning people, “*Hey, I think these guys are driving right toward that cliff*” — and yet I’m still taken aback to see them drive off the cliff.


It’s a complete fantasy that E2EE can be toggled like a light switch and still allow messages to be delivered. The end-to-end encryption isn’t a sugar coating, some sort of extra layer of protection — it’s fundamental to the messaging protocols themselves. It has to be, when you think about it. If it were possible for, say, Signal, to silently disable E2EE but still have messages go through, how could users ever trust the service? You could neither trust that what you were sending would be delivered securely, nor that what you received wasn’t intercepted by an interloper. There’s an explicit guarantee with all of these E2EE messaging platforms [that messages can *only* go through securely](https://signal.org/docs/specifications/doubleratchet/). Removing E2EE wouldn’t require some mere tweak to the protocols, it would require replacing the protocols entirely (with inherently insecure ones).


And the notion that security updates, for every user in the world, would need the approval of the U.K. Home Office just to make sure the patches weren’t closing vulnerabilities that the government itself is exploiting — it boggles the mind. Even if the U.K. were the only country in the world to pass such a law, it would be madness, but what happens when other countries follow?


As I see it, the most likely outcome is that the U.K. passes the law, *thinking* that the grave concerns conveyed to them by the messaging services are overblown. That the platform providers are saying they *can’t* comply but they really just mean they don’t *want* to comply because it’s just difficult, not impossible. And when it becomes law, the platforms will hand it off to the nerds, the nerds will nerd harder, and boom, the platforms will fall into compliance with this law. That’s what they *think* will happen. What will actually happen, I believe, is that E2EE messaging platforms like WhatsApp (overwhelmingly popular in the U.K.), Signal, and iMessage *will stop working and be pulled from app stores in the U.K.*, full stop. The U.K. seems to think it’s a bluff; I don’t.


Perhaps the argument — as made by Kouvakas — that these changes would run afoul of international law will resonate with the U.K. in a way that technical arguments, thus far, have not.



| **Previous:** | [Walt Disney’s Mid-Century Business Strategy Charts](https://daringfireball.net/2023/08/disney_strategy_charts) |
| **Next:** | [Idle Speculation on the Widely-Assumed Switch to USB-C Ports on the Upcoming iPhones 15](https://daringfireball.net/2023/08/idle_speculation_on_the_widely-assumed_switch_to_usb-c_ports_on_the_upcoming_iphones_15) |


PreviousNext