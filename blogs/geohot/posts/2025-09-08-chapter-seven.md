---
title: "chapter seven: nudge"
date: 2025-09-08
url: https://geohot.github.io/blog/jekyll/update/2025/09/08/chapter-seven.html
slug: chapter-seven
word_count: 1361
---

“Why are you here on a Sunday?”

“John’s in town,” I said. “And he knows I’m looking for him.”

I’ve carried this case for five years. When Operant moved its compute out to Long Island—cheaper power, easier permits—it landed in my world by accident. Detective James Reese, Nassau County Police. Since then, every time I think I’ve got a straight line, the story bends. People call it “mind control.” That’s the wrong phrase. You hear that and you start hunting for sci-fi. What you should be hunting for is timing.

There are the clean facts. It started with a private investigator caught at night inside Jane Street’s office. He was there to plant a device. Not a camera, not a mic. A flat plastic square the size of a drop ceiling tile, featureless, no lens, no obvious grill. If you tapped it with a knuckle it sounded dead, like dense foam. The FBI took the evidence, said as little as possible, and then Trump dissolved the Bureau and the chain of custody with it. The PI pled to B&E, did eighteen months, swore a friend offered him ten grand and a location. The friend never existed long enough for us to find.

While the tile vanished, Operant didn’t. They grew. They put their name on the Ducks’ ballpark, donated to everyone they should, and pushed eight percent of Long Island’s power through their meter. Every time I asked questions, a lawyer answered them. I still have a job mostly because I don’t stick my questions in microphones.

But the corporate espionage wasn’t the hook. The hook’s name was Tom Park. Young, gifted, on Operant’s “research” payroll. He died off the roof of their building. We asked for the CCTV. They delayed until the delay became its own story, and when the files came they were grainy enough you could convince yourself resolution had gone out of style. We couldn’t prove a cut. We couldn’t prove a lie. We could see a silhouette on the roof with a phone in his hand, see him put it away, and watch him walk forward like he’d decided to walk forward an hour ago.

We pulled his phone records. The carrier said the device never left his parents’ house that night. The family’s router logs said the same thing—MAC associated all evening, steady signal, Netflix on the downstairs TV. At the time of death the rooftop access point didn’t record a roam. No one found a phone with the body.

If you’re generous, you call that “inconsistency.” If you’ve been around long enough, you call it “choreography.”

I didn’t see the tile again, but I kept a copy of the photos and I stared at the connector pads until I’d memorized the geometry. Four edge pads, power bus shape. Months later, a fire inspection at an Operant satellite site flagged “non-listed luminaires with integrated driver boards.” That’s code for “custom lights.” The brand on the sticker didn’t exist in any registry. It matched nothing you could buy.

What does a ceiling tile do if it isn’t a ceiling tile? You can guess: a planar array under plastic, phaseable, a clock inside that doesn’t drift. You don’t need to read thoughts. You need to make the room keep time.

We ran a small experiment in our squad room. Nothing that requires approval. We set up a tapping game on a laptop—left or right as quickly as you can when a cue appears. We added a desk lamp we could modulate in the last hundred milliseconds before the cue—no visible flicker, just PWM phase changes—and a piezo disc under the mouse pad that could make a vibration too soft to notice unless you were trying to notice. We told the script to wait until the model thought the subject was likely to pick left, then line up the lamp phase and the tick so “left” felt a hair earlier.

The hit rate shifted eight points. The officers said it felt like the computer was “on it” that round. No one said they felt pushed. That’s the thing about timing: when it works, it feels like you were going to do it anyway.

I went back to Tom. We subpoenaed what we could: badge swipes, elevator logs, building automation schedules for lights and HVAC. The elevator cabin he rode at 23:41 ran a “door nudge” cycle at floor 35—exact term in the manual. Not a stop, a shove. At the same minute the east conference rooms above ran a luminance ramp—35 to 50 percent and back down—logged as a “pattern test.” Two minutes later the air handlers kicked a “night purge,” unscheduled. The lobby mic’s spectrogram shows the change as a clean band sliding up. None of those facts make a person move. Together they draw a rhythm line through a building.

We never found what Tom had in his hand, his “not a phone,” but a year after his death, one of their contractors quit and dumped an issue tracker on a public repo by accident. It was up for an hour before it vanished, but the internet is full of raccoons, and one of them sent me a ZIP. Half the issues were boring—install scripts, driver mismatches, bad GPIO pull-ups. The other half had words like “phase,” “latency,” “confidence gate,” “avoid visible artifacts,” “EEG-free,” and the tag “ROOM.”

There was a set of comments on a bug titled “End Token Misfires.” The engineers were arguing about whether printing the full predicted sequence at the start of a session biased the subject into making it true. One person said that was the point. Another said if your only wins are the ones you can cause you aren’t measuring prediction anymore, you’re measuring control. The thread ends with a “resolved—won’t fix.”

Mind control isn’t the right term. It makes people look for sci-fi. The right term is “nudge,” the one the elevator manuals use. You put your thumb on the timing. You don’t push the person; you lean on the moment.

Tom stood on a roof with a clock in his pocket that belonged to the room, and a room that belonged to the company, and a company that had learned you can make a person look like a prediction if you take away all the moments where they would have surprised you.

Sometimes I think the real trick isn’t the tile or the lights. It’s the bookkeeping. You arrange your systems so that there’s nothing to subpoena. The carrier shows a phone at home. The Wi-Fi shows a phone at home. The building shows a test pattern and a purge cycle and a polite door. Nothing is illegal in a log file.

I keep a copy of that ZIP on a USB stick in my desk. There’s a folder called “SAFE_GATES” with a README someone wrote in plain English. “Do not schedule interventions if subject arousal > threshold. Do not schedule end token if subject mentions self-harm. Cooldown after consecutive errors.” Half the rules are commented out. The most recent commit message is just a shrug emoji.

The worst part is how ordinary it all is. The elevator nudge. The lamp nudge. The HVAC tone. The not-a-phone. If you want to find the devil, you don’t go looking for horns. You go looking for clock edges.

I told my sergeant I was taking the rest of the day. I stopped by a hardware store and bought a dimmer I knew I could open, and a roll of white tape. Back at the office I put a strip of tape on the lamp in interview room two, covering the LED that the supplier put there to indicate “smart mode.” We don’t use smart mode. We don’t use anything with a mode. When I left, the room looked like every other room. That’s the point. You only notice the timing when it slips.

On the way home I drove past the Ducks ballpark. Operant’s name on the sign looked like every other naming deal. Families walking in, kids with foam fingers, warm light over the field. If you didn’t know to look, you’d think it was all just baseball.
