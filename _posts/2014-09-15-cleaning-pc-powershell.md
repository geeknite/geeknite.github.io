---

title:  "Cleaning a pc: recursive delete all empty folders with powershell help"
date: "2014-09-15 17:00:00 +0200"
tags: powershell maintenance computing
redirect_to: https://ferransalguero.github.io/blog/Powershell-recursive-deletion-script/
---

I've been using powershell to automatize some tedious tasks done through visual interface on windows, this is a powerful tool and I recommend everybody with some programmatic to check it out.

The powershell is an advanced command line console, like the old MS-DOS or a terminal in Linux systems, but with improved option, so programmers and system administrators can use it more efficiently.

The last task has been removing empty directories in hierarchy, so the deepest directory being empty will be deleted, the parent, when all children directories are deleted for being empty will be deleted if it's empty, that's the main idea.I've taken an already posted script [in links section] by Guy Ellis on his blog to delete empty folders and taken one step further, I've created a recursive function for this deletion that is being called before the check of the content of the directory.

The function is this:

![Learn Windows PowerShell in a Month of Lunches](https://m.media-amazon.com/images/I/4184kkT4ELL._SL160_.jpg)

Learn Windows PowerShell in a Month of Lunches](<https://www.amazon.com/dp/1617294160?tag>={{ site.constants.amazon_com }}&linkCode=ogi&th=1&psc=1)

[ Buy Now](<https://www.amazon.com/dp/1617294160?tag>={{ site.constants.amazon_com }}&linkCode=ogi&th=1&psc=1)

Edit
-----

I've found some problem in the second get-childitem for some dir-names with strange character, probably can be changed to some other cmdlet to know if the current dir is empty

And remember to give any insight you consider appropiate. **Thanks!**

Guy Ellis post
--------------

- [Powershell script to remove empty directories : Guy Ellis Rocks](http://guyellisrocks.com/powershell/powershell-script-to-remove-empty-directories/)\
    Here's a Powershell script that I've just created to remove empty folders which I'm sure I'm not going to need again in the future. Normal 0 false false false EN-US X-NONE X-NONE MicrosoftInternetExplorer4 /*Style Definitions*/ table.MsoNormalTable
