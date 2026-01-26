---
title: "Headless Component: a pattern for composing React UIs"
description: "As React UI controls become more sophisticated, complex logic can get       intertwined with the visual representation. This makes it hard to reason       about the behavior of the component, hard to "
date: 2023-11-07T00:00:00
tags: ["front-end"]
url: https://martinfowler.com/articles/headless-component.html
slug: headless-component
word_count: 5948
---


React has revolutionized the way we think about UI components and state
      management in UI. But with every new feature request or enhancement, a
      seemingly simple component can quickly evolve into a complex amalgamation
      of intertwined state and UI logic.


Imagine building a simple dropdown list. Initially, it appears
      straightforward – you manage the open/close state and design its
      appearance. But, as your application grows and evolves, so do the
      requirements for this dropdown:

- **Accessibility Support**: Ensuring your dropdown is usable for
        everyone, including those using screen readers or other assistive
        technologies, adds another layer of complexity. You need to manage focus
        states, `aria` attributes, and ensure your dropdown is semantically
        correct.
- **Keyboard Navigation**: Users shouldn’t be limited to mouse
        interactions. They might want to navigate options using arrow keys, select
        using `Enter`, or close the dropdown using `Escape`. This requires
        additional event listeners and state management.
- **Async Data Considerations**: As your application scales, maybe the
        dropdown options aren't hardcoded anymore. They might be fetched from an
        API. This introduces the need to manage loading, error, and empty states
        within the dropdown.
- **UI Variations and Theming**: Different parts of your application
        might require different styles or themes for the dropdown. Managing these
        variations within the component can lead to an explosion of props and
        configurations.
- **Extending Features**: Over time, you might need additional
        features like multi-select, filtering options, or integration with other
        form controls. Adding these to an already complex component can be
        daunting.


Each of these considerations adds layers of complexity to our dropdown
      component. Mixing state, logic, and UI presentation makes it less
      maintainable and limits its reusability. The more intertwined they become,
      the harder it gets to make changes without unintentional side effects.


## Introducing the Headless Component Pattern


Facing these challenges head-on, the Headless Component pattern offers
      a way out. It emphasizes the separation of the calculation from the UI
      representation, giving developers the power to build versatile,
      maintainable, and reusable components.


A Headless Component is a design pattern in React where a component -
      normally inplemented as React hooks - is responsible solely for logic and
      state management without prescribing any specific UI (User Interface). It
      provides the “brains” of the operation but leaves the “looks” to the
      developer implementing it. In essence, it offers functionality without
      forcing a particular visual representation.


When visualized, the Headless Component appears as a slender layer
      interfacing with JSX views on one side, and communicating with underlying
      data models on the other when required. This pattern is particularly
      beneficial for individuals seeking solely the behavior or state management
      aspect of the UI, as it conveniently segregates these from the visual
      representation.


![](headless-component/headless-component.png)


Figure 1: The Headless Component pattern


For instance, consider a headless dropdown component. It would handle
      state management for open/close states, item selection, keyboard
      navigation, etc. When it's time to render, instead of rendering its own
      hardcoded dropdown UI, it provides this state and logic to a child
      function or component, letting the developer decide how it should visually
      appear.


In this article, we'll delve into a practical example by constructing a
      complex component—a dropdown list from the ground up. As we add more
      features to the component, we'll observe the challenges that arise.
      Through this, we'll demonstrate how the Headless Component pattern can
      address these challenges, compartmentalize distinct concerns, and aid us
      in crafting more versatile components.


## Implementing a Dropdown List


A dropdown list is a common component used in many places. Although
        there's a native select component for basic use cases, a more advanced
        version offering more control over each option provides a better user
        experience.


![](headless-component/dropdown-list.png)


Figure 2: Dropdown list component


Creating one from scratch, a complete implementation, requires more
        effort than it appears at first glance. It's essential to consider
        keyboard navigation, accessibility (for instance, screen reader
        compatibility), and usability on mobile devices, among others.


We'll begin with a simple, desktop version that only supports mouse
        clicks, and gradually build in more features to make it realistic. Note
        that the goal here is to reveal a few software design patterns rather
        than teach how to build a dropdown list for production use - actually, I
        don’t recommend doing this from scratch and would instead suggest using
        more mature libraries.


Basically, we need an element (let's call it a trigger) for the user
        to click, and a state to control the show and hide actions of a list
        panel. Initially, we hide the panel, and when the trigger is clicked, we
        show the list panel.


```
import { useState } from "react";

interface Item {
  icon: string;
  text: string;
  description: string;
}

type DropdownProps = {
  items: Item[];
};

const Dropdown = ({ items }: DropdownProps) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedItem, setSelectedItem] = useState<Item | null>(null);

  return (
    <div className="dropdown">
      <div className="trigger" tabIndex={0} onClick={() => setIsOpen(!isOpen)}>
        <span className="selection">
          {selectedItem ? selectedItem.text : "Select an item..."}
        </span>
      </div>
      {isOpen && (
        <div className="dropdown-menu">
          {items.map((item, index) => (
            <div
              key={index}
              onClick={() => setSelectedItem(item)}
              className="item-container"
            >
              <img src={item.icon} alt={item.text} />
              <div className="details">
                <div>{item.text}</div>
                <small>{item.description}</small>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

```


In the code above, we've set up the basic structure for our dropdown
        component. Using the `useState` hook, we manage the `isOpen` and
        `selectedItem` states to control the dropdown's behavior. A simple click
        on the trigger toggles the dropdown menu, while selecting an item
        updates the `selectedItem` state.


Let's break down the component into smaller, manageable pieces to see
        it more clearly. This decomposition isn't part of the Headless Component
        pattern, but breaking a complex UI component into pieces is a valuable
        activity.


We can start by extracting a `Trigger` component to handle user
        clicks:


```
const Trigger = ({
  label,
  onClick,
}: {
  label: string;
  onClick: () => void;
}) => {
  return (
    <div className="trigger" tabIndex={0} onClick={onClick}>
      <span className="selection">{label}</span>
    </div>
  );
};

```


The `Trigger` component is a basic clickable UI element, taking in a
        `label` to display and an `onClick` handler. It remains agnostic to its
        surrounding context. Similarly, we can extract a `DropdownMenu`
        component to render the list of items:


```
const DropdownMenu = ({
  items,
  onItemClick,
}: {
  items: Item[];
  onItemClick: (item: Item) => void;
}) => {
  return (
    <div className="dropdown-menu">
      {items.map((item, index) => (
        <div
          key={index}
          onClick={() => onItemClick(item)}
          className="item-container"
        >
          <img src={item.icon} alt={item.text} />
          <div className="details">
            <div>{item.text}</div>
            <small>{item.description}</small>
          </div>
        </div>
      ))}
    </div>
  );
};

```


The `DropdownMenu` component displays a list of items, each with an
        icon and a description. When an item is clicked, it triggers the
        provided `onItemClick` function with the selected item as its
        argument.


And then Within the `Dropdown` component, we incorporate `Trigger`
        and `DropdownMenu` and supply them with the necessary state. This
        approach ensures that the `Trigger` and `DropdownMenu` components remain
        state-agnostic and purely react to passed props.


```
const Dropdown = ({ items }: DropdownProps) => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedItem, setSelectedItem] = useState<Item | null>(null);

  return (
    <div className="dropdown">
      <Trigger
        label={selectedItem ? selectedItem.text : "Select an item..."}
        onClick={() => setIsOpen(!isOpen)}
      />
      {isOpen && <DropdownMenu items={items} onItemClick={setSelectedItem} />}
    </div>
  );
};

```


In this updated code structure, we've separated concerns by creating
        specialized components for different parts of the dropdown, making the
        code more organized and easier to manage.


![](headless-component/list-native.png)


Figure 3: List native implementation


As depicted in the image above, you can click the “Select an item...”
        trigger to open the dropdown. Selecting a value from the list updates
        the displayed value and subsequently closes the dropdown menu.


At this point, our refactored code is clear-cut, with each segment
        being straightforward and adaptable. Modifying or introducing a
        different `Trigger` component would be relatively straightforward.
        However, as we introduce more features and manage additional states,
        will our current components hold up?


Let's find out with a a crucial enhancement for a serious dopdown
        list: keyboard navigation.


## Implementing Keyboard Navigation


Incorporating keyboard navigation within our dropdown list enhances
        the user experience by providing an alternative to mouse interactions.
        This is particularly important for accessibility and offers a seamless
        navigation experience on the web page. Let's explore how we can achieve
        this using the `onKeyDown` event handler.


Initially, we'll attach a `handleKeyDown` function to the `onKeyDown`
        event in our `Dropdown` component. Here, we utilize a switch statement
        to determine the specific key pressed and perform actions accordingly.
        For instance, when the “Enter” or “Space” key is pressed, the dropdown
        is toggled. Similarly, the “ArrowDown” and “ArrowUp” keys allow
        navigation through the list items, cycling back to the start or end of
        the list when necessary.


```
const Dropdown = ({ items }: DropdownProps) => {
  // ... previous state variables ...
  const [selectedIndex, setSelectedIndex] = useState<number>(-1);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    switch (e.key) {
      // ... case blocks ...
      // ... handling Enter, Space, ArrowDown and ArrowUp ...
    }
  };

  return (
    <div className="dropdown" onKeyDown={handleKeyDown}>
      {/* ... rest of the JSX ... */}
    </div>
  );
};

```


Additionally, we have updated our `DropdownMenu` component to accept
        a `selectedIndex` prop. This prop is used to apply a highlighted CSS
        style and set the `aria-selected` attribute to the currently selected
        item, enhancing the visual feedback and accessibility.


```
const DropdownMenu = ({
  items,
  selectedIndex,
  onItemClick,
}: {
  items: Item[];
  selectedIndex: number;
  onItemClick: (item: Item) => void;
}) => {
  return (
    <div className="dropdown-menu" role="listbox">
      {/* ... rest of the JSX ... */}
    </div>
  );
};

```


Now, our `Dropdown` component is entangled with both state management code and rendering logic. It houses an extensive switch case along with all the state management constructs such as `selectedItem`, `selectedIndex`, `setSelectedItem`, and so forth.


## Implementing Headless Component with a Custom Hook


To address this, we'll introduce the concept of a Headless Component
        via a custom hook named `useDropdown`. This hook efficiently wraps up
        the state and keyboard event handling logic, returning an object filled
        with essential states and functions. By de-structuring this in our
        `Dropdown` component, we keep our code neat and sustainable.


The magic lies in the `useDropdown` hook, our protagonist—the
        Headless Component. This versatile unit houses everything a dropdown
        needs: whether it's open, the selected item, the highlighted item,
        reactions to the Enter key, and so forth. The beauty is its
        adaptability; you can pair it with various visual presentations—your JSX
        elements.


```
const useDropdown = (items: Item[]) => {
  // ... state variables ...

  // helper function can return some aria attribute for UI
  const getAriaAttributes = () => ({
    role: "combobox",
    "aria-expanded": isOpen,
    "aria-activedescendant": selectedItem ? selectedItem.text : undefined,
  });

  const handleKeyDown = (e: React.KeyboardEvent) => {
    // ... switch statement ...
  };
  
  const toggleDropdown = () => setIsOpen((isOpen) => !isOpen);

  return {
    isOpen,
    toggleDropdown,
    handleKeyDown,
    selectedItem,
    setSelectedItem,
    selectedIndex,
  };
};

```


Now, our `Dropdown` component is simplified, shorter and easier to
        understand. It leverages the `useDropdown` hook to manage its state and
        handle keyboard interactions, demonstrating a clear separation of
        concerns and making the code easier to understand and manage.


```
const Dropdown = ({ items }: DropdownProps) => {
  const {
    isOpen,
    selectedItem,
    selectedIndex,
    toggleDropdown,
    handleKeyDown,
    setSelectedItem,
  } = useDropdown(items);

  return (
    <div className="dropdown" onKeyDown={handleKeyDown}>
      <Trigger
        onClick={toggleDropdown}
        label={selectedItem ? selectedItem.text : "Select an item..."}
      />
      {isOpen && (
        <DropdownMenu
          items={items}
          onItemClick={setSelectedItem}
          selectedIndex={selectedIndex}
        />
      )}
    </div>
  );
};

```


Through these modifications, we have successfully implemented
        keyboard navigation in our dropdown list, making it more accessible and
        user-friendly. This example also illustrates how hooks can be utilized
        to manage complex state and logic in a structured and modular manner,
        paving the way for further enhancements and feature additions to our UI
        components.


The beauty of this design lies in its distinct separation of logic
        from presentation. By 'logic', we refer to the core functionalities of a
        `select` component: the open/close state, the selected item, the
        highlighted element, and the reactions to user inputs like pressing the
        ArrowDown when choosing from the list. This division ensures that our
        component retains its core behavior without being bound to a specific
        visual representation, justifying the term “Headless Component”.


## Testing the Headless Component


The logic of our component is centralized, enabling its reuse in
        diverse scenarios. It's crucial for this functionality to be reliable.
        Thus, comprehensive testing becomes imperative. The good news is,
        testing such behavior is straightforward.


We can evaluate state management by invoking a public method and
        observing the corresponding state change. For instance, we can examine
        the relationship between `toggleDropdown` and the `isOpen` state.


```
const items = [{ text: "Apple" }, { text: "Orange" }, { text: "Banana" }];

it("should handle dropdown open/close state", () => {
  const { result } = renderHook(() => useDropdown(items));

  expect(result.current.isOpen).toBe(false);

  act(() => {
    result.current.toggleDropdown();
  });

  expect(result.current.isOpen).toBe(true);

  act(() => {
    result.current.toggleDropdown();
  });

  expect(result.current.isOpen).toBe(false);
});

```


Keyboard navigation tests are slightly more intricate, primarily due
        to the absence of a visual interface. This necessitates a more
        integrated testing approach. One effective method is crafting a fake
        test component to authenticate the behavior. Such tests serve a dual
        purpose: they provide an instructional guide on utilizing the Headless
        Component and, since they employ JSX, offer a genuine insight into user
        interactions.


Consider the following test, which replaces the prior state check
        with an integration test:


```
it("trigger to toggle", async () => {
  render(<SimpleDropdown />);

  const trigger = screen.getByRole("button");

  expect(trigger).toBeInTheDocument();

  await userEvent.click(trigger);

  const list = screen.getByRole("listbox");
  expect(list).toBeInTheDocument();

  await userEvent.click(trigger);

  expect(list).not.toBeInTheDocument();
});

```


The `SimpleDropdown` below is a fake 1 component, 
        designed exclusively for testing. It also doubles as a
        hands-on example for users aiming to implement the Headless
        Component.


1: [Fake](https://martinfowler.com/bliki/TestDouble.html) is an object that encapsulates access to an external system or resource.
    It's useful when you don't want to scatter all the adoption logic into your codebase, and that
    can be easier to change in one place when the external system changes.


```
const SimpleDropdown = () => {
  const {
    isOpen,
    toggleDropdown,
    selectedIndex,
    selectedItem,
    updateSelectedItem,
    getAriaAttributes,
    dropdownRef,
  } = useDropdown(items);

  return (
    <div
      tabIndex={0}
      ref={dropdownRef}
      {...getAriaAttributes()}
    >
      <button onClick={toggleDropdown}>Select</button>
      <p data-testid="selected-item">{selectedItem?.text}</p>
      {isOpen && (
        <ul role="listbox">
          {items.map((item, index) => (
            <li
              key={index}
              role="option"
              aria-selected={index === selectedIndex}
              onClick={() => updateSelectedItem(item)}
            >
              {item.text}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

```


The `SimpleDropdown` is a dummy component crafted for testing. It
        uses the centralized logic of `useDropdown` to create a dropdown list.
        When the “Select” button is clicked, the list appears or disappears.
        This list contains a set of items (Apple, Orange, Banana), and users can
        select any item by clicking on it. The tests above ensure that this
        behavior works as intended.


With the `SimpleDropdown` component in place, we're equipped to test
        a more intricate yet realistic scenario.


```
it("select item using keyboard navigation", async () => {
  render(<SimpleDropdown />);

  const trigger = screen.getByRole("button");

  expect(trigger).toBeInTheDocument();

  await userEvent.click(trigger);

  const dropdown = screen.getByRole("combobox");
  dropdown.focus();

  await userEvent.type(dropdown, "{arrowdown}");
  await userEvent.type(dropdown, "{enter}");

  await expect(screen.getByTestId("selected-item")).toHaveTextContent(
    items[0].text
  );
});

```


The test ensures that users can select items from the dropdown using
        keyboard inputs. After rendering the `SimpleDropdown` and clicking on
        its trigger button, the dropdown is focused. Subsequently, the test
        simulates a keyboard arrow-down press to navigate to the first item and
        an enter press to select it. The test then verifies if the selected item
        displays the expected text.


While utilizing custom hooks for Headless Components is common, it's not the sole approach. 
        In fact, before the advent of hooks, developers employed render props or Higher-Order 
        Components to implement Headless Components. Nowadays, even though Higher-Order 
        Components have lost some of their previous popularity, a declarative API employing 
        React context continues to be fairly favoured.


## Declarative Headless Component with context API


I'll showcase an alternate declarative method to attain a similar outcome,
          employing the React context API in this instance. By establishing a hierarchy
          within the component tree and making each component replaceable, we can offer
          users a valuable interface that not only functions effectively (supporting
          keyboard navigation, accessibility, etc.), but also provides the flexibility
          to customize their own components.


```
import { HeadlessDropdown as Dropdown } from "./HeadlessDropdown";

const HeadlessDropdownUsage = ({ items }: { items: Item[] }) => {
  return (
    <Dropdown items={items}>
      <Dropdown.Trigger as={Trigger}>Select an option</Dropdown.Trigger>
      <Dropdown.List as={CustomList}>
        {items.map((item, index) => (
          <Dropdown.Option
            index={index}
            key={index}
            item={item}
            as={CustomListItem}
          />
        ))}
      </Dropdown.List>
    </Dropdown>
  );
};

```


The `HeadlessDropdownUsage` component takes an `items`
          prop of type array of `Item` and returns a `Dropdown`
          component. Inside `Dropdown`, it defines a `Dropdown.Trigger`
          to render a `CustomTrigger` component, a `Dropdown.List`
          to render a `CustomList` component, and maps through the
          `items` array to create a `Dropdown.Option` for each
          item, rendering a `CustomListItem` component.


This structure enables a flexible, declarative way of customizing the
          rendering and behavior of the dropdown menu while keeping a clear hierarchical
          relationship between the components. Please observe that the components
          `Dropdown.Trigger`, `Dropdown.List`, and
          `Dropdown.Option` supply unstyled default HTML elements (button, ul,
          and li respectively). They each accept an `as` prop, enabling users
          to customize components with their own styles and behaviors.


For example, we can define these customised component and use it as above.


```
const CustomTrigger = ({ onClick, ...props }) => (
  <button className="trigger" onClick={onClick} {...props} />
);

const CustomList = ({ ...props }) => (
  <div {...props} className="dropdown-menu" />
);

const CustomListItem = ({ ...props }) => (
  <div {...props} className="item-container" />
);

```


![](headless-component/declarative-ui.png)


Figure 4: Declarative User Interface with customised
          elements


The implementation isn't complicated. We can simply define a context in
          `Dropdown` (the root element) and put all the states need to be
          managed inside, and use that context in the children nodes so they can access
          the states (or change these states via APIs in the context).


```
type DropdownContextType<T> = {
  isOpen: boolean;
  toggleDropdown: () => void;
  selectedIndex: number;
  selectedItem: T | null;
  updateSelectedItem: (item: T) => void;
  getAriaAttributes: () => any;
  dropdownRef: RefObject<HTMLElement>;
};

function createDropdownContext<T>() {
  return createContext<DropdownContextType<T> | null>(null);
}

const DropdownContext = createDropdownContext();

export const useDropdownContext = () => {
  const context = useContext(DropdownContext);
  if (!context) {
    throw new Error("Components must be used within a <Dropdown/>");
  }
  return context;
};

```


The code defines a generic `DropdownContextType` type, and a
          `createDropdownContext` function to create a context with this type.
          `DropdownContext` is created using this function.
          `useDropdownContext` is a custom hook that accesses this context,
          throwing an error if it's used outside of a `<Dropdown/>`
          component, ensuring proper usage within the desired component hierarchy.


Then we can define components that use the context. We can start with the
          context provider:


```
const HeadlessDropdown = <T extends { text: string }>({
  children,
  items,
}: {
  children: React.ReactNode;
  items: T[];
}) => {
  const {
    //... all the states and state setters from the hook
  } = useDropdown(items);

  return (
    <DropdownContext.Provider
      value={{
        isOpen,
        toggleDropdown,
        selectedIndex,
        selectedItem,
        updateSelectedItem,
      }}
    >
      <div
        ref={dropdownRef as RefObject<HTMLDivElement>}
        {...getAriaAttributes()}
      >
        {children}
      </div>
    </DropdownContext.Provider>
  );
};

```


The `HeadlessDropdown` component takes two props:
          `children` and `items`, and utilizes a custom hook
          `useDropdown` to manage its state and behavior. It provides a context
          via `DropdownContext.Provider` to share state and behavior with its
          descendants. Within a `div`, it sets a ref and applies ARIA
          attributes for accessibility, then renders its `children` to display
          the nested components, enabling a structured and customizable dropdown
          functionality.


Note how we use `useDropdown` hook we defined in the previous
          section, and then pass these values down to the children of
          `HeadlessDropdown`. Following this, we can define the child
          components:


```
HeadlessDropdown.Trigger = function Trigger({
  as: Component = "button",
  ...props
}) {
  const { toggleDropdown } = useDropdownContext();

  return <Component tabIndex={0} onClick={toggleDropdown} {...props} />;
};

HeadlessDropdown.List = function List({
  as: Component = "ul",
  ...props
}) {
  const { isOpen } = useDropdownContext();

  return isOpen ? <Component {...props} role="listbox" tabIndex={0} /> : null;
};

HeadlessDropdown.Option = function Option({
  as: Component = "li",
  index,
  item,
  ...props
}) {
  const { updateSelectedItem, selectedIndex } = useDropdownContext();

  return (
    <Component
      role="option"
      aria-selected={index === selectedIndex}
      key={index}
      onClick={() => updateSelectedItem(item)}
      {...props}
    >
      {item.text}
    </Component>
  );
};

```


We defined a type `GenericComponentType` to handle a component or an
          HTML tag along with any additional properties. Three functions
          `HeadlessDropdown.Trigger`, `HeadlessDropdown.List`, and
          `HeadlessDropdown.Option` are defined to render respective parts of
          a dropdown menu. Each function utilizes the `as` prop to allow custom
          rendering of a component, and spreads additional properties onto the rendered
          component. They all access shared state and behavior via
          `useDropdownContext`.


`HeadlessDropdown.Trigger` renders a button by default that
              toggles the dropdown menu.
`HeadlessDropdown.List` renders a list container if the
              dropdown is open.
`HeadlessDropdown.Option` renders individual list items and
              updates the selected item when clicked.


These functions collectively allow a customizable and accessible dropdown menu
          structure.


It largely boils down to user preference on how they choose to utilize the
          Headless Component in their codebase. Personally, I lean towards hooks as they
          don't involve any DOM (or virtual DOM) interactions; the sole bridge between
          the shared state logic and UI is the ref object. On the other hand, with the
          context-based implementation, a default implementation will be provided when the
          user decides to not customize it.


In the upcoming example, I'll demonstrate how effortlessly we can
        transition to a different UI while retaining the core functionality with the `useDropdown` hook.


## Adapting to a New UI Requirement


Consider a scenario where a new design requires using a button as a
        trigger and displaying avatars alongside the text in the dropdown list.
        With the logic already encapsulated in our `useDropdown` hook, adapting
        to this new UI is straightforward.


In the new `DropdownTailwind` component below, we've made use of
        Tailwind CSS (Tailwind CSS is a utility-first CSS framework for rapidly
        building custom user interfaces) to style our elements. The structure is
        slightly modified - a button is used as the trigger, and each item in
        the dropdown list now includes an image. Despite these UI changes, the
        core functionality remains intact, thanks to our `useDropdown` hook.


```
const DropdownTailwind = ({ items }: DropdownProps) => {
  const {
    isOpen,
    selectedItem,
    selectedIndex,
    toggleDropdown,
    handleKeyDown,
    setSelectedItem,
  } = useDropdown<Item>(items);

  return (
    <div
      className="relative"
      onClick={toggleDropdown}
      onKeyDown={handleKeyDown}
    >
      <button className="btn p-2 border ..." tabIndex={0}>
        {selectedItem ? selectedItem.text : "Select an item..."}
      </button>

      {isOpen && (
        <ul
          className="dropdown-menu ..."
          role="listbox"
        >
          {(items).map((item, index) => (
            <li
              key={index}
              role="option"
            >
            {/* ... rest of the JSX ... */}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

```


In this rendition, the `DropdownTailwind` component interfaces with
        the `useDropdown` hook to manage its state and interactions. This design
        ensures that any UI modifications or enhancements do not necessitate a
        reimplementation of the underlying logic, significantly easing the
        adaptation to new design requirements.


We can also visualise the code a bit better with the React Devtools,
        note in the *hooks* section, all the states are listed in it:


![](headless-component/dev-tools.png)


Figure 5: Devtools


Every dropdown list, regardless of its external appearance, shares
        consistent behavior internally, all of which is encapsulated within the
        `useDropdown` hook (the Headless Component). However, what if we need to
        manage more states, like, async states when we have to fetch data from
        remote.


## Diving Deeper with Additional States


As we advance with our dropdown component, let's explore more
        intricate states that come into play when dealing with remote data. The
        scenario of fetching data from a remote source brings forth the
        necessity to manage a few more states - specifically, we need to handle
        loading, error, and data states.


![](headless-component/dropdown-async-status.png)


Figure 6: Different status


## Unveiling Remote Data Fetching


To load data from a remote server, we will need to define three new
        states: `loading`, `error`, and `data`. Here's how we can go about it
        typically with a `useEffect` call:


```
//...
  const [loading, setLoading] = useState<boolean>(false);
  const [data, setData] = useState<Item[] | null>(null);
  const [error, setError] = useState<Error | undefined>(undefined);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);

      try {
        const response = await fetch("/api/users");

        if (!response.ok) {
          const error = await response.json();
          throw new Error(`Error: ${error.error || response.status}`);
        }

        const data = await response.json();
        setData(data);
      } catch (e) {
        setError(e as Error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

//...

```


The code initializes three state variables: `loading`, `data`, and
        `error`. When the component mounts, it triggers an asynchronous function
        to fetch data from the “/api/users” endpoint. It sets `loading` to
        `true` before the fetch and to `false` afterwards. If the data is
        fetched successfully, it's stored in the `data` state. If there's an
        error, it's captured and stored in the `error` state.


## Refactoring for Elegance and Reusability


Incorporating fetching logic directly within our component can work,
        but it's not the most elegant or reusable approach. We can push the
        principle behind Headless Component a bit further here, separate the
        logic and state out of the UI. Let’s refactor this by extracting the
        fetching logic into a separate function:


```
const fetchUsers = async () => {
  const response = await fetch("/api/users");

  if (!response.ok) {
    const error = await response.json();
    throw new Error('Something went wrong');
  }

  return await response.json();
};

```


Now with the `fetchUsers` function in place, we can take a step
        further by abstracting our fetching logic into a generic hook. This hook
        will accept a *fetch function* and will manage the associated loading,
        error, and data states:


```
const useService = <T>(fetch: () => Promise<T>) => {
  const [loading, setLoading] = useState<boolean>(false);
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<Error | undefined>(undefined);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);

      try {
        const data = await fetch();
        setData(data);
      } catch(e) {
        setError(e as Error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [fetch]);

  return {
    loading,
    error,
    data,
  };
}

```


Now, the `useService` hook emerges as a reusable solution for data
        fetching across our application. It's a neat abstraction that we can
        employ to fetch various types of data, as demonstrated below:


```
// fetch products
const { loading, error, data } = useService(fetchProducts);
// or other type of resources
const { loading, error, data } = useService(fetchTickets);

```


With this refactoring, we've not only simplified our data fetching
        logic but also made it reusable across different scenarios in our
        application. This sets a solid foundation as we continue to enhance our
        dropdown component and delve deeper into more advanced features and
        optimizations.


## Maintaining Simplicity in the Dropdown Component


Incorporating remote data fetching has not complicated our `Dropdown`
        component, thanks to the abstracted logic in the `useService` and
        `useDropdown` hooks. Our component code remains in its simplest form,
        effectively managing the fetching states and rendering the content based
        on the data received.


```
const Dropdown = () => {
  const { data, loading, error } = useService(fetchUsers);

  const {
    toggleDropdown,
    dropdownRef,
    isOpen,
    selectedItem,
    selectedIndex,
    updateSelectedItem,
    getAriaAttributes,
  } = useDropdown<Item>(data || []);

  const renderContent = () => {
    if (loading) return <Loading />;
    if (error) return <Error />;
    if (data) {
      return (
        <DropdownMenu
          items={data}
          updateSelectedItem={updateSelectedItem}
          selectedIndex={selectedIndex}
        />
      );
    }
    return null;
  };

  return (
    <div
      className="dropdown"
      ref={dropdownRef as RefObject<HTMLDivElement>}
      {...getAriaAttributes()}
    >
      <Trigger
        onClick={toggleDropdown}
        text={selectedItem ? selectedItem.text : "Select an item..."}
      />
      {isOpen && renderContent()}
    </div>
  );
};

```


In this updated `Dropdown` component, we utilize the `useService`
        hook to manage the data fetching states, and the `useDropdown` hook to
        manage the dropdown-specific states and interactions. The
        `renderContent` function elegantly handles the rendering logic based on
        the fetching states, ensuring that the correct content is displayed
        whether it's loading, an error, or the data.


In the above example, observe how the Headless Component promotes
        loose coupling among parts. This flexibility lets us interchange parts
        for varied combinations. With shared `Loading` and `Error` components,
        we can effortlessly craft a `UserDropdown` with default JSX and styling,
        or a `ProductDropdown` using TailwindCSS that fetches data from a
        different API endpoint.


## Concluding the Headless Component Pattern


The Headless Component pattern unveils a robust avenue for cleanly
        segregating our JSX code from the underlying logic. While composing
        declarative UI with JSX comes naturally, the real challenge burgeons in
        managing state. This is where Headless Components come into play by
        shouldering all the state management intricacies, propelling us towards
        a new horizon of abstraction.


In essence, a Headless Component is a function or object that
        encapsulates logic, but doesn’t render anything itself. It leaves the
        rendering part to the consumer, thus offering a high degree of
        flexibility in how the UI is rendered. This pattern can be exceedingly
        useful when we have complex logic that we want to reuse across different
        visual representations.


```
function useDropdownLogic() {
  // ... all the dropdown logic
  return {
    // ... exposed logic
  };
}

function MyDropdown() {
  const dropdownLogic = useDropdownLogic();
  return (
    // ... render the UI using the logic from dropdownLogic
  );
}

```


Headless Components offer several benefits, including enhanced
        reusability as they encapsulate logic that can be shared across multiple
        components, adhering to the DRY (Don’t Repeat Yourself) principle. They
        emphasize a clear separation of concerns by distinctly differentiating
        logic from rendering, a foundational practice for crafting maintainable
        code. Additionally, they provide flexibility by allowing developers to
        adopt varied UI implementations using the same core logic, which is
        particularly advantageous when dealing with different design
        requirements or working with various frameworks.


However, it's essential to approach them with discernment. Like any
        design pattern, they come with challenges. For those unfamiliar, there
        might be an initial learning curve that could temporarily slow down
        development. Moreover, if not applied judiciously, the abstraction
        introduced by Headless Components might add a level of indirection,
        potentially complicating the code's readability.


I'd like to note that this pattern could be applicable in other
        frontend libraries or frameworks. For instance, Vue refers to this
        concept as a `renderless` component. It embodies the same principle,
        prompting developers to segregate logic and state management into a
        distinct component, thereby enabling users to construct the UI around
        it.


I'm uncertain about its implementation or compatibility in Angular or
        other frameworks, but I recommend considering its potential benefits in
        your specific context.


## Revisiting the root patterns in GUI


If you've been in the industry long enough, or have experience with GUI applications in a
       desktop setup, you'll likely recognize some familiarity with the Headless Component
       pattern—perhaps under a different name—be it View-Model in MVVM, [Presentation
       Model](https://martinfowler.com/bliki/PresentationModel.html), or other terms depending on
       your exposure. Martin Fowler provided a deep dive into these terms in a [comprehensive
       article](https://martinfowler.com/eaaDev/uiArchs.html) several years ago, where he clarified
       many terminologies that have been widely used in the GUI world, such as MVC,
       Model-View-Presenter, among others.


> Presentation Model abstracts the state and behavior of the view into a model class
>          within the presentation layer. This model coordinates with the domain layer and provides
>          an interface to the view, minimizing decision-making in the view...
> -- [Martin Fowler](https://martinfowler.com/bliki/PresentationModel.html)


Nevertheless, I believe it's necessary to expand a bit on this established pattern and
       explore how it operates within the React or front-end world. As technology evolves, some of
       the challenges faced by traditional GUI applications may no longer hold relevance,
       rendering certain mandatory elements now optional.


For instance, one reason behind separating the UI and logic was the difficulty in testing
       their combination, especially on the headless [CI](https://martinfowler.com/articles/continuousIntegration.html)/[CD](https://martinfowler.com/bliki/ContinuousDelivery.html) environments. 
       Thus, we aimed to extract as much as possible into UI-less code to ease the testing process. However, this
       isn't a significant issue in React and many other web frameworks. For one, we have robust
       in-memory testing mechanisms like [jsdom](https://github.com/jsdom/jsdom) to test the UI behaviour, DOM manipulations,
       etc. These tests can be run in any environment, like on headless CI/CD servers, and we
       can easily execute real browser tests using [Cypress](https://www.cypress.io) in an in-memory browser (headless
       Chrome, for example)—a feat not feasible for Desktop applications when MVC/MVP was
       conceived.


Another major challenge MVC faced was data synchronization, necessitating Presenters, or
       Presentation Models to orchestrate changes on the underlying data and notify other
       rendering parts. A classic example of the is illustrated below:


![](headless-component/mvc-trans.png)


Figure 7: One model has multiple presentations


In the illustration above, The three UI components (table, line chart and heatmap) are
       entirely independent, but all of them are rendering the same model data. When you modified
       data from table, the other two graphs will be refreshed. To be able to detect the change,
       and apply the change to refresh correpondingly components, you will need setup event
       listener manually.


However, with the advent of unidirectional data flow, React (along with many other modern
       frameworks) has forged a different path. As developers, we no longer need to monitor
       model changes. The fundamental idea is to treat every change as a whole new instance, and
       re-render everything from scratch - It's crucial to note that I'm significantly simplifying
       the entire process here, overlooking the [virtual DOM](https://legacy.reactjs.org/docs/faq-internals.html#what-is-the-virtual-dom) and the differentiation and
       reconciliation processes - implying that within the codebase, the requirement to register
       event listeners to accurately update other segments post model alterations has been
       eliminated.


In summary, the Headless Component doesn't aim to reinvent established UI patterns; instead, 
      it serves as an implementation within the component-based UI architecture. The principle of 
      segregating logic and state management from views retains its importance, especially in 
      delineating clear responsibilities and in scenarios where there's an opportunity to substitute 
      one view for another.


## Understanding the community


The concept of Headless Components isn't novel, it has existed for
        some time but hasn't been widely acknowledged or incorporated into
        projects. However, several libraries have adopted the Headless Component
        pattern, promoting the development of accessible, adaptable, and
        reusable components. Some of these libraries have already gained
        significant traction within the community:

- [React ARIA](https://react-spectrum.adobe.com/react-aria/): A
          library from Adobe that provides accessibility primitives and hooks for
          building inclusive React applications. It offers a collection of hooks
          to manage keyboard interactions, focus management, and ARIA annotations,
          making it easier to create accessible UI components.
- [Headless UI](https://headlessui.dev/): A completely unstyled,
          fully accessible UI component library, designed to integrate beautifully
          with Tailwind CSS. It provides the behavior and accessibility foundation
          upon which you can build your own styled components.
- [React Table](https://react-table.tanstack.com/): A headless
          utility for building fast and extendable tables and datagrids for React.
          It provides a flexible hook that allows you to create complex tables
          with ease, leaving the UI representation up to you.
- [Downshift](https://www.downshift-js.com/): A minimalist
          library to help you create accessible and customizable dropdowns,
          comboboxes, and more. It handles all the logic while letting you define
          the rendering aspect.


These libraries embody the essence of the Headless Component pattern
        by encapsulating complex logic and behaviors, making it straightforward
        to create highly interactive and accessible UI components. While the
        provided example serves as a learning stepping stone, it's prudent to
        leverage these production-ready libraries for building robust,
        accessible, and customizable components in a real-world scenario.


This pattern not only educates us on managing complex logic and state
        but also nudges us to explore production-ready libraries that have honed
        the Headless Component approach to deliver robust, accessible, and
        customizable components for real-world use.


## Summary


In this article, we delve into the concept of Headless Components, a
        sometimes overlooked pattern in crafting reusable UI logic. Using the
        creation of an intricate dropdown list as an example, we begin with a
        simple dropdown and incrementally introduce features such as keyboard
        navigation and asynchronous data fetching. This approach showcases the
        seamless extraction of reusable logic into a Headless Component and
        highlights the ease with which we can overlay a new UI.


Through practical examples, we illuminate how such separation paves
        the way for building reusable, accessible, and tailored components. We
        also spotlight renowned libraries like React Table, Downshift, React
        UseGesture, React ARIA, and Headless UI that champion the Headless
        Component pattern. These libraries offer pre-configured solutions for
        developing interactive and user-friendly UI components.


This deep dive emphasizes the pivotal role of the separation of
        concerns in the UI development process, underscoring its significance in
        crafting scalable, accessible, and maintainable React applications.


---
