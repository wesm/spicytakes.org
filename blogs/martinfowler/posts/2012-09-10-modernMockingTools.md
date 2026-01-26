---
title: "Modern Mocking Tools and Black Magic"
description: "The positive effect modern mocking tools can have on our ability to work         with legacy code and the possible negative implications of using those tools."
date: 2012-09-10T00:00:00
tags: ["testing"]
url: https://martinfowler.com/articles/modernMockingTools.html
slug: modernMockingTools
word_count: 5311
---


In
            [Working Effectively with Legacy Code](https://www.amazon.com/gp/product/0131177052/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0131177052&linkCode=as2&tag=martinfowlerc-20)
            Michael Feathers defines legacy code as code without automated tests. Sometime
            in 2010 I was introduced to
            [JMockIt](http://code.google.com/p/jmockit/)
            and shown how it allows us to write automated tests that seemingly violate the
            semantics of Java. For example, it is possible to replace a static method during
            the execution of a test. If I were to use the âoldâ style suggested by Michael Feathers,
            I'd do something like introduce an instance delegator to make it possible to write
            the test I wanted to write. Now, with a modern mocking tool, I could just skip that step.
            My initial reaction was amazement as I saw this as a way to open up existing
            code that is hard to test and get something written faster and with less mucking
            about in existing code.


Fast forward to late 2011 where I was teaching a class in Berlin and asked to
            give a presentation at a user's group ([you
                can see that talk here](http://vimeo.com/31927512)). In that video you can see me fuddle about trying
            to get some legacy code under test using JMockIt and in the end I manage to do so
            without actually changing the underlying code. What you don't see in the video
            is that next day in class we take the resulting code and apply more traditional
            legacy refactoring techniques to it and then rewrite the JMockIt-based test. The
            results are staggering and I believe they speak for themselves. What follows is that
            story recreated in full, which much of the fuddling about, I hope, removed.


## The Usual Suspects


To get started, here is some code for your consideration:


```
public static BigDecimal convertFromTo(String fromCurrency, String toCurrency) {
    Map<String, String> symbolToName = currencySymbols();
    if (!symbolToName.containsKey(fromCurrency))
        throw new IllegalArgumentException(String.format(
                "Invalid from currency: %s", fromCurrency));
    if (!symbolToName.containsKey(toCurrency))
        throw new IllegalArgumentException(String.format(
                "Invalid to currency: %s", toCurrency));

    String url = String.format("http://www.gocurrency.com/v2/dorate.php?inV=1&from=%s&to=%s&Calculate=Convert", toCurrency, fromCurrency);

    try {
        HttpClient httpclient = new DefaultHttpClient();
        HttpGet httpget = new HttpGet(url);
        HttpResponse response = httpclient.execute(httpget);
        HttpEntity entity = response.getEntity();
        StringBuffer result = new StringBuffer();
        if (entity != null) {
            InputStream instream = entity.getContent();
            InputStreamReader irs = new InputStreamReader(instream);
            BufferedReader br = new BufferedReader(irs);
            String l;
            while ((l = br.readLine()) != null) {
                result.append(l);
            }
        }
        String theWholeThing = result.toString();
        int start = theWholeThing.lastIndexOf("<div id=\"converter_results\"><ul><li>");
        String substring = result.substring(start);
        int startOfInterestingStuff = substring.indexOf("<b>") + 3;
        int endOfIntererestingStuff = substring.indexOf("</b>",
                startOfInterestingStuff);
        String interestingStuff = substring.substring(
                startOfInterestingStuff, endOfIntererestingStuff);
        String[] parts = interestingStuff.split("=");
        String value = parts[1].trim().split(" ")[0];
        BigDecimal bottom = new BigDecimal(value);
        return bottom;
    } catch (Exception e) {
        throw new RuntimeException(e);
    }
}
```


Ostensibly this code screens scrapes currency conversion information in a rather obtuse way, however the
                real purpose of this code is to discuss poor coding choices and their effect on our ability to
                understand, test, and maintain this code.


### Challenges to Testing


Before delving into the method itself, first observe that this is a static method. In Java, C#,
                    C++ (and many other languages), static methods are always bound at compile (or by link) time.
                    What this means is that code calling static methods is directly coupled to those methods. The
                    selection of the method and the calling mechanism are selected too early to easily allow
                    tests to setup an environment in which they can divert to something the test controls. It is
                    possible to call a different static method at runtime using what Michael Feathers calls a âlink
                    seam.â In the case of Java, you could make sure a different version of the class with the static
                    method is available in the classpath earlier. There is more on this below.


#### Validation


The first thing this method does is perform some basic validation. It confirms that the symbols
                        provided as method arguments actually exist. To do this, it calls another method in the same
                        class.


```
Map<String, String> symbolToName = currencySymbols();
if (!symbolToName.containsKey(fromCurrency))
    throw new IllegalArgumentException(String.format(
            "Invalid from currency: %s", fromCurrency));
if (!symbolToName.containsKey(toCurrency))
    throw new IllegalArgumentException(String.format(
            "Invalid to currency: %s", toCurrency));
```


##### Required


The method to get the known symbols is static and in the same class. This makes it impossible
                            within the language to simulate it or otherwise not perform validation. While it may seem
                            a good idea to always perform validation, it does increase the testing burden, which makes
                            tests somewhat more fragile as they depend on a larger number of things
                            that could change over time. That is only scratching the surface. It might seem that always
                            testing validation when testing other things makes the checks on validation more thorough,
                            in fact such testing typically represents duplicated rather than deeper testing; it adds
                            bulk without increasing value.


All I want to do is verify that parsing is correct. As written, validation and parsing
                            must be done together, in a particular order. That order seems logical; to have input
                            I need valid currencies. However, while that may seem like a necessary constraint, nothing
                            about parsing depends on valid currencies, nor should it. It just cares that the text
                            to parse follows a form, not that part of that form happens to additionally include valid
                            currency symbols. So the validation's business is bleeding unnecessarily into the next step.
                            I'd say this is an example of unnecessary temporal coupling. While parsing does follow
                            validation in time, it should not therefore follow that validation must be required to
                            allow us to verify parsing. A given test knows what it is testing. It knows, for example,
                            if the input it wants to be parsed is valid or not. So forcing validation before parsing
                            is incidental to how the code was written. It is not essential for parsing.


This last point is worth emphasizing as it is a common misconception. In my experience, most
                            people would suggest that validation before parsing is essential. In a sense it is; to
                            get some valid input, I need valid currency symbols in the real system. However, for the
                            purpose of testing, I do not need the real system, so the requirement of passing validation
                            is really incidental. If we check that validation works and we check that parsing works, then
                            is there any likelihood that what we've written won't work? I think not and so I don't
                            see the need for a fully-integrated functional test. Someone might disagree with me. On a
                            real project I'd probably write one because the argument would take more time than just
                            writing an automated check. However, breaking things down into smaller and smaller pieces
                            is both an essential skill and it takes years to learn. However, even if you disagree with
                            me on that point, I hope we can agree on is that if I could verify parsing independently
                            from validation, that would make checking things easier. In
                            [An Introduction to General Systems Thinking](https://www.amazon.com/gp/product/0932633498/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0932633498&linkCode=as2&tag=martinfowlerc-20), Weinberg
                            describes the
                            [
                                The Square Law of Computation
                            ](http://schuchert.wikispaces.com/Fundamental+Terms+With+Examples#SquareLawOfComputation), which you might be more familiar with as âdivide an conquer.â This code clearly does
                            not follow any such rules and the unnecessary, incidental coupling is going to make things
                            comparatively difficult.


##### Calls currencySymbols()


The call of the static method as mentioned is an issue, but more of an issue is that the
                            method in question makes a call out of the system using the[
                                HttpClient](http://hc.apache.org/), so calling it requires an internet connection. This call is necessary,
                            or at least used by, validation. Is the existence of this static method essentially related
                            to other parts of this method or incidentally related? Don't confuse âas writtenâ with
                            ânecessary.â


##### Traditional Options


To address these issues, we could do a number of things:

- Extract validation to its own class by
                                using[Sprout Class](http://xunitpatterns.com/Sprout%20Class.html), or
                                [Extract Class
                                ](http://www.refactoring.com/catalog/extractClass.html)
- Make all methods in this class non-static and non private, and use a
                                [testing
                                    subclass
                                ](http://xunitpatterns.com/Test-Specific%20Subclass.html)
                                to make testing easier
- Use an instance delegator - where the static methods are left but internally they
                                call an instance method on an object


These solutions address an underlying language design issue (non-override-able static stuff
                            is how they are designed but not fundamentally necessary, consider Smalltalk, JavaScript,
                            Self, ...). In any case, which one to pick depends on many factors including the starting
                            point, how much existing code currently depends on the class, etc.


#### [HttpClient](http://hc.apache.org/)


Next, the code reads a web page using the HttpClient:


```
HttpClient httpclient = new DefaultHttpClient();
HttpGet httpget = new HttpGet(url);
HttpResponse response = httpclient.execute(httpget);
HttpEntity entity = response.getEntity();
```


##### Directly Uses


This code directly uses the HttpClient, and uses
                            ***new***
                            to boot. Inheritance is the highest form of coupling in Java followed closely by calling
                            ***new***
                            . As this code is written, there is no language-defined way to avoid the use of this class.
                            You can use a link seam by testing with a different jar file (or classpath). In a pinch I'll
                            consider doing that, but not if I have access to the code and can change it, or, as we'll
                            see, access to what I'd call fourth generation mocking tool like
                            [JMockIt
                            ](http://code.google.com/p/jmockit/)
                            (Java-Open Source),
                            [powermock](http://code.google.com/p/powermock/)
                            (Java-Open Source) or
                            [Isolator.Net (commercial,
                                .Net)
                            ](http://www.typemock.com/typemock-isolator-product3)


##### Violates Dependency Inversion


In this example, the business domain is currency conversion but the business logic directly
                            uses the HttpClient. This is a violation
                            of the[Dependency Inversion
                                Principle](http://www.objectmentor.com/resources/articles/dip.pdf). In this case, if someone wants to get a currency conversion, as the code
                            is written, trying to do so introduces direct, compile-time coupling to a class that needs
                            a connection to the Internet. High-level stuff depends on low-level details. This code
                            will not age as well as an alternative that tends to invert this kind of dependency.


##### Fixing This Problem


The options to address this are the same as with validation: introduce an instance method,
                            sprout a class, etc. There's a deeper problem, however. Not only does this code directly
                            depend on a connection to the internet, as we are about to see, it returns HTML, which must
                            be parsed. We care about conversion rates, not parsing HTML, but to get to what we want we
                            have to go through a number of technology layers and after all of that we have to deal with
                            HTML.


#### File I/O


The HttpClient makes an
                        ***InputStream***
                        available, which is then read to completion:


```
StringBuffer result = new StringBuffer();
if (entity != null) {
    InputStream instream = entity.getContent();
    InputStreamReader irs = new InputStreamReader(instream);
    BufferedReader br = new BufferedReader(irs);
    String l;
    while ((l = br.readLine()) != null) {
        result.append(l);
    }
}
String theWholeThing = result.toString();
```


##### Embedded


As with the previous sections, this code is directly embedded in the method, making it
                            harder to ignore it.


##### Complexity & Duplication


This code is not terribly complex but to know what it is doing, you have to read it.
                            One way to improve communication is to reduce the need for it and the same can be said for
                            code. As this code is written, you have to read it to understand it. If this were in its
                            own method or class, with a good name, it might be easier to pass over. Since we tend
                            to read code more than write it, anything we can do to reduce the need to read code is
                            time well invested in the life of a project.


##### Required to get through the method


This code is embedded and as written, it must be executed every time to exercise the code.
                            This is another example of temporal coupling. As hinted to in the previous section, if this
                            were organized in a way that made it possible to better understand it, then it might also be
                            easier to get rid of it when the thing we are trying to check is not directly related to
                            reading the contents of a stream.


#### Parsing


Now that the stream has been converted into a string, it's time to parse the results:


```
int start = theWholeThing.lastIndexOf("<div id=\"converter_results\"><ul><li>");
String substring = result.substring(start);
int startOfInterestingStuff = substring.indexOf("<b>") + 3;
int endOfIntererestingStuff = substring.indexOf("</b>",
        startOfInterestingStuff);
String interestingStuff = substring.substring(
        startOfInterestingStuff, endOfIntererestingStuff);
String[] parts = interestingStuff.split("=");
String value = parts[1].trim().split(" ")[0];
```


##### Third verse same as the first...


At this point you might notice that I'm sounding like a skipping record. This code has all
                            of the issues mentioned above: it must be executed as written, it violates dependency
                            inversion, it must be read to be understood.


#### SRP Violation


This method is a classic demonstration of violating the
                        [
                            Single Responsibility Principle](http://www.objectmentor.com/resources/articles/srp.pdf). It does many different things, each of which have
                        different reasons to change at different times. In fact, in the original form of this method,
                        I was hitting one web site, which became unavailable, so I had to change it to another site
                        to get the information I wanted. This broke things in several places, speaking towards the
                        issues with violation of SRP and DIP. Not only did I need to hit a different location
                        (HttpStuff), I was getting back different HTML (parsing) and I had to for a different URL (Http
                        stuff again).


## Diving In


Modern mocking tools make most of the things I mention above irrelevant; at least on the surface.
                Rather than try to fix these things in the production code first, let's dive in by trying to get this
                method executing via an automated unit test.


### Getting setup - exercise the code


One place to start is to simply try to execute the code in question with either null arguments
                    or âreasonableâ values. Since the domain is currency conversion, and the method takes in two
                    currencies, that seems like a reasonable starting place.


Here is the beginning of an automated unit test to simply exercise the code. My goal is to get
                    through the method. One note, while this code will run with a live internet connection, I've turned
                    off my connection while writing this test to make sure I do not require a live internet connection
                    for my test to work:


```
@Test
public void returnExpectedConversion_v1() {
    CurrencyConversion.convertFromTo("USD", "EUR");
}
```


This works if the network is enabled, but if not, the code generates a
                    ***java.net.UnknownHostException***
                    . However, the actual place where it happens is in the method
                    ***CurrencyConversion.currencySymbols***
                    ,
                    and not in the method we care about. Using older tools, this is a bit of work, not so with our tool
                    of choice for this article:
                    [JMockIt](http://code.google.com/p/jmockit/)


### Getting past validation


Here is a second version of the test that gets past the first exception:


```
@Test
public void returnExpectedConversion_v2() {
    new NonStrictExpectations(CurrencyConversion.class) {
        {
            CurrencyConversion.currencySymbols();
            result = mapFrom("USD", "EUR");
        }
    };
    CurrencyConversion.convertFromTo("USD", "EUR");
}

private Map<String, String> mapFrom(String... keyValuePairs) {
    Map<String, String> result = new ConcurrentHashMap<String, String>();
    for (int i = 0; i < keyValuePairs.length; ++i)
        result.put(keyValuePairs[i], keyValuePairs[i]);
    return result;
}
```


Running this, the same exception is thrown,
                    ***UnknownHostException***
                    , but the exception is now in
                    the method under test rather than a called method. That's an improvement. This allows the code to
                    get past validation, but how?


```
new NonStrictExpectations(CurrencyConversion.class) {
    {
        CurrencyConversion.currencySymbols();
        result = mapFrom("USD", "EUR");
    }
};
```


Notice the creation of an anonymous inner class using
                    ***NonStrictExpectations**?
                    *
                    This form tells JMockIt to do something with the CurrencyConversion
                    ***class***
                    (replace a static
                    method in this case). The code in the inner set of {} is a standard Java instance initializer. Code
                    executed in that instance initializer tells JMockIt to replace the method executed,
                    ***currencySymbols**.
                    *
                    This is an example of a partial mocking of the class; we replace one of the methods in the class
                    such that any time it is called, it returns whatever is assigned to the inherited field âresultâ.


This involve some black magic. JMockIt is doing some Java bytecode magic and this code uses the
                    JMockIt DSL to make this happen. Making this work involves adding the JMockIt jar file into the
                    classpath. If you make sure it is listed before JUnit's jar file, that's enough to make this happen.
                    JMockIt uses a JavaAgent registered in its MANIFEST.MF file to make this all automatic.


### Dealing with the client


Now the code is failing on the part of the code that tries to read a webpage:


```
HttpClient httpclient = new DefaultHttpClient();
HttpGet httpget = new HttpGet(url);
HttpResponse response = httpclient.execute(httpget);
HttpEntity entity = response.getEntity();
```


This code is a bit more complex since it is embedded in the method, but we can get past this
                    problem. However, to do so will be a bit more work:

- The first two lines call
                        ***new***
                        . We need to make those uses of the new operator return a class under our control.
- The next line calls the
                        ***execute***
                        method on an
                        ***HttpClient***
                        , so we'll need to get that under control.
- The last line calls the
                        ***getEntity***
                        method on an
                        ***HttpResponse***
                        , which was the return value from the previous line, so this is much more involved overall.


Here is one way to take care of these three issues in one fell swoop:


```
new NonStrictExpectations() {
    DefaultHttpClient httpclient;
    HttpResponse response;
    HttpEntity entity;

    {
        httpclient.execute((HttpUriRequest) any);
        result = response;
        response.getEntity();
        result = entity;
        entity.getContent();
        result = bais;
    }
};
```


In this use of
                    ***NonStrictExpectations**,
                    *
                    there is no parameter passed in on the first line, meaning we are working with instances in some
                    way rather than static stuff. This anonymous inner class has three fields: DefaultHttpClient,
                    HttpResponse, HttpEntity. Those classes are wholly replaced in the Java classloader for this test
                    only. This means, for example, calling new DefaultHttpClient will return an instance of the
                    JMockIt-created class rather than the version found in the HttpClient jar.


This is an example of what I call a dynamic link seam. It's a link seam like Michael Feathers
                    discusses in his book, which is normally accomplished with build script/file magic. However, unlike
                    using build scripts, this is using a library, which makes it available to Java code âwithinâ the
                    language, rather than outside of the language.


This code replaces those three classes but with what?

- The
                        ***HttpClient.execute***
                        method will always return response, which is an instance of the JMockIt-created HttpResponse
                        subclass.
- The
                        ***HttpResponse.getEntity***
                        method will always return entity, which is an instance of the JMockIt-created HttpEntity
                        subclass.
- The
                        ***HttpEntity.getContent***
                        method will always return âbaisâ, which we will see in the next section.


Make no mistake, this is powerful stuff. In fact, I have a personal rule of thumb: If I think
                    something is cool, then it may not be appropriate for real development. JMockIt makes my âcool
                    spider sensesâ tingle on overdrive.


### Handling File I/O


The underlying code needs the contents of a stream. To create this, the test uses some standard
                    Java magic to make an in-memory stream:


```
final ByteArrayInputStream bais = new ByteArrayInputStream(
        "<div id=\"converter_results\"><ul><li><b>1 USD = 0.98 EUR</b>"
                .getBytes());
```


This creates an in-memory
                    ***ByteArrayInputStream***
                    from a string. How did I know what to put in the string? I had to reverse-engineer the underlying
                    code. Even so, this makes the code execute.


### Putting it together


Here is the test as a single method rather than broken up as it has been so far:


```
@Test
public void returnExpectedConversion_v3() throws Exception {
    final ByteArrayInputStream bais = new ByteArrayInputStream(
            "<div id=\"converter_results\"><ul><li><b>1 USD = 0.98 EUR</b>"
                    .getBytes());

    new NonStrictExpectations() {
        DefaultHttpClient httpclient;
        HttpResponse response;
        HttpEntity entity;

        {
            httpclient.execute((HttpUriRequest) any);
            result = response;
            response.getEntity();
            result = entity;
            entity.getContent();
            result = bais;
        }
    };

    new NonStrictExpectations(CurrencyConversion.class) {
        {
            CurrencyConversion.currencySymbols();
            result = mapFrom("USD", "EUR");
        }
    };
    BigDecimal result = CurrencyConversion.convertFromTo("USD", "EUR");
    assertThat(result.subtract(new BigDecimal(2)), is(lessThanOrEqualTo(new BigDecimal(0.001))));
}
```


On the one hand, this is pretty impressive. We've managed to exercise the code end-to-end without
                    touching it. If we want to write something that uses this class, we now have a way to do it.
                    Often, before trying to touch some code, we need to get it under test so we know if we broke
                    anything after making changes. This is called[Characterization
                        Testing](http://en.wikipedia.org/wiki/Characterization_test). Poorly written code like this typically makes doing so very hard. While it is still
                    hard, at least we are able to do so without touching the production code. Having characterization
                    tests around code makes refactoring safer.


So we're done, right?


**Wrong.**


## Going Old School


### We've addressed the symptom, not the cause


Notice that JMockIt made it possible to accomplish near black magic, but can we do better? If we
                    try, will the time invested be worth the effort? In this section we start with the same method and
                    make a few so-called legacy refactorings to the code to make it testable using more traditional
                    tools, hand-rolled test doubles in this case. Then we'll compare, make an observation and then look
                    at what would become possible.


### Introduce instance delegator


A typical problem with static methods is they cannot be overridden. To fix this, we might simply
                    make the class use all instance methods instead. However, let's assume for this example that we need
                    to maintain backwards compatibility so we need to keep the static methods in place (in my experience
                    this is not contrived).


While I might try to do this test-first, in fact, I have an existing JMockIt test, so instead I'm
                    going to simply make the necessary changes. I'll do this by copying CurrencyConversion into a new
                    package with the name v2 added to it (the source for this blog is generated from source code, so I
                    need to keep the original version around).


To introduce an instance delegator:

- Introduce a static instance of the class.
- Copy the static methods into instance methods (you'll need to create new method names as
                        static methods and instance methods cannot have the same name and signature).
- Change the static methods to call the instance methods on the internal static instance.


Here's one way to do that (the lazy initialization of the internal instance is deliberate and if
                    you're concerned about threading issues, we could use double-checked locking or just make the method
                    synchronized):


```
private static CurrencyConversion instance;

private static CurrencyConversion getInstance() {
    if (instance == null) {
        instance = new CurrencyConversion();
    }

    return instance;
}

public static BigDecimal convertFromTo(String fromCurrency, String toCurrency) {
    return getInstance().convert(fromCurrency, toCurrency);
}

public static Map<String, String> currencySymbols() {
    return getInstance().getAllCurrencySymbols();
}
```


### Extract a few methods


There are several opportunities to extract some methods, so here's a version of v2/CurrencyConversion
                    after a few method extractions:


```
public BigDecimal convert(String fromCurrency, String toCurrency) {
    validateCurrencies(fromCurrency, toCurrency);

    try {
        String result = getPage(fromCurrency, toCurrency);
        String value = extractToValue(result);
        return new BigDecimal(value);
    } catch (Exception e) {
        throw new RuntimeException(e);
    }
}

protected void validateCurrencies(String fromCurrency, String toCurrency) {
    Map<String, String> symbolToName = currencySymbols();
    if (!symbolToName.containsKey(fromCurrency))
        throw new IllegalArgumentException(String.format(
                "Invalid from currency: %s", fromCurrency));
    if (!symbolToName.containsKey(toCurrency))
        throw new IllegalArgumentException(String.format(
                "Invalid to currency: %s", toCurrency));
}

protected String extractToValue(String result) {
    String theWholeThing = result;
    int start = theWholeThing.lastIndexOf("<div id=\"converter_results\"><ul><li>");
    String substring = result.substring(start);
    int startOfInterestingStuff = substring.indexOf("<b>") + 3;
    int endOfIntererestingStuff = substring.indexOf("</b>",
            startOfInterestingStuff);
    String interestingStuff = substring.substring(
            startOfInterestingStuff, endOfIntererestingStuff);
    String[] parts = interestingStuff.split("=");
    return parts[1].trim().split(" ")[0];
}

protected String getPage(String fromCurrency, String toCurrency) throws URISyntaxException, IOException, HttpException {
    String url = String.format("http://www.gocurrency.com/v2/dorate.php?inV=1&from=%s&to=%s&Calculate=Convert", toCurrency, fromCurrency);
    HttpClient httpclient = new DefaultHttpClient();
    HttpGet httpget = new HttpGet(url);
    HttpResponse response = httpclient.execute(httpget);
    HttpEntity entity = response.getEntity();
    StringBuffer result = new StringBuffer();
    if (entity != null) {
        InputStream instream = entity.getContent();
        InputStreamReader irs = new InputStreamReader(instream);
        BufferedReader br = new BufferedReader(irs);
        String l;
        while ((l = br.readLine()) != null) {
            result.append(l);
        }
    }
    return result.toString();
}
```


Here is a version of the last test targeting this class (the one in the v2 package). This test
                    passes:


```
@Test
public void returnExpectedConversion_v4() throws Exception {
    final ByteArrayInputStream bais = new ByteArrayInputStream(
            "<div id=\"converter_results\"><ul><li><b>1 USD = 0.98 EUR</b>"
                    .getBytes());

    new NonStrictExpectations() {
        DefaultHttpClient httpclient;
        HttpResponse response;
        HttpEntity entity;

        {
            httpclient.execute((HttpUriRequest) any);
            result = response;
            response.getEntity();
            result = entity;
            entity.getContent();
            result = bais;
        }
    };

    new NonStrictExpectations(CurrencyConversion.class) {
        {
            CurrencyConversion.currencySymbols();
            result = mapFrom("USD", "EUR");
        }
    };
    BigDecimal result = CurrencyConversion.convertFromTo("USD", "EUR");
    assertThat(result.subtract(new BigDecimal(2)), is(lessThanOrEqualTo(new BigDecimal(0.001))));
}
```


### Testing subclass


Now I'll rewrite this test using hand-written test doubles instead JMockIt. Rather than show all of
                    the intermediate steps, I'll just show a final result:


```
class CurrencyConversion2_testingSubclass extends CurrencyConversion {
    @Override
    public void validateCurrencies(String fromCurrency, String toCurrency) {
    }

    @Override
    public Map<String, String> getAllCurrencySymbols() {
        return mapFrom("USD", "EUR");
    }

    @Override
    public String getPage(String fromCurrency, String toCurrency) {
        return "<div id=\"converter_results\"><ul><li><b>1 USD = 0.98 EUR</b>";
    }
}

@Test
public void returnExpectedConversion_v5() throws Exception {
    CurrencyConversion original = CurrencyConversion.reset(new CurrencyConversion2_testingSubclass());

    BigDecimal result = CurrencyConversion.convertFromTo("USD", "EUR");

    assertThat(result.subtract(new BigDecimal(2)), is(lessThanOrEqualTo(new BigDecimal(0.001))));

    CurrencyConversion.reset(original);
}
```


This test produces the same result as the JMockIt test doing much of the work by hand.


Note, to make this possible, we need to allow for the new-created Singleton class to be set and
                    reset:


```
public static CurrencyConversion reset(CurrencyConversion other) {
    CurrencyConversion original = instance;
    instance = other;
    return original;
}
```


## Observations


### Actual amount of time to do this


This technique of introducing an instance delegator, with an override-able static singleton and
                    several extracted methods might seem like quite a bit. In practice this kind of change is quick. How
                    quick? For this example, it took me 3 minutes using IntelliJ. Eclipse would have taken the same
                    amount of time. In vi, maybe 1 minute (ok, maybe not, but I do use a vi plugin in Eclipse, IntelliJ
                    and even Visual Studio). In any case, once you've practiced this, it's quick. We could have avoided
                    much of this if the class had not used all static methods to begin with, but that's a common problem
                    so knowing how to handle it is a good general technique to know.


### Yes, but...


A common concern raised is what about making all of those extracted methods protected? It does not
                    bother me because I believe test-ability is more important than design. That's actually a false
                    dichotomy but it sounds controversial so I like to say it anyway. In fact, many of these âprotected
                    methodsâ are complex enough to warrant individual classes. Next, introduce dependency inversion and
                    suddenly I'm wiring in dependent objects that are under my control, with override-able methods and
                    checking individual parts of this overall flow become a snap. Divide and conquer.


### First test versus second test


Here are the two tests again, for comparison:


***Using JMockIt***


```
@Test
public void returnExpectedConversion_v4() throws Exception {
    final ByteArrayInputStream bais = new ByteArrayInputStream(
            "<div id=\"converter_results\"><ul><li><b>1 USD = 0.98 EUR</b>"
                    .getBytes());

    new NonStrictExpectations() {
        DefaultHttpClient httpclient;
        HttpResponse response;
        HttpEntity entity;

        {
            httpclient.execute((HttpUriRequest) any);
            result = response;
            response.getEntity();
            result = entity;
            entity.getContent();
            result = bais;
        }
    };

    new NonStrictExpectations(CurrencyConversion.class) {
        {
            CurrencyConversion.currencySymbols();
            result = mapFrom("USD", "EUR");
        }
    };
    BigDecimal result = CurrencyConversion.convertFromTo("USD", "EUR");
    assertThat(result.subtract(new BigDecimal(2)), is(lessThanOrEqualTo(new BigDecimal(0.001))));
}
```


***Using Hand-rolled mocks and Refactoring***


```
class CurrencyConversion2_testingSubclass extends CurrencyConversion {
    @Override
    public void validateCurrencies(String fromCurrency, String toCurrency) {
    }

    @Override
    public Map<String, String> getAllCurrencySymbols() {
        return mapFrom("USD", "EUR");
    }

    @Override
    public String getPage(String fromCurrency, String toCurrency) {
        return "<div id=\"converter_results\"><ul><li><b>1 USD = 0.98 EUR</b>";
    }
}

@Test
public void returnExpectedConversion_v5() throws Exception {
    CurrencyConversion original = CurrencyConversion.reset(new CurrencyConversion2_testingSubclass());

    BigDecimal result = CurrencyConversion.convertFromTo("USD", "EUR");

    assertThat(result.subtract(new BigDecimal(2)), is(lessThanOrEqualTo(new BigDecimal(0.001))));

    CurrencyConversion.reset(original);
}
```


If you have to support test code, which version do you prefer? Wait, don't answer yet.


### First test still passes


I want to reiterate that even though I made several changes to the production code, the JMockIt test
                    still passes. That's pretty interesting to me. In fact, if you think in terms of how JMockIt
                    manipulates the classloader, it makes sense. Even so, it's still pretty cool.


### What if we try with JMockIt again


Why stop here? What happens if we take the time to rewrite the JMockIt test taking into consideration
                    the changes made to the production code?


```
@Test
public void returnExpectedConversion_final() throws Exception {
    new NonStrictExpectations(CurrencyConversion.class) {
        CurrencyConversion c;
        {
            c.validateCurrencies(anyString, anyString);
            c.getPage(anyString, anyString);
            result = "<div id=\"converter_results\"><ul><li><b>1 USD = 0.98 EUR</b>";
        }
    };
    BigDecimal result = CurrencyConversion.convertFromTo("USD", "EUR");
    assertThat(result.subtract(new BigDecimal(2)), is(lessThanOrEqualTo(new BigDecimal(0.001))));
}
```


Now which one do you want to maintain?


Notice, a little bit of refactoring makes the final JMockIt test much better. In fact, the amount of
                    refactoring required to write this version of the test is smaller than the amount I did refactor.
                    Simply extracting methods would have been enough to greatly improve the JMockIt test. Notice,
                    however, that JMockIt did not force this. Not using a mocking tool or using a tool like Mockito
                    would have forced me to do some amount of refactoring to get this class under test.


## Closing the Feedback Loop


What happens when people work[open
                loop](http://en.wikipedia.org/wiki/Open-loop_controller)? That is, you write some code and then tools like JMockIt make it possible to go back in
                and write tests after the fact without having to suffer for poor decisions? I ask because this
                example demonstrates such a situation. The original code is a mess, JMockIt allowed me to write a
                characterization test to exercise the code. That is great. It did not, however, force me to address the
                original problem. In a sense, it also allowed me to avoid the pain associated with having to fix a
                mess. If we take away the powerful tool, then we have to clean up the mess to get a test written. Notice
                when we did clean up the code, it's still a mess but it's better than it was and the refactored code
                suggests other improvements as well. Also, maybe the next time someone is writing code they might have
                learned something and maybe, just maybe, they will not make the same mistake again, or at least not as
                often.


While not direclty related, here is a great article to read that relates to this idea of feedback:
                [Secrets of a
                    Mind-Gamer by Joshua Foer
                ](http://www.nytimes.com/interactive/2011/02/20/magazine/mind-secrets.html). One of the things discussed in this article is what it takes to improve a skill: failure. That
                is, we need to make mistakes and then learn from those mistakes. What happens when tools allow us to
                not learn from our mistakes? I'm concerned that powerful tools might loosen or remove the pain
                associated with failure, which will lead to stagnation. If we are not always striving to make new stupid
                mistakes, then we aren't really learning, right?


## Conclusions


Do I think we should not use tools like JMockIt? No. I think JMockIt is an amazing tool and I have been
                in situations where its power is welcome, necessary even. However, what about its use during new
                development? I'm of two minds. On the one hand, I want the most powerful tool available to me when
                working. Even though my favorite mocking library is Mockito, it is not as powerful as JMockIt. On the
                other hand, JMockIt actually requires more discipline to use effectively because it allows me to leave
                in a bit more of a mess and still accomplish what I want to accomplish.


Maybe this is a red herring. I generally practice[Test Driven Development](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd).
                While I don't have experience practicing TDD on a real project using JMockIt, I do with Mockito and I
                don't think I have any issues with over using it. I still have a problem of sometimes being too
                cute/clever, but I cannot blame a tool on that. I can say I have seen other teams use Mockito and Moq
                (Mockito's equivalent in C#) and way over used them. However, when I've seen that, those teams were
                writing tests after much development - that is not the fault of the tool. It seems if someone
                has the discipline to work in small increments, writing tests along the way (hopefully first) then the
                power of JMockIt won't cause any issues. On the other hand, if the power of JMockIt is going to be an
                issue, there's probably deeper issues to worry about.


In any case, I encourage you to give these kinds of tools a try and learn for yourself if having such
                power helps or hinders your learning.


---
