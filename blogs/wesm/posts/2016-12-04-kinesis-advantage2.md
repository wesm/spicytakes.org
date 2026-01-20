---
title: "Kinesis Advantage2: Impressions"
date: 2016-12-04T00:00:00
tags: ["work", "gear"]
slug: kinesis-advantage2
word_count: 882
source_file: blog/kinesis-advantage2/index.qmd
content_type: blog
---

**TL;DR** I discuss my impressions of the newest version of the classic Kinesis
Advantage contoured mechnical keyboard, the [Advantage2][6].

## Mechanical keyboards

Mechanical keyboards have become a big business the last 5 years or so, with
clackity-clack Cherry MX key switches becoming all the rage amongst programmers
and gamers alike. In the age of ever-thinner laptop keyboards (and Apple even
getting rid of physical buttons and keys in recent Macbook Pros), the strong
tactile feedback and satisfying feel of mechanical key switches are a welcome
change for professionals who spend long days at the computer.

I was introduced to these keyboards through the Kinesis Advantage back in
2008. I was suffering from repetitive strain injury (RSI) pain at the time and
the Kinesis layout (with modifier keys at your thumbs) and lower key actuation
force was exactly what I needed. They are expensive keyboards (at US $\$$300 to
$\$$400, depending on the model and where you buy it), but given that they can
last a decade or more, properly taken care of, you can think of it as an
investment in your professional productivity and health.

I'm not an expert on keyboard history, but the two companies which popularized
keyboard layouts with thumb-based modifier keys were [Maltron][1] and
[Kinesis][2]. Since then, there have been other new keyboard designs taking
inspiration from these, like the open source [Ergodox][3] and [Dactyl][4]
keyboards.

The Kinesis Corporation itself has always been sleeper hit amongst programmers
with RSI issues. So I was interested when they released a new version of the
Advantage keyboard with some hardware changes and internal software
changes. They were kind enough to provide me with a demo unit to try out the
new features.

## Advantage2: what's new

The big changes in the Advantage2 are:

* The function keys are now proper mechanical Cherry ML switches rather than
  the spongier capacitative ones in the older models. They're a big step up
  from the old function keys.

* New internal hardware / firmware bringing improved programmability for
  modifying keyboard layouts and macros. Macros have been improved in some good
  ways, too.

* An internal USB-based "V-Drive" enabling you to edit configuration files
  (layouts and macros) and install firmware updates on the keyboard
  programmability and firmware updates from your computer.

Otherwise, not much has changed about the physical design of the keyboard
(which is already tried and true). It's missing a USB port for a mouse (which
I'm told had caused issues for users on KVM switches), but you can still
connect a set of foot pedals, which behave like generic programmable keys.

## Easier programmability

The new programmability system I've referred to is now collectively known as
the "SmartSet Programming Engine". I updated the [keyboard firmware][5] using
the V-Drive, so at this time I have (this status report printed out by a
special keyboard macro):

```
Model> Advantage2
Firmware> 1.0.168.us (2MB), 09/26/2016
Active layout file> qwerty.txt
Thumb keys mode> win
Macro play status> active
Macro play speed> slow=1, normal=3, fast=9> 9
Status report play speed> off=0, slow=1, normal=3, fast=4> 3
Keyclick status> off
Toggle tone status> on
Stored macros> 2
Keys remapped> 4
Power user mode> on
```

Pressing `progm - F1` mounts a special USB drive which contains an `active`
folder containing configuration files for keyboard layouts and macros, and a
special `firmware` folder for firmware updates.

Inside `active`, there is a read-only file `state.txt` which has some of the
basic high level settings.

```
startup_file=qwerty.txt
thumb_mode=WINDOWS
key_click_tone=OFF
toggle_tone=ON
macro_disable=OFF
macro_speed=9
power_user=true
```

The macro speed can be a big deal in practice. The original Advantage had a
fixed macro playback speed that wasn't too speedy. The default speed setting of
3 corresponds to 150 words per minute (WPM) corresponds roughly to a fast
typing speed. The top speed of 9 is 20 times faster, a blistering 250
characters per second (around 3000 words per minute). For longer macros, this
makes the output appear almost instantaneously. You can set the macro speed
globally or on a per-macro basis (since some macros need to be entered more
slowly).

The `qwerty.txt` file contains modifications to the default QWERTY layout. Any
remappings that you make using traditional onboard programming (by pressing
`progrm - remap`) are stored in this file. For example, I have long remapped
Caps Lock to left bracket `[` and backslash to `]` (for Python
programming). These appear in my `qwerty.txt` file as:

```
[caps]>[obrack]
[\]>[cbrack]
```

Things get more interesting with macros. For example, I used the keyboard's
macro recording mode (`progm - F11`) to set Ctrl-Alt-Shift-F to type `This is a
Macro Example`. This then appears in `qwerty.txt` as:

```
{lalt}{lshift}{lctrl}{f}>{-lshift}{t}{+lshift}{h}{i}{s}{space}{i}{s}{space}{a}{space}{-lshift}{m}{+lshift}{a}{c}{r}{o}{-lshift}{space}{e}{+lshift}{x}{a}{m}{p}{l}{e}
```

Any macros created onboard are similarly reflected in the text file, so you can
make tweaks to more complicated macros from a text editor (so-called "direct
editing").

## Summary

For Kinesis users who take advantage of customization and macros, the
Advantage2 is a very nice upgrade for its improved programmability and the
better feel of the function keys.

If you are a new or potential user, and you can afford the investment (of money
and time to learn the contoured keyboard shape), it should be worth your
consideration over the increasingly long list of mechanical keyboards now
available.

[1]: http://www.maltron.com/
[2]: https://www.kinesis-ergo.com
[3]: https://ergodox-ez.com/
[4]: https://github.com/adereth/dactyl-keyboard
[5]: https://www.kinesis-ergo.com/advantage2-resources/
[6]: https://www.kinesis-ergo.com/shop/advantage2/