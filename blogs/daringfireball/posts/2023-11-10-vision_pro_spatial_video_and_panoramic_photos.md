---
title: "Vision Pro, Spatial Video, and Panoramic Photos"
date: 2023-11-10
url: https://daringfireball.net/2023/11/vision_pro_spatial_video_and_panoramic_photos
slug: vision_pro_spatial_video_and_panoramic_photos
word_count: 2840
---


Yesterday [Apple released developer beta 2 of iOS 17.2](https://daringfireball.net/linked/2023/11/09/ios-17-2-beta-2-spatial-video), the first version of iOS to include support for capturing spatial video with iPhone 15 Pro models. Today came the public beta, enabling the same feature. Apple invited me to New York yesterday, not merely to preview capturing spatial video using an iPhone, but to experience watching those spatial videos using a Vision Pro.


The experience was, like my first Vision Pro demo back at WWDC in June, astonishing.


## Capturing Spatial Video on an iPhone


Shooting spatial video on an iPhone 15 Pro is easy. The feature is — for now at least — disabled by default, and can be enabled in Settings → Camera → Formats. The option is labeled “Spatial Video for Apple Vision Pro”, which is apt, because (again, for now at least) spatial video only looks different from non-spatial video when playing it back on Vision Pro. When viewed on any other device it just looks like a regular flat video.


Once enabled, you can toggle spatial video capture in the Camera app whenever you’re in the regular Video mode. It’s very much akin to the toggle for Live Photos when taking still photos, or the Action mode toggle for video — not a separate mode in the main horizontal mode switcher in Camera, but a toggle button in the main Video mode.


When capturing spatial video, you have no choice regarding resolution, frame rate, or file format. All spatial video is captured at 1080p, 30 fps, in the HEVC file format.1 You also need to hold the phone horizontally, to put the two capturing lenses on the same plane. The iPhone uses the main (1×) and ultra wide (0.5×) lenses for capture when shooting spatial video, and in fact, Apple changed the arrangement of the three lenses on the iPhone 15 Pro in part to support this feature. (On previous iPhone Pro models, when held horizontally, the ultra wide camera was on the bottom, and the main and telephoto lenses were next to each other on the top.)


I believe resolution is limited to 1080p because to get an image from the ultra wide 0.5× camera that is the equivalent field of view as from the main 1× camera, it needs to crop the ultra wide image significantly. The ultra wide camera has a mere 12 MP sensor, so there just aren’t enough pixels to crop a 1× equivalent field of view from the center of the sensor and get a 4K image.


There are two downsides to shooting spatial video with your iPhone. First, the aforementioned 1080p resolution and 30 fps frame rate. I’ve been shooting 4K video by default for years, because why not? I wish we could capture spatial video at 4K, but alas, not yet. The second downside to shooting spatial video is that it effectively doubles the file size compared to non-spatial 1080p, for the obvious reason that each spatial video contains two 1080p video streams. That file-size doubling is a small price to pay — the videos are still smaller than non-spatial 4K 30 fps video.2


Really, it’s just no big deal to capture spatial video on your iPhone. If the toggle button is off, you capture regular video with all the regular options for resolution (720p/1080p/4K) and frame rates (24/30/60). If the toggle for spatial video is on — and when on it’s yellow, impossible to miss — you lose those choices but it just looks like capturing a regular video. And when you play it back, or share it with others who are viewing it on regular devices like their phones or computers, it just looks like a regular flat video.


If you own an iPhone 15 Pro, there’s no good reason not to start capturing spatial videos this year — like, say, this holiday season — to record any sort of moments that feel like something you might want to experience as “memories” with a Vision headset in the future, even if you don’t plan to buy the first-generation Vision Pro next year.


## Viewing Spatial Video on Vision Pro


Before my demo, I provided Apple with my eyeglasses prescription, and the Vision Pro headset I used had appropriate corrective lenses in place. As with my demo back in June, everything I saw through the headset looked incredibly sharp.


Apple has improved and streamlined the onboarding/calibration process significantly since June. There are a few steps where you’re presented with a series of dots in a big circle floating in front of you, like the hour indexes on a clock. As you look at each circle, it lights up a bit, and you do the finger tap gesture. It’s the Vision Pro’s way to calibrate that what it thinks you’re looking is what you actually are looking at. Once that calibration step was over — and it took just a minute or two — I was in, ready to go on the home screen of VisionOS. (And the precision of this calibration is amazing — UI elements can be placed relatively close to each other and it knows exactly which one you’re looking at when you tap. iOS UI design needs to be much more forgiving of our relatively fat fingertips than VisionOS UI design needs to be about the precision of our gaze.)


My demo yesterday was expressly limited to photography in general, and spatial video in particular, and so my demo was, per Apple’s request, limited to the Photos app in VisionOS. It was tempting, at times, to see where else I could go and what else I could do. But there was so much to see and do in Photos alone that my demo — about 30 minutes in total wearing Vision Pro — raced by.


Prior to separating us in smaller rooms for our time using Vision Pro, I was paired with Joanna Stern from The Wall Street Journal for a briefing on the details of spatial video capturing using the iPhones 15 Pro. We were each provided with a demo iPhone, and were allowed to capture our own spatial videos. We were in a spacious modern high-ceiling’d kitchen, bathed in natural light from large windows. A chef was busy preparing forms of sushi, and served as a model for us to shoot. Joanna and I also, of course, shot footage of each other, while we shot each other. It was very meta. The footage we captured ourselves was then preloaded onto the respective Vision Pro headsets we used for our demos.


We were not permitted to capture spatial video on Vision Pro.3 However, our demo units had one video in the Photos library that was captured on Vision Pro — a video I had experienced before, back in June, of a group of twenty-somethings sitting around a fire pit at night, having fun in a chill atmosphere. There were also several other shot-by-Apple spatial videos which were captured using an iPhone 15 Pro.


One obvious question: How different do spatial videos captured using iPhone 15 Pro look from those captured using a Vision Pro itself? Given that Apple provided only one example spatial video captured on Vision Pro, I don’t feel like I can fully answer that based on my experience yesterday. It did not seem like the differences were dramatic or significant. The spatial videos shot using iPhone 15 Pro that I experienced, including those I captured myself, seemed every bit as remarkable as the one captured using Vision Pro.


Apple won’t come right out and say it but I do get the feeling that all things considered, spatial video captured using Vision Pro will be “better”. The iPhone might win out on image quality, given the fact that the 1× main camera on the iPhone 15 Pro is the single best camera system Apple makes, but the Vision Pro should win out on spatiality — *3D-ness* — because Vision Pro’s two lenses for spatial video capture are roughly as far apart from each other as human eyes. The two lenses used for capture on an iPhone are, of course, much closer to each other than any pair of human eyes. But despite how close the two lenses are to each other, the 3D effect is *very* compelling on spatial video captured on an iPhone. It’s somehow simultaneously very natural-looking and utterly uncanny.


It’s a stunning effect and remarkable experience to watch them. And so the iPhone, overall, is going to win out as the “best” capture device for spatial video — even if footage captured on Vision Pro is technically superior — because, as the old adage states, the best camera is the one you have with you. I have my iPhone with me almost everywhere. That will never be even close to true for Vision Pro next year.


[Here’s what I wrote about spatial video back in June, after my first hands-on time with Vision Pro](https://daringfireball.net/2023/06/first_impressions_of_vision_pro_and_visionos):


> Spatial photos and videos — photos and videos shot with the 
> Vision Pro itself — are viewed as a sort of hybrid between 2D 
> content and fully immersive 3D content. They don’t appear in a 
> crisply defined rectangle. Rather, they appear with a hazy 
> dream-like border around them. Like some sort of teleportation 
> magic spell in a Harry Potter movie or something. The effect 
> reminded me very much of Steven Spielberg’s *Minority Report*, in 
> the way that Tom Cruise’s character [could obsessively watch 
> “memories” of his son](https://hachyderm.io/@tcook/110509376936866896), and the way the psychic “precogs” 
> perceive their visions of murders about to occur. It’s like 
> watching a dream, but through a portal opened into another world.


When you watch regular (non-spatial) videos using Vision Pro, or view regular still photography, the image appears in a crisply defined window in front of you. Spatial videos don’t appear like that at all. I can’t describe it any better today than I did in June: it’s like watching — and listening to — a dream, through a hazy-bordered portal opened into another world.


Several factors contribute to that dream-like feel. Spatial videos don’t look *real*. It doesn’t look or feel like the subjects are truly there in front of you. That *is* true of the live pass-through video you see in Vision Pro, of the actual real world around you. That pass-through video of actual reality is so compelling, so realistic, that in both my demo experiences to date I forgot that I was always looking at video on screens in front of my eyes, not just looking through a pair of goggles with my eyes’ own view of the world around me.


So Vision Pro is capable of presenting video that looks utterly real — because that’s exactly how pass-through video works and feels. Recorded spatial videos are different. For one thing, reality is not 30 fps, nor is it only 1080p. This makes spatial videos not look low-resolution or crude, per se, but rather more like movies. The upscaled 1080p imagery comes across as film-like grain, and the obviously-lower-than-reality frame rate conveys a movie-like feel as well. Higher resolution would look better, sure, but I’m not sure a higher frame rate would. Part of the magic of movies and TV is that 24 and 30 fps footage has a dream-like aspect to it.


Nothing you’ve ever viewed on a screen, however, can prepare you for the experience of watching these spatial videos, especially the ones you will have shot yourself, of your own family and friends. They truly are more like memories than videos. The spatial videos I experienced yesterday that were shot by Apple looked *better* — framed by professional photographers, and featuring professional actors. But the ones I shot myself were more compelling, and took my breath away. There’s my friend, Joanna, right in front of me — like I could reach out and touch her — but that was 30 minutes ago, in a different room.


Prepare to be moved, emotionally, when you experience this.


## Panoramic and Still Photos


My briefing and demo experience yesterday was primarily about capturing spatial video on iPhone 15 Pro and watching it on Vision Pro, but my demo went through the entire Photos app experience in VisionOS.


Plain old still photos look *amazing*. You can resize the virtual window in which you’re viewing photos to as large as you can practically desire. It’s not merely like having a 20-foot display — a size far more akin to that of a movie theater screen than a television. It’s like having a 20-foot display with retina quality resolution, and the best brightness and clarity of any display you’ve ever used. I spend so much time looking at my own iPhone-captured still photos on my iPhone display that it’s hard to believe how good they can look blown up to billboard-like dimensions. Just plain still photos, captured using an iPhone.


And then there are panoramic photos. Apple first introduced Pano mode back in 2012, with the introduction of the iPhone 5. That feature has never struck me as better than “Kind of a cool trick”. In the decade since the feature has been available, I’ve only taken about 200 of them. They just look too unnatural, too optically distorted, when viewed on a flat display. And the more panoramic you make them, the more unnatural they look when viewed flat.


Panoramic photos viewed using Vision Pro are breathtaking.


There is no optical distortion at all, no fish-eye look. It just looks like you’re standing at the place where the panoramic photo was taken — and the wider the panoramic view at capture, the more compelling the playback experience is. It’s incredible, and now I wish I’d spent the last 10 years taking way more of them.


As a basic rule, going forward, I plan to capture spatial videos of *people*, especially my family and dearest friends, and panoramic photos of *places* I visit. It’s like teleportation.


## Miscellaneous Observations


The Vision Pro experience is highly dependent upon [foveated rendering](https://en.wikipedia.org/wiki/Foveated_rendering), which Wikipedia succinctly describes as “a rendering technique which uses an eye tracker integrated with a virtual reality headset to reduce the rendering workload by greatly reducing the image quality in the peripheral vision (outside of the zone gazed by the fovea).” Our retinas work like this too — we really only see crisply what falls on the maculas at the center of our retinas. Vision Pro really only renders at high resolution what we are directly staring at. The rest is lower-resolution, but that’s not a problem, because when you shift your gaze, Vision Pro is extraordinarily fast at updating the display.


I noticed yesterday that if I darted my eyes from one side to the other fast enough, I could sort of catch it updating the foveation. Just for the briefest of moments, you can catch something at less than perfect resolution. I think. It is so fast fast fast at tracking your gaze and updating the displays that I can’t be sure. It’s just incredible, though, how detailed and high resolution the overall effect is. My demo yesterday was limited to the Photos app, but I came away more confident than ever that Vision Pro is going to be a great device for reading and writing — and thus, well, *work*.


The sound quality of the speakers in the headset strap is impressive. The visual experience of Vision Pro is so striking — I mean, the product has “Vision” in its name for a reason — that the audio experience is easy to overlook, but it’s remarkably good.


Navigating VisionOS with your gaze and finger taps is so natural. I’ve spent a grand total of about an hour, spread across two 30-minute demos, using Vision Pro, but I already feel at home using the OS. It’s an incredibly natural interaction model based simply on what you are looking at. My enthusiasm for this platform, and the future of spatial computing, could not be higher.


---

1. The HEVC spec allows for a single file to contain multiple video streams. That’s what Apple is doing, with metadata describing which stream is “left” and which is “right”. [Apple released preliminary documentation for this format](https://developer.apple.com/av-foundation/HEVC-Stereo-Video-Profile.pdf) back in June, just after WWDC. ↩︎
2. According to Apple, these are the average file sizes per minute of video:
• Regular 1080p 30 fps: 65 MB
3. Paraphrased:
“This is the digital crown. You’ll be using this today to adjust the immersiveness by turning it, and you’ll press the crown if you need to go back to the home screen. On the other side is the button you would use to capture photos or videos using Vision Pro. We won’t be using that button today.”
“But does that button work? If I did press that button, would it capture a photo or video?”
“Please don’t press that button.” ↩︎︎



| **Previous:** | [The 2023 M3 MacBook Pros](https://daringfireball.net/2023/11/the_2023_m3_macbook_pros) |
| **Next:** | [Qualcomm’s Awkward Boasting Regarding Its Forthcoming X Elite Platform](https://daringfireball.net/2023/11/qualcomm_awkward_boasting) |


PreviousNext