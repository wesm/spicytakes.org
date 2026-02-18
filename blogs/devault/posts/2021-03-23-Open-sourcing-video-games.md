---
title: "The complete guide for open sourcing video games"
date: 2021-03-23
url: https://drewdevault.com/2021/03/23/Open-sourcing-video-games.html
slug: Open-sourcing-video-games
word_count: 2384
---

Video games are an interesting class of software. Unlike most software, they are
a creative endeavour, rather than a practical utility. Where most software
calls for new features to address practical needs of their users, video games
call for new features to serve the creative vision of their makers. Similarly,
matters like refactoring and paying down tech debt are often heavily
de-prioritized in favor of shipping something ASAP. Many of the collaborative
benefits of open source are less applicable to video games. It is perhaps for
these reasons that there are very few commercial open source games.

However, there are some examples of such games, and they have had a great deal
of influence on gaming.  Id is famous for this, having released the source code
for several versions of DOOM. The Quake engine was also released under the GPL,
and went on to be highly influential, serving as the basis for dozens of games,
including time-honored favorites such as the Half Life series. Large swaths of
the gaming canon were made possible thanks to the generous contributions of open
source game publishers.

Publishing open source games is also a matter of historical preservation.
Proprietary games tend to atrophy. Long after their heyday, with suitable
platforms scarce and physical copies difficult to obtain, many games die a slow
and quiet death, forgotten to the annals of time. Some games have overcome this
by releasing their source code, making it easier for fans to port the game to
new platforms and keep it alive.

What will your game’s legacy be? Will it be forgotten entirely, unable to run on
contemporary platforms? Will it be source-available, occasionally useful to the
devoted player, but with little reach beyond? Perhaps it goes the way of DOOM,
living forever in ports to hundreds of devices and operating systems. Maybe it
goes the way of Quake, its soul forever a part of the beloved classics of the
future. If you keep the source code closed, the only conclusion is the first:
enjoyed once, now forgotten.

With this in mind, how do you go about securing your game’s legacy?

## Source available: the bare minimum

The bare minimum is to make your game “source available”. Be aware that this is
not the same thing as making it open source! Some of your famous peers in this
category include Alien 3, Civilization IV and V, Crysis, Deus Ex, Prince of
Persia, Unreal Tournament, and VVVVVV.

This approach makes your source code available to view and perhaps to compile
and run, but prohibits derivative works. This is definitely better than leaving
it closed source: it provides helpful resources for modders, speedrunners, and
other fans; and devoted players may be able to use it as the basis for getting
the game running on future platforms, albeit alone and unable to share their
work.

If you choose a minimal enforcement approach, then some players might ultimately
share their work, but you’re leaving them on tenuous legal grounds. I would
recommend this if you’re very protective of your IP, but know that you’re
limiting the potential second life of your game if you take this approach.

## Copyleft with proprietary assets

The next step up is to make your game open source using a  *copyleft*  license,
but refraining from extending the license to the assets — anyone who wants
to get the source code working would either need to buy the game from you and
extract the assets, or supply their own community-made assets. This is a popular
approach among open source games, and gives you most of the benefits and few of
the drawbacks. You’ll join the ranks of our DOOM and Quake examples, as well as
Amnesia: the Dark Descent, System Shock, Duke Nukem 3D, and Wolfenstein 3D.

Games like this enjoy a long life as their software is more easily ported to new
platforms and shared with other users. DOOM runs on phones, digital cameras,
ATMs, even toasters! Its legacy is secure without any ongoing commitment from
the original developers. This also allows derivatives works — new games
based on your code — though it may turn some developers away. Using a
copyleft license like the  [GPL](https://www.gnu.org/licenses/gpl-3.0.en.html) 
requires derivative works to  *also*  be made open source. The community generally
has no problem with this, but it may affect the willingness of future developers
to incorporate your work into their own commercial games. I personally think
that the proliferation of open source software that’s implied in the use of a
copyleft license is a positive thing — but you may want to use another
approach.

## Permissive license, proprietary assets

If you want to allow your source code to find its way into as many future games
as possible, a permissive open source license like  [MIT](https://opensource.org/licenses/MIT)  is the way to go.
 [Flotilla](https://github.com/blendogames/flotilla)  is an example of a game
which went with this approach. It allows developers to incorporate your source
code into their own games with little restriction, either by creating a direct
derivative, or by taking little samples of your code and incorporating it into
their own project. This comes with no obligation to release their own changes or
works in a similar fashion: they can just take it, with very few strings
attached. Such an approach makes it very easy to incorporate into new commercial
games.

This is the most selfless way to release your code. I would recommend this if
you don’t care about what happens to your code later, and you just want to make
it open source and move on. Though this will definitely enable the largest
number of future projects to make use of your work, the copyleft approach is
better for ensuring that the largest possible number of future games are  *also* 
open source.

## Open assets

If you’re feeling especially generous, you could release the assets, too. Good
licenses for this includes the  [Creative Commons](https://creativecommons.org/) 
licenses. All of them permit free redistribution of your assets, so future
players won’t have to buy your game to get them. This could be important if the
distribution platform you used is defunct, or if you’re not around to buy it
from — consider this well before deciding that you’d rather keep your
share of the dwindling asset sales as your game ages.

Using Creative Commons also allows you to tune the degree to which your assets
may be re-used. You can choose different CC licenses to control the
commercialization of your assets and use in derivative works. To allow free
redistribution and nothing else, the CC-NC-ND license (noncommercial, no
derivatives) will do the trick. The CC-BY-SA license is the copyleft of creative
commons: it will allow free redistribution, commercialization, and derivative
works,  *if*  the derivatives are also shared with the same rights. The permissive
approach is CC-0, which is equivalent to releasing your assets into the public
domain.

Permitting derivatives and re-commercialization of your assets can save a lot of
time for new game developers, especially indie devs with a small budget. It’s
also cool for making derivative  *games* , similar to modding, where creative
players can remix your assets to make a new game or expansion pack.

## What if I don’t completely own my game?

You can’t give away the rights to anything you don’t own. If you rely on
proprietary libraries, or a third-party level editor, or you don’t own the
rights to the music or sprites, you cannot make them open source.

In this situation, I recommend open sourcing everything that you’re able to.
This might mean that you open source an ultimately broken game — it simply
might not work, or not even compile, without these resources. This is
unfortunate, but by releasing everything you can, you leave your community in a
good position to fill in the gaps themselves, perhaps by refactoring your code
to work around them, or by replacing the proprietary bits with free
alternatives. This also allows the parts of your game which are open to be
reused in future games.

## But cheaters could use it!

This is true. And it’s worth noting that if your game has a mandatory online
component based on your own servers, then making it open source doesn’t make
nearly as much sense, especially if you ultimately decide to shut those servers
off.

There is a trade-off to be made here. In truth, it’s very difficult to prevent
cheating in your game. If you’ve made a popular competitive multiplayer game,
you and I both know that there are still cheaters using it despite your best
efforts. Keeping it proprietary is not going to stave off cheaters. Social
solutions are better — like a system to report cheaters, or to let friends
play on private servers.

Making your game open source might help less skilled script kiddie figure out
how to cheat more easily in your game. I can’t decide for you if the trade-off
is worth it for your game, but I can tell you that the benefits of making it
open are vast, and the efficacy of keeping it closed to prevent cheating is
questionable.

## But my code is embarrassing!

So is everyone else’s. 🙂 We all know that games are running up against tight
deadlines and clean code is not going to be the #1 priority. I assure you that
your community will be too busy having fun to judge you for the quality of your
code. The idea that it just needs to be “cleaned up” first is the death of many
projects which would otherwise have been made open source. If you feel this way,
you will probably never be satisfied, and thus you’ll never open it. I assure
you: your game is ready to make open source, no matter what state it’s in!

Bonus: Ethan Lee tipped me off to some truly awful code which was left in
VVVVVV, which you can freely browse on the  [2.2 tag](https://github.com/TerryCavanagh/vvvvvv/tree/2.2) . It’s not
great, but you probably didn’t know that — you only remember VVVVVV as a
critically acclaimed game. Game developers are working under tight constraints
and no one is judging them for that — we just want to have fun!

## So what do I need to do?

Let’s lay out the specific steps. You need to answer the following questions
first:

* Do I actually own the entire game? What parts am I allowed to open source?
* Will I make the code source-available, copyleft, or permissively licensed?
* And the assets? Proprietary? Creative Commons? If the latter, which version?

If you’re not sure what’s best, I would recommend using the GPL for your code,
and CC-BY-SA for the assets. This allows for derivative works, so long as
they’re also made open with a similar license. This enables the community to
build on your work, porting it to new platforms, building a thriving modding
community, and freely sharing your assets, ensuring an enduring legacy for your
game. If you’d like to decide the details for yourself, review the comments
above once again and pick out the licenses you’d like to use for each before
moving on.

If you need help with any of these steps, or have any questions, please  [send me
an email](mailto:sir@cmpwn.com) , and I will help you to the best of my ability.

**Publishing the source code**

Prepare an archive of your source code, and add the license file. If you went
with the source-available approach, simply write “Copyright ©
< *you* > < *current year* >. All rights reserved.” into a text file
named LICENSE. If you chose something else, copy the license text into a
LICENSE file.

If you want this over with quickly, just stick the code and license into a zip
file or a tarball and drop it on your website. A better approach, if you have
the patience, would be to publish it as a git repository. If you already use
version control, you may want to consider carefully if you want to publish your
full version control history — the answer might be “yes”, but if you’re
unsure, the answer is probably “no”. Just make a copy of the code, delete the
.git directory, and import it into a new repository if you need to.

Double check that you aren’t checking in any artifacts — assets,
executables, libraries, etc — and then push it to the hosting service of
your choice. GitHub is a popular choice, but I would selfishly recommend
 [sourcehut](https://sourcehut.org)  as well. If you have time, write a little
README file which gives an introduction to the project as well.

**Publishing the assets**

If you choose to leave the assets proprietary, then there are no further steps.
Players can figure out how to extract the assets from their purchased game.

If you choose to make them open, prepare an archive of your assets. Include a
copy of the license you choose — e.g. which Creative Commons license you
used — and drop it into a zip file or a tarball or something similar.
Stick this on your website, and if you’re feeling generous, prepare some
instructions for how to incorporate the asset bundle into the game once a player
compiles your code.

**Tell the world!**

Let everyone know that you’ve made your game open source! Write a little blog
post, link to the source and assets, and enjoy a little bit more of the
limelight while the press and the community thanks you for your contribution.

One final request on this note: if you choose the source-available approach,
please refer to it as such in your public statements. Source available is  *not* 
the same thing as “open source”, and the distinction is important.

And now it’s my turn to thank you: I’m so happy that you’ve released your game
as an open source project! The community is much richer for your contribution to
it, and I hope that your game will live on for many years to come, both in self
through ports and mods, and in spirit through its contributions to future games.
You’ve done a wonderful thing. Thank you!

If you found this guide helpful in publishing your game, please  [email
me](mailto:sir@cmpwn.com)  so I can play it!

List of FOSS games inspired by this guide:

* [Castaway](https://www.usebox.net/jjm/blog/castaway-source-code/)
* [The Return of Traxtor](https://www.usebox.net/jjm/blog/the-return-of-traxtor-cpc-source-code/)
* Yours?
