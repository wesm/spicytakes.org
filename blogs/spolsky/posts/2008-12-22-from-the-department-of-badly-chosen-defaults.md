---
title: "From the Department of Badly Chosen Defaults"
date: 2008-12-22
url: https://www.joelonsoftware.com/2008/12/22/from-the-department-of-badly-chosen-defaults/
word_count: 91
---


Alert reader Chris S. emailed me to point out [this post](http://code.flickr.com/blog/2008/11/12/on-ui-quality-the-little-things-client-side-image-resizing/) by a developer at flickr about how to make IE scale images more smoothly. All you have to do is add


> img { -ms-interpolation-mode:bicubic; }


to the stylesheet. It worked!


Note that all the other browsers use bicubic interpolation for scaling by default, because that’s the only thing that make sense, but IE requires a non-standard CSS extension. So, pictures on this site should be a little smoother for those of you determined to use Internet Explorer.


Happy Hannuka!
