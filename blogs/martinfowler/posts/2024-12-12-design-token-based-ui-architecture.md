---
title: "Design Token-Based UI Architecture"
description: "Design tokens are design decisions as data and serve as a single source of truth for design and engineering.     Utilizing deployment pipelines, they enable automated code generation across platforms,"
date: 2024-12-12T00:00:00
tags: ["front-end"]
url: https://martinfowler.com/articles/design-token-based-ui-architecture.html
slug: design-token-based-ui-architecture
word_count: 3443
---


Design tokens, or “tokens” are fundamental design decisions represented
    as data. They are the foundational building blocks of design systems.


Since the release of the [second editor’s
    draft](https://second-editors-draft.tr.designtokens.org/format/) of the
    design token specification in 2022 and the [call for tool
    makers](https://www.w3.org/community/design-tokens/2022/06/14/call-to-implement-the-second-editors-draft-and-share-feedback/)
    to start implementing and providing feedback, the landscape of design token
    tools has evolved rapidly. Tools like code generators, documentation
    systems, and UI design software are now better equipped to support design
    tokens, underscoring their growing importance in modern UI architecture.


In this article, I'll explain what design tokens are, when they are useful and how to apply
    them effectively. We'll focus on key architectural decisions that are often difficult to change later, including:

1. How to organize design tokens in layers to balance scalability, maintainability and developer experience.
2. Whether all tokens should be made available to product teams or just a subset.
3. How to automate the distribution process of tokens across teams.


## Role of design tokens


Around 2017, I was involved in a large project that used the [Micro
      Frontend
      Architecture](https://martinfowler.com/articles/micro-frontends.html) to
      scale development teams. In this setup, different teams were responsible
      for different parts of the user interface, which could be even on the same
      page. Each team could deploy its micro-frontend independently.


There were various cases where components would be displayed on top of
      each other (such as dialogs or toasts appearing on top of content areas),
      which were not part of the same micro frontend. Teams used the CSS
      property `z-index` to control the stacking order, often relying on magic
      numbers—arbitrary values that weren’t documented or standardized. This approach
      did not scale as the project grew. It led to issues that took effort to
      fix, as cross-team collaboration was needed.


The issue was eventually addressed with design tokens and I think makes
      a good example to introduce the concept. The respective token file might
      have looked similar to this:


```
{
  "z-index": {
    "$type": "number",
    "default": {
      "$value": 1
    },
    "sticky": {
      "$value": 100
    },
    "navigation": {
      "$value": 200
    },
    "spinner": {
      "$value": 300
    },
    "toast": {
      "$value": 400
    },
    "modal": {
      "$value": 500
    }
  }
}

```


The design tokens above represent the set of `z-index` values that can
      be used in the application and the name gives developers a good idea of
      where to use them. A token file like this can be integrated into the
      designers’ workflow and also be used to generate code, in a format that
      each team requires. For example, in this case, the token file might have
      been used to generate CSS or SCSS variables:


css


```
  :root {
    --z-index-default: 1;
    --z-index-sticky: 100;
    --z-index-navigation: 200;
    --z-index-spinner: 300;
    --z-index-toast: 400;
    --z-index-modal: 500;
  }
```


scss


```
  
  $z-index-default: 1;
  $z-index-sticky: 100;
  $z-index-navigation: 200;
  $z-index-spinner: 300;
  $z-index-toast: 400;
  $z-index-modal: 500;
```


### What are design tokens?


Salesforce [originally introduced design tokens](https://www.smashingmagazine.com/2019/11/smashing-podcast-episode-3/) to streamline design
      updates to multiple
      platforms.


The Design Tokens Community Group [describes design tokens](https://second-editors-draft.tr.designtokens.org/format/#introduction) as “a
      methodology for expressing design decisions in a platform-agnostic way so
      that they can be shared across different **disciplines**, **tools**, and
      **technologies**


Let’s break this down:

- **Cross-Disciplinary Collaboration:** Design tokens act as a common language
        that aligns designers, developers, product managers, and other disciplines. By
        offering a single source of truth for design decisions, they ensure that
        everyone involved in the product life cycle is on the same page, leading to more
        efficient workflows.
- **Tool integration:** Design tokens can be integrated into various design
        and development tools, including UI design software, token editors, translation
        tools (code generators), and documentation systems. This enables design updates
        to be quickly reflected in the code base and are synchronized across teams.
- **Technology adaptability:** Design tokens can be translated into different
        technologies like CSS, SASS, and JavaScript for the web, and even used on native
        platforms like Android and iOS. This flexibility enables design consistency
        across a variety of platforms and devices.


## Establishing a single source of truth


A key benefit of design tokens is their ability to serve as a single
      source of truth for both design and engineering teams. This ensures that
      multiple products or services maintain visual and functional
      consistency.


A [translation
      tool](https://tr.designtokens.org/format/#translation-tool) takes one or
      more design token files as input and generates platform-specific code as
      output. Some translation tools can also produce documentation for the
      design tokens in the form of HTML. At the time of writing, popular
      translation tools include ﻿[Style
      Dictionary](https://styledictionary.com/),
      ﻿[Theo](https://github.com/salesforce-ux/theo), ﻿[Diez](https://diez.org/)
      or ﻿[Specify App](https://specifyapp.com/).


![](design-token-based-ui-architecture/translation-tool.svg)


Figure 1: Translation tool


## Automated design token distribution


In this section, we’ll explore how to automate the distribution of
      design tokens to product teams.


Let’s assume our goal is to provide teams with updated, tech-specific
      design tokens immediately after a designer makes a change. To achieve
      this, we can automate the translation and distribution process using a
      deployment pipeline for design tokens. Besides platform-specific code
      artifacts (like CSS for the web, XML for Android etc.), the pipeline might
      also deploy the documentation for the design tokens.


One crucial requirement is keeping design tokens under version control.
      Thankfully, plugins for popular design tools like Figma already integrate
      with Git providers like GitHub. It's considered best practice to use the
      Git repository as the single source of truth for design tokens—not the
      design tool itself. However, this requires the plugin to support syncing
      both ways between the repository and the design tool, which not all
      plugins do. As of now, Tokens Studio is a plugin that offers this
      bidirectional syncing. For detailed guidance on integrating Tokens Studio
      with different Git providers, please refer to their
      [documentation](https://docs.tokens.studio/token-storage-and-sync/sync-provider-overview).
      The tool enables you to configure a target branch and supports a
      trunk-based as well as a pull-request-based workflow.


Once the tokens are under version control, we can set up a deployment
      pipeline to build and deploy the artifacts needed by the product teams,
      which include platform-specific source code and documentation. The source
      code is typically packaged as a library and distributed via an artifact
      registry. This approach gives product teams control over the upgrade
      cycle. They can adopt updated styles by simply updating their
      dependencies. These updates may also be applied indirectly through updates of component
      libraries that use the token-based styles.


![](design-token-based-ui-architecture/token-distribution.svg)


Figure 2: Automated design token distribution


This overall setup has allowed teams at Thoughtworks to roll out
      smaller design changes across multiple front-ends and teams in a single
      day.


### Fully automated pipeline


The most straightforward way to design the pipeline would be a
          fully automated trunk-based workflow. In this setup, all changes
          pushed to the main branch will be immediately deployed as long as they
          pass the automated quality gates.


Such a pipeline might consist of the following jobs:

1. **Check:** Validate the design token files using a design token validator
            or a JSON validator.
2. **Build:** Use a translation tool like [Style
            Dictionary](https://styledictionary.com/) to convert design token files into
            platform-specific formats. This job might also build the docs using the
            translation tool or by integrating a dedicated documentation tool.
3. **Test:** This job is highly dependent on the testing strategy. Although
            some tests can be done using the design token file directly (like checking the
            color contrast), a common approach is to test the generated code using a
            documentation tool such as Storybook. Storybook has excellent [test
            support](https://storybook.js.org/docs/writing-tests) for visual regression
            tests, accessibility tests, interaction tests, and other test types.
4. **Publish:** Publish updated tokens to a package manager (for example,
            npm). The release process and versioning can be fully automated with a package
            publishing tool that is based on [Conventional
            Commits](https://www.conventionalcommits.org/) like
            [semantic-release](https://github.com/semantic-release/semantic-release).
            semantic-release also allows the deployment of packages to multiple platforms.
            The publish job might also deploy documentation for the design tokens.
5. **Notify:** Inform teams of the new token version via email or chat, so
            that they can update their dependencies.


![](design-token-based-ui-architecture/pipeline-fully-automated.svg)


Figure 3: Fully automated deployment pipeline


### Pipeline including manual approval


Sometimes fully automated quality gates are not sufficient. If a
          manual review is required before publishing, a common approach is to
          deploy an updated version of the documentation with the latest design
          token to a preview environment (a temporary environment).


If a tool like Storybook is used, this preview might contain not
          only the design tokens but also show them integrated with the
          components used in the application.


An approval process can be implemented via a pull-request workflow.
          Or, it can be a manual approval / deployment step in the pipeline.


![](design-token-based-ui-architecture/pipeline-incl-review.svg)


Figure 4: Deployment pipeline with manual approval


## Organizing tokens in layers


As discussed earlier, design tokens represent design decisions as data.
      However, not all decisions operate at the same level of detail. Instead,
      ideally, general design decisions guide more specific ones. Organizing
      tokens (or design decisions) into layers allows designers to make
      decisions at the right level of abstraction, supporting consistency and
      scalability.


For instance, making individual color choices for every new component isn’t practical.
      Instead, it’s more efficient to define a foundational color palette and then
      decide how and where those colors are applied. This approach reduces the
      number of decisions while maintaining a consistent look and feel.


There are three key types of design decisions for which design tokens
      are used. They build on top of one another:

- **What** design options are available to use?
- **How** are those styles applied across the user interface?
- **Where** exactly are those styles applied (in which components)?


There are various names for these three types of tokens (as usual,
      naming is the hard part). In this article, we’ll use the terms [proposed
      by Samantha
      Gordashko](https://samiamdesigns.substack.com/p/a-new-approach-to-naming-design-tokens):
      option tokens, decision tokens and component tokens.


Let’s use our color example to illustrate how design tokens can
      answer the three questions above.


### Option tokens: defining what design options are provided


*Option tokens* (also called *primitive tokens*, *base tokens*, *core
      tokens*, *foundation tokens* or *reference tokens*) define **what**
      styles can be used in the application. They define things like color
      palettes, spacing/sizing scales or font families. Not all of them are
      necessarily used in the application, but they present reasonable
      options.


Using our example, let’s assume we have a color palette with 9 shades for each color,
      ranging from very light to highly saturated. Below, we define the blue tones and grey tones as option-tokens:


```
{
  "color": {
    "$type": "color",
    "options": {
      "blue-100": {"$value": "#e0f2ff"},
      "blue-200": {"$value": "#cae8ff"},
      "blue-300": {"$value": "#b5deff"},
      "blue-400": {"$value": "#96cefd"},
      "blue-500": {"$value": "#78bbfa"},
      "blue-600": {"$value": "#59a7f6"},
      "blue-700": {"$value": "#3892f3"},
      "blue-800": {"$value": "#147af3"},
      "blue-900": {"$value": "#0265dc"},
      "grey-100": {"$value": "#f8f8f8"},
      "grey-200": {"$value": "#e6e6e6"},
      "grey-300": {"$value": "#d5d5d5"},
      "grey-400": {"$value": "#b1b1b1"},
      "grey-500": {"$value": "#909090"},
      "grey-600": {"$value": "#6d6d6d"},
      "grey-700": {"$value": "#464646"},
      "grey-800": {"$value": "#222222"},
      "grey-900": {"$value": "#000000"},
      "white": {"$value": "#ffffff"}
    }
  }
}
```


Although it’s highly useful to have reasonable options, option tokens fall short
      of being sufficient for guiding developers on how and where to apply them.


### Decision tokens: defining how styles are applied


*Decision tokens* (also called *semantic tokens* or *system tokens*)
      specify **how** those style options should be applied contextually across
      the UI.


In the context of our color example, they might include decisions like the following:

- grey-100 is used as a surface color.
- grey-200 is used for the background of disabled elements.
- grey-400 is used for the text of disabled elements.
- grey-900 is used as a default color for text.
- blue-900 is used as an accent color.
- white is used for text on accent color backgrounds.


The corresponding decision token file would look like this:


```
{
  "color": {
    "$type": "color",
    "decisions": {
      "surface": {
        "$value": "{color.options.grey-100}",
        "description": "Used as a surface color."
      },
      "background-disabled": {
        "$value": "{color.options.grey-200}",
        "description":"Used for the background of disabled elements."
      },
      "text-disabled": {
        "$value": "{color.options.grey-400}",
        "description": "Used for the text of disabled elements."
      },
      "text": {
        "$value": "{color.options.grey-900}",
        "description": "Used as default text color."
      },
      "accent": {
        "$value": "{color.options.blue-900}",
        "description": "Used as an accent color."
      },
      "text-on-accent": {
        "$value": "{color.options.white}",
        "description": "Used for text on accent color backgrounds."
      }
    }
  }
}
```


As a developer, I would mostly be interested in the decisions, not the
      options. For example, color tokens typically contain a long list of options (a
      color palette), while very few of those options are actually used in
      the application. The tokens that are actually relevant when deciding which
      styles to apply, would be usually the decision tokens.


Decision tokens use
      [references](https://tr.designtokens.org/format/#alias-reference) to the
      option tokens. I think of organizing tokens this way as a layered
      architecture. In other articles, I have often seen the term *tier* being
      used, but I think *layer* is the better word, as there is no physical
      separation implied. The diagram below visualizes the two layers we talked
      about so far:


![](design-token-based-ui-architecture/2-layer.svg)


Figure 5: 2-layer pattern


### Component tokens: defining where styles are applied


*Component tokens* (or *component-specific tokens*) map the *decision
      tokens* to specific parts of the UI. They show **where** styles are
      applied.


The term *component* in the context of design tokens does not always
      map to the technical term component. For example, a button might be
      implemented as a UI component in some applications, while other
      applications just use the `button` HTML element instead. *Component
      tokens* could be used in both cases.


Component tokens can be organised in a [*group*](https://tr.designtokens.org/format/#group) referencing multiple decision tokens. In our example, this references
      might include text- and background-colors for different variants of the button (primary, secondary) as well as disabled buttons.
      They might also include references to tokens of other types (spacing/sizing, borders etc.) which I'll omit in the
      following example:


```
{
  "button": {
    "primary": {
      "background": {
        "$value": "{color.decisions.accent}"
      },
      "text": {
        "$value": "{color.decisions.text-on-accent}"
      }
    },
    "secondary": {
      "background": {
        "$value": "{color.decisions.surface}"
      },
      "text": {
        "$value": "{color.decisions.text}"
      }
    },
    "background-disabled": {
      "$value": "{color.decisions.background-disabled}"
    },
    "text-disabled": {
      "$value": "{color.decisions.text-disabled}"
    }
  }
}
```


To some degree, component tokens are simply the result of applying
      decisions to specific components. However, as this
      example shows, this process isn’t always straightforward—especially for
      developers without design experience. While decision tokens can offer a
      general sense of which styles to use in a given context, component tokens
      provide additional clarity.


![](design-token-based-ui-architecture/3-layer.svg)


Figure 6: 3-layer pattern


**Note:** there may be âsnowflakeâ situations where layers are skipped.
      For example, it might not be possible to define a general decision for
      every single component token, or those decisions might not have been made
      yet (for example at the beginning of a project).


### How many layers shall I use?


Two or three layers are quite common amongst the bigger design
      systems.


However, even a single layer of design tokens already greatly limits
      the day-to-day decisions that need to be made. For example, just deciding
      what units to use for spacing and sizing became a somewhat nontrivial task
      with up to [43 units for length implemented in some
      browsers](https://developer.mozilla.org/en-US/docs/Web/CSS/length#browser_compatibility)
      (if I counted correctly).


A three-layer architecture should offer the best developer experience.
      However, it also increases maintenance effort and token count, as new
      tokens are introduced with each new component. This can result in a larger
      code base and heavier package size.


**Starting with two layers** (option and decision tokens) can be a good
      idea for projects where the major design decisions are already in place
      and/or relatively stable. A third layer can still be added if there is a
      clear need.


**An additional component layer** makes it easier for designers to
      change decisions later or let them evolve over time. This flexibility
      could be a driving force for a three-layer architecture. In some cases, it
      might even make sense to [start with component
      tokens](https://medium.com/@hereinthehive/component-tokens-first-hear-me-out-6258f54935a9)
      and to add the other layers later on.


Ultimately, the number of layers depends on your project's needs and
      how much flexibility and scalability are required.


## Token scope


I already mentioned that while option tokens are very helpful to
    designers, they might not be relevant for application developers using the
    platform-specific code artifacts. Application developers will typically be
    more interested in the decision/component tokens.


Although token scope is not yet included in the design token
    spec, some design
    systems already separate tokens into private (also called *internal*) and
    public (also called *global*) tokens. For example, the Salesforce Lightning
    Design System introduced [a flag for each
    token](https://www.lightningdesignsystem.com/design-tokens/). There are
    various reasons why this can be a good idea:

- it guides developers on which tokens to use
- fewer options provide a better developer experience
- it reduces the file size as not all tokens need to be included
- private/internal tokens can be changed or removed without breaking
      changes


A downside of making option tokens private is that developers would rely
    on designers to always make those styles available as decision or component
    tokens. This could become an issue in case of limited availability of the
    designers or if not all decisions are available, for example at the start of
    a project.


Unfortunately, there is no standardized solution yet for implementing
    scope for design tokens. So the approach depends on the tool-chain of the
    project and will most likely need some custom code.


### File-based scope


Using Style Dictionary, we can use a
      [*filter*](https://styledictionary.com/reference/hooks/filters/) to
      expose only public tokens. The most straightforward approach would be to
      filter on the file ending. If we use different file endings for component,
      decision and option tokens, we can use a filter on the file path, for
      example, to make the option tokens layer private.


Style Dictionary config


```
  const styleDictionary = new StyleDictionary({
    "source": ["color.options.json", "color.decisions.json"],
    "platforms": {
      "css": {
        "transformGroup": "css",
        "files": [
          {
            "destination": "variables.css",
            "filter": token => !token.filePath.endsWith('options.json'),
            "format": "css/variables"
          }
        ]
      }
    }
  });
```


The resulting CSS variables would contain
      only these decision tokens, and not the option tokens.


Generated CSS variables


```
  :root {
    --color-decisions-surface: #f8f8f8;
    --color-decisions-background-disabled: #e6e6e6;
    --color-decisions-text-disabled: #b1b1b1;
    --color-decisions-text: #000000;
    --color-decisions-accent: #0265dc;
    --color-decisions-text-on-accent: #ffffff;
  }
```


### A more flexible approach


If more flexibility is needed, it might be preferable to add a scope
      flag to each token and to filter based on this flag:


Style Dictionary config


```
  const styleDictionary = new StyleDictionary({
    "source": ["color.options.json", "color.decisions.json"],
    "platforms": {
      "css": {
        "transformGroup": "css",
        "files": [
          {
            "destination": "variables.css",
            "filter": {
              "public": true
            },
            "format": "css/variables"
          }
        ]
      }
    }
  });
```


If we then add the flag to the decision tokens, the resulting CSS would
      be the same as above:


Tokens with scope flag


```
  {
    "color": {
      "$type": "color",
      "decisions": {
        "surface": {
          "$value": "{color.options.grey-100}",
          "description": "Used as a surface color.",
          "public": true
        },
        "background-disabled": {
          "$value": "{color.options.grey-200}",
          "description":"Used for the background of disabled elements.",
          "public": true
        },
        "text-disabled": {
          "$value": "{color.options.grey-400}",
          "description": "Used for the text of disabled elements.",
          "public": true
        },
        "text": {
          "$value": "{color.options.grey-900}",
          "description": "Used as default text color.",
          "public": true
        },
        "accent": {
          "$value": "{color.options.blue-900}",
          "description": "Used as an accent color.",
          "public": true
        },
        "text-on-accent": {
          "$value": "{color.options.white}",
          "description": "Used for text on accent color backgrounds.",
          "public": true
        }
      }
    }
  }
```


Generated CSS variables


```
  :root {
    --color-decisions-surface: #f8f8f8;
    --color-decisions-background-disabled: #e6e6e6;
    --color-decisions-text-disabled: #b1b1b1;
    --color-decisions-text: #000000;
    --color-decisions-accent: #0265dc;
    --color-decisions-text-on-accent: #ffffff;
  }
```


Such flags can now also be set [through the Figma
      UI](https://help.figma.com/hc/en-us/articles/360039238193-Hide-styles-components-and-variables-when-publishing#h_01HD20M7HS9044NHB2YBJNE9C2)
      (if using Figma variables as a source of truth for design tokens). It is
      available as
      [`hiddenFromPublishing`](https://www.figma.com/plugin-docs/api/properties/Variable-hiddenfrompublishing/)
      flag via the Plugins API.


## Should I use design tokens?


Design tokens offer significant benefits for modern UI architecture,
      but they may not be the right fit for every project.


**Benefits** include:

- Improved lead time for design changes
- Consistent design language and UI architecture across platforms and
            technologies
- Design tokens being relatively lightweight from an implementation point of
            view


**Drawbacks** include:

- Initial effort for automation
- Designers might have to (to some degree) interact with Git
- Standardization is still in progress


Consider the following when deciding whether to adopt design
      tokens:


### When to use design tokens

1. **Multi-Platform or Multi-Application Environments:** When working across
          multiple platforms (web, iOS, Android…) or maintaining several applications or
          frontends, design tokens ensure a consistent design language across all of
          them.
2. **Frequent Design Changes**: For environments with regular design
          updates, design tokens provide a structured way to manage and propagate changes
          efficiently.
3. **Large Teams**: For teams with many designers and developers, design
          tokens facilitate collaboration.
4. **Automated Workflows**: If you’re familiar with CI/CD pipelines, the
          effort to add a design token pipeline is relatively low. There are also
          commercial offerings.


### When design tokens might not be necessary

1. **Small projects:** For smaller projects with limited scope and minimal
          design complexity, the overhead of managing design tokens might not be worth the
          effort.
2. **No issue with design changes:** If the speed of design changes,
          consistency and collaboration between design and engineering are not an issue,
          then you might also not need design tokens.


---
