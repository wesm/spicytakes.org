---
title: "Dependency Composition"
description: "Based on frustrations with conventional framework-based dependency injection, I have        adopted a composition strategy that utilizes partial application to inject context into modules.       When "
date: 2023-05-23T00:00:00
tags: ["object collaboration design", "application architecture"]
url: https://martinfowler.com/articles/dependency-composition.html
slug: dependency-composition
word_count: 6032
---


## Origin Story


It all started a few years ago when members of one of my teams asked,
        âwhat pattern should we adopt for [dependency injection](https://www.martinfowler.com/articles/injection.html#FormsOfDependencyInjection) (DI)â?
        The team's stack was Typescript on Node.js, not one I was terribly familiar with, so I
        encouraged them to work it out for themselves. I was disappointed to learn
        some time later that team had decided, in effect, not to decide, leaving
        behind a plethora of patterns for wiring modules together. Some developers
        used factory methods, others manual dependency injection in root modules, 
        and some objects in class constructors.


The results were less than ideal: a hodgepodge of object-oriented and
        functional patterns assembled in different ways, each requiring a very
        different approach to testing. Some modules were unit testable, others
        lacked entry points for testing, so simple logic required complex HTTP-aware
        scaffolding to exercise basic functionality. Most critically, changes in
        one part of the codebase sometimes caused broken contracts in unrelated areas.
        Some modules were interdependent across namespaces; others had completely flat collections of modules with
        no distinction between subdomains.


With the benefit of hindsight, I continued to think
        about that original decision: what DI pattern should we have picked.
        Ultimately I came to a conclusion: that was the wrong question.


## Dependency injection is a means, not an end


In retrospect, I should have guided the team towards asking a different
        question: what are the desired qualities of our codebase, and what
        approaches should we use to achieve them? I wish I had advocated for the
        following:

- discrete modules with minimal incidental coupling, even at the cost of some duplicate
          types
- business logic that is kept from intermingling with code that manages the transport,
          like HTTP handlers or GraphQL resolvers
- business logic tests that are not transport-aware or have complex
          scaffolding
- tests that do not break when new fields are added to types
- very few types exposed outside of their modules, and even fewer types exposed
          outside of the directories they inhabit.


Over the last few years, I've settled on an approach that leads a 
        developer who adopts it toward these qualities. Having come from a 
        [Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html) (TDD) background, I naturally start there.
        TDD encourages incrementalism but I wanted to go even further, 
        so I have taken a minimalist âfunction-firstâ approach to module composition.     
        Rather than continuing to describe the process, I will demonstrate it.
        What follows is an example web service built on a relatively simple
        architecture wherein a controller module calls domain logic which in turn
        calls repository functions in the persistence layer.


## The problem description


Imagine a user story that looks something like this:


As a registered user of RateMyMeal and a would-be restaurant patron who
        doesn't know what's available, I would like to be provided with a ranked
        set of recommended restaurants in my region based on other patron ratings.


**Acceptance Criteria**

- The restaurant list is ranked from the most to the least
          recommended.
- The rating process includes the following potential rating
        levels:
- The overall rating is the sum of all individual ratings.
- Users considered âtrustedâ get a 4X multiplier on their
          rating.
- The user must specify a city to limit the scope of the returned
        restaurant.


## Building a solution


I have been tasked with building a REST service using Typescript,
      Node.js, and PostgreSQL. I start by building a very coarse integration
      as a [walking skeleton](https://wiki.c2.com/?WalkingSkeleton) that defines the 
      boundaries of the problem I wish to solve. This test uses as much of
      the underlying infrastructure as possible. If I use any stubs, it's
      for third-party cloud providers or other services that can't be run
      locally. Even then, I use server stubs, so I can use real SDKs or
      network clients. This becomes my acceptance test for the task at hand,
      keeping me focused. I will only cover one âhappy pathâ that exercises the
      basic functionality since the test will be time-consuming to build
      robustly. I'll find less costly ways to test edge cases. For the sake of
      the article, I assume that I have a skeletal database structure that I can
      modify if required.


![](dependency-composition/db.png)


Tests generally have a `given/when/then` structure: a set of
      given conditions, a participating action, and a verified result. I prefer to
      start at `when/then` and back into the `given` to help me focus the problem I'm trying to solve.


â**When** I call my recommendation endpoint, **then** I expect to get an OK response
        and a payload with the top-rated restaurants based on our ratings
        algorithmâ. In code that could be:


test/e2e.integration.spec.tsâ¦


```
  describe("the restaurants endpoint", () => {
    it("ranks by the recommendation heuristic", async () => {
      const response = await axios.get<ResponsePayload>(    â
        "http://localhost:3000/vancouverbc/restaurants/recommended",
        { timeout: 1000 },
      );
      expect(response.status).toEqual(200);
      const data = response.data;
      const returnRestaurants = data.restaurants.map(r => r.id);
      expect(returnRestaurants).toEqual(["cafegloucesterid", "burgerkingid"]);    â
    });
  });
  
  type ResponsePayload = {
    restaurants: { id: string; name: string }[];
  };
```


There are a couple of details worth calling out:

1. `Axios` is the HTTP client library I've chosen to use.
        The Axios `get` function takes a type argument
        (`ResponsePayload`) that defines the expected structure of
        the response data. The compiler will make sure that all uses of
        `response.data` conform to that type, however, this check can
        only occur at compile-time, so cannot guarantee the HTTP response body
        actually contains that structure. My assertions will need to do
        that.
2. Rather than checking the entire contents of the returned restaurants,
          I only check their ids. This small detail is deliberate. If I check the 
          contents of the entire object, my test becomes fragile, breaking if I 
          add a new field. I want to write a test that will accommodate the natural 
          evolution of my code while at the same time verifying the specific condition 
          I'm interested in: the order of the restaurant listing.


Without my `given` conditions, this test isn't very valuable, so I add them next.


test/e2e.integration.spec.tsâ¦


```
  describe("the restaurants endpoint", () => {
    let app: Server | undefined;
    let database: Database | undefined;
  
    const users = [
      { id: "u1", name: "User1", trusted: true },
      { id: "u2", name: "User2", trusted: false },
      { id: "u3", name: "User3", trusted: false },
    ];
  
    const restaurants = [
      { id: "cafegloucesterid", name: "Cafe Gloucester" },
      { id: "burgerkingid", name: "Burger King" },
    ];
  
    const ratingsByUser = [
      ["rating1", users[0], restaurants[0], "EXCELLENT"],
      ["rating2", users[1], restaurants[0], "TERRIBLE"],
      ["rating3", users[2], restaurants[0], "AVERAGE"],
      ["rating4", users[2], restaurants[1], "ABOVE_AVERAGE"],
    ];
  
    beforeEach(async () => {
      database = await DB.start();
      const client = database.getClient();
  
      await client.connect();
      try {
        // GIVEN
        // These functions don't exist yet, but I'll add them shortly
        for (const user of users) {
          await createUser(user, client);
        }
  
        for (const restaurant of restaurants) {
          await createRestaurant(restaurant, client);
        }
  
        for (const rating of ratingsByUser) {
          await createRatingByUserForRestaurant(rating, client);
        }
      } finally {
        await client.end();
      }
  
      app = await server.start(() =>
        Promise.resolve({
          serverPort: 3000,
          ratingsDB: {
            ...DB.connectionConfiguration,
            port: database?.getPort(),
          },
        }),
      );
    });
  
    afterEach(async () => {
      await server.stop();
      await database?.stop();
    });
  
    it("ranks by the recommendation heuristic", async () => {
      // .. snip
```


My `given` conditions are implemented in the `beforeEach` function. `
        beforeEach` accommodates the addition of more tests should
        I wish to utilize the same setup scaffold and keeps the pre-conditions
        cleanly independent of the rest of the test. You'll notice a lot of
        `await` calls. Years of experience with reactive platforms
        like Node.js have taught me to define asynchronous contracts for all 
        but the most straight-forward functions.
        Anything that ends up IO-bound, like a database call or file read,
        should be asynchronous and synchronous implementations are very easy to 
        wrap in a Promise, if necessary. By contrast, choosing a synchronous
        contract, then finding it needs to be async is a much uglier problem to
        solve, as we'll see later.


I've intentionally deferred creating explicit types for the users and
        restaurants, acknowledging I don't know what they look like yet.
        With Typescript's structural typing, I can continue to defer creating that
        definition and still get the benefit of type-safety as my module APIs
        begin to solidify. As we'll see later, this is a critical means by which
        modules can be kept decoupled.


At this point, I have a shell of a test with test dependencies
        missing. The next stage is to flesh out those dependencies by first building
        stub functions to get the test to compile and then implementing these helper
        functions. That is a non-trivial amount of work, but it's also highly
        contextual and out of the scope of this article. Suffice it to say that it
        will generally consist of:

- starting up dependent services, such as databases. I generally use [testcontainers](https://github.com/testcontainers/testcontainers-node) to run dockerized services, but these could
          also be network fakes or in-memory components, whatever you prefer.
- fill in the `create...` functions to pre-construct the entities required for
          the test. In the case of this example, these are SQL `INSERT`s.
- start up the service itself, at this point a simple stub. We'll dig a
          little more into the service initialization since it's germaine to the
          discussion of composition.


If you are interested in how the test dependencies are initialized, you can
        see [the results](https://github.com/danielsomerfield/function-first-composition-example-typescript/blob/main/test/e2e.integration.spec.ts) in the GitHub repo.


Before moving on, I run the test to make sure it fails as I would
      expect. Because I have not yet implemented my service
      `start`, I expect to receive a connection refused error when
      making my http request. With that confirmed, I disable my big integration
      test, since it's not going to pass for a while, and commit.


## On to the controller


I generally build from the outside in, so my next step is to
      address the main HTTP handling function. First, I'll build a controller
      unit test. I start with something that ensures an empty 200
      response with expected headers:


test/restaurantRatings/controller.spec.tsâ¦


```
  describe("the ratings controller", () => {
    it("provides a JSON response with ratings", async () => {
      const ratingsHandler: Handler = controller.createTopRatedHandler();
      const request = stubRequest();
      const response = stubResponse();
  
      await ratingsHandler(request, response, () => {});
      expect(response.statusCode).toEqual(200);
      expect(response.getHeader("content-type")).toEqual("application/json");
      expect(response.getSentBody()).toEqual({});
    });
  });
```


I've already started to do a little design work that will result in
        the highly decoupled modules I promised. Most of the code is fairly
        typical test scaffolding, but if you look closely at the highlighted function
        call it might strike you as unusual.


This small detail is the first step toward 
        [partial application](https://en.wikipedia.org/wiki/Partial_application),
         or functions returning functions with context. In the coming paragraphs, 
         I'll demonstrate how it becomes the foundation upon which the compositional approach is built.


Next, I build out the stub of the unit under test, this time the controller, and
        run it to ensure my test is operating as expected:


src/restaurantRatings/controller.tsâ¦


```
  export const createTopRatedHandler = () => {
    return async (request: Request, response: Response) => {};
  };
```


My test expects a 200, but I get no calls to `status`, so the
      test fails. A minor tweak to my stub it's passing:


src/restaurantRatings/controller.tsâ¦


```
  export const createTopRatedHandler = () => {
    return async (request: Request, response: Response) => {
      response.status(200).contentType("application/json").send({});
    };
  };
```


I commit and move on to fleshing out the test for the expected payload. I
        don't yet know exactly how I will handle the data access or
        algorithmic part of this application, but I know that I would like to
        delegate, leaving this module to nothing but translate between the HTTP protocol
        and the domain. I also know what I want from the delegate. Specifically, I
        want it to load the top-rated restaurants, whatever they are and wherever
        they come from, so I create a âdependenciesâ stub that has a function to
        return the top restaurants. This becomes a parameter in my factory function.


test/restaurantRatings/controller.spec.tsâ¦


```
  type Restaurant = { id: string };
  type RestaurantResponseBody = { restaurants: Restaurant[] };

  const vancouverRestaurants = [
    {
      id: "cafegloucesterid",
      name: "Cafe Gloucester",
    },
    {
      id: "baravignonid",
      name: "Bar Avignon",
    },
  ];

  const topRestaurants = [
    {
      city: "vancouverbc",
      restaurants: vancouverRestaurants,
    },
  ];

  const dependenciesStub = {
    getTopRestaurants: (city: string) => {
      const restaurants = topRestaurants
        .filter(restaurants => {
          return restaurants.city == city;
        })
        .flatMap(r => r.restaurants);
      return Promise.resolve(restaurants);
    },
  };

  const ratingsHandler: Handler =
    controller.createTopRatedHandler(dependenciesStub);
  const request = stubRequest().withParams({ city: "vancouverbc" });
  const response = stubResponse();

  await ratingsHandler(request, response, () => {});
  expect(response.statusCode).toEqual(200);
  expect(response.getHeader("content-type")).toEqual("application/json");
  const sent = response.getSentBody() as RestaurantResponseBody;
  expect(sent.restaurants).toEqual([
    vancouverRestaurants[0],
    vancouverRestaurants[1],
  ]);
```


With so little information on how the `getTopRestaurants` function is implemented,
      how do I stub it? I know enough to design a basic client view of the contract I've
      created implicitly in my dependencies stub: a simple unbound function that
      asynchronously returns a set of Restaurants. This contract might be
      fulfilled by a simple static function, a method on an object instance, or
      a stub, as in the test above. This module doesn't know, doesn't
      care, and doesn't have to. It is exposed to the minimum it needs to do its
      job, nothing more.


src/restaurantRatings/controller.tsâ¦


```
  
  interface Restaurant {
    id: string;
    name: string;
  }
  
  interface Dependencies {
    getTopRestaurants(city: string): Promise<Restaurant[]>;
  }
  
  export const createTopRatedHandler = (dependencies: Dependencies) => {
    const { getTopRestaurants } = dependencies;
    return async (request: Request, response: Response) => {
      const city = request.params["city"]
      response.contentType("application/json");
      const restaurants = await getTopRestaurants(city);
      response.status(200).send({ restaurants });
    };
  };
```


For those who like to visualize these things, we can visualize the production
      code so far as the handler function that requires something that
      implements the `getTopRatedRestaurants` interface using
      a [ball and socket](https://martinfowler.com/bliki/BallAndSocket.html) notation.


The tests create this function and a stub for the required
      function. I can show this by using a different colour for the tests, and
      the socket notation to show implementation of an interface.


This `controller` module is brittle at this point, so I'll need to
        flesh out my tests to cover alternative code paths and edge cases, but that's a bit beyond
        the scope of the article. If you're interested in seeing a more thorough [test](https://github.com/danielsomerfield/function-first-composition-example-typescript/blob/main/test/restaurantRatings/controller.spec.ts) and the [resulting controller module](https://github.com/danielsomerfield/function-first-composition-example-typescript/blob/main/src/restaurantRatings/controller.ts), both are available in
      the GitHub repo.


## Digging into the domain


At this stage, I have a controller that requires a function that doesn't exist. My
        next step is to provide a module that can fulfill the `getTopRestaurants`
        contract. I'll start that process by writing a big clumsy unit test and
        refactor it for clarity later. It is only at this point I start thinking
        about how to implement the contract I have previously established. I go
        back to my original acceptance criteria and try to minimally design my
        module.


test/restaurantRatings/topRated.spec.tsâ¦


```
  describe("The top rated restaurant list", () => {
    it("is calculated from our proprietary ratings algorithm", async () => {
      const ratings: RatingsByRestaurant[] = [
        {
          restaurantId: "restaurant1",
          ratings: [
            {
              rating: "EXCELLENT",
            },
          ],
        },
        {
          restaurantId: "restaurant2",
          ratings: [
            {
              rating: "AVERAGE",
            },
          ],
        },
      ];
  
      const ratingsByCity = [
        {
          city: "vancouverbc",
          ratings,
        },
      ];
  
      const findRatingsByRestaurantStub: (city: string) => Promise<    â
        RatingsByRestaurant[]
      > = (city: string) => {
        return Promise.resolve(
          ratingsByCity.filter(r => r.city == city).flatMap(r => r.ratings),
        );
      }; 
  
      const calculateRatingForRestaurantStub: (    â
        ratings: RatingsByRestaurant,
      ) => number = ratings => {
        // I don't know how this is going to work, so I'll use a dumb but predictable stub
        if (ratings.restaurantId === "restaurant1") {
          return 10;
        } else if (ratings.restaurantId == "restaurant2") {
          return 5;
        } else {
          throw new Error("Unknown restaurant");
        }
      }; 
  
      const dependencies = {    â
        findRatingsByRestaurant: findRatingsByRestaurantStub,
        calculateRatingForRestaurant: calculateRatingForRestaurantStub,
      }; 
  
      const getTopRated: (city: string) => Promise<Restaurant[]> =
        topRated.create(dependencies);
      const topRestaurants = await getTopRated("vancouverbc");
      expect(topRestaurants.length).toEqual(2);
      expect(topRestaurants[0].id).toEqual("restaurant1");
      expect(topRestaurants[1].id).toEqual("restaurant2");
    });
  });
  
  interface Restaurant {
    id: string;
  }
  
  interface RatingsByRestaurant {    â
    restaurantId: string;
    ratings: RestaurantRating[];
  } 
  
  interface RestaurantRating {
    rating: Rating;
  }
  
  export const rating = {    â
    EXCELLENT: 2,
    ABOVE_AVERAGE: 1,
    AVERAGE: 0,
    BELOW_AVERAGE: -1,
    TERRIBLE: -2,
  } as const; 
  
  export type Rating = keyof typeof rating;
```


I have introduced a lot of new concepts into the domain at this point, so I'll take them one at a time:

1. I need a âfinderâ that returns a set of ratings for each restaurant. I'll
            start by stubbing that out.
2. The acceptance criteria provide the algorithm that will drive the overall rating, but
            I choose to ignore that for now and say that, *somehow*, this group of ratings
              will provide the overall restaurant rating as a numeric value.
3. For this module to function it will rely on two new concepts:
            finding the ratings of a restaurant, and given that set or ratings,
            producing an overall rating. I create another âdependenciesâ interface that
            includes the two stubbed functions with naive, predictable stub implementations
            to keep me moving forward.
4. The `RatingsByRestaurant` represents a collection of
            ratings for a particular restaurant. `RestaurantRating` is a
            single such rating. I define them within my test to indicate the
            intention of my contract. These types might disappear at some point, or I
            might promote them into production code. For now, it's a good reminder of
            where I'm headed. Types are very cheap in a structurally-typed language
            like Typescript, so the cost of doing so is very low.
5. I also need `rating`, which, according to the ACs, is composed of 5 
            values: âexcellent (2), above average (1), average (0), below average (-1), terrible (-2)â. 
            This, too, I will capture within the test module, waiting until the âlast responsible momentâ
            to decide whether to pull it into production code.


Once the basic structure of my test is in place, I try to make it compile
        with a minimalist implementation.


src/restaurantRatings/topRated.tsâ¦


```
  interface Dependencies {}
  
  
  export const create = (dependencies: Dependencies) => {    â
    return async (city: string): Promise<Restaurant[]> => [];
  }; 
  
  interface Restaurant {    â
    id: string;
  }  
  
  export const rating = {    â
    EXCELLENT: 2,
    ABOVE_AVERAGE: 1,
    AVERAGE: 0,
    BELOW_AVERAGE: -1,
    TERRIBLE: -2,
  } as const;
  
  export type Rating = keyof typeof rating; 
```

1. Again, I use my partially applied function
            factory pattern, passing in dependencies and returning a function. The test
            will fail, of course, but seeing it fail in the way I expect builds my confidence
            that it is sound.
2. As I begin implementing the module under test, I identify some
            domain objects that should be promoted to production code. In particular, I
            move the direct dependencies into the module under test. Anything that isn't
            a direct dependency, I leave where it is in test code.
3. I also make one anticipatory move: I extract the `Rating` type into
            production code. I feel comfortable doing so because it is a universal and explicit domain
            concept. The values were specifically called out in the acceptance criteria, which says to
            me that couplings are less likely to be incidental.


Notice that the types I define or move into the production code are *not* exported
        from their modules. That is a deliberate choice, one I'll discuss in more depth later.
        Suffice it to say, I have yet to decide whether I want other modules binding to
        these types, creating more couplings that might prove to be undesirable.


Now, I finish the implementation of the `getTopRated.ts` module.


src/restaurantRatings/topRated.tsâ¦


```
  interface Dependencies {    â
    findRatingsByRestaurant: (city: string) => Promise<RatingsByRestaurant[]>;
    calculateRatingForRestaurant: (ratings: RatingsByRestaurant) => number;
  }
  
  interface OverallRating {    â
    restaurantId: string;
    rating: number;
  }
  
  interface RestaurantRating {    â
    rating: Rating;
  }
  
  interface RatingsByRestaurant {
    restaurantId: string;
    ratings: RestaurantRating[];
  }
  
  export const create = (dependencies: Dependencies) => {    â
    const calculateRatings = (
      ratingsByRestaurant: RatingsByRestaurant[],
      calculateRatingForRestaurant: (ratings: RatingsByRestaurant) => number,
    ): OverallRating[] =>
      ratingsByRestaurant.map(ratings => {
        return {
          restaurantId: ratings.restaurantId,
          rating: calculateRatingForRestaurant(ratings),
        };
      });
  
    const getTopRestaurants = async (city: string): Promise<Restaurant[]> => {
      const { findRatingsByRestaurant, calculateRatingForRestaurant } =
        dependencies;
  
      const ratingsByRestaurant = await findRatingsByRestaurant(city);
  
      const overallRatings = calculateRatings(
        ratingsByRestaurant,
        calculateRatingForRestaurant,
      );
  
      const toRestaurant = (r: OverallRating) => ({
        id: r.restaurantId,
      });
  
      return sortByOverallRating(overallRatings).map(r => {
        return toRestaurant(r);
      });
    };
  
    const sortByOverallRating = (overallRatings: OverallRating[]) =>
      overallRatings.sort((a, b) => b.rating - a.rating);
  
    return getTopRestaurants;
  };
  
  //SNIP ..
```


Having done so, I have

1. filled out the Dependencies type I modeled in my unit test
2. introduced the `OverallRating` type to capture the domain concept.          This could be a
            tuple of restaurant id and a number, but as I said earlier, types are cheap and I believe
            the additional clarity easily justifies the minimal cost.
3. extracted a couple of types from the test that are now direct dependencies of my `topRated` module
4. completed the simple logic of the primary function returned by the factory.


The dependencies between the main production code functions look like
        this


When including the stubs provided by the test, it looks ike this


With this implementation complete (for now), I have a passing test for my
        main domain function and one for my controller. They are entirely decoupled.
        So much so, in fact, that I feel the need to prove to myself that they will
        work together. It's time to start composing the units and building toward a
      larger whole.


## Beginning to wire it up


At this point, I have a decision to make. If I'm building something
        relatively straight-forward, I might choose to dispense with a test-driven
        approach when integrating the modules, but in this case, I'm going to continue
        down the TDD path for two reasons:

- I want to focus on the design of the integrations between modules, and writing a test is a
          good tool for doing so.
- There are still several modules to be implemented before I can
          use my original acceptance test as validation. If I wait to integrate
          them until then, I might have a lot to untangle if some of my underlying
          assumptions are flawed.


If my first acceptance test is a boulder and my unit tests are pebbles,
      then this first integration test would be a fist-sized rock: a chunky test
      exercising the call path from the controller into the first layer of
      domain functions, providing test doubles for anything beyond that layer. At least that is how
      it will start. I might continue integrating subsequent layers of the
      architecture as I go. I also might decide to throw the test away if
      it loses its utility or is getting in my way.


After initial implementation, the test will validate little more than that
      I've wired the routes correctly, but will soon cover calls into
      the domain layer and validate that the responses are encoded as
      expected.


test/restaurantRatings/controller.integration.spec.tsâ¦


```
  describe("the controller top rated handler", () => {
  
    it("delegates to the domain top rated logic", async () => {
      const returnedRestaurants = [
        { id: "r1", name: "restaurant1" },
        { id: "r2", name: "restaurant2" },
      ];
  
      const topRated = () => Promise.resolve(returnedRestaurants);
  
      const app = express();
      ratingsSubdomain.init(
        app,
        productionFactories.replaceFactoriesForTest({
          topRatedCreate: () => topRated,
        }),
      );
  
      const response = await request(app).get(
        "/vancouverbc/restaurants/recommended",
      );
      expect(response.status).toEqual(200);
      expect(response.get("content-type")).toBeDefined();
      expect(response.get("content-type").toLowerCase()).toContain("json");
      const payload = response.body as RatedRestaurants;
      expect(payload.restaurants).toBeDefined();
      expect(payload.restaurants.length).toEqual(2);
      expect(payload.restaurants[0].id).toEqual("r1");
      expect(payload.restaurants[1].id).toEqual("r2");
    });
  });
  
  interface RatedRestaurants {
    restaurants: { id: string; name: string }[];
  }
```


These tests can get a little ugly since they rely heavily on the web framework. Which
        leads to a second decision I've made. I could use a framework like Jest or Sinon.js and
        use module stubbing or spies that give me hooks into unreachable dependencies like 
        the `topRated` module. I don't particularly want to expose those in my API, 
        so using testing framework trickery might be justified. But in this case, I've decided to 
        provide a more conventional entry point: the optional collection of factory
        functions to override in my `init()` function. This provides me with the 
        entry point I need during the development process. As I progress, I might decide I don't 
        need that hook anymore in which case, I'll get rid of it.


Next, I write the code that assembles my modules.


src/restaurantRatings/index.tsâ¦


```
  
  export const init = (
    express: Express,
    factories: Factories = productionFactories,
  ) => {
    // TODO: Wire in a stub that matches the dependencies signature for now.
    //  Replace this once we build our additional dependencies.
    const topRatedDependencies = {
      findRatingsByRestaurant: () => {
        throw "NYI";
      },
      calculateRatingForRestaurant: () => {
        throw "NYI";
      },
    };
    const getTopRestaurants = factories.topRatedCreate(topRatedDependencies);
    const handler = factories.handlerCreate({
      getTopRestaurants, // TODO: <-- This line does not compile right now. Why?
    });
    express.get("/:city/restaurants/recommended", handler);
  };
  
  interface Factories {
    topRatedCreate: typeof topRated.create;
    handlerCreate: typeof createTopRatedHandler;
    replaceFactoriesForTest: (replacements: Partial<Factories>) => Factories;
  }
  
  export const productionFactories: Factories = {
    handlerCreate: createTopRatedHandler,
    topRatedCreate: topRated.create,
    replaceFactoriesForTest: (replacements: Partial<Factories>): Factories => {
      return { ...productionFactories, ...replacements };
    },
  };
```


Sometimes I have a dependency for a module defined but nothing to fulfill
        that contract yet. That is totally fine. I can just define an implementation inline that
        throws an exception as in the `topRatedHandlerDependencies` object above.
        Acceptance tests will fail but, at this stage, that is as I would expect.


## Finding and fixing a problem


The careful observer will notice that there is a compile error at the point the `
        topRatedHandler` is constructed because I have a conflict between two definitions:

- the representation of the restaurant as understood by
        `controller.ts`
- the restaurant as defined in `topRated.ts` and returned
        by `getTopRestaurants`.


The reason is simple: I have yet to add a `name` field to the `
        Restaurant` type in `topRated.ts`. There is a
        trade-off here. If I had a single type representing a restaurant, rather than one in each module,
        I would only have to add `name` once, and
        both modules would compile without additional changes. Nonetheless,
        I choose to keep the types separate, even though it creates 
        extra template code. By maintaining two distinct types, one for each
        layer of my application, I'm much less likely to couple those layers
        unnecessarily. No, this is not very [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), but I
        am often willing to risk some repetition to keep the module contracts as
        independent as possible.


src/restaurantRatings/topRated.tsâ¦


```
  
    interface Restaurant {
      id: string;
      name: string,
    }
  
    const toRestaurant = (r: OverallRating) => ({
      id: r.restaurantId,
      // TODO: I put in a dummy value to
      //  start and make sure our contract is being met
      //  then we'll add more to the testing
      name: "",
    });
```


My extremely naive solution gets the code compiling again, allowing me to continue on my
        current work on the module. I'll shortly add validation to my tests that ensure that the
        `name` field is mapped as it should be. Now with the test passing, I move on to the
        next step, which is to provide a more permanent solution to the restaurant mapping.


## Reaching out to the repository layer


Now, with the structure of my `getTopRestaurants` function more or
        less in place and in need of a way to get the restaurant name, I will fill out the
        `toRestaurant` function to load the rest of the `Restaurant` data.
        In the past, before adopting this highly function-driven style of development, I probably would
        have built a repository object interface or stub with a method meant to load the `
        Restaurant` object. Now my inclination is to build the minimum the I need: a
        function definition for loading the object without making any assumptions about the
        implementation. That can come later when I'm binding to that function.


test/restaurantRatings/topRated.spec.tsâ¦


```
  
      const restaurantsById = new Map<string, any>([
        ["restaurant1", { restaurantId: "restaurant1", name: "Restaurant 1" }],
        ["restaurant2", { restaurantId: "restaurant2", name: "Restaurant 2" }],
      ]);
  
      const getRestaurantByIdStub = (id: string) => {    â
        return restaurantsById.get(id);
      };
  
      //SNIP...
```


```

    const dependencies = {
      getRestaurantById: getRestaurantByIdStub,     â
      findRatingsByRestaurant: findRatingsByRestaurantStub,
      calculateRatingForRestaurant: calculateRatingForRestaurantStub,
    };

    const getTopRated = topRated.create(dependencies);
    const topRestaurants = await getTopRated("vancouverbc");
    expect(topRestaurants.length).toEqual(2);
    expect(topRestaurants[0].id).toEqual("restaurant1");
    expect(topRestaurants[0].name).toEqual("Restaurant 1");    â
    expect(topRestaurants[1].id).toEqual("restaurant2");
    expect(topRestaurants[1].name).toEqual("Restaurant 2");
```


In my domain-level test, I have introduced:

1. a stubbed finder for the `Restaurant`
2. an entry in my dependencies for that finder
3. validation that the name matches what was loaded from the `Restaurant` object.


As with previous functions that load data, the
      `getRestaurantById` returns a value wrapped in
      `Promise`. Although I continue to play the little game,
      pretending that I don't know how I will implement the
      function, I know the `Restaurant` is coming from an external
      data source, so I will want to load it asynchronously. That makes the
      mapping code more involved.


src/restaurantRatings/topRated.tsâ¦


```
  const getTopRestaurants = async (city: string): Promise<Restaurant[]> => {
    const {
      findRatingsByRestaurant,
      calculateRatingForRestaurant,
      getRestaurantById,
    } = dependencies;

    const toRestaurant = async (r: OverallRating) => {    â
      const restaurant = await getRestaurantById(r.restaurantId);
      return {
        id: r.restaurantId,
        name: restaurant.name,
      };
    };

    const ratingsByRestaurant = await findRatingsByRestaurant(city);

    const overallRatings = calculateRatings(
      ratingsByRestaurant,
      calculateRatingForRestaurant,
    );

    return Promise.all(     â
      sortByOverallRating(overallRatings).map(r => {
        return toRestaurant(r);
      }),
    );
  };
```

1. The complexity comes from the fact that `toRestaurant` is asynchronous
2. I can easily handled it in the calling code with `Promise.all()`.


I don't want each of these requests to block,
      or my IO-bound loads will run serially, delaying the entire user request, but I need to
      block until all the lookups are complete. Luckily, the Promise library
      provides `Promise.all` to collapse a collection of Promises
      into a single Promise containing a collection.


With this change, the requests to look up the restaurant go out in parallel. This is fine for
        a top 10 list since the number of concurrent requests is small. In an application of any scale, 
        I would probably restructure my service calls to load the `name` field via a database 
        join and eliminate the extra call. If that option was not available, for example, 
        I was querying an external API, I might wish to batch them by hand or use an async
        pool as provided by a third-party library like [Tiny Async Pool](https://www.npmjs.com/package/tiny-async-pool)
        to manage the concurrency.


Again, I update by assembly module with a dummy implementation so it
        all compiles, then start on the code that fulfills my remaining
        contracts.


src/restaurantRatings/index.tsâ¦


```
  
  export const init = (
    express: Express,
    factories: Factories = productionFactories,
  ) => {
  
    const topRatedDependencies = {
      findRatingsByRestaurant: () => {
        throw "NYI";
      },
      calculateRatingForRestaurant: () => {
        throw "NYI";
      },
      getRestaurantById: () => {
        throw "NYI";
      },
    };
    const getTopRestaurants = factories.topRatedCreate(topRatedDependencies);
    const handler = factories.handlerCreate({
      getTopRestaurants,
    });
    express.get("/:city/restaurants/recommended", handler);
  };
```


## The last mile: implementing domain layer dependencies


With my controller and main domain module workflow in place, it's time to implement the
        dependencies, namely the database access layer and the weighted rating
      algorithm.


This leads to the following set of high-level functions and dependencies


For testing, I have the following arrangement of stubs


For testing, all the elements are created by the test code, but I
      haven't shown that in the diagram due to clutter.


The
      process for implementing these modules is follows the same pattern:

- implement a test to drive out the basic design and a `Dependencies` type if
        one is necessary
- build the basic logical flow of the module, making the test pass
- implement the module dependencies
- repeat.


I won't walk through the entire process again since I've already demonstrate the process. 
        The code for the modules working end-to-end is available [in the
      repo](https://github.com/danielsomerfield/function-first-composition-example-typescript/). Some aspects of the final implementation require additional commentary.


By now, you might expect my ratings algorithm to be made available via yet another factory implemented as a
      partially applied function. This time I chose to write a pure function instead.


src/restaurantRatings/ratingsAlgorithm.tsâ¦


```
  interface RestaurantRating {
    rating: Rating;
    ratedByUser: User;
  }
  
  interface User {
    id: string;
    isTrusted: boolean;
  }
  
  interface RatingsByRestaurant {
    restaurantId: string;
    ratings: RestaurantRating[];
  }
  
  export const calculateRatingForRestaurant = (
    ratings: RatingsByRestaurant,
  ): number => {
    const trustedMultiplier = (curr: RestaurantRating) =>
      curr.ratedByUser.isTrusted ? 4 : 1;
    return ratings.ratings.reduce((prev, curr) => {
      return prev + rating[curr.rating] * trustedMultiplier(curr);
    }, 0);
  };
```


I made this choice to signal that this should always be
      a simple, stateless calculation. Had I wanted to leave an easy pathway
      toward a more complex implementation, say something backed by data science
      model parameterized per user, I would have used the factory pattern again.
      Often there isn't a right or wrong answer. The design choice provides a
      trail, so to speak, indicating how I anticipate the software might evolve.
      I create more rigid code in areas that I don't think should
      change while leaving more flexibility in the areas I have less confidence
      in the direction.


Another example where I âleave a trailâ is the decision to define
      another `RestaurantRating` type in
      `ratingsAlgorithm.ts`. The type is exactly the same as
      `RestaurantRating` defined in `topRated.ts`. I
      could take another path here:

- export `RestaurantRating` from `topRated.ts`
          and reference it directly in `ratingsAlgorithm.ts` or
- factor `RestaurantRating` out into a common module.
          You will often see shared definitions in a module called
          `types.ts`, although I prefer a more contextual name like
          `domain.ts` which gives some hints about the kind of types
          contained therein.


In this case, I am not confident that these types are literally the
      same. They might be different projections of the same domain entity with
      different fields, and I don't want to share them across the
      module boundaries risking deeper coupling. As unintuitive as this may
      seem, I believe it is the right choice: collapsing the entities is
      very cheap and easy at this point. If they begin to diverge, I probably
      shouldn't merge them anyway, but pulling them apart once they are bound
      can be very tricky.


## If it looks like a duck


I promised to explain why I often choose not to export types.
      I want to make a type available to another module only if
      I am confident that doing so won't create incidental coupling, restricting
      the ability of the code to evolve. Luckily, Typescript's structural or âduckâ typing makes it very
      easy to keep modules decoupled while at the same time guaranteeing that
      contracts are intact at compile time, even if the types are not shared.
      As long as the types are compatible in both the caller and callee, the
      code will compile.


A more rigid language like Java or C# forces you into making some
      decisions earlier in the process. For example, when implementing
      the ratings algorithm, I would be forced to take a different approach:

- I could extract the `RestaurantRating` type to make it
          available to both the module containing the algorithm and the one
          containing the overall top-rated workflow. The downside is that other
          functions could bind to it, increasing module coupling.
- Alternatively, I could create two different
          `RestaurantRating` types, then provide an adapter function
          for translating between these two identical types. This would be okay,
          but it would increase the amount of template code just to tell
          the compiler what you wish it already knew.
- I could collapse the algorithm into the
          `topRated` module completely, but that would give it more
          responsibilities than I would like.


The rigidity of the language can mean more costly tradeoffs with an
      approach like this. In his 2004 article on dependency
      injection and service locator patterns, Martin Fowler talks about using a
      [role interface](https://martinfowler.com/articles/injection.html#UsingASegregatedInterfaceForTheLocator) to reduce coupling
      of dependencies in Java despite the lack of structural types or first
      order functions. I would definitely consider this approach if I were
      working in Java.


I intend to port this project to several other strongly-typed languages to see how
      well the pattern applies in other contexts. Having ported it so far to 
      [Kotlin](https://github.com/danielsomerfield/function-first-composition-example-kotlin) and [Go](https://github.com/danielsomerfield/function-first-composition-example-go),
      there are signs that the pattern applies, but not without requiring some adjustments. I also believe
      that I might have to port it more than once to each language to get a better sense
      of what adjustments produce the best results. More explanation on the choices I made
      and my sense of the results are documented in the respective repositories.


## In summary


By choosing to fulfill dependency contracts with functions rather than
      classes, minimizing the code sharing between modules and driving the
      design through tests, I can create a system composed of highly discrete,
      evolvable, but still type-safe modules. If you have similar priorities in
      your next project, consider adopting some aspects of the approach I have
      outlined. Be aware, however, that choosing a foundational approach for
      your project is rarely as simple as selecting the âbest practiceâ requires
      taking into account other factors, such as the idioms of your tech stack and the
      skills of your team. There are many ways to
      put a system together, each with a complex set of tradeoffs. That makes software architecture 
      often difficult and always engaging. I wouldn't have it any other way.


---
