---
title: "A practical understanding of Flux"
date: 2015-07-20
url: https://drewdevault.com/2015/07/20/A-practical-understanding-of-Flux.html
slug: A-practical-understanding-of-Flux
word_count: 1451
---

[React.js](https://facebook.github.io/react/)  and the
 [Flux](https://facebook.github.io/flux/)  are shaping up to be some of the most
important tools for web development in the coming years. The MVC model was
strong on the server when we decided to take the frontend seriously, and it was
shoehorned into the frontend since we didn’t know any better. React and Flux
challenge that and I like where it’s going very much. That being said, it was
very difficult for me to get into. I put together this blog post to serve as a
more  *practical*  guide - the upstream documentation tells you a lot of concepts
and expects you to put them together yourself. Hopefully at the end of this
blog post you can confidently start writing things with React+Flux instead of
reading brain-melting docs for a few hours like I did.

At the core of it, React and Flux are very simple and elegant. Far more simple
than the voodoo sales pitch upstream would have you believe. To be clear,
 **React**  is a framework-ish that lets you describe your UI through reusable
components, and includes  *jsx*  for describing HTML elements directly in your
JavaScript code.  **Flux**  is an  *optional*  architectural design philosophy that
you can adopt to help structure your applications. I have been using
 [Babel](https://babeljs.io/)  to compile my React+Flux work, which gives me
ES6/ES7 support - I strongly suggest you do the same. This blog post assumes
you’re doing so. For a crash course on ES6,  [read this entire
page](http://git.io/es6features) . Crash course for ES7 is omitted here for
brevity, but  [click this](https://gist.github.com/SirCmpwn/2e8e455c91494b7c3713) 
if you’re interested.

## Flux overview

Flux is based on a unidirectional data flow. The direction is: dispatcher ➜
stores ➜ views, and the data is actions. At the stores or views level, you can
give actions to the dispatcher, which passes them down the line.

Let’s explain exactly what piece is, and how it fits in to your application.
After this I’ll tell you some specific details and I have a starter kit prepared
for you to grab as well.

### Dispatcher

The dispatcher is very simple. Anything can register to receive a callback when
an “action” happens. There is one dispatcher and one set of callbacks, and
everything that registers for it will receive every action given to the
dispatcher, and can do with this as it pleases. Generally speaking you will only
have the stores listen to this. The kind of actions you will send along may look
something like this:

* Add a record
* Delete a record
* Fetch a record with a given ID
* Refresh a store

Anything that would change data is going to be given to the dispatcher and
passed along to the actions. Since everything receives every action you give to
the dispatcher, you have to encode something into each action that describes
what it’s for. I use objects that look something like this:

```
{
    "action": "STORE_NAME.ACTION_TYPE.ETC",
    ...
}
```

Where  `...`  is whatever extra data you need to include (the ID of the record
to fetch, the contents of the record to be added, the property that needs to
change, etc). Here’s an example payload:

```
{
    "action": "ACCOUNTS.CREATE.USER",
    "username": "SirCmpwn",
    "email": "sir@cmpwn.com",
    "password": "hunter2"
}
```

The Accounts store is listening for actions that start with  `ACCOUNTS.`  and when
it sees  `CREATE.USER` , it knows a new user needs to be created with these
details.

### Stores

The stores just have ownership of data and handle any changes that happen to
that data. When the data changes, they raise events that the views can subscribe
to to let them know what’s up. There’s nothing magic going on here (I initially
thought there was magic). Here’s a really simple store:

```
import Dispatcher from "whatever";

export class UserStore {
    constructor() {
        this._users = [];
        this.action = this.action.bind(this);
        Dispatcher.register(this.action);
    }

    get Users() {
        return this._users;
    }

    action(payload) {
        switch (payload.action) {
        case "ACCOUNTS.CREATE.USER":
            this._users.push({ 
                "username": payload.username,
                "email": payload.email,
                "password": payload.password
            });
            raiseChangeEvent(); // Exercise for the reader
            break;
        }
    }
}

let store = new UserStore();
export default new UserStore();
```

Yeah, that’s all there is to it. Each store should be a singleton. You use it
like this:

```
import UserStore from "whatever/UserStore";

console.log(UserStore.Users);

UserStore.registerChangeEvent(() => {
    console.log(UserStore.Users); // This has changed now
});
```

Stores end up having a lot of boilerplate. I haven’t quite figured out the best
way to address that yet.

### Views

Views are react components. What makes React components interesting is that they
re-render the whole thing when you call  `setState` . If you want to change the
way it appears on the page for any reason, a call to  `setState`  will need to
happen. And here are the two circumstances under which they will change:

* In response to user input to change non-semantic view state
* In response to a change event from a store

The first bullet here means that you can call  `setState`  to change view states,
but not data. The second bullet is for when the data changes. When you change
view states, this refers to things like “click button to reveal form”. When you
change data, this refers to things like “a new record was created, show it”, or
even “a single property of a record changed, show that change”.

**Wrong way** : you have a text box that updates the “name” of a record. When the
user presses the “Apply” key, the view will re-render itself with the new name.

**Right way** : When you press “Apply”, the view sends an action to the
dispatcher to apply the change. The relevant store picks up the action, applies
the change to its own data store, and raises an event. Your view hears that
event and re-renders itself.

### Why bother?

* Easy to have stores depend on each other
* All views that depend on the same stores are updated when it changes
* It follows that all cross-store dependencies are updated in a similar fashion
* Single source of truth for data
* Easy as pie to pick up and maintain with little knowledge of the codebase

## Practical problems

Here are some problems I ran into, and the fluxy solution to each.

### Need to load data async

You have a list of DNS records to show the user, but they’re hanging out on the
server instead of in JavaScript objects. Here’s how you accomodate for this:

* When you use a store, call  `Store.fetchIfNecessary()`  first.
* When you pull data from the store, expect  `null`  and handle this elegantly.
* When the initial fetch finishes in the store, raise a change event.

From  `fetchIfNecessary`  in the store, go do the request unless it’s in progress or
done. On the view side, show a loading spinner or something if you get  `null` .
When the change event happens, whatever code set the state of your component
initially will be re-run, and this time it won’t get  `null`  - deal with it
appropriately (show the actual UI).

This works for more than things that are well-defined at dev time. If you need
to, for example, fetch data for an arbitrary ID:

* View calls  `Store.userById(10)`  and gets  `null` , renders lack of data
appropriately
* Store is like “my bad” and fetches it from the server
* Store raises change event when it arrives and the view re-renders

### Batteries not included

Upstream, in terms of actual usable code, flux just gives you a dispatcher. You
also need something to handle your events. This is easy to roll yourself, or you
can grab one of a bazillion things online that will do it for you. There is also
no base Store class for you, so make one of those. You should probably just
include some shared code for raising events and consuming actions. Mine looks
something like this:

```
class UserStore extends Store {
    constructor() {
        super("USER");
        this._users = [];
        super.action("CREATE.USER", this.userCreated);
    }

    userCreated(payload) {
        this._users.push(...);
        super.raiseChangeEvent();
    }

    get Users {
        return this._users;
    }
}
```

Do what works best for you.

## Starter Kit

If you want something with the batteries in and a base to build from, I’ve got
you covered. Head over to
 [SirCmpwn/react-starter-kit](https://github.com/SirCmpwn/react-starter-kit)  on
Github.

## Conclusion

React and Flux are going to be big. This feels like the right way to build a
frontend. Hopefully I saved you from all the headache I went through trying to
“get” this stuff, and I hope it serves you well in the future. I’m going to be
pushing pretty hard for this model at my new gig, so I may be writing more blog
posts as I explore it in a large-scale application - stay tuned.
