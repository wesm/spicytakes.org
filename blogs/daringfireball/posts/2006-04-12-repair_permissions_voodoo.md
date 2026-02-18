---
title: "Seriously, ‘Repair Permissions’ Is Voodoo"
date: 2006-04-12
url: https://daringfireball.net/2006/04/repair_permissions_voodoo
slug: repair_permissions_voodoo
word_count: 1124
---


Boot Camp mania hasn’t caused me to forget about those of you who,
despite last week’s “[‘Repair Permissions’ Is Not a Recommended Step
When Applying System Updates](http://daringfireball.net/2006/04/repair_permissions)”, still believe, or want to
believe, in the voodoo of running “Repair Permissions” as a periodic
maintenance task.


One problem is the name of the feature itself; either “Restore
Permissions” or “Reset Permissions” would be a more apt name.
“Repair” makes it sound as though files are broken if their
permissions are affected by this process; that’s not the case. Files
might have perfectly valid permissions but differ from what’s
expected by the Repair Permissions process.


According to [Apple’s own description of the feature](http://docs.info.apple.com/article.html?artnum=25751):


> When you use Disk Utility to verify or repair disk permissions,
> it reviews each of the .bom files in */Library/Receipts/* and
> compares its list to the actual permissions on each file listed.
> If the permissions differ, Disk Utility reports the difference
> (and corrects them if you use the Repair feature).


However, just because a file’s current permissions differ from its
original permissions as specified in the corresponding BOM file,
does not mean that the current permissions are “wrong”. The reason
this feature exists is that sometimes, the permissions *are* wrong,
causing some sort of problem, and running Repair Permissions solves
the problem.


Back in the 10.0 and 10.1 era, these permissions problems occurred
frequently due to bugs in the system itself. In my experience, these
bugs were long ago eradicated, if not in 10.2, then by 10.3. I think
many people who experience “permissions” problems under 10.3 and
10.4 caused the problems themselves, by diddling with system files
they ought not have diddled with.


If you are not experiencing any symptoms that would indicate
permission-related problems, there is no reason to run Repair
Permissions. Repair Permissions is not a periodic maintenance task
or a preventive measure.


Arguing that you (a) run Repair Permissions all the time and (b)
have no permission problems, and then drawing the conclusion that
there’s a cause-and-effect relationship there, is like arguing that
your diligent avoidance of sidewalk cracks has a causal relationship
to the fact that your mother’s back is doing just fine.
Troubleshooting computers is science, not magic.


To be fair to everyone who persists in believing that it *is* a
periodic maintenance task, there is at least [one Apple support
documentation that hints that it is](http://docs.info.apple.com/article.html?path=Mac/10.4/en/mh1928.html), but note the title of
that document: “My Computer Keeps Freezing or I See a Flashing
Question Mark”.


Even if you “verify” permissions and it shows some that don’t match,
it doesn’t mean they’re *wrong*. They might be wrong, but they might
just be different but still OK.


Those of you who do this probably aren’t doing any harm to your
system, but you’re wasting an awful lot of your time. Running Repair
Permissions before you have an actual permissions problem is like
taking antibiotics before you’re actually sick.


Don’t just take my word for all of this; here’s a weblog post titled
“[Exercises in Futility Part 2: Repairing Permissions Is
Useless](http://www.unsanity.org/archives/000410.php)” by Unsanity’s Rosyna from last May:


> As [Jason Harris](http://www.geekspiff.com/) said (and I am
> paraphrasing), “Repairing permissions is zapping the PRAM for
> the twenty-first century”. I couldn’t agree more. Both are
> equally futile attempts to fix a completely unrelated problem.
> In other words, 99% of the time, neither will fix nor prevent
> any problem. Especially not the problems they are recommended
> for. Covering yourself in vaseline and rolling around naked in
> the dirt and repairing permissions are just as likely to fix
> your Mac OS X problem. People swear by repairing permissions
> as often as they save files and present as proof the fact they
> don’t have any problems. That’s rather [specious
> reasoning](http://www.snpp.com/episodes/3F20.html).


When Rosyna and I are in nearly complete agreement, that’s
something, and I think the odds are pretty good we’re right.


## MacFixIt Madness


The page is now hidden behind their subscribers-only firewall, but
here are MacFixIt’s [absurd upgrade instructions for Mac OS X
10.4.6](http://www.macfixit.com/article.php?story=20060403142321217):


> We recommend the following procedure when installing Mac OS X
> 10.4.6.
> First, avoid performing any other operations (in Mac OS X or
> third-party applications) while the update process is occurring.
> In addition, before installing this security update, make sure all
> Apple-installed applications and utilities are in their original
> locations. Moving one of these applications to a different
> location on your hard drive can lead to an incomplete update.
> Also, disconnect any FireWire/USB devices before applying Mac OS X
> 10.4.6, then re-connect the devices one by one after the update
> process is complete and the system has restarted.


Well, that’s not too bad. I’m not sure what they mean by “re-connect
[*sic*] the devices one-by-one”, though, and I’m assuming mice and
keyboards are exempt from their unplug-all-USB-devices policy.


What comes next is where they dive deep into la-la land, and where
by “even more cautious”, they mean “totally nutso”:1


> If you’d like to take an even more cautious route, use the following
> process:
> First create a backup of your startup volume.
> Drag the folder com.apple.SoftwareUpdate located in
> */Library/Caches* (the Library folder at the root level of your
> hard drive) to the trash.
> Download the standalone version of Mac OS X 10.4.6 and save it
> for later.
> Startup (restart) your Mac using a drive other than your usual
> startup drive as the boot volume. This can include an eDrive
> created by TechTool Pro, or better, an external FireWire. Make
> sure that this drive includes a copy of Disk Utility (which can
> simply be copied from your normal startup volume).
> Launch Disk Utility from the temporary startup drive. Perform a
> “Repair Disk” operation on your normal startup drive (which
> should now appear as another mounted volume in the Finder)
> Again restart, this time booting from your normal startup
> volume, while holding the “Shift” key to boot in Safe Mode.
> Apply Mac OS X 10.4.6 and restart when prompted, this time
> without holding the “Shift” key.


They apparently forgot to document the initial step, where you wrap
your head in heavy-duty aluminum foil to block the mind-control
rays emitted from installer packages.2


And yet even *these* nutty instructions don’t mention running Repair
Permissions.


---

1. Except for the part about making a backup — that’s actually great advice. ↩︎
2. Where do you think [MindVision Software](http://www.mindvision.com/) got their name? ↩︎



| **Previous:** | [Several Asinine and/or Risky Ideas Regarding Apple’s Strategy That Boot Camp Does Not Portend](https://daringfireball.net/2006/04/asinine_and_or_risky_ideas) |
| **Next:** | [O’Grady v. Superior Court](https://daringfireball.net/2006/04/ogrady) |


PreviousNext