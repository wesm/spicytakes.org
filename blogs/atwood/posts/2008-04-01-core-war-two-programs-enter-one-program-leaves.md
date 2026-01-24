---
title: "Core War: Two Programs Enter, One Program Leaves"
date: 2008-04-01
url: https://blog.codinghorror.com/core-war-two-programs-enter-one-program-leaves/
slug: core-war-two-programs-enter-one-program-leaves
word_count: 906
---

Our [old pal A. K. Dewdney](https://blog.codinghorror.com/practicing-the-fundamentals-the-new-turing-omnibus/) first introduced the world to [Core War](http://en.wikipedia.org/wiki/Core_War) in a series of [Scientific American articles](http://www.koth.org/info/akdewdney/) starting in 1984. (Full page scans of the articles, including the illustrations, are [also available](http://www.corewars.org/sciam/).)


> Core War was inspired by a story I heard some years ago about a mischievous programmer at a large corporate research laboratory I shall designate X. The programmer wrote an assembly-language program called Creeper that would duplicate itself every time it was run. It could also spread from one computer to another in the network of the X corporation. The program had no function other than to perpetuate itself. Before long there were so many copies of Creeper that more useful programs and data were being crowded out. The growing infestation was not brought under control until someone thought of fighting fire with fire. A second self-duplicating program called Reaper was written. Its purpose was to destroy copies of Creeper until it could find no more and then to destroy itself. Reaper did its job, and things were soon back to normal at the X lab.
> (The story of Creeper and Reaper seems to be based on a compounding of two actual programs. One program was [a computer game called Darwin](http://en.wikipedia.org/wiki/Darwin_%28programming_game%29), invented by M. Douglas McIlroy of AT&T Bell Laboratories. The other was called Worm and was written by John F. Shoch of the Xerox Palo Alto Research Center. Both programs are some years old, allowing ample time for rumors to blossom.)


Core War, surprisingly, is still around. The current hub appears to be at [corewar.co.uk](http://corewar.co.uk/). You can download simulators for a variety of operating systems there. Here’s how a Core War battle works:


> Core War has four main components: a memory array of 8,000 addresses, the assembly language Redcode, an executive program called MARS (an acronym for Memory Array Redcode Simulator) and the set of contending battle programs. Two battle programs are entered into the memory array at randomly chosen positions; neither program knows where the other one is. MARS executes the programs in a simple version of time-sharing, a technique for allocation the resources of a computer among numerous users. The two programs take turns: a single instruction of the first program is executed, then a single instruction of the second, and so on.
> What a battle program does during the execution cycles allotted to it is entirely up to the programmer. The aim, of course, is to destroy the other program by ruining its instructions. A defensive strategy is also possible: a program might undertake to repair any damage it has received or to move out of the way when it comes under attack. The battle ends when MARS comes to an instruction in one of the programs that cannot be executed. The program with the faulty instruction – which presumably is a casualty of war – is declared the loser.


Let’s see it in action using one of the simulators. What you’re watching here is a round-robin tournament between the **Imp** [yellow], **Mice** [blue], **Midget** [white], and **Piper** [green] programs.


![Core Wars,  animated](https://blog.codinghorror.com/content/images/uploads/2008/04/6a0120a85dcdae970b0120a86de323970b-pi.gif)


The winner is **Piper** [green], with 2 wins, 0 losses, and 1 tie.


These programs are written in an assembly-like dialect known as Redcode. Here’s the source code for **Midget**:

kg-card-begin: html

```

;redcode
;name Midget
;author Chip Wendell
;strategy stone (bomber)
;history Third place at the 1986 ICWS tournament
Bomb	dat	#0,	#-980
Spacer	equ	28
Start	mov	Bomb,	@Bomb
sub	#Spacer,Bomb
jmp	Start,	#0
end	Start

```

kg-card-end: html

The [Redcode instruction set](http://vyznev.net/corewar/guide.html#start_instr) is deliberately simple. There are two variants, ICWS-88 with 10 instructions and 4 addressing modes, and ICWS-94 with 19 instructions and 8 addressing modes.

kg-card-begin: html


| `DAT` | data | `DJN` | decrement and jump if not zero |
| `MOV` | move / copy | `SPL` | split |
| `ADD` | add | `CMP` | compare |
| `SUB` | subtract | `SEQ` | skip if equal |
| `MUL` | multiply | `SNE` | skip if not equal |
| `DIV` | divide | `SLT` | skip if lower than |
| `MOD` | modulus | `LDP` | load from private space |
| `JMP` | jump | `STP` | save to private space |
| `JMZ` | jump if zero | `NOP` | no operation |
| `JMN` | jump if not zero |  |  |


kg-card-end: html

It’s structured so that there is no “killer app”; three broad strategies are possible, each with its own strengths and weaknesses.

1. **Paper** or Replicator
Try to fill the core with copies of your program, so you are harder to kill.
2. **Rock** or Bomber
Attack by writing illegal instructions throughout the core – but not on your own program’s memory.
3. **Scissors** or Scanner
Attempt to identify enemy programs lurking in the core, then target writes to eliminate them.


Of course, combinations of the above strategies are possible as well. As you might imagine after 25 years of battlefield evolution, some modern Core War programs are quite baroque by now.


It’s not particularly useful, but it is a programming *game*, after all. It’s also a fascinating bit of computer science history. If you’re interested in participating in the venerable sport of Core War, it’s still very much alive and kicking. The [top 10 links for Core War newbies](http://corewar.atspace.com/top10.html) is a great place to get started.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[security](https://blog.codinghorror.com/tag/security/)
