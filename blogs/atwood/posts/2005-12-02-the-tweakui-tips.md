---
title: "The TweakUI Tips"
date: 2005-12-02
url: https://blog.codinghorror.com/the-tweakui-tips/
slug: the-tweakui-tips
word_count: 1265
---

I’ve been running some version of Microsoft’s cool TweakUI powertoy since the heady days of Windows 95. I recently found out that the author is none other than [Raymond Chen](https://web.archive.org/web/20051226044410/http://blogs.msdn.com/oldnewthing/archive/2005/02/02/365432.aspx):


> *Some people claim that Tweak UI was written because Microsoft got tired of responding to customer complaints. I don’t know where they got that from. Tweak UI was written because I felt like writing it.*


TweakUI has a Tips section which contains some highly useful advice about cool little Windows subtleties. I’ve seen at least three of these tips posted verbatim as “Eureka!” blog entries by various people at various times, so I think **everyone would benefit from a quick TweakUI tips refresher**, including myself. I used the SysInternals strings utility to dump all the strings from the executable and isolated the tips. Here they are, in order:

1. Press Win+L to switch to the Welcome screen or to lock your workstation.
2. You can switch users without going through the Welcome screen: From Task Manager, go to the Users tab, right-click a user, and select Connect.
3. Hold down the shift key in the shutdown dialog to change “Stand By” to “Hibernate.” Or just press H to hibernate instantly. You can even use the Power Control Panel to configure your power button to hibernate.
4. To disable the password when resuming from standby or hibernation, open the Power Control Panel and uncheck “Prompt for password after returning from standby” on the Advanced tab.
5. You can rename multiple files all at once: Select a group of files, right-click the first file, and select “Rename.” Type in a name for the first file, and the rest will follow.
6. Hold down the shift key when switching to thumbnail view to hide the file names. Do it again to bring them back.
7. If you create a file called Folder.jpg, that image will be used as the thumbnail for the folder. What’s more, that image will also be used as the album art in Windows Media Player for all media files in that folder.
8. From the View Menu, select “Choose Details” to select which file properties should be shown in the Explorer window. To sort by a file property, check its name in the “Choose Details” in order to make that property available in the “Arrange Icons by” menu.
9. To display the volume control icon in the taskbar, go to the Sounds and Audio Devices Control Panel and select “Place volume icon in the taskbar.”
10. Hold down the shift key when deleting a file to delete it immediately instead of placing it in the Recycle Bin. Files deleted in this way cannot be restored.
11. If you hold down the shift key while clicking “No” in a Confirm File Operation dialog, the response will be interpreted as “No to All.”
12. To save a document with an extension other than the one a program wants to use, enclose the entire name in quotation marks. For example, if you run Notepad and save a file under the name Dr.Z, it will actually be saved under the name Dr.Z.txt. But if you type “Dr.Z” then the document will be saved under the name Dr.Z. Note that a document so-named cannot be opened via double-clicking since the extension is no longer “.txt.”
13. Put a shortcut to your favorite editor in your Send To folder and it will appear in your “Send To” menu. You can then right-click any file and send it to your editor.
14. Ctrl+Shift+Escape will launch Task Manager.
15. To arrange two windows side-by-side, switch to the first window, then hold the Control key while right-clicking the taskbar button of the second window. Select “Tile Vertically.”
16. To close several windows at once, hold down the Control key while clicking on the taskbar buttons of each window. Once you have selected all the windows you want to close, right-click the last button you selected and pick “Close Group.”
17. Some objects (such as Control Panel applications) support additional commands which are available by holding the Shift key while right-clicking.
18. In the Address Bar, type “Microsoft” and hit Ctrl+Enter. Internet Explorer automatically inserts the “http://www.” and “.com” for you.
19. To remove an AutoComplete entry from a Web form, highlight the item in the AutoComplete dropdown and press the Delete key. To remove all Web form AutoComplete entries, go to the Internet Explorer Tools menu, select Internet Options, Content, AutoComplete, then press the “Clear Forms” button.
20. To organize your Favorites in Explorer instead of using the Organize Favorites dialog, hold the shift key while selecting “Organize Favorites” from the Favorites menu of an Explorer window.
21. You can organize your Favorites by dragging the items around your Favorites menu. Alternatively, you can open the Favorites pane and hold the Alt key while pressing the up and down arrows to change the order of your Favorites.
22. To run Internet Explorer full screen, press F11. Do it again to return to normal mode.
23. When dragging a file in Explorer, you can control the operation that will be performed when you release the mouse button:
Hold the Control key to force a Copy.
Hold the Shift key to force a Move.
Hold the Alt key to force a Create Shortcut.
24. If your “Printers and Faxes” folder is empty, you can hide the “Printers and Faxes” icon when viewed from other computers by stopping the Print Spooler service.
25. You can turn a folder into a desktop toolbar by dragging the icon of the desired folder to the edge of the screen. You can then turn it into a floating toolbar by dragging it from the edge of the screen into the middle of the screen. (It helps if you minimize all application windows first.)
26. You can turn a folder into a taskbar toolbar.
First, unlock your taskbar.
Next, drag the icon of the desired folder to the space between the taskbar buttons and the clock. (Wait for the no-entry cursor to change to an arrow. It’s a very tiny space; you will have to hunt for it.)
You can rearrange and resize the taskbar toolbar you just created. You can even turn the taskbar toolbar into a menu by resizing it until only its name is visible.
27. To add or remove columns from Details mode, select Choose Details from the View menu, or just right-click the column header bar.
28. In Internet Explorer, hold the Shift key while turning the mouse wheel to go forwards or backwards.
29. In Internet Explorer, hold the Shift key while clicking on a link to open the Web page in a new window.
30. In Internet Explorer, type Ctrl+D to add the current page to your Favorites. This and many more keyboard shortcuts can be found by going to Internet Explorer, clicking the Help menu, then selecting Contents and Index. From the table of contents, open Accessibility and click “Using Internet Explorer keyboard shortcuts.”
31. In some applications (such as Internet Explorer), holding the Control key while turning the mouse wheel will change the font size.
32. To shut down via Remote Desktop, click the Start button, then type Alt+F4.


If you knew all these, then you’re either the world’s biggest liar, or a true Windows [Ninja](https://web.archive.org/web/20051212051028/http://www.thinkgeek.com/books/humor/783f/). I’ll add one of my own that isn’t listed here but most people don’t know: many standard windows message box dialogs (of the OK, CANCEL variety) can be copied to the clipboard by pressing CTRL+C. Try it.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
[tips and tricks](https://blog.codinghorror.com/tag/tips-and-tricks/)
