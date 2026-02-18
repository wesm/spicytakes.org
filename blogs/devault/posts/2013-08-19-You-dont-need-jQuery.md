---
title: "You don't need jQuery"
date: 2013-08-19
url: https://drewdevault.com/2013/08/19/You-dont-need-jQuery.html
slug: You-dont-need-jQuery
word_count: 728
---

It’s true. You really don’t need jQuery. Modern web browsers can do most of what you want from jQuery,
without jQuery.

For example, take  [MediaCrush](https://mediacru.sh) . It’s a website I spent some time working on with a friend.
It’s actually quite sophisticated - drag-and-drop uploading, uploading via a hidden form, events wired up to
links and dynamically generated content, and ajax requests/file uploads, the whole she-bang. It does all of
that without jQuery. It’s  [open source](https://github.com/MediaCrush/MediaCrush) , if you’re looking for a good
example of how all of this can be used in the wild.

Let’s walk through some of the things you like jQuery for, and I’ll show you how to do it without.

## Document Querying with CSS Selectors

You like jQuery for selecting content. I don’t blame you - it’s really cool. Here’s some code using jQuery:

```
$('div.article p').addClass('test');
```

Now, here’s how you can do it on vanilla JS:

```
var items = document.querySelectorAll('div.article p');
for (var i = 0; i < items.length; i++)
    items[i].classList.add('test');
```

Documentation:  [querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Document.querySelectorAll) ,  [classList](https://developer.mozilla.org/en-US/docs/Web/API/element.classList)

This is, of course, a little more verbose. However, it’s probably a lot simpler than you expected. Works in
IE 8 and newer - except for classList, which works in IE 10 and newer. You can instead use className, which is
a little less flexible, but still pretty easy to work with.

## Ajax

You want to make requests in JavaScript. This is how you POST with jQuery:

```
$.post('/path/to/endpoint', {
    parameter: value
    otherParameter: otherValue
},
success: function(data) {
    alert(data);
});
```

Here’s the same code, without jQuery:

```
var xhr = new XMLHttpRequest(); // A little deceptively named
xhr.open('POST', '/path/to/endpoint');
xhr.onload = function() {
    alert(this.responseText);
};
var formData = new FormData();
formData.append('parameter', value);
formData.append('otherParameter', value);
xhr.send(formData);
```

Documentation:  [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)

Also a bit more verbose than jQuery, but much simpler than you might’ve expected. Now here’s the real kicker:
It works in IE 7, and IE 5 with a little effort. IE actually pioneered XHR.

## Animations

This is where it starts to get more subjective and breaks backwards compatability. Here’s my opinion on the
matter of transitions: dropping legacy browser support for fancy animations is acceptable. I don’t think it’s
a problem if your website isn’t pretty and animated on older browsers. Keep that in mind as we move on.

I want to animate the opacity of a  `.foobar`  when you hover over it. With jQuery:

```
$('.foobar').on('mouseenter', function() {
    $(this).animate({
        opacity: 0.5
    }, 2000);
}).on('mouseleave', function() {
    $(this).animate({
        opacity: 1
    }, 2000);
});
```

Without jQuery, I wouldn’t do this in Javascript. I’d use the magic of CSS animations:

```
.foobar {
    transition: opacity 2s linear;
}

.foobar:hover {
    opacity: 0;
}
```

Hover over this text

Documentation:  [CSS animations](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Using_CSS_animations)

Much better, eh? Works in IE 10+. You can do much more complicated animations with CSS, but I can’t think of
a good demo, so that’s an exercise left to the reader.

## Tree traversal

jQuery lets you navigate a tree pretty easily. Let’s say you want to find the container of a button and remove
all .foobar elements underneath it, upon clicking the button.

```
$('#mybutton').click(function() {
    $(this).parent().children('.foobar').remove();
});
```

Nice and succinct. I’m sure you can tell the theme so far - the main advantage of jQuery is a less verbose
syntax. Here’s how it’s done without jQuery:

```
document.getElementById('mybutton').addEventListener('click', function() {
    var foobars = this.parentElement.querySelectorAll('.foobar');
    for (var i = 0; i < foobars.length; i++)
        this.parentElement.removeChild(foobars[i]);
}, false);
```

A little wordier, but not so bad. Works in IE 9+ (8+ if you don’t use addEventListener).

## In conclusion

jQuery is, of course, based on JavaScript, and as a result, anything jQuery can do can be done without jQuery.
Feel free to  [ask me](mailto:sir@cmpwn.com)  if you’re curious about how I’d do something else without jQuery.

I feel like adding jQuery is one of the first things a web developer does to their shiny new website. It just
isn’t really necessary in this day and age. That extra request, 91kb, and load time are probably negligible,
but it’s still a little less clean than it could be. There’s no need to go back and rid all of your projects of
jQuery, but I’d suggest that for your next one, you try to do without. Keep MDN open in the next tab over and
I’m sure you’ll get through it fine.
