---
title: "Rejection Sampling with Perl 6"
date: 2017-07-27
url: https://blog.mempko.com/rejection-sampling-with-perl-6/
slug: rejection-sampling-with-perl-6
word_count: 165
tags: ['perl6', 'programmers', '#wordpress', '#Import 2024-11-03 23:36']
---



[Perl 6](http://www.perl6.org/?ref=blog.mempko.com) provides a way to create lazy lists using the gather/take keywords. What I wanted to do was create an infinite list of samples from a known distribution of values. A simple way to sample from a known distribution is to do Rejection Sampling and doing this in Perl 6 is super easy.


[code lang=”perl”]


sub sample(%distribution) {

  gather {

    loop {

      my $v = %distribution.pick;

      take $v.key if rand <= $v.value;

    }

  }

}

[/code]


This function creates a [Seq](https://docs.perl6.org/type/Seq?ref=blog.mempko.com) and you grab values from it in a lazy way. Here is a simple example assigning 100 samples from a distribution

to an array.


[code lang=”perl”]


my %distribution = a=> 0.3, b=> 0.4, c=>0.1, d=>0.2;

my @samples = sample(%distribution)[0..^100];

[/code]


Perl 6 is super fun. It has taken all the cool features from all the other languages and ignored the bad stuff. In this case, lazy lists from Haskell.


Read [Seqs, Drugs, and Rock’n Roll](https://rakudo.party/post/Perl-6-Seqs-Drugs-and-Rock-n-Roll?ref=blog.mempko.com) to learn more about Sequences in Perl 6.

