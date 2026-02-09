---
title: "Write a distributed white board app using Firestr"
date: 2013-03-23
url: https://blog.mempko.com/write-a-distributed-white-board-app-using-firestr/
slug: write-a-distributed-white-board-app-using-firestr
word_count: 1378
tags: ['firestr demo', '#wordpress', '#Import 2024-11-03 23:36']
---



# Introduction


I have just added a widget to draw lines, so of course the natural thing to do is create a drawing program. I will show you how to code a distributed white board app in Firestr.


For those that don’t know what Firestr is please read this [introduction.](https://blog.mempko.com/2013/03/02/firestr-v0-1/)


# Demo


Here is a video showing the app in action!


# The Code


The first thing we want to do is add our interface elements and buttons. Firestr uses the Lua programming language and has a custom API to create widgets.


Create a new session in Firestr and open up the app editor. Create a new app. We will need a drawing canvas and some buttons for the four colors.


```
d = app:draw(300,300)
cl = app:button("clear")
blackb = app:button("black")
redb = app:button("red")
greenb = app:button("green")
blueb = app:button("blue")


```


The first line creates a canvas of size 300,300 pixels and the rest create the buttons. You won’t see anything yet because we have to place the widgets on our app’s canvas. You can think of the canvas as an imaginary grid.


```
app:place_across(d,0,0,1,5)
app:place(cl,1,4)
app:place(blackb, 1,0)
app:place(redb,1,1)
app:place(greenb,1,2)
app:place(blueb,1,3)
app:place(cl,1,4)


```


Firestr runs your code behind the scenes as you program. If you type in an error, you will see it in the error window above your code. You should now see the following.


The white area is the draw canvas you created and you can see a row of buttons below it. The button’s don’t do anything yet, so we need to give them some functionality. First, let’s give the drawing area some functionality.


```
d:when_mouse_pressed("pressed")
d:when_mouse_dragged("dragged")
px = -1
py = -1

function pressed(b, x, y) 
    px = x 
    py = y 
end  
 
function dragged(b, x, y) 
    d:line(px, py, x , y) 
    px = x 
    py = y 
end


```


After you type that in, try drawing on the canvas!


The first two lines, we give function names for when a mouse is pressed and dragged on the draw canvas ‘d’ that we defined previously. ‘px’ and ‘py’ store the previous mouse position when dragging. When the mouse button is first pressed, set the previous is set to the current. Then when the mouse is dragged, draw a line on ‘d’ from the previous position to the current mouse position. Then set our previous to the current.


Some color is in good order so let’s create some pens.


```
redp = app:pen("red",2)
greenp = app:pen("green",2)
bluep = app:pen("blue",2)
blackp = app:pen("black",2)


```


Each pen has a width of 2. You can put any hex HTML color code where you see the color name. Now let’s create a function that sets the color of the current pen.


```
cur_pen = ""
function set_color(p, pt)
    d:pen(p)
    cur_pen = pt
end


```


The cur_pen variable stores the name of our pen that we set. We will use this later to send drawing events over the network. Now let’s make all the color button’s work


```
redb:when_clicked("set_color(redp,'r' )")
greenb:when_clicked("set_color(greenp,'g')")
blueb:when_clicked("set_color(bluep,'b')")
blackb:when_clicked("set_color(blackp,\"bl\")")


```


For each button we give the code to call when the button is clicked. In this case, call our set_color function with the appropriate values. Also let’s get the clear button to work.


```
cl:when_clicked("clear()")
function clear()
    d:clear()
end


```


The draw has a ‘clear’ method which erases everything.


We now have a very simple drawing application where you can change colors and clear the canvas.


# Making it Networky


Let’s make it more fun by making it work where you can draw together with a friend. We need to first tell firestr what function to call when a message is received.


```
app:when_message_received("got")
function got(m)
end


```


When a message is received, the “got” function is called with the message ‘m’. Let’s create a function that will send a line to the other side.


```
function send_line(x1,y1,x2,y2, pen)
    local m = app:message()
    m:set("t","l")
    m:set("ln", x1.." "..y1.." "..x2.." "..y2.." "..pen)
    app:send(m)
end


```


This function receives the start and end position of the line and the name of the pen. Firestr has a message object where you can set key,value pairs. The key ‘t’ stores the type of message. In this case, the type is a line ‘l’. The line is encoded as a space separated string of values and stores in the “ln” key. Now update the mouse drag function to send a line every time the mouse is dragged.


```
function dragged(b, x, y)
    d:line(px, py, x , y)
    send_line(px, py, x, y,cur_pen)
    px = x
    py = y
end


```


Let’s now update our “got” function to handle our new line messages.


```
app:when_message_received("got")
function got(m)
    local type = m:get("t")
    if type == "l" then
        local ln = m:get("ln")
        local x1, y1, x2, y2,p = ln:match("(%d+) (%d+) (%d+) (%d+) (%l+)")
        local prev_pen = d:get_pen()
        local cp = get_color(p)
        d:pen(cp)
        d:line(x1, y1, x2, y2)
        d:pen(prev_pen)
    end
end


```


Let’s go over this bit of code. First the message type is stored in a local variable called ‘type’. The the encoded line is stored in ‘ln’ and Lua’s string matching library is used to parse out the values. Before the line is drawn, the current user’s pen needs to be stored so that we can set it back. We then need to get the line’s pen by name. The function get_color will need to be created. Once we have the pen, we can draw the line on canvas. Here is the get_color function.


```
function get_color(p)
    if p == 'r' then
        return redp
    elseif p == 'g' then
        return greenp
    elseif p == 'b' then
        return bluep
    elseif p == "bl" then
        return blackp
    end
    return blackp
end


```


It simply checks the name and returns the appropriate pen.


At this point you can draw with a buddy!


# Testing it if You are Forever Alone


But wait! How do you test the application’s network code before you send it to someone?


The simplest way is to create a test user and run them locally alongside your main user. Here is the bash script I use to run my test user.


```
#!/bin/bash
/home/mempko/firestr --home=/home/mempko/.firestr_test --port 6061


```


When you run this the first time, it will ask you for a user name. Call the user ‘test’, and add them as your contact, and you as theirs using invite files. The bash script sets a custom home directory and port for your second instance of firestr to run. The home directory is where all your firestr related files live, including your applications.


Once you run your test user, you can try out the Draw application and test the networking.


The last bit is creating a message for when the clear button is pressed. I won’t go into that, you can just see the full source for the drawing app below.


# Help Me Make This Awesomer


Firestr is GPLv3


Help me improve firestr at [http://github/mempko/firestr](http://github.com/mempko/firestr?ref=blog.mempko.com)


I need to add more wiz bang. Oh, and I need help with security!


# The Full Source


```
 
d = app:draw(300,300)
cl = app:button("clear")
blackb = app:button("black")
redb = app:button("red")
greenb = app:button("green")
blueb = app:button("blue")

app:place_across(d,0,0,1,5)
app:place(cl,1,4)
app:place(blackb, 1,0)
app:place(redb,1,1)
app:place(greenb,1,2)
app:place(blueb,1,3)
app:place(cl,1,4)

d:when_mouse_pressed("pressed")
d:when_mouse_dragged("dragged")
cl:when_clicked("clear()")

redp = app:pen("red",2)
greenp = app:pen("green",2)
bluep = app:pen("blue",2)
blackp = app:pen("black",2)

redb:when_clicked("set_color(redp,'r' )")
greenb:when_clicked("set_color(greenp,'g')")
blueb:when_clicked("set_color(bluep,'b')")
blackb:when_clicked("set_color(blackp,\"bl\")")

px = -1
py = -1

cur_pen = ""
function set_color(p, pt)
    d:pen(p)
    cur_pen = pt
end
set_color(blackp, "bl")

function pressed(b, x, y)
    px = x
    py = y
end

function dragged(b, x, y)
    d:line(px, py, x , y)
    send_line(px, py, x, y,cur_pen)
    px = x
    py = y
end

function clear()
    d:clear()
    send_clear()
end

function get_color(p)
    if p == 'r' then
        return redp
    elseif p == 'g' then
        return greenp
    elseif p == 'b' then
        return bluep
    elseif p == "bl" then
        return blackp
    end
    return blackp
end

app:when_message_received("got")
function got(m)
    local type = m:get("t")
    if type == "l" then
        local ln = m:get("ln")
        local x1, y1, x2, y2,p = ln:match("(%d+) (%d+) (%d+) (%d+) (%l+)")
        local prev_pen = d:get_pen()
        local cp = get_color(p)
        d:pen(cp)
        d:line(x1, y1, x2, y2)
        d:pen(prev_pen)
    elseif type == "cl" then
        d:clear()
    end
end

function send_line(x1,y1,x2,y2, pen)
    local m = app:message()
    m:set("t","l")
    m:set("ln", x1.." "..y1.." "..x2.." "..y2.." "..pen)
    app:send(m)
end

function send_clear()
    local m = app:message()
    m:set("t", "cl")
    app:send(m)
end
```

