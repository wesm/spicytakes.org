---
title: "Static Substitution"
description: "As I listen to our development teams talk about their work, one   common theme is their dislike of things held in statics. Typically   we see common services or components held in static variables wit"
date: 2004-10-20T00:00:00
tags: ["testing", "application architecture", "refactoring"]
url: https://martinfowler.com/bliki/StaticSubstitution.html
slug: StaticSubstitution
word_count: 734
---


As I listen to our development teams talk about their work, one
  common theme is their dislike of things held in statics. Typically
  we see common services or components held in static variables with
  static initializers. One of the big problems with statics (in most
  languages) is you can't use polymorphism to substitute one
  implementation with another. This bits us a lot because we are great
  fans of testing - and to test well it's important to be able to replace
    services with a [Service Stub](https://martinfowler.com/eaaCatalog/serviceStub.html).


Here's an example of this kind of static.


```

public class AddressBook {
  private static String connectionString, username, password;

  static {
    Properties props = getProperties();
    connectionString =(String) props.get("db.connectionString");
    password = (String) props.get("db.password");
    username = (String) props.get("db.username");
  }

  public static Person findByLastName(String s) {
    String query = 
      "SELECT lastname, firstname FROM PEOPLE where lastname = ?";
    Connection conn = null;
    PreparedStatement st = null;
    ResultSet rs = null;
    try {
      conn = DriverManager.getConnection(connectionString, 
                                         username, 
                                         password);
      st = conn.prepareStatement(query);
      st.setString(1, s);
      rs = st.executeQuery();
      rs.next();
      Person result = new Person (rs.getString(2), rs.getString(1));
      return result;
    } catch (Exception e) {
      throw new RuntimeException(e);
    } finally {
      cleanUp(conn, st, rs);
    }
    }
```


So what we have here is a bunch of configuration stuff
  initialized in the static initializer, and then a static method to
  run a query against the database.


Some changes are easy with this. By altering a properties file we
  can easily change which database this program runs against. But for
  testing we might not want to run it against a database at all - a
  simple stub would just return canned data.


To allow simple substitution we need do a little refactoring. The
  first step is to turn the statics into a singleton.


```


public class AddressBook {

    private static AddressBook soleInstance = new AddressBook();

    private String connectionString, username, password;

    public AddressBook() {
        Properties props = getProperties();
        connectionString =(String) props.get("db.connectionString");
        password = (String) props.get("db.password");
        username = (String) props.get("db.username");
    }

    public static Person findByLastName(String s) {
        return  soleInstance.findByLastNameImpl(s);
    }

    public Person findByLastNameImpl(String s) {
        String query = "SELECT lastname, firstname FROM PEOPLE where lastname = ?";
        Connection conn = null;
        PreparedStatement st = null;
        ResultSet rs = null;
        try {
            conn = DriverManager.getConnection(connectionString, username, password);
            st = conn.prepareStatement(query);
            st.setString(1, s);
            rs = st.executeQuery();
            rs.next();
            Person result = new Person (rs.getString(2), rs.getString(1));
            return result;
        } catch (Exception e) {
            throw new RuntimeException(e);
        } finally {
            cleanUp(conn, st, rs);
        }
    }


```


This is a pretty straightforward refactoring.

- We take all the
  static data on the old class and turn it into instance data.
- We move the static initialization code and move it into the constructor.
- We take all the public methods and move the body of them onto
    the instance leaving the static method as a simple delegator.


I don't have this refactoring in the catalog - perhaps I should
  call it Replace Statics With Singleton. As it stands this doesn't
  change anything, but it is a step towards supporting
  substitution. The next step is to introduce a method to load the
  sole instance.


```
    public static void loadInstance(AddressBook arg) {
        soleInstance = arg;
    }


```


This now prepares us to do substitution for testing (or other)
  purposes. Now in a test case we can add a suitable call in a test
    `setUp` method: `AddressBook.loadInstance(new
    StubAddressBook());`. As long as the stub subclasses the
    AddressBook, we can now test against a stub instead of the real thing.


This isn't the end of the story. In particular with this code we
  have to create an instance of the actual service even if we never
  use it - because the sole instance is initialized in a static
  initializer. This forces a dependency upon the service access code
  which can cause its own pain. To deal with this we need to move any
  such initialization out of static initializers and into a separate
    initializer class that is itself substitutable. (see [Chris](http://www.skizz.biz/archives/000421.html) for more
  on this.) But at least this provides a useful first step.


This also brings out some problems that singletons can store
    up. In particular if you use a singleton (or other form of [Registry](https://martinfowler.com/eaaCatalog/registry.html))
  make sure that they can be easily substituted and that their
  initialization can also be easily replaced.


I just got a copy of Michael Feathers's new book [Working
  Effectively With Legacy Code](https://www.amazon.com/gp/product/0131177052/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0131177052&linkCode=as2&tag=martinfowlerc-20). He talks more (and better) about many
  of these kinds of issues.
