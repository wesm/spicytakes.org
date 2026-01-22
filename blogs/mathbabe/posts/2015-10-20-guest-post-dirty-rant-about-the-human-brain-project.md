---
title: "Guest post: Dirty Rant About The Human Brain Project"
date: 2015-10-20
url: https://mathbabe.org/2015/10/20/guest-post-dirty-rant-about-the-human-brain-project/
word_count: 1215
---


*This is a guest post by a neuroscientist who may or may not be a graduate student somewhere in Massachusetts.*


You asked me about the Human Brain Project. Well, there is only one way to properly address that topic: with a rant.


[Henry Markram](https://en.wikipedia.org/wiki/Henry_Markram) at [EPFL](https://en.wikipedia.org/wiki/%C3%89cole_Polytechnique_F%C3%A9d%C3%A9rale_de_Lausanne) in Switzerland was the leader of [the “Blue Brain” project](https://en.wikipedia.org/wiki/Blue_Brain_Project), to simulate a brain (well, actually just one cubic millimeter of a mouse brain) on an IBM Blue-Gene supercomputer. He got tons of money for this project, including the IBM supercomputer for the simulations. Of course he never published anything showing that these simulations lead to any understanding of brain function whatsoever. But he did create a team of graphics professionals to make cool pictures of the simulations. Building on this “success”, he led the [“Human Brain” EU flagship project](https://en.wikipedia.org/wiki/Human_Brain_Project) into being funded by some miracle of bureaucratic gullibility. The clearly promised goal was simulating a human brain (hence the name of the project). Almost everyone in Europe publicly supported the project, although in private the neuroscientists (who, if they have done any simulations, know that the stated goal is completely absurd) would say something more like “hey, maybe it’s crazy, but it’ll bring a bunch of money.”


Now, some simple observations must be made, which are true now, and will still be true in ten years’ time, at the conclusion of this flagship project:


**(1) We have no fucking clue how to simulate a brain. **


We can’t simulate the brain of C. Elegans, a very well studied roundworm (first animal to have its genome sequenced) in which every animal has exactly the same 302-neuron brain (out of 959 total cells) and we know the wiring diagram and we have tons of data on how the animal behaves, including how it behaves if you kill this neuron or that neuron. Pretty much whatever data you want, we can generate it. And yet we don’t know how this brain works. Simply put, data does not equal understanding. You might see a talk in which someone argues for some theory for a subnetwork of 6 or 8 neurons in this animal. Our state of understanding is that bad.


**(2) We have no fucking clue how to wire up a brain. **


Ok, we do have a macroscopic clue, this region connects to that region and so on. You can get beautiful pictures with methods like DTI, with a resolution of one cubic millimeter per voxel. Very detailed, right?  Well, apart from DTI being a noisy and controversial method to begin with, remember that one cubic millimeter of brain required a supercomputer to simulate it (not worrying here about how worthless that “simulation” was), so any map with cubic-millimeter voxels is a very coarse map indeed. And microscopically, we have no clue. It looks pretty random. We collect statistics (with great difficulty), and do tons of measurements (also with great difficulty), but not on humans. Even for well studied animals such as cats, rats, and mice, it’s anyone’s guess what the fine structure of the connectivity matrix is. As an overly simplistic comparison, imagine taking statistics on the connectivity of transistors in a Pentium chip and then trying to make your own chip based on those statistics. There’s just no way it’s gonna work.


**(3) We have no fucking clue what makes human brains work so well. **


Humans (and great apes and whales and elephants and dolphins and a few other animals that we love) happen to have a class of neurons (“spindle neurons”) that we don’t see in the animals that we spend most of our time studying. Is it important? Who knows. We know for sure that we are missing a lot about what makes a human brain human — it’s definitely not just its size. There’s a guy whose [brain is mostly not there](https://www.newscientist.com/article/dn12301-man-with-tiny-brain-shocks-doctors/), and he was probably one of the dumber kids in class, but still he functions fine in human society ([has a job, family, etc.](http://www.thelancet.com/journals/lancet/article/PIIS0140-6736(07)61127-1/abstract)). Is this surprising? Not surprising? How would we know, we don’t know how brains work anyway.


**(4) We have no fucking clue what the parameters are. **


If you try to do a simulation to see how neurons behave when they are connected in networks, you need to know a bunch of biophysical parameters. For example, what’s the time constant for voltage leak across the cell membrane? And a ton of other parameters, which are of course different for different classes of cells. So let’s just take the most common excitatory cell class and the most common inhibitory cell class and try to make a network. Luckily, there are papers that report numbers for this or that parameter of these cells. But the reported numbers are all over the place! One lengthy detailed study will find a parameter to be 35±4, and the next in-depth study will find the same parameter to be 12±3. So what should you use in your simulation for this or the many, many other uncertain parameters? Who the fuck knows.


**(5) We have no fucking clue what the important thing to simulate is. **


Neurons in vertebrates communicate (*) via “spikes”, where the neuron’s voltage level suddenly goes way up for a millisecond or so. This electro-chemical process, involving various ions flowing across the cell membrane, is very well understood. But now, what do these spikes mean? Is it the number of spikes per second that matters? Or is it the precise timing of the spikes? Who the fuck knows. For certain types of cells in certain areas, we see that they are active (producing a lot of spikes) under certain conditions. For example, in the primary visual cortex of a cat, a cell will be active when the eye sees a line at a certain position and a certain orientation moving in a certain direction. Is the timing of these spikes important? We don’t know! Some experts believe one way, some experts believe the other, and the rest admit they don’t know. And primary visual cortex of the cat is the most well studied area of any brain in any animal.


(*) How does a spike allow communication? The voltage spike triggers the release of chemicals at “synapses” (the connections to target neurons), which in turn dock with the target cell’s membrane in various ways to allow ions to cross the membrane, thereby affecting the voltage of the targeted cell. If the voltage in a cell reaches a certain threshold, a spike will occur. Each neuron targets (and is targeted by) thousands of other neurons. And the total number of neurons in a human brain is about a fourth of the number of stars in the milky way. You wanna map that circuit?


So, the next time you see a pretty 3D picture of many neurons being simulated, think “cargo cult brain”. That simulation isn’t gonna think any more than the [cargo cult planes](https://en.wikipedia.org/wiki/Cargo_cult_science) are gonna fly. The reason is the same in both cases: We have no clue about what principles allow the real machine to operate. We can only create pretty things that are superficially similar in the ways that we currently understand, which an enlightened being (who has some vague idea how the thing actually works) would just laugh at.
