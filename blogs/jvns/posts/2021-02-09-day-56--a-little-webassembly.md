---
title: "Day 56: A little WebAssembly"
date: 2021-02-09
url: https://jvns.ca/blog/2021/02/09/day-56--a-little-webassembly/
slug: day-56--a-little-webassembly
word_count: 135
---


I spent a bunch of time yesterday pairing with Rachel and Jeff on figuring out
how to do art in Rust!


I learned that it’s easier to get started with WebAssembly than I thought –
all we had to do to get this [canvas smiley face example](https://rustwasm.github.io/wasm-bindgen/examples/2d-canvas.html)
running was:


```
git clone https://github.com/rustwasm/wasm-bindgen/
cd wasm-bindgen/examples/canvas
npm install
npm run serve

```


At first I was confused because the instructions said to use `npm`, but this is a Rust program! What’s going on!
But `npm run serve`) is actually running a bunch of cargo commands behind the scenes.


On my slow computer the example took maybe 10 minutes to compile, and it took
about 2 minutes on my fast about.


That’s all! Having been reminded that Rust exists, I might work on some `rbspy`
issues today.
