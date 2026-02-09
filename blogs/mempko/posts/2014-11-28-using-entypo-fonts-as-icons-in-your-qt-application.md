---
title: "Using Entypo Pictographs as Icons in Your Qt Application"
date: 2014-11-28
url: https://blog.mempko.com/using-entypo-fonts-as-icons-in-your-qt-application/
slug: using-entypo-fonts-as-icons-in-your-qt-application
word_count: 548
tags: ['code', 'entypo', 'firestr', 'qt', 'tutorial', '#wordpress', '#Import 2024-11-03 23:36']
---



I wanted to replace buttons with fancier icons for [Fire★](http://www.firestr.com/?ref=blog.mempko.com) but…

1. I Wanted to use vector graphics instead of bitmaps.
2. Didn’t want to complicate my installation by using many resource files.


I came across a font that had pictographs that look really nice called [Entypo](http://entypo.com/?ref=blog.mempko.com). It is a Creative Commons font by Daniel Bruce.


Once you learn about Entypo, you see these pictographs everywhere!


These looked really nice and using them as icons on buttons would be perfect. Qt has the ability to load fonts for the application through the [QFontDatabase](http://qt-project.org/doc/qt-5/QFontDatabase.html?ref=blog.mempko.com) class which provides two static functions.

1. int QFontDatabase::**addApplicationFont**(const QString &* fileName*)
2. int QFontDatabase::**addApplicationFontFromData**(const QByteArray &* fontData*)


The first one allows you to load the font from the file system, but I would have to package Entypo separately from my application. But look at that second one, you can load a font from a byte array! All I need to do is download the font and convert the file to a byte array.


On unix systems there is a nice tool called [xxd](http://man.cx/xxd?ref=blog.mempko.com) which can take a file and convert it into a hex dump. It has a nice option called ‘–include’ which converts the file into a C include file.


[code language=”bash”]


$ xxd -i entypo.ttf > entypo.dat


[/code]


This converts the font file into a C include file with two variables


[code language=”C”]

const unsigned char entypo_ttf[] = {

0x00, 0x01, 0x00, 0x00, 0x00

0x4c, 0x54, 0x53, 0x48, 0x2d,

0x00, 0x00, 0x00, 0xf4, 0x4f,…};


unsigned int entypo_ttf_len = 80708;

[/code]


Including the whole font this way is not a problem because it is so small, only 80k. For the byte array I added const because I won’t be changing it.


We can now include this into our code and convert it to a QByteArray.


[code language=”C”]

#include "entypo.dat"


void setup_entypo()

{

    auto entypo =

        QByteArray::fromRawData(

            reinterpret_cast<const char*>(entypo_ttf), entypo_ttf_len);

    auto id =

        QFontDatabase::addApplicationFontFromData(entypo);


ENSURE(id != -1);

}

[/code]


You have to recast to signed char* here because xxd converts the data to unsigned char. The **addApplicationFontFromData** function returns -1 if there was a problem loading the font. I simply assert that this isn’t true since I am confident that the converted ttf file is correct.


One very important note here, make sure you create your [QApplication](http://qt-project.org/doc/qt-5/qapplication.html?ref=blog.mempko.com) object before you call **addApplicationFontFromData** otherwise you will get a **segfault**. I figured this out the hard way and it appears that QApplication is initializing some important global state that the **QFontDatabase** needs.


Now you can use the font in your labels and buttons!


[code language=”C”]


QPushButton b{ u8"\U0001F465"};


b.setFont(QFont{"Entypo", 26});

b.setStyleSheet("border: 0px; color: ‘green’;");


[/code]


Notice that I am using the new C++11 Unicode literal. You can insert a Unicode character directly using the hex code point using **‘\u’** for 16-bit code points and** ‘\U**‘ for 32-bit code points. Also the string is prefixed with **‘u8’** to indicate that this is a utf-8 string.


Also, make sure you attribute Entypo properly in your code and mention the [website](http://entypo.com/?ref=blog.mempko.com).


Hope you enjoyed my post. Check out my project [Fire★](http://firestr.com/?ref=blog.mempko.com) and follow me on [twitter](https://twitter.com/mempko?ref=blog.mempko.com).


EDIT:


It was mentioned to me that it is better to use [rcc](http://qt-project.org/doc/qt-4.8/resources.html?ref=blog.mempko.com) instead of xxd for storing binaries in a Qt app. This is superior, so don’t use my silly silly way.

