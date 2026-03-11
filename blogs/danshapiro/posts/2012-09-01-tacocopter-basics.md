---
title: "Tacocopter Basics"
date: 2012-09-01
url: https://www.danshapiro.com/blog/2012/09/tacocopter-basics/
word_count: 2538
---


The Tacocopters are coming. Sure, the [original pitch](http://tacocopter.com/) was a clever troll aimed at credulous and impatient fast-food junkies. But the numbers don’t lie – a typical taco weighs less than a pound, and aircraft that can autonomously fly a few dozen ounces of payload to your doorstep are already available for around a thousand bucks. Amazon Prime is cool, and I can’t wait for self-driving delivery cars – but there’s a reason they call a beeline a beeline. Flying autonomous deliverybots are coming.  Fast.


Lest you doubt the logistics, the Hong Kong based hobbyshop of wonderment, Hobbyking, recently sponsored a contest called [“Beerlift 2012”](http://www.hobbyking.com/hobbyking/store/beerlift.asp). While the contestants mostly used water as a standin for the bubbly, the [winner](http://www.youtube.com/watch?v=UVwt7oWC5fc&feature=player_embedded), Romanian pilot Muresan Alexandru Camil, lifted over a hundred pounds of liquid – meaning that deliveries of entire beer kegs are not out of the question.  While his massive octocopter looks like quite an endeavor, American David Ditch lifted a respectable 50 lbs with a 2-foot-square quadcopter – enough for quite a few [Taco Bell Doritos Locos](http://www.cnn.com/2012/06/08/tech/web/bellini-doritos-locos-tacos/index.html) to your door.  279 of them, if you’re [counting](http://www.theatlantic.com/health/archive/2012/06/4-space-shuttles-of-insanity-100-million-doritos-locos-tacos-by-the-numbers/258123/).


But this all begs a basic question: What kind of aircraft is best suited for door-to-door drone deliveries? With the FAA [already overdue](http://www.avweb.com/avwebflash/news/FAAMissesDroneDeadline_207242-1.html) to create rules for drones in urban airspace, it’s just a matter of time till your mexican food is delivered airmail. But what’s the right design to make the tacos fly?


## Traditional Helicopter


Traditional helicopters are amazing machines. It’s been said, “They don’t so much fly as they beat the air in to submission.” The basic idea of a helicopter is that you have a big motor that spins a pair of blades, and a few actuators – probably servos – that tilt the blades as they spin.


What’s amazing is that once you’ve got the blades of a helicopter whirling at full tilt, the motor never really needs to change speed. The servos actually change the tilt of the blades mid-revolution as they whirl around. Want to go up? Increase the blade pitch. Go down? Decrease it. Go forward? Yes, the blades actually alternate between pitching up and down as they whirl around the masthead, bringing the back of the helicopter up and tipping the front down to accomplish forward motion.  This tilting happens at thousands of times per second (although the clever design of the [swashplate](http://en.wikipedia.org/wiki/Swashplate_(helicopter)) means the servos don’t have to move that fast). Similar gymnastics are responsible for sliding left and right.


Helicopters do have a problem with spinning around wildly though – [Newton’s Third](http://www.khanacademy.org/science/physics/v/newton-s-third-law-of-motion) and all that – so they have a tail rotor to keep them from equally and oppositely reacting. The tail rotor, too, has variable pitch – more pitch to rotate the helicopter to the right, and less to turn left. (In some copters the tail is run by a separate motor whose speed is varied, but this is generally less reliable).


Helicopters can be kitted out with all sorts of smarts, and their lifting capacity is limited only by the size of motor you decide to put in it. Which is not much of a limit.  But the place where they really shine is precision navigation.  While you may have seen quadcopters do some pretty amazing things, it’s absolutely nothing compared to what helicopters can do.  [Fly upside down](http://www.youtube.com/watch?v=1Lg6wASg76o).  Fly with the [tail pointed towards the ground](http://www.youtube.com/watch?v=PWkpPmXd-SQ).  [Land on a bloody wall](http://www.break.com/index/rc-helicopter-lands-on-wall-2088129). You know, just [watch this](http://www.youtube.com/watch?v=q6F-0rIpLJE).  I’ll wait.


OK, so a traditional helicopter is physically capable of delivering your Mexi-melt to your doorstep, even if your doorstep happens to be, you know, sideways or spinning around or something.  But traditional helicopters have one major drawback: fragility.


The list of things that can go wrong with a helicopter is truly impressive.


**Main power system failure:** Battery goes kaput.  Speed controller goes up in smoke.  Main motor grinds to a halt.  There’s just one source of juice keeping the bird in the sky, and it’s very hard to make these things redundant.  Moreover, if you do want, say, a redundant motor, the second motor has to be able to lift the entire helicopter by itself if the first one should fail.  That means you’re carrying double the weight around, just in case of a problem.  And if the main power system does fail, things get very bad, very fast.  Your only hope is to [autorotate](http://www.youtube.com/watch?v=4JqmoWAhv5g) down – that means kicking the thing in to neutral gear, spinning up the blades as fast as you can, plummeting, and trying to use *the momentum of your rotor blades* to slow down your crash at the last possible minute.  That’s what helicopter pilots mean when they talk about emergency maneuvers.


**Servo failure:**  You’re almost certainly coming down immediately.  Making servos redundant is really, really hard because when they fail they tend to lock up.  Servos are overly complicated (at least as compared to a regular motor) and like to fail.  Depending on which servo fails you might have the joy of unstoppable acceleration in any randomly-chosen direction, spinning wildly, or even using the full force and power of the main motor to accelerate you downward, faster than gravity can pull you.


**Tiny bit of something gets somewhere:**  Helicopters are full of delicate linkages and stiff-but-brittle parts.  Little things break off and take out big things.  The results are nearly always catastrophic.


So that’s the problem.  Helicopters are basically a giant spinning ball of disaster continuously waiting to happen, and when anything goes wrong, it does.


## Airplane


RC planes have come a long way.  To give you an idea of where they started out at, I was at Ye Olde Timey Airfielde, [Marymoor Park RC club](http://www.mar-c.org/), a few weeks ago.  It sounded like the place was under aerial assault by a landscaping platoon.  That’s because, I learned, the guy next to me was flying an airplane powered by an I-am-not-making-this-up [Weed Wacker](http://www.sears.com/search=craftsman+weedwacker?vName=Lawn+%26+Garden&cName=Handheld+Power+Tools&viewItems=25&autoRedirect=true). He’d literally removed the motor from one and bolted it to an airframe.  And I’ll be damned if the thing didn’t fly.


That was more or less the state of the art 20 years ago.  Now things are different.  And by different, I mean awesome.  Take thrust-to-weight ratio.  That’s the power put out by the motor, divided by the weight of the plane.  Normal planes, like a [747](http://www.grc.nasa.gov/WWW/k-12/BGP/Donna/t_w_ratio_answers.htm) or our weed wacky friend, have thrust to weight ratios of about 0.3.  This weekend I was flying a $20 piece of foam around the park that had a thrust to weight ratio of about TWO.  That is, I could have pointed the plane to the sky and accelerated straight up, *while towing a second plane*.  This is now pretty standard: the only reason not to have a thrust-to-weight ratio greater than one is because thrust and top speed are a tradeoff, so if you want to go 100 mph, you lose bottom-end thrust.  It’s like flying in 5th gear.  (unrelated note: if you want to go really fast, your best bet is to ditch the motor completely like this [400 mph unpowered glider](http://www.youtube.com/watch?v=Oix6sHKzOLU)).


Now airplanes have a huge advantage over helicopters or multicopters of any stripe: they’re actually capable of real, high school physics, [Bernoulli’s principle](http://hyperphysics.phy-astr.gsu.edu/hbase/fluids/airfoil.html) style flight.  They can have airfoils and generate lift while moving sideways, instead of just assaulting the air in a general upwards direction and hoping for the best (I’m looking at you, helicopters).  This means they’re way more fuel efficient.


For example, the  Sikorsky S-76C++ twin turbine helicopter gets about 20 miles per gallon, per passenger.  An Airbus A380 gets about 80.


So it’s way, way cheaper to keep a plane in the air.  And they can fly for way, way longer on an equivalent weight of fuel.


Survivability of a plane in case of an accident is somewhat better too.  If you lose the main power system, you can glide pretty effectively, although finding a landing strip in the urban jungle does not sound like a good idea.  More practically, you can carry a second engine.  Each one can be just barely capable of getting the thing around, and both of them put together will probably be less than half as powerful (and heavy) as a helicopter’s, meaning way less weight.  Control systems failures are trickier, but airplanes can be engineered with redundancy: a rudder can make up for an engine slowing down or vice versa, clever use of ailerons and flaps can cover for a failed elevator, etc.  It turns out that even two wings are [one more than necessary](http://www.youtube.com/watch?v=ZaXMrFh3n7M), a fact that surprised everyone including the pilot at the time.


The tough part of airplanes is the maneuvering.  Stabilization is the same as for helicopters.  Flying to the right neighborhood through the open air is more or less a [solved problem](http://diydrones.com).  Much more difficult is coming down to ground level and zig-zagging your way up the driveway. Some [progress has been made](http://www.youtube.com/watch?v=kYs215TgI7c&feature=player_embedded#!), but the state of the art today still requires a super-accurate 3D map of the environment. Still, we’ll get there in time.


The tough bit is the final dropoff and subsequent takeoff.  You’ve got three options.

1. **The bombing run.**  Fly over your doorstep and drop the package.  Problem: cruelly shattered Doritos Locos.
2. **The dropoff.**  Land the plane, release the package gently, take off again. Problem: only works for homes with small runways.
3. **The helicopter imitation.**  Take advantage of your thrust-to-weight ratio and just set the thing down while hanging from your propeller. Problem: have to carry enough engine power to lift your plane and your package, which basically means you’re now a helicopter with ailerons.


And all of these suffer from one more issue, which is the “idiot walked in front of my plane” problem.  In the bombing run or the dropoff, you have a potential collision.  In the helicopter imitation, you have the risk of having to shut off your propeller – and then you can’t get airborne again without a runway.


## Multicopter


At last, we get to the belle of the ball – the multicopter.  Whether it’s a [quad](http://www.hobbyking.com/hobbyking/store/__26023__Mini_Beetle_Quadcopter_RTF_Mode_2_.html), [Y4](http://www.hobbyking.com/hobbyking/store/__20986__Hobbyking_Y4_Scorpion_Glass_Fiber_Micro_Multi_Rotor_Frame_320mm_x_220mm_w_Motors.html), [hex](http://www.hobbyking.com/hobbyking/store/__24380__Turnigy_Integrated_PCB_Micro_Hex_KIT_.html), [octo](http://www.mikrokopter.de/ucwiki/en/MK-OktoXL), or something [really wierd](http://www.youtube.com/watch?v=L75ESD9PBOw), multicopters have shown up from nowhere to become all the rage.  And that’s because of your phone.


Well, not just your phone.  Everyone’s phone.  Also their Wiis, their Rock Band guitars, and all the other products that have driven demand for cheap solid-state gyroscopes and accelerometers through the roof.  A single high-quality gyro used to go for a thousand bucks.  Now, you can get 3 gyros, 3 accelerometers, and a nice CPU to manage the whole thing for [under a sawbuck](https://www.sparkfun.com/products/10937).  (For [$2 more](http://www.hobbyking.com/hobbyking/store/uh_viewItem.asp?idProduct=12974) you get a CPU to manage the whole thing, and an open-source flight stabilization program preloaded to boot).


You see, quadrotors need a lot of stabilization to fly.  What’s more, there has to be some onboard brains to actually coordinate even the simplest turns.  On a helicopter or a plane, the rudder stick moves the rudder servo.  On a multicopter, it’s got to slow down the counter-clockwise-spinning blades, while accelerating the clockwise-spinning-blades enough to make up the difference.  All the while stabilizing the whole thing from wind gusts and the like.


So these just weren’t very practical until a few years ago when position sensor prices dropped two zeroes.  But now they’re practical and awesome.


#### Advantage one: There’s only one thing you have to get right.


Helicopters are a nightmare of motors, servos, control linkages, and swashplates.  All those different parts have to be engineered right, or you’re mowing the lawn (briefly).  With quadrotors, there’s just one moving part: motors. Lots of motors. And these are modern, brushless motors – a ring of permanent magnets around a bundle of wires.  No commutators or brushes or whatnot.  The engineers can focus all their energy on just nailing this one, simple thing.


#### Advantage two: Cheap redundancy


To get redundancy in a helicopter or plane, you have to double the lifting power.   For a multicopter, you just add arms.  A pentarotor can lose a motor and still be fine (assuming the remaining motors have enough lift).  For more redundancy, add more and build a hex or octo.  The key bits that like to go boom (battery, speed controller, motor) are all separated, so you can lose them without bringing down the whole shebang.  In fact, the only single points of failure are the RC receiver and the controller board (and clever engineering can build redundancy in to those as well).


#### Advantage three: Blade guards


While you do pay a price in performance, a multicopter is the only one of the three aircraft designs that works reasonably well with [blade guards](http://ardrone.parrot.com/parrot-ar-drone/select-site/splash_ar2.jpg).  These may come in handy when the house you’re delivering to has a cat that likes to chase birds.


#### Advantage four: Prop mass


A multicopter spreads out its lift across many rotors, so each one can be smaller, lighter, and more fragile.  Sound like a bad thing?  Not when it hits your leg.


## **Design: The Bottom Line**


For maximum airtime, a plane wins hands down.  But for mono- and multi-copters, 20 minutes on a charge is easily achievable.  That gives you a range of over five miles (10 miles roundtrip) at a modest 40mph speed.  The Taco Bell density of Seattle is about 1 per 22 square miles, meaning the average home is just 2 miles away (as the ‘copter flies).


For the actual delivery, helicopters have the edge on agility.  They can accelerate upwards and downwards, and change thrust on a dime, while multicopters have to deal with rotor inertia.  That said, it’s something of a theoretical  limitation – multicopters can [do just fine](http://www.youtube.com/watch?v=E7X0_6o9J10).  Certainly well enough to get the taco to your door.  But this is where airplanes fall out of the contest.  They’re just not agile enough to deliver the goods and get home, particularly not when carrying a full load of junk food.


Ultimately, it’s all going to come down to robustness and safety.  And here it’s no contest.  Multicopters’ simpler design, easy redundancy, lower prop mass, and ability to support blade guards mean that multi-taco-copters outperform heli-taco-copters in the crucial tiebreaker of “not killing people with spinning death from above”.


So there you have it.  FAA, get a move on.  I’m getting hungry and the multicopters are restless.


## Postscript: Want one?


Start with a plane.  [You can do this for under a hundred bucks](http://boingboing.net/2009/10/21/a-geeky-introduction.html) and you’ll get many of the necessary skills quickly & cheaply.


The [AR Drone](http://ardrone.parrot.com/parrot-ar-drone/select-site) lies  in the uncanny valley between “You fly it” and “It flies itself”, which leaves you feeling like you’re fighting with an unseen autopilot who has the intelligence and attention span of a chihuahua. I don’t recommend it.


Instead (and for half the price), once you can keep your plane airborne, [the Blade mQX](http://www.horizonhobby.com/products/blade-mqx-bnf-BLH7580) is an ideal first quadcopter.  If your transmitter (from the plane) was made by Spektrum, you can re-use it.


Then you’re ready to rumble.  Get yourself started at [diydrones](http://diydrones.com) to learn about electronics, [rcgroups](http://rcgroups.com) to learn about hardware, and [hobbyking](http://hobbyking.com) for buying both on the cheap.


Happy flying!

[Powered by](https://follow.it)

You might want to [subscribe](https://www.danshapiro.com/blog/feed/) or [follow me on Twitter](https://www.twitter.com/danshapiro) so you don't miss new articles.
