---
title: "Instructive and Persuasive Examples"
date: 2017-08-29
url: https://www.hillelwayne.com/post/persuasive-examples/
slug: persuasive-examples
word_count: 941
---

I recently read [No excuses, write unit tests](https://dev.to/jackmarchant/no-excuses-write-unit-tests), which argues Unit Tests are Good and You Should Write Them. For the most part I strongly agree with their message, which is why I feel kinda bad criticizing the essay. They provide this as “an example of simple testing”:


```
const add = (...numbers) => {
  return numbers.reduce((acc, val) => {
    return acc + val;
  }, 0);
};

it('should add numbers', () => {
  const expected = 15;
  const actual = add(1, 2, 3, 4, 5);

  expect(actual).to.equal(expected); // true
});

```


This is a bad example. More specifically, it’s *inappropriate*. By reading it I get a sense of what a unit test is. If the article was titled “What is unit testing?”, it’d be just fine.


But it’s *not* called “What is unit testing?” It’s called “No excuses, write unit tests.” The target audience isn’t people who haven’t heard of testing before. It’s people who *know about* unit testing but aren’t convinced it’s worth doing. The example needs to show the benefits of having a unit test, not just what it is. And this example doesn’t do that. For one, it’s pretty obvious that `add` is correct; why should I bother to write test code if I can tell it’s right by just looking at it? For another, the test code is longer than the entire function, so it’s a big investment for no clear benefit. Etc etc etc.


The issue is that `add` is an *instructive example*, when what we want is a *persuasive example*. Instructive examples show you what and how, while persuasive examples show you why and why not. Without making that distinction clear, it’s easy to accidentally write the former when you really need the latter.


It is also a lot harder to write a good persuasive example.

- If your example is too simple, people brush it off.
- If your example is too complicated, people won’t follow. They’re also less likely to trust it, because you complicated example might be concealing a simpler way.
- If your example is too abstract, people won’t see how it’s useful in practice.
- If your example is too concrete, people won’t see how it generalizes to their own problems.


So a good persuasive example has to be simple without being trivial, complex without being convoluted, and just the right balance between general and specific. On the other hand, instructive examples just need to be understandable.


I don’t blame the article for using the wrong ‘kind’ of example. Let’s try to find a better one.


### Finding an example


Unit tests catch bugs. We want an example function that *looks* easy to implement but has a bug in it. Show how the unit test catches the bug. Then, either show how unit tests catch edge cases or they catch regressions, both things that mean bugs in your code.


When I think “simple but finicky” I immediately jump to string processing. This is also good because everybody’s dealt with string processing before, and everybody’s gotten burnt by it. Let’s try a string processing problem then:


*You have a list of citations in [MLA format](https://owl.english.purdue.edu/owl/resource/747/06/). Write a function that takes the list of citations and two authors and returns if they have ever been coauthors.*


To keep this example lean, we’ll make two assumptions: first, that there are at most two authors per cite (no et. al), and that when testing authors, we always submit them in “Lastname, Firstname” format.1


```
def are_coauthors(citations, author1, author2) -> bool:
  ...

citations = ["Ayers, Alice and Bob Barker. Title1",
             "Chen, Carol and Alice Ayers. Title2",
             "Barker, Bob and Don Diez. Title3"]

are_coauthors(citations, "Ayers, Alice", "Barker, Bob") == True
are_coauthors(citations, "Ayers, Alice", "Diez, Don") == False

```


As you can probably tell, the main challenge (or at least the obvious one) is that the second author of a citation is in “Firstname Lastname” format, not “Lastname, Firstname”. Let’s write a couple of unit tests.


```
def test_are_coauthors():
    assert are_coauthors(citations, "Ayers, Alice", "Barker, Bob")

def test_are_not_coauthors():
    assert not are_coauthors(citations, "Ayers, Alice", "Diez, Don")

```


And then a simple function that passes both tests:


```
def are_coauthors(citations, author1, author2):
    author2_names = author2.split(", ")
    author2 = f"{author2_names[1]} {author2_names[0]}"
    for cite in citations:
        if author1 in cite and author2 in cite:
            return True
    return False

```


This *looks* mostly correct, but we can add a new test case that will fail:


```
def test_are_coauthors_flip():
    assert are_coauthors(citations, "Barker, Bob", "Ayers, Alice")

```


That’s because `are_coauthors` isn’t commutative! We can fix that by redefining authors:


```
def are_coauthors(citations, author1, author2):
    def first_last(author):
        names = author.split(", ")
        return f"{names[1]} {names[0]}"

    for cite in citations:
        if author1 in cite and first_last(author2) in cite:
            return True
        if author2 in cite and first_last(author1) in cite:
            return True
    return False

```


Another finicky edge case we missed is if there’s a name in the title. This will fail:


```
def test_ignores_title():
    assert not are_coauthors(["Ayers, Alice and Bob Barker. Life of Don Diez"], "Ayers, Alice", "Diez, Don")

```


We could fix that too, but would that potentially regress something else? What about books with only one author? Etc etc etc. After a while, there are too many edge cases to track, and you can no longer be confident about the correctness of your program by just looking at it. I’d argue this example is more ‘persuasive’ than ‘adding numbers’.


One downside is this took me a while to think up. Writing persuasive examples is hard. I think it’s worth it, though, because it leads to a stronger article.


*Thanks to [Alex Koppel](http://alexkoppel.com/) and [Noah Tye](http://twitter.com/noahlt) for their feedback.*


---

1. All examples are in Python with [pytest](https://docs.pytest.org/en/latest/).
 [return]
