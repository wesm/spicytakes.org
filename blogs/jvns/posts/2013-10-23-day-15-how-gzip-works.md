---
title: "Day 15: How a .gz file is structured, redux"
date: 2013-10-23
url: https://jvns.ca/blog/2013/10/23/day-15-how-gzip-works/
slug: day-15-how-gzip-works
word_count: 953
---


So I’ve finished implementing gunzip in Julia! I paired with a lot of
wonderful people along the way, so I ended up trying to explain how the file
format works a lot of times, probably often in a fairly confused way (sorry!).
Here is another disorganized attempt at explaining gzip, mainly for my own
benefit.


The basic idea behind gzip (aka the DEFLATE algorithm) is that there are 2 passes:

1. LL87 pass: Replace repeated sequences with pointers to where they appeared
previously in the text. There is a good diagram of this at the beginning of
[this page](http://www.infinitepartitions.com/art001.html)
2. Huffman coding pass: Use Huffman coding to represent the text and pointers in an efficient way


There is a pretty good explanation of what Huffman coding is on the
[aforementioned page](http://www.infinitepartitions.com/art001.html), so I’m
just going to go ahead and talk about the gzip file format. Probably this will
make no sense if you have not been absorbed in gzip for the last 5 days.


That said, here is how a gzip file is laid out, and some of the code I wrote to
decode it. The github repository is here: [github.com/jvns/gzip.jl](http://github.com/jvns/gzip.jl)


## Gzip headers and metadata (20 bytes or so)


This part of the file isn’t that interesting. Every gzip file has to start
with the magic bits `1F86`. There is a 9 byte header, followed by some
variable length metadata, which includes the filename and some other stuff.
I am not sure why the filename is included in the metadata!


Apparently gunzip also knows how to deflate some other legacy compression
format, but for our purposes `compression_method` is always `8`.


Here are the Julia data structures I used to store the header & metadata:


```
type GzipHeader
  id::Vector{Uint8} # length 2
  compression_method::Uint8
  flags::GzipFlags
  mtime::Vector{Uint8} # length 4
  extra_flags::Uint8
  os::Uint8
end

```


```
type GzipMetadata
  header::GzipHeader
  xlen::Uint16
  extra::ASCIIString
  fname::ASCIIString
  fcomment::ASCIIString
  crc16::Uint16
end

```


## Blocks!


The rest of the gzip file after the headers and metadata is a series of
blocks, to be read in order. As far as I can tell it is impossible to
decompress gzip files in parallel – there’s no way to know when a block
has ended without fully decompressing it.


### Block header (3 bits)


Each block starts with 3 bits indicating

- Whether this block is the last block (1 bit)
- How the block is compressed (2 bits). My gunzip only supports one compression method,
though one of the options is “not compressed”, so that would be easy to add.


### Header for the Huffman codes (14 bits)


There is a recursive thing going on where there is a Huffman tree encoded with
another Huffman tree. This header is the metadata that helps you get started
with reading all these trees.

- `hclen` is the number of codes in the first tree (minus four)
- `hlit`: the number of ’literal codes’ in the second tree
- `hdist`: the number of ‘distance codes’ (minus one) in the second tree


This minus four and minus one business basically drove me insane. But they are
easy to represent at least:


```
type HuffmanHeader
    hlit::Uint8
    hdist::Uint8
    hclen::Uint8
end

```


### Code lengths for first Huffman tree (`(hclen + 4) * 3` bits)


Next, there is a series of numbers from 0 to 7 which you can use to put
together a Huffman tree. I read these in `read_first_tree()`.


### Code lengths for second Huffman tree (unknown number of bits)


The second Huffman tree’s code lengths are encoded using the first Huffman tree.


So you have to read `(258 + hlit + hdist)` code lengths, using the first
Huffman tree as your guide. I read these in `read_second_tree_codes()`


You actually end up with two Huffman trees here – they’re called
`literal_tree` and `distance_tree`.  `literal_tree` is made from the first
`257 + hlit` codes, and `distance_tree` is made from the next `hdist + 1`
codes. This was really not obvious and took me forever to figure out.


### The compressed data! (unknown number of bits)


To read the compressed data, you have to

1. Read a code
  1. If it’s the stop code, stop!
  2. If it represents a literal character (like ‘a’ or ‘2’), just add it to the decoded text
  3. If it instead represents a pointer to some previous text, figure out the length and the relative distance and copy the text.


Here is the actual code I wrote to do this!


```
function inflate_block!(decoded_text, bs::BitStream, literal_tree::HuffmanTree, distance_tree::HuffmanTree)
    while true
    	# Read a code from the file
        code = read_huffman_bits(bs, literal_tree)
        if code == 256 # Stop code; end of block!
            break
        end
        if code <= 255 # ASCII character
            append!(decoded_text, [convert(Uint8, code)])
        else # Pointer to previous text
            len = read_length_code(bs, code)
            distance = read_distance_code(bs, distance_tree)
            # Copy the previous text into our decoded text
            copy_text!(decoded_text, distance, len)
        end
    end
    return decoded_text
end

```


### Main function for reading a block!


And here’s the main block-reading function! It does a lot of things, but it
came out in (I thought) a fairly readable way.


It modifies `decoded_text` in place because it turns out that blocks can refer
to text in previous blocks. So there needs to be some shared state.


```
function inflate_block!(decoded_text, bs::BitStream)
    head = read(bs, HuffmanHeader)
    
    # Read the first Huffman tree
    first_tree = read_first_tree(bs, head.hclen)

    # Read the codes for the second Huffman tree
    codes = read_second_tree_codes(bs, head, first_tree)
    
    # Put together the tree of literals (0 - 255), stop code (256), and length codes (257-285ish)
    literal_codes = codes[1:257 + head.hlit]
    lit_code_table = create_code_table(literal_codes, [0:length(literal_codes)-1])
    literal_tree = create_huffman_tree(lit_code_table)
    
    # Put together the tree of distance codes (0-17)
    distance_codes = codes[end-head.hdist:end]
    dist_code_table = create_code_table(distance_codes, [0:length(distance_codes)-1])
    distance_tree = create_huffman_tree(dist_code_table)
    
    return inflate_block!(decoded_text, bs, literal_tree, distance_tree)
end

```
