---
title: "The Fox in the Henhouse"
date: 2016-08-23
url: https://blog.mempko.com/the-fox-in-the-henhouse/
slug: the-fox-in-the-henhouse
word_count: 1277
tags: ['#wordpress', '#Import 2024-11-03 23:36']
---



## **Slogging**


I’m writing a new time series DB in C++ called Henhouse and this is a story about a bug and my heroic battle with it. Actually, it’s not really a story about a bug, but more of a way of finding bugs and preventing them. I hope to convince you that there are better ways of writing code that don’t involve slogging with unit tests.


## **Freakin Lasers!**


So I ran a randomized test that hammered my new precious DB. It dumped random data into it and did random queries. I started it and came back several hours later to find this…


```
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!! require failed
!! expr: (_metadata->size >= 170) [_metadata->size = 171, _max_items = 170]
!! func: size
!! file: /home/maxim/src/max/henhouse/src/db/../util/mapped_vector.hpp (63)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

./henhouse(_ZN8henhouse4util5traceERSo+0x35) [0x68dbea]
./henhouse(_ZN8henhouse4util5raiseEPKc+0x81) [0x68dd32]
./henhouse(_ZN8henhouse4util6raise2ImiEEvPKcS3_iS3_S3_S3_RKT_S3_RKT0_+0x2b8) [0x67923f]
....

```


**See that?! That is a bug right there! **


You see, I am writing the DB in a style of programming called Design by Contract. My code is littered with contracts and whenever one of them fails, the program prints a helpful message with a stack trace and then violently aborts. No remorse. Want a guaranteed way to have a fairly bug free system? Make sure the system can detect bugs, and then can find your family and send them down river.


The nasty bug above was found in this bit of code.


[code language=”cpp”]

uint64_t size() const

{

    REQUIRE(_metadata);

    REQUIRE_LESS_EQUAL(_metadata->size, _max_items);


return _metadata->size;

}

[/code]


This is a member function which implements a memory mapped vector. Every time you call size on the vector, the contracts are tested.


## **This Machine Kills Fascist Bugs**


Design by Contract is one of those secret weapons nobody teaches you. The term was coined by [Bertrand Meyer](https://en.wikipedia.org/wiki/Bertrand_Meyer?ref=blog.mempko.com) who created the [Eiffel programming language](https://en.wikipedia.org/wiki/Eiffel_%28programming_language%29?ref=blog.mempko.com). Eiffel is really the only language that has truly native support for this technique, well, Eiffel and [Perl 6](http://perl6.org/?ref=blog.mempko.com). But we all know Perl 6 is from the future, but talking about Perl 6 is for another day.


The idea is that units in your software, like a function, or an object, establish contracts between the caller and the callee. The callee says “I **REQUIRE** you give me parameters that meet this criteria and I will **ENSURE** you this result”.


### Preconditions

Postconditions

Invariants


The important bit to understand here is that a **RELATIONSHIP** is established between pieces of code. Not just an informal relationship, but an executable one! A relationship that can be tested millions of times a second. All day, every day on real user data.


This is substantially different than Unit testing, which ignores relationships between code.


## **Parallel Monkeys Are Terrible

**


The bug was introduced when I added support for parallel puts and queries into my DB. As data is put into the DB I have a function that would resize the memory mapped file that looked like this.


[code language=”cpp”]

void resize(size_t new_size)

{

    REQUIRE(_data_file);

    REQUIRE_GREATER_EQUAL(new_size, _data_file&amp;gt;size() + sizeof(data_type));

    const auto old_max = _max_items;


_data_file->resize(new_size);

    _items = reinterpret_cast<data_type>(_data_file->data());

    _max_items = _data_file->size() / sizeof(data_type);


ENSURE_GREATER(_max_items, old_max);

}

[/code]


The failure detected that “_max_items” was being stale somewhere, which indicated a copy was being made in another thread.


**Amazing! our contract found a multi-threading error!**


I solved the bug by a standard method. I created a worker pool and made sure puts and gets for a piece of data always went to the same worker. The worker has a request queue that it pulls from and processes requests one after another. No more chances of a get and a put happening in parallel. The much more tricky solution would have been to use read/write locks, but I know better.


## **The Fat Bollard**


What would our code above look like using unit tests instead? Well first thing, we would not have contracts, because we are TDD people and TDD people don’t know about contracts.


[code language=”cpp”]

void resize(size_t new_size)

{

    _data_file->resize(new_size);

    _items = reinterpret_cast<data_type>(_data_file->data());

    _max_items = _data_file->size() / sizeof(data_type);

}

[/code]


What we lose should be immediately obvious. For example, the requirement that **new_size** should be bigger than the old size. If we enjoy defensive programming, we may further refine the code to look like this.


[code language=”cpp”]

void resize(size_t new_size)

{

    if(new_size < _data_file->size() + sizeof(data_type))

        throw runtime_error("new size too small");


_data_file->resize(new_size);

    _items = reinterpret_cast<data_type>(_data_file->data());

    _max_items = _data_file->size() / sizeof(data_type);

}

[/code]


I get a lot of people asking me “*What the difference is between Design by Contract and plain old defensive programming?*” I think it should be pretty obvious from above why defensive programming is not the same thing. First with defensive programming, you allow the caller to recover. With the Design by Contract approach there is no remorse. Fail early and fail fast. Second, the caller has no information about what the callee ensures in the result, requiring the caller to check the result.


Being good [TDD](https://en.wikipedia.org/wiki/Test-driven_development?ref=blog.mempko.com) folks we would actually have written a test first that looks like this.


[code language=”cpp”]

void test_resize()

{

    size_t initial_capacity=50

    mapped_vector<int> v{"test_file", initial_capacity};

    for(int a = 0; a < 100; a++)

        v.push_back(a)

    EXPECT_EQ(v.size(), 100);

}

[/code]


And guess what, this would **not have** found the parallel bug! Even if we modified the test to use threads to insert into the vector, the bug would still not fail the tests. We would also have to query the size as we insert in parallel for the bug to show up, and guess what, in that query the size would necessarily be unknown since the query and insert are done in parallel. The best you can do is maybe somehow coerce the test to segfault (which it won’t since it is accessing valid memory). Or worse, expose **max_items** to the outside world muddying the interface.


I tested to see what would happen if I removed the contract. I ran the test and waited a day. And guess what? nothing happened except that the DB put data in the wrong place. In other words, a silent and deadly data corruption.


## **Not All Tests Are Created Equal**


I combined Design by Contract with other powerful tools such as randomized testing and fuzzing. There are many tools for randomized testing such as [QuickCheck](https://en.wikipedia.org/wiki/QuickCheck?ref=blog.mempko.com) and for fuzz testing such as [afl-fuzz](http://lcamtuf.coredump.cx/afl/?ref=blog.mempko.com). I decided to write my own tests using [Perl 6](http://perl6.org/?ref=blog.mempko.com). For example, here is a test for dumping random data into the DB. Henhouse is compatible with [Graphite’s](http://graphiteapp.org/?ref=blog.mempko.com) input format.


[code language=”perl”]

use v6;


sub MAIN($workers, $a, $z)

{

    my @keys = "$a".."$z";

    my @ps;


for (1..$workers) -> $w {

        @ps.push: start { put(@keys); };

    }

    await Promise.allof(@ps);

}


sub put(@keys)

{

    my $s = IO::Socket::INET.new(:host<localhost>, :port<2003>);

    loop

    {

        my $c = (0..10).pick;

        my $k = @keys.pick;

        $s.print("{$k} {$c} {DateTime.now.posix}\n");

        sleep 0.01;

    }

}

[/code]


Why should I write many manually created unit tests when I can create a test that makes tests! A typical project using unit testing has tens of thousands of hand written tests. Look Ma! I just made a million!


## **Do This, Be Brave**


Design by Contract is a far better weapon to fight bugs and improve code quality than Unit Testing. Design By Contract…

- Helps you do code reviews by being explicit about assumptions.
- Tests both input domain and output codomain
- Tests ranges of values instead of individual points.
- Tests real data in production vs fake data in development.
- Always on. Ships with production code.
- Prevents data corruption and secures code.
- Failures happen close to the source of the problem.


If you combine this technique with…

- Randomized Testing
- Fuzz Testing
- Acceptance and Behavioral Testing


You will never look back. Stop unit testing, do it, be brave.

