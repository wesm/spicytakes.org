---
title: "Day 23: a little Rails testing"
date: 2020-12-10
url: https://jvns.ca/blog/2020/12/10/day-23--some-rails-testing/
slug: day-23--some-rails-testing
word_count: 597
---


I’ve been working on a little Rails app to manage a bunch of virtual machines
that run programming puzzles, and in the last couple days I ran into a problem
I run into a lot: I forgot about testing!


here’s how it goes:

1. start writing some code with no tests, think “this is fine”
2. 2 days later, realize I’m spending a lot of time manually testing and fixing
the same bug 3 times because I broke it again
3. remember that automated testing exists
4. write tests and everything is 10x better


A few small nice things that I’ve found in my first day or two of doing testing in Rails:


### my Rails app comes with tests!


I’ve haven’t really used Rails much before, and when I started writing tests I
noticed that `rails generate scaffold Puzzle` had generated a bunch of tests
for me for the Puzzle controller!


This was really nice because it gave me a template to start from


### there are fixtures!


Every model has a corresponding file called `test/fixtures/MODEL_NAME.yml` that
has a bunch of data used to create test objects. For example, here are some
fixtures for my `VirtualMachineInstance` model:


```
manuela: 
   email: manuela@example.com
rishi:
   email: rishi@example.com

```


This means that I can quickly create a test object like this:


```
@user = users(:rishi)

```


### there are authentication helpers to help manage logins!


I’m using a gem called Devise right now to handle logins, and it comes with a
bunch of test helpers to pretend that I’m logged in to the site when accessing
a page. This is super useful in integration tests!


Here’s what that looks like


```
  setup do
    @user = users(:rishi)
    @user.save
    login_as(@user, :scope => :user)
  end

```


### mocking HTTP requests is easy


I have some code in my project that talks to an API to launch virtual machine
instances. I obviously don’t *actually* want to launch VM instances in my tests
(could get expensive!), so I wanted to mock out the calls to the API. Here’s
how that works:


```
WebMock.disable_net_connect!
stub_request(:get, "https://api.digitalocean.com/v2/account/keys?page=1&per_page=20").
  to_return(status: 200, body: '{"ssh_keys":[],"links":{},"meta":{"total":2}}')

```


The nice thing is that `WebMock.disable_net_connect!` prevents Ruby from making
any external API requests, and if one happens then it prints out an example of
some code I could write to mock that request.


### integration tests seem easy at first


I was spending a lot of time clicking on links and making sure that if it
worked if I went to X page and then Y page from there.


I was surprised by how easy Rails makes it to write integration tests! Here’s
an example of an integration test that I have that makes sure that right after
you start a puzzle (which launches an instance), the instance’s status is
“pending”. So little code!


```
test "status is pending right after instance started" do
    get '/puzzles/1/start'
    get '/instances/220816290/status'
    assert_response :success
    assert_equal({"status" => "pending"}, response.parsed_body)
end

```


This code definitely has a “magical Ruby” feel but I don’t really mind and it’s
fun to write so far.


### that’s all!


One thing I really appreciate about Rails is that there are like 15 million
blog posts and Stack Overflow answers about using it, which has made it pretty
easy so far to get all my questions answered.


It really feels like if I’m confused about something, many thousands of people
have been confused about the exact same thing and have written about it in 1000
different places, which is a nice change of pace from some of the weirder
things I’ve tried to learn about.
