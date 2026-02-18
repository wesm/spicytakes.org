---
title: "Locations of Media Files in MacOS 10.15 Catalina"
date: 2020-02-24
url: https://daringfireball.net/2020/02/catalina_media_file_locations
slug: catalina_media_file_locations
word_count: 489
---


[Kirk McElhearn, back in June, right after Catalina was announced](https://kirkville.com/locations-of-media-files-in-macos-catalina/):


> **Music**: By default, these files will be stored in *~/Music*. (~
> is a shortcut for your home folder, the one with the house icon
> and your user name.)
> **Apple TV**: For TV shows and movies, the default location is
> *~/Movies*. Music Videos, however, will stay in the Music app.
> **Podcasts**: Podcasts are stored in a cache folder in
> *~/Library/Group Containers/243LU875E5.groups.com.apple.podcasts*.
> This is not designed to be user accessible, and the podcast files
> do not display the original file names. You can, however, drag
> podcast files from the Podcasts app to the Desktop or to a folder.


I needed this because my Mac version of Podcasts had gotten screwy. I don’t really listen to podcasts using Podcasts, but I subscribe to my own show in it just to make sure it looks and works right. I usually do this checking on my iPhone, but I was taking a look at it on my Mac this week, and noticed that four episodes (#245–248) were missing from the listing of “all episodes”. My first thought was that something must be corrupt in my RSS feed for the show. My second thought, a split-second later, was, nah, it’s probably a bug in the Mac Podcasts app. My second thought was right. Those four episodes of my show were not missing in any other podcast client, including Apple Podcasts on my iPhone and iPad.


Nothing I did within the Podcasts app, like unsubscribing / resubscribing, fixed the problem. The same four episodes were always missing — but only on my Mac. This reeked of a caching problem — but how to delete the cache? The Catalina Music and Movies apps continue to store their media files in the traditional, obvious places. That’s because they’re traditional Mac apps derived from the old iTunes app. I really had no idea where to look for Podcasts data to delete to try to unscrew whatever was screwed up. Trashing the folder McElhearn cites above — *~/Library/Group Containers/243LU875E5.groups.com.apple.podcasts* — and relaunching Podcasts did the trick. Problem solved.


When I saw McElhearn’s folder name, my first thought was that he had overlooked that the “243LU875E5” part must be generated per-user, and wouldn’t be the same for everyone. It certainly looks random, right? But it’s not — that’s the name of the Apple Podcasts cache folder for everyone on Catalina, so far as I can see. Why in the world all the folders in *~/Library/Group Containers/* are prefixed with these ugly seemingly-random identifiers, I have no idea, but it strikes me as one more step along the path of Apple now caring less and less [about what the back of the cabinet looks like](https://www.goodreads.com/quotes/445621-when-you-re-a-carpenter-making-a-beautiful-chest-of-drawers).



| **Previous:** | [The DF Tootbot Is Once Again Fully Operational](https://daringfireball.net/2020/02/df_tootbot_is_fully_operational) |
| **Next:** | [What You See in the Finder Should Always Be Correct](https://daringfireball.net/2020/02/what_you_see_in_the_finder_should_be_correct) |


PreviousNext