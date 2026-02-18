---
title: "GitHub's new notifications: a case of regressive design"
date: 2020-03-13
url: https://drewdevault.com/2020/03/13/GitHub-notifications.html
slug: GitHub-notifications
word_count: 840
---

*Disclaimer: I am the founder of a company which competes with GitHub. However,
I still use tools like GitHub, GitLab, and so on, as part of regular
contributions to projects all over the FOSS ecosystem. I don’t dislike GitHub,
and I use it frequently in my daily workflow.*

GitHub is rolling out a new notifications UI. A few weeks ago, I started seeing
the option to try it. Yesterday, I received a warning that the old UI will soon
be deprecated. At this pace, I would not be surprised to see the new UI become
mandatory in a week or two. I’m usually optimistic about trying out new
features, but this change worried me right away. I still maintain a few projects
on GitHub, and I frequently contribute to many projects there. Using the
notification page to review these projects is a ritual I usually conduct several
times throughout the workday. So, I held my breath and tried it out.

The new UI looks a lot more powerful initially. The whole page is used to
present your notifications, and there are a lot more buttons to click, many of
them with cute emojis to quickly convey meaning. The page is updated in
real-time, so as you interact with the rest of the website your notifications
page in the other tab will be updated accordingly.

Let’s stop and review my workflow using the  *old*  UI. I drew this beautiful
graphic up in GIMP to demonstrate:

I open the page, then fix my eyes on the notification titles. I move my mouse to
the right, and while reading titles I move the mouse down, clicking to mark any
notifications as read that I don’t need to look at, and watching in my
peripheral vision to see that the mouse hits its mark over the next button. The
notifications are grouped by repository, so I can read the name of the repo then
review all of its notifications in one go. The page is fairly narrow, so reading
the titles usually leads my eyes naturally into reading any other information I
might need, like the avatars of participants or age of the notification.

I made an equally beautiful picture for the new UI 1 :

This one is a lot harder to scan quickly or get into your muscle memory. The
title of the notification no longer stands out, as it’s the same size as the
name of the repo that was affected. They’re no longer grouped by repo, either,
so I have to read both every time to get the full context. I then have to move
my eyes  *all the way*  across the page to review any of those other details,
through vast fields of whitespace, where I can easily lose my place and end up
on a different row.

Once I’ve decided what to do with it, I have to move my mouse over the row, and
wait for the action buttons to appear. They were invisible a second ago, so I
have to move my mouse again to get closer to the target. Clicking it will mark
it as read. Then, because I have it filtered to unread (because “all”
notifications is really  *all*  notifications, and there’s no “new” notifications
like the old UI had), the row disappears, making it difficult to undo if it was
a mistake. Then I heave my eyes to the left again to read the next one.

This page is updated in real-time. In the old UI, after I had marked everything
as read that I didn’t need to look at, I would middle click on each remaining
notification to open it in a new tab. On the new real-time page, as soon as the
other tab loads, the notification I clicked disappears (again, because I have it
filtered to “unread”). This isn’t immediate, though — it takes at least as
long as it takes for the new tab to load. Scanning the list and middle-clicking
every other message becomes a Sisyphean task.

And the giant sticky header that follows you around! A whole 160 pixels, 14% of
my vertical space, is devoted to a new header which shows up on the next page
when I follow through a notification. And it’s implemented with JavaScript and
done in a bizzare way, so writing a user style to get rid of it was rather
difficult.

Aside: I tried adding a custom filter to show only pull requests, but it seems
to silently fail, and I just see all of my notifications when I use it.

Anyway, we’re probably stuck with this. Now that they’ve announced the imminent
removal of the old UI, we can probably assume that this feature is on the
non-stop release train. Negative feedback almost never leads to cancelling the
roll-out of a change, because the team’s pride is on the line.

I haven’t spoken to anyone who likes the new UI. Do you?

1. Both of these pictures were sent to GitHub as feedback on the feature, three weeks ago. ↩︎
