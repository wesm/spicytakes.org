---
title: "ASCII Pronunciation Rules for Programmers"
date: 2008-06-12
url: https://blog.codinghorror.com/ascii-pronunciation-rules-for-programmers/
slug: ascii-pronunciation-rules-for-programmers
word_count: 1313
---

As programmers, we deal with a lot of unusual keyboard characters that typical users rarely need to type, much less think about:

kg-card-begin: html

```

$ # % {} * [] ~ & <>

```

kg-card-end: html

Even the characters that are fairly regularly used in everyday writing – such as the humble dash, parens, period, and question mark – have radically different meaning in programming languages.


This is all well and good, but you’ll eventually have to read code out loud to another developer for some reason. And then you’re in an awkward position, indeed.


**How do you *pronounce* these unusual ASCII characters?**


We all do it, but we don’t necessarily think much about the words we choose. I certainly hadn’t thought much about this until yesterday, when I read the following comment left on [Exploring Wide Finder](https://blog.codinghorror.com/exploring-wide-finder/):


> A friend sent me a Java code fragment in which he looped through printing “Thank You!” a million times (it was a response to a professor who had extended the deadline on a paper). I responded with a single line of Ruby to do the same, and a single line of Lisp.
> He wrote back: “**Underscores, pipes, octothorpes, curly braces** – sheesh... I’ll take a mild dose of verbosity if means I don’t have to code something that looks like it’s been zipped already!”


What the heck is an [*octothorpe*](http://www.worldwidewords.org/weirdwords/ww-oct1.htm)*?* I know this as the *pound* key, but that turns out to be a US-centric word; most other cultures know it as the *hash* key.


I’m often surprised to hear what other programmers name their ASCII characters. Not that the words I personally use to identify my ASCII characters are any more correct, but there’s far more variability than you’d expect considering the rigid, highly literal mindset of most programmers.


Perhaps that’s why I was so excited to discover the [ASCII entry](http://catb.org/jargon/html/A/ASCII.html) in The New Hacker’s Dictionary, which Phil Glockner turned me on to. It’s a fairly exhaustive catalog of the common names, rare names, and occasionally downright *weird *names that programmers associate with the ASCII characters sprinkled throughout their code.


How many of these ASCII pronunciations do you recognize? Which ones are the “correct” ones in your shop?

kg-card-begin: html


|  | Common Names | Rare Names |
| **!** | **exclamation mark**
[bang](http://catb.org/jargon/html/B/bang.html)
pling
excl
not
shriek | factorial
exclam
smash
cuss
boing
yell
wow
hey
wham
eureka
spark-spot
soldier
control | factorial
exclam
smash
cuss
boing
yell | wow
hey
wham
eureka
spark-spot
soldier
control |
| factorial
exclam
smash
cuss
boing
yell | wow
hey
wham
eureka
spark-spot
soldier
control |
| **"** | **quotation marks**
quote
double quote | literal mark
double-glitch
dieresis
dirkrabbit-ears
double prime | literal mark
double-glitch
dieresis
dirk | rabbit-ears
double prime |
| literal mark
double-glitch
dieresis
dirk | rabbit-ears
double prime |
| **#** | **hash
**pound sign**
**number sign
pound**
**sharp
[crunch](http://catb.org/jargon/html/C/crunch.html)
hex
mesh | **hash
**pound sign**
**number sign
pound**
** | sharp
[crunch](http://catb.org/jargon/html/C/crunch.html)
hex
mesh | grid
crosshatch
octothorpe
flash
square
pig-pentictactoe
scratchmark
thud
thump
[splat](http://catb.org/jargon/html/S/splat.html) | grid
crosshatch
octothorpe
flash
square
pig-pen | tictactoe
scratchmark
thud
thump
[splat](http://catb.org/jargon/html/S/splat.html) |
| **hash
**pound sign**
**number sign
pound**
** | sharp
[crunch](http://catb.org/jargon/html/C/crunch.html)
hex
mesh |
| grid
crosshatch
octothorpe
flash
square
pig-pen | tictactoe
scratchmark
thud
thump
[splat](http://catb.org/jargon/html/S/splat.html) |
| $ | **dollar sign
**dollar | currency symbol
buck
cash
stringescape
ding
cache
big money | currency symbol
buck
cash
string | escape
ding
cache
big money |
| currency symbol
buck
cash
string | escape
ding
cache
big money |
| % | **percent sign
**mod
grapes | double-oh-seven |
| & | **ampersand**
amp
amper
and
and sign | address
reference
andpersand
bitand
background
pretzel |
| ' | **apostrophe**
single quote
quote | prime
glitch
tick
irk
pop
spark
closing single quotation mark
acute accent | prime
glitch
tick
irk | pop
spark
closing single quotation mark
acute accent |
| prime
glitch
tick
irk | pop
spark
closing single quotation mark
acute accent |
| ( ) | **opening / closing parenthesis
**left / right paren
left / right parenthesis
left / right
open / close
open / close paren
paren / thesis | so/already
lparen/rparen
opening/closing parenthesis
opening/closing round bracket
left/right round bracket
wax/wane
parenthisey/unparenthisey
left/right ear |
| **[ ]** | **opening / closing bracket
**left / right bracket
left / right square bracket
bracket / unbracket | square / unsquare
u turn / u turn back |
| **{ }** | **opening / closing brace**
open / close brace
left / right brace
left / right squiggly
left / right squiggly bracket/brace
left / right curly bracket/brace | brace / unbrace
curly / uncurly
leftit / rytit
left / right squirrelly
embrace / bracelet |
| **< >** | **less / greater than**
bra / ket
left / right angle
left / right angle bracket
left / right broket | from / into (or towards)
read from / write to
suck / blow
comes-from / gozinta
in / out
crunch / zap
tic / tac
angle / right angle |
| ***** | **asterisk
**star
splat | wildcard
gear
dingle
mult
spideraster
times
twinkle
[glob](http://catb.org/jargon/html/G/glob.html)
[Nathan Hale](http://catb.org/jargon/html/N/Nathan-Hale.html) | wildcard
gear
dingle
mult
spider | aster
times
twinkle
[glob](http://catb.org/jargon/html/G/glob.html)
[Nathan Hale](http://catb.org/jargon/html/N/Nathan-Hale.html) |
| wildcard
gear
dingle
mult
spider | aster
times
twinkle
[glob](http://catb.org/jargon/html/G/glob.html)
[Nathan Hale](http://catb.org/jargon/html/N/Nathan-Hale.html) |
| **+** | **plus**
add | cross
intersection |
| **,** | **comma** | cedilla
tail |
| - | **dash**
hyphen
minus | worm
option
dak
bithorpe |
| **.** | **period
**dot
point
decimal point | radix point
full stop
spot |
| **/** | **slash**
stroke
slant
forward slash | diagonal
solidus
over
slak
virgule
slat |
| **\** | **backslash
**hack
whack
escape
reverse slashslosh
backslant
backwhack | **backslash
**hack
whack
escape
reverse slash | slosh
backslant
backwhack | bash
reverse slant
reversed virgule
backslat |
| **backslash
**hack
whack
escape
reverse slash | slosh
backslant
backwhack |
| **:** | **colon** | dots
two-spot |
| **;** | **semicolon**
semi | weenie
hybrid
pit-thwong |
| **=** | **equals
**gets
takes | quadrathorpe
half-mesh |
| **?** | **question mark
**query
[ques](http://catb.org/jargon/html/Q/ques.html) | quiz
whatmark
what
wildcharhuh
hook
buttonhook
hunchback | quiz
whatmark
what
wildchar | huh
hook
buttonhook
hunchback |
| quiz
whatmark
what
wildchar | huh
hook
buttonhook
hunchback |
| **@** | **at sign
**at
strudel | each
vortex
whorl
whirlpool
cyclonesnail
ape
cat
rose
cabbage
commercial at | each
vortex
whorl
whirlpool
cyclone | snail
ape
cat
rose
cabbage
commercial at |
| each
vortex
whorl
whirlpool
cyclone | snail
ape
cat
rose
cabbage
commercial at |
| **^** | **circumflex
**caret**
**hat
control
uparrow | xor sign
chevron
shark (or shark-fin)
to the
fang
pointer |
| **_** | **underline**
underscore
underbar
under | score
backarrow
skid
flatworm |
| **`** | **grave accent**
backquote
left quote
left single quote
open quote
grave | backprime
backspark
unapostrophe
birk
blugleback tick
back glitch
push
opening single quote
quasiquote | backprime
backspark
unapostrophe
birk
blugle | back tick
back glitch
push
opening single quote
quasiquote |
| backprime
backspark
unapostrophe
birk
blugle | back tick
back glitch
push
opening single quote
quasiquote |
| **|** | **bar**
or
or-bar
v-bar
pipe
vertical bar | vertical line
gozinta
thru
pipesinta
spike |
| **~** | **tilde**
squiggle
[twiddle](http://catb.org/jargon/html/T/twiddle.html)
not | approx
wiggle
swung dash
enyay
sqiggle (sic) |


kg-card-end: html

If you’re curious about the derivation of some of the odder names here, there are an extensive set of footnotes (and even *more* possible pronunciations) at the ascii-table.com [pronunciation guide](https://web.archive.org/web/20080828003201/http://ascii-table.com/pronunciation-guide.php).


So the next time a programmer walks up to you and says, “oh, it’s easy! Just type wax bang at hash buck grapes circumflex and splat wane,” you’ll know what they mean.


Maybe.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[ascii](https://blog.codinghorror.com/tag/ascii/)
[communication](https://blog.codinghorror.com/tag/communication/)
[pronunciation](https://blog.codinghorror.com/tag/pronunciation/)
[character encoding](https://blog.codinghorror.com/tag/character-encoding/)
