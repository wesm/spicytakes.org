---
title: "P2P File Sharing with Fire★"
date: 2013-12-27
url: https://blog.mempko.com/p2p-file-sharing-with-fire-e2-98-85/
slug: p2p-file-sharing-with-fire-e2-98-85
word_count: 1231
tags: ['firestr', '#wordpress', '#Import 2024-11-03 23:36']
---



I have been expanding the functionality of [Fire★](http://firestr.com/?ref=blog.mempko.com) based on use cases. The first was creating the building blocks for a [chat App](https://blog.mempko.com/2013/03/02/firestr-v0-1/), the next was the basics for a distributed [drawing App](https://blog.mempko.com/2013/03/23/write-a-distributed-white-board-app-using-firestr/). I thought the next obvious use case was a file transfer app.


## Demo


## Primitives


At a minimum I needed a way to open files, split the files into chunks, send them over the wire, and reassemble the file and save it. For safety the file open API is very simple and only allows the user to select a file…


[code language=”ruby”]

file = app:open_bin_file()

[/code]


And saving a file…


[code language=”ruby”]

app:save_bin_file("my_file", bin_data)

[/code]


Since Lua doesn’t have a native type to deal with bytes, I had to create one that allows to extract a sub array of bytes, get the size, and also append bytes.


## Algorithm


For sending the file across the network, I needed several types of messages. The basic algorithm I decided on was that the sender would send a file initiation message with metadata about the file, including how many chunks. Then the receiver would ask the sender for a specific chunk. When the chunk arrived, it would be appended to the working set on the receiver end, where the receiver would then ask for the next chunk.


This pull model provides an obvious advantage, which is that it allows a limited rate of transfer allowing multiplexing with other messages that would be sent. So you can keep chatting, or drawing, or whatever while the file transferred.


Another obvious advantage to the pull model is that you can send multiple files at a time and they will be properly multiplexed. And if you have multiple people you are sending the file to, each one can receive it at their own speed.


The file data structure looks like this


[code language=”ruby”]

local file = {

    id = send_id,

    name=file:name(),

    data=file:data(),

    size=file:size(),

    chunk=0,

    chunks = math.ceil(file:size() / CHUNK),

    ch = {},

    mode=1}

[/code]


Sending the initiation message looks like this


[code language=”ruby”]

function send_start_file(f)

	local m = app:message()

	m:set("t","sf")

	m:set("name", f.name )

	m:set("id", f.id)

	m:set("size", f.size)

	m:set("chunks", f.chunks)

	app:send(m)

end

[/code]


When the receiver gets the message, the following function handles it.


[code language=”ruby”]

app:when_message_received("got")

function got(m)

	local t = m:get("t")


if t == "sf" then

		got_start_file(m)

	elseif t == "gc" then

		got_get_chunk(m)

	elseif t == "sc" then

		got_chunk(m)

	end

end

[/code]


This function is the most important one. “got_start_file” adds the metadata to its set and asks for the first chunk. Which the sender will then get a “gc” message which then “got_get_chunk” is called where the sender will then construct a chunk message and send it. The receiver will then get the “sc” message and call “got_chunk” function which will append the chunk to the working set and ask for the next one.


This file transfer application is not built into Fire★, but is built on basic building blocks. You can imagine many ways to improve this application such as adding a pause or a cancel button. This transfer App is part of the standard distribution of packaged apps.


## Contribute


I am excited with the progress Fire★ has made. I am adding a breadth of features first to make this platform maximally useful. You can now chat, draw, and transfer files with multiple peers via p2p where all messages are encrypted and private.


Like what you see? Fire★ is GPLv3, please contribute using [Github](http://github.com/mempko/firestr?ref=blog.mempko.com)


or email firestr.dev@gmail.com


## Full Source


[code language=”ruby”]

s = app:button("send")

app:place(s, 0,0)

app:height(100)

row=1

send_id = 1

CHUNK=1024 * 40


sfiles = {}

gfiles = {}


s:when_clicked("send()")


function send()

	local file = app:open_bin_file()


if not file:good() then

		return

	end


local nf = {

		id = send_id,

		name=file:name(),

		data=file:data(),

		size=file:size(),

		chunk=0,

		chunks = math.ceil(file:size() / CHUNK),

		ch = {},

		mode=1}

	send_id = send_id + 1

	add_sfile(nf)

	send_start_file(nf)

end


function format_percent(p)

	p = p * 1000

	p = math.ceil(p)

	p = p / 10

	return p .. "%"

end


function g_percent(f)

	return format_percent(f.chunk / f.chunks)

end


function s_percent(f)

	local sc = f.chunks

	for k, v in pairs(f.ch) do

		if v < sc then

			sc = v

		end

	end

	return format_percent( sc / f.chunks)

end


function s_status(f)

	local s = ""

	local mode = f.mode

	local p = s_percent(f)

	if mode == 1 then

		s = "sending…"

	elseif mode == 2 then

		s = "… " .. p

	elseif mode == 3 then

		s = "done"

	end

	return f.name .. " ".. s

end


function g_status(f)

	local s = ""

	local mode = f.mode

	local p = g_percent(f)

	if mode == 1 then

		s = "getting…"

	elseif mode == 2 then

		s = "… " .. p

	elseif mode == 3 then

		s = "done"

	end

	return f.name .. " ".. s

end


function update_s_status(fd)

	local lb = fd.label

	local bt = fd.bt

	lb:set_text(s_status(fd.file))

end


function update_g_status(fd)

	local lb = fd.label

	local bt = fd.bt

	lb:set_text(g_status(fd.file))

	if fd.file.mode == 3 then

		bt:enable()

		bt:set_text("save")

		bt:when_clicked("save_file_by_id(\"".. fd.id .."\")")

	end

end


function add_sfile(f)

	local i = f.id

	row = row + 1


local cv = app:grid()

	app:place(cv, row, 0)

	local fl= app:label(s_status(f))

	cv:place(fl, 0, 0)

	local bt = nil


app:grow()

	local fd = {id=i, file=f, label=fl, cv=cv}

	sfiles[i] = fd

end


function add_gfile(f)

	local i = f.id

	row = row + 1


local cv = app:grid()

	app:place(cv, row, 0)

	local fl= app:label(g_status(f))

	cv:place(fl, 0, 0)


local bt= app:button("save")

	bt:disable()

	cv:place(bt, 0, 1)


app:grow()

	local fd = {id=i, file=f, label=fl, bt=bt, cv=cv}

	gfiles[i] = fd

end


function send_start_file(f)

	local m = app:message()

	m:set("t","sf")

	m:set("name", f.name )

	m:set("id", f.id)

	m:set("size", f.size)

	m:set("chunks", f.chunks)

	app:send(m)

end


function got_start_file(m)


local n = m:get("name")

	local orig_id = m:get("id") + 0

	local from = m:from()

	local id = from:id() .. "_" .. orig_id

	local chunks = m:get("chunks")  + 0

	local size = m:get("size")

	local nf = {

		from = from,

		orig_id = orig_id,

		id=id,

		name=n,

		data=d,

		chunks=chunks,

		chunk=-1,

		size = size,

		mode=4}


add_gfile(nf)

	send_get_chunk(nf)

end


function send_get_chunk(f)

	local m = app:message()

	local chunk = f.chunk + 1

	m:set("t","gc")

	m:set("id", f.orig_id)

	m:set("chunk", chunk)


app:send_to(f.from, m)

end


function got_get_chunk(m)

	local id = m:get("id") + 0

	local chunk = m:get("chunk") + 0

	local f = sfiles[id].file


send_chunk(m:from(), f, chunk)

end


function sent_all(f)

	local all = true

	for k,v in pairs(f.ch) do

		if v < (f.chunks – 1) then

			all = false

		end

	end

	return all

end


function send_chunk(to, f, c)

	local b = c * CHUNK

	if b >= f.size then return end

	local s = math.min(CHUNK, (f.size – b))

	local ch = f.data:sub(b, s)


f.ch[to:id()] = c

	if sent_all(f) then

		f.mode = 3

	else

		f.mode = 2

	end


local m = app:message()

	m:set("t", "sc")

	m:set("id", f.id)

	m:set("chunk", c)

	m:set_bin("data", ch)

	app:send_to(to, m)

	update_s_status(sfiles[f.id])

end


function got_chunk(m)

	local orig_id = m:get("id") + 0

	local id = m:from():id() .. "_" .. orig_id

	local chunk = m:get("chunk") + 0

	local chunk_data = m:get_bin("data")


local fd = gfiles[id]

	local file = fd.file

	if file.data == nil then

		file.data = chunk_data

	else

		file.data:append(chunk_data)

	end

	file.chunk = chunk


local last_chunk = file.chunks  – 1


if file.chunk == last_chunk then

		file.mode = 3

		update_g_status(fd)

		return

	end


file.mode = 2

	update_g_status(fd)


send_get_chunk(file)


end


app:when_message_received("got")

function got(m)


local t = m:get("t")


if t == "sf" then

		got_start_file(m)

	elseif t == "gc" then

		got_get_chunk(m)

	elseif t == "sc" then

		got_chunk(m)

	end

end


function save_file_by_id(gid)

	local f = gfiles[gid].file

	save_file(f)

end


function save_file(f)

	f.saved = 1

	app:save_bin_file(f.name, f.data)

end

[/code]

