---
title: "MT Configuration Language Module for BBEdit 8"
date: 2004-09-07
url: https://daringfireball.net/2004/09/mt_config_module
slug: mt_config_module
word_count: 217
---


Here’s another codeless language module for BBEdit 8, for Movable Type
configuration files (‘mt.cfg’). It provides syntax coloring for comments
and MT directive keywords; by default, it claims any file whose name
ends with ‘mt.cfg’.


Download link and installation instructions (cinchy) at the
[module’s project page](https://daringfireball.net/projects/mtconfig/).


The Movable Type user manual has a section on [Configuration Settings](http://www.movabletype.org/docs/mtmanual_configuration.html); this module supports all the directive keywords listed there, plus
the following six which aren’t documented, but which I found in the
default ‘mt.cfg’ file for MT 3.11:

- AdminScript
- TypeKeyVersion
- ObjectDriver
- Database
- DBUser
- DBHost


## Update


[Phil Ringnalda](http://philringnalda.com/) emailed to point out that the canonical list of supported
MT configuration directives is in the `/mt/lib/MT/ConfigMgr.pm` source
file. From there, I slurped out 25 additional keywords:

- AltTemplatePath
- AtomApp
- CSSPath
- DBPassword
- DBPort
- DBSocket
- DebugEmailAddress
- DefaultLanguage
- DynamicComments
- IdentityURL
- IgnoreISOTimezones
- NewsboxURL
- NoPlacementCache
- NoPublishMeansDraft
- OneDayMaxPings
- OneHourMaxPings
- PluginPath
- SearchSortOrder
- Serializer
- SignOffURL
- SignOnURL
- TechnoratiPingURL
- TimeOffset
- TransparentProxyIPs
- Type


(Note to Six Apart: It’d be nice to have these documented.)



| **Previous:** | [You Can Choose Any Color You Want, as Long as It’s Black](https://daringfireball.net/2004/09/choose_microsoft) |
| **Next:** | [MSN Music ‘iPod’ Help Page Updated Again](https://daringfireball.net/2004/09/msn_music_ipod_update) |


PreviousNext