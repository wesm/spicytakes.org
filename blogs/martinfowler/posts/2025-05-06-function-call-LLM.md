---
title: "Function calling using LLMs"
description: "While LLMs excel at generating cogent text based on their training   data, they may also need to interact with external systems. Function   calling allows them to construct such calls. The LLM does no"
date: 2025-05-06T00:00:00
tags: ["application integration", "generative ai"]
url: https://martinfowler.com/articles/function-call-LLM.html
slug: function-call-LLM
word_count: 3277
---


One of the key applications of LLMs is to enable programs (agents) that
    can interpret user intent, reason about it, and take relevant actions
    accordingly.


**Function calling** is a capability that enables LLMs to go beyond
    simple text generation by interacting with external tools and real-world
    applications. With function calling, an LLM can analyze a natural language
    input, extract the user’s intent, and generate a structured output
    containing the function name and the necessary arguments to invoke that
    function.


It’s important to emphasize that when using function calling, the LLM
    itself does not execute the function. Instead, it identifies the appropriate
    function, gathers all required parameters, and provides the information in a
    structured JSON format. This JSON output can then be easily deserialized
    into a function call in Python (or any other programming language) and
    executed within the program’s runtime environment.


![](function-call-LLM/image2.png)


Figure 1: natural langauge request to structured output


To see this in action, we’ll build a *Shopping Agent* that helps users
    discover and shop for fashion products. If the user’s intent is unclear, the
    agent will prompt for clarification to better understand their needs.


For example, if a user says *“I’m looking for a shirt”* or *“Show me
    details about the blue running shirt,”* the shopping agent will invoke the
    appropriate API—whether it’s searching for products using keywords or
    retrieving specific product details—to fulfill the request.


## Scaffold of a typical agent


Let's write a scaffold for building this agent. (All code examples are
      in Python.)


```
class ShoppingAgent:

    def run(self, user_message: str, conversation_history: List[dict]) -> str:
        if self.is_intent_malicious(user_message):
            return "Sorry! I cannot process this request."

        action = self.decide_next_action(user_message, conversation_history)
        return action.execute()

    def decide_next_action(self, user_message: str, conversation_history: List[dict]):
        pass

    def is_intent_malicious(self, message: str) -> bool:
        pass

```


Based on the user’s input and the conversation history, the
      shopping agent selects from a predefined set of possible actions, executes
      it and returns the result to the user. It then continues the conversation
      until the user’s goal is achieved.


Now, let’s look at the possible actions the agent can take:


```
class Search():
    keywords: List[str]

    def execute(self) -> str:
        # use SearchClient to fetch search results based on keywords 
        pass

class GetProductDetails():
    product_id: str

    def execute(self) -> str:
 # use SearchClient to fetch details of a specific product based on product_id 
        pass

class Clarify():
    question: str

    def execute(self) -> str:
        pass

```


## Unit tests


Let's start by writing some unit tests to validate this functionality
      before implementing the full code. This will help ensure that our agent
      behaves as expected while we flesh out its logic.


```
def test_next_action_is_search():
    agent = ShoppingAgent()
    action = agent.decide_next_action("I am looking for a laptop.", [])
    assert isinstance(action, Search)
    assert 'laptop' in action.keywords

def test_next_action_is_product_details(search_results):
    agent = ShoppingAgent()
    conversation_history = [
        {"role": "assistant", "content": f"Found: Nike dry fit T Shirt (ID: p1)"}
    ]
    action = agent.decide_next_action("Can you tell me more about the shirt?", conversation_history)
    assert isinstance(action, GetProductDetails)
    assert action.product_id == "p1"

def test_next_action_is_clarify():
    agent = ShoppingAgent()
    action = agent.decide_next_action("Something something", [])
    assert isinstance(action, Clarify)

```


Let's implement the `decide_next_action` function using OpenAI's API
      and a GPT model. The function will take user input and conversation
      history, send it to the model, and extract the action type along with any
      necessary parameters.


```
def decide_next_action(self, user_message: str, conversation_history: List[dict]):
    response = self.client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *conversation_history,
            {"role": "user", "content": user_message}
        ],
        tools=[
            {"type": "function", "function": SEARCH_SCHEMA},
            {"type": "function", "function": PRODUCT_DETAILS_SCHEMA},
            {"type": "function", "function": CLARIFY_SCHEMA}
        ]
    )
    
    tool_call = response.choices[0].message.tool_calls[0]
    function_args = eval(tool_call.function.arguments)
    
    if tool_call.function.name == "search_products":
        return Search(**function_args)
    elif tool_call.function.name == "get_product_details":
        return GetProductDetails(**function_args)
    elif tool_call.function.name == "clarify_request":
        return Clarify(**function_args)
```


Here, we are calling OpenAI’s chat completion API with a system prompt
      that directs the LLM, in this case `gpt-4-turbo-preview` to determine the
      appropriate action and extract the necessary parameters based on the
      user’s message and the conversation history. The LLM returns the output as
      a structured JSON response, which is then used to instantiate the
      corresponding action class. This class executes the action by invoking the
      necessary APIs, such as `search` and `get_product_details`.


## System prompt


Now, let’s take a closer look at the system prompt:


```
SYSTEM_PROMPT = """You are a shopping assistant. Use these functions:
1. search_products: When user wants to find products (e.g., "show me shirts")
2. get_product_details: When user asks about a specific product ID (e.g., "tell me about product p1")
3. clarify_request: When user's request is unclear"""

```


With the system prompt, we provide the LLM with the necessary context
      for our task. We define its role as a *shopping assistant*, specify the
      expected *output format* (functions), and include *constraints and
      special instructions*, such as asking for clarification when the user's
      request is unclear.


This is a basic version of the prompt, sufficient for our example.
      However, in real-world applications, you might want to explore more
      sophisticated ways of guiding the LLM. Techniques like **One-shot
      prompting**—where a single example pairs a user message with the
      corresponding action—or **Few-shot prompting**—where multiple examples
      cover different scenarios—can significantly enhance the accuracy and
      reliability of the model’s responses.


This part of the Chat Completions API call defines the available
      functions that the LLM can invoke, specifying their structure and
      purpose:


```
tools=[
    {"type": "function", "function": SEARCH_SCHEMA},
    {"type": "function", "function": PRODUCT_DETAILS_SCHEMA},
    {"type": "function", "function": CLARIFY_SCHEMA}
]
```


Each entry represents a function the LLM can call, detailing its
      expected parameters and usage according to the *OpenAI API
      specification*.


Now, let’s take a closer look at each of these function schemas.


```
SEARCH_SCHEMA = {
    "name": "search_products",
    "description": "Search for products using keywords",
    "parameters": {
        "type": "object",
        "properties": {
            "keywords": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Keywords to search for"
            }
        },
        "required": ["keywords"]
    }
}

PRODUCT_DETAILS_SCHEMA = {
    "name": "get_product_details",
    "description": "Get detailed information about a specific product",
    "parameters": {
        "type": "object",
        "properties": {
            "product_id": {
                "type": "string",
                "description": "Product ID to get details for"
            }
        },
        "required": ["product_id"]
    }
}

CLARIFY_SCHEMA = {
    "name": "clarify_request",
    "description": "Ask user for clarification when request is unclear",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "Question to ask user for clarification"
            }
        },
        "required": ["question"]
    }
}


```


With this, we define each function that the LLM can invoke, along with
      its parameters—such as `keywords` for the âsearchâ function and
      `product_id` for `get_product_details`. We also specify which
      parameters are mandatory to ensure proper function execution.


Additionally, the `description` field provides extra context to
      help the LLM understand the function's purpose, especially when the
      function name alone isn’t self-explanatory.


With all the key components in place, let's now fully implement the
      `run` function of the `ShoppingAgent` class. This function will
      handle the end-to-end flow—taking user input, deciding the next action
      using OpenAI’s function calling, executing the corresponding API calls,
      and returning the response to the user.


Here’s the complete implementation of the agent:


```
class ShoppingAgent:
    def __init__(self):
        self.client = OpenAI()

    def run(self, user_message: str, conversation_history: List[dict] = None) -> str:
        if self.is_intent_malicious(user_message):
            return "Sorry! I cannot process this request."

        try:
            action = self.decide_next_action(user_message, conversation_history or [])
            return action.execute()
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

    def decide_next_action(self, user_message: str, conversation_history: List[dict]):
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *conversation_history,
                {"role": "user", "content": user_message}
            ],
            tools=[
                {"type": "function", "function": SEARCH_SCHEMA},
                {"type": "function", "function": PRODUCT_DETAILS_SCHEMA},
                {"type": "function", "function": CLARIFY_SCHEMA}
            ]
        )
        
        tool_call = response.choices[0].message.tool_calls[0]
        function_args = eval(tool_call.function.arguments)
        
        if tool_call.function.name == "search_products":
            return Search(**function_args)
        elif tool_call.function.name == "get_product_details":
            return GetProductDetails(**function_args)
        elif tool_call.function.name == "clarify_request":
            return Clarify(**function_args)

    def is_intent_malicious(self, message: str) -> bool:
        pass


```


## Restricting the agent's action space


It's essential to restrict the agent's action space using
      explicit conditional logic, as demonstrated in the above code block.
      While dynamically invoking functions using `eval` might seem
      convenient, it poses significant security risks, including prompt
      injections that could lead to unauthorized code execution. To safeguard
      the system from potential attacks, always enforce strict control over
      which functions the agent can invoke.


## Guardrails against prompt injections


When building a user-facing agent that communicates in natural language and performs background actions via function calling, it's critical to anticipate adversarial behavior. Users may intentionally try to bypass safeguards and trick the agent into taking unintended actions—like SQL injection, but through language.


A common attack vector involves prompting the agent to reveal its system prompt, giving the attacker insight into how the agent is instructed. With this knowledge, they might manipulate the agent into performing actions such as issuing unauthorized refunds or exposing sensitive customer data.


While restricting the agent’s action space is a solid first step, it’s not sufficient on its own.


To enhance protection, it's essential to sanitize user input to detect and prevent malicious intent. This can be approached using a combination of:

- Traditional techniques, like regular expressions and input denylisting, to filter known malicious patterns.
- LLM-based validation, [where another model screens inputs](https://martinfowler.com/articles/gen-ai-patterns/#guardrails) for signs of manipulation, injection attempts, or prompt exploitation.


Here’s a simple implementation of a denylist-based guard that flags potentially malicious input:


```
def is_intent_malicious(self, message: str) -> bool:
    suspicious_patterns = [
        "ignore previous instructions",
        "ignore above instructions",
        "disregard previous",
        "forget above",
        "system prompt",
        "new role",
        "act as",
        "ignore all previous commands"
    ]
    message_lower = message.lower()
    return any(pattern in message_lower for pattern in suspicious_patterns)

```


This is a basic example, but it can be extended with regex matching, contextual checks, or integrated with an LLM-based filter for more nuanced detection.


Building robust prompt injection guardrails is essential for maintaining the safety and integrity of your agent in real-world scenarios


## Action classes


This is where the action really happens! **Action classes** serve as
      the gateway between the LLM’s decision-making and actual system
      operations. They translate the LLM’s interpretation of the user’s
      request—based on the conversation—into concrete actions by invoking the
      appropriate APIs from your microservices or other internal systems.


```
class Search:
    def __init__(self, keywords: List[str]):
        self.keywords = keywords
        self.client = SearchClient()

    def execute(self) -> str:
        results = self.client.search(self.keywords)
        if not results:
            return "No products found"
        products = [f"{p['name']} (ID: {p['id']})" for p in results]
        return f"Found: {', '.join(products)}"

class GetProductDetails:
    def __init__(self, product_id: str):
        self.product_id = product_id
        self.client = SearchClient()

    def execute(self) -> str:
        product = self.client.get_product_details(self.product_id)
        if not product:
            return f"Product {self.product_id} not found"
        return f"{product['name']}: price: ${product['price']} - {product['description']}"

class Clarify:
    def __init__(self, question: str):
        self.question = question

    def execute(self) -> str:
        return self.question

```


In my implementation, the conversation history is stored in the
      user interface’s session state and passed to the `run` function on
      each call. This allows the shopping agent to retain context from
      previous interactions, enabling it to make more informed decisions
      throughout the conversation.


For example, if a user requests details about a specific product, the
      LLM can extract the `product_id` from the most recent message that
      displayed the search results, ensuring a seamless and context-aware
      experience.


Here’s an example of how a typical conversation flows in this simple
      shopping agent implementation:


![](function-call-LLM/image1.png)


Figure 2: Conversation with the shopping agent


## Refactoring to reduce boiler plate


A significant portion of the verbose boilerplate code in the
      implementation comes from defining detailed function specifications for
      the LLM. You could argue that this is redundant, as the same information
      is already present in the concrete implementations of the action
      classes.


Fortunately, libraries like [instructor](https://pypi.org/project/instructor/) help reduce
      this duplication by providing functions that can automatically serialize
      Pydantic objects into JSON following the OpenAI schema. This reduces
      duplication, minimizes boilerplate code, and improves maintainability.


Let’s explore how we can simplify this implementation using
      instructor. The key change
      involves defining action classes as *Pydantic* objects, like so:


```
from typing import List, Union
from pydantic import BaseModel, Field
from instructor import OpenAISchema
from neo.clients import SearchClient

class BaseAction(BaseModel):
    def execute(self) -> str:
        pass

class Search(BaseAction):
    keywords: List[str]

    def execute(self) -> str:
        results = SearchClient().search(self.keywords)
        if not results:
            return "Sorry I couldn't find any products for your search."
        
        products = [f"{p['name']} (ID: {p['id']})" for p in results]
        return f"Here are the products I found: {', '.join(products)}"

class GetProductDetails(BaseAction):
    product_id: str

    def execute(self) -> str:
        product = SearchClient().get_product_details(self.product_id)
        if not product:
            return f"Product {self.product_id} not found"
        
        return f"{product['name']}: price: ${product['price']} - {product['description']}"

class Clarify(BaseAction):
    question: str

    def execute(self) -> str:
        return self.question

class NextActionResponse(OpenAISchema):
    next_action: Union[Search, GetProductDetails, Clarify] = Field(
        description="The next action for agent to take.")

```


The agent implementation is updated to use NextActionResponse, where
      the `next_action` field is an instance of either Search, GetProductDetails,
      or Clarify action classes. The `from_response` method from the instructor
      library simplifies deserializing the LLM’s response into a
      NextActionResponse object, further reducing boilerplate code.


```
class ShoppingAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def run(self, user_message: str, conversation_history: List[dict] = None) -> str:
        if self.is_intent_malicious(user_message):
            return "Sorry! I cannot process this request."
        try:
            action = self.decide_next_action(user_message, conversation_history or [])
            return action.execute()
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

    def decide_next_action(self, user_message: str, conversation_history: List[dict]):
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *conversation_history,
                {"role": "user", "content": user_message}
            ],
            tools=[{
                "type": "function",
                "function": NextActionResponse.openai_schema
            }],
            tool_choice={"type": "function", "function": {"name": NextActionResponse.openai_schema["name"]}},
        )
        return NextActionResponse.from_response(response).next_action

    def is_intent_malicious(self, message: str) -> bool:
        suspicious_patterns = [
            "ignore previous instructions",
            "ignore above instructions",
            "disregard previous",
            "forget above",
            "system prompt",
            "new role",
            "act as",
            "ignore all previous commands"
        ]
        message_lower = message.lower()
        return any(pattern in message_lower for pattern in suspicious_patterns)

```


## Can this pattern replace traditional rules engines?


[Rules engines](https://martinfowler.com/bliki/RulesEngine.html) have long held sway in enterprise software architecture, but in 
      practice, they rarely live up their promise. Martin Fowler’s observation about them from over 
      15 years ago still rings true:


> Often the central pitch for a rules engine is that it will allow the business people to specify the rules themselves, so they can build the rules without involving programmers. As so often, this can sound plausible but rarely works out in practice


The core issue with rules engines lies in their complexity over time. As the number of rules grows, so does the risk of unintended interactions between them. While defining individual rules in isolation — often via drag-and-drop tools might seem simple and manageable, problems emerge when the rules are executed together in real-world scenarios. The combinatorial explosion of rule interactions makes these systems increasingly difficult to test, predict and maintain.


LLM-based systems offer a compelling alternative. While they don’t yet provide full transparency or determinism in their decision making, they can reason about user intent and context in a way that traditional static rule sets cannot. Instead of rigid rule chaining, you get context-aware, adaptive behaviour driven by language understanding. And for business users or domain experts, expressing rules through natural language prompts may actually be more intuitive and accessible than using a rules engine that ultimately generates hard-to-follow code.


A practical path forward might be to combine LLM-driven reasoning with explicit manual gates for executing critical decisions—striking a balance between flexibility, control, and safety


## Function calling vs Tool calling


While these terms are often used interchangeably, âtool callingâ is the more general and modern term. It refers to broader set of capabilities that LLMs can use to interact with the outside world. For example, in addition to calling custom functions, an LLM might offer inbuilt tools like code interpreter ( for executing code ) and retrieval mechanisms ( for accessing data from uploaded files or connected databases ).


## How Function calling relates to MCP ( Model Context Protocol )


[The Model Context Protocol ( MCP )](https://modelcontextprotocol.io/introduction) is an open protocol proposed by Anthropic that's gaining traction as a standardized way to structure how LLM-based applications interact with the external world. [A growing number of software as a service providers ](https://github.com/modelcontextprotocol/servers)are now exposing their service to LLM Agents using this protocol.


MCP defines a client-server architecture with three main components:


![](function-call-LLM/mcp.svg)


Figure 3: High level architecture - shopping agent using MCP

- MCP Server: A server that exposes data sources and various tools (i.e functions) that can be invoked over HTTP
- MCP Client: A client that manages communication between an application and the MCP Server
- MCP Host: The LLM-based application (e.g our âShoppingAgentâ) that uses the data and tools provided by the MCP Server to accomplish a task (fulfill user's shopping request). The MCPHost accesses these capabilities via the MCPClient


The core problem MCP addresses is flexibility and dynamic tool discovery. In our above example of âShoppingAgentâ, you may notice that the set of available tools is hardcoded to three functions the agent can invoke i.e `search_products`,        `get_product_details` and `clarify`. This in a way, limits the agent's ability to adapt or scale to new types of requests, but inturn makes it easier to secure it agains malicious usage.


With MCP, the agent can instead query the MCPServer at runtime to discover which tools are available. Based on the user's query, it can then choose and invoke the appropriate tool dynamically.


This model decouples the LLM application from a fixed set of tools, enabling modularity, extensibility, and dynamic capability expansion - which is especially valuable for complex or evolving agent systems.


Although MCP adds extra complexity, there are certain applications (or agents) where that complexity is justified. For example, LLM-based IDEs or code generation tools need to stay up to date with the latest APIs they can interact with. In theory, you could imagine a general-purpose agent with access to a wide range of tools, capable of handling a variety of user requests — unlike our example, which is limited to shopping-related tasks.


Let's look at what a simple MCP server might look like for our shopping application. Notice the `GET /tools `endpoint - it returns a list of all the functions (or tools) that server is making available.


```
TOOL_REGISTRY = {
    "search_products": SEARCH_SCHEMA,
    "get_product_details": PRODUCT_DETAILS_SCHEMA,
    "clarify": CLARIFY_SCHEMA
}

@app.route("/tools", methods=["GET"])
def get_tools():
    return jsonify(list(TOOL_REGISTRY.values()))

@app.route("/invoke/search_products", methods=["POST"])
def search_products():
    data = request.json
    keywords = data.get("keywords")
    search_results = SearchClient().search(keywords)
    return jsonify({"response": f"Here are the products I found: {', '.join(search_results)}"}) 

@app.route("/invoke/get_product_details", methods=["POST"])
def get_product_details():
    data = request.json
    product_id = data.get("product_id")
    product_details = SearchClient().get_product_details(product_id)
    return jsonify({"response": f"{product_details['name']}: price: ${product_details['price']} - {product_details['description']}"})

@app.route("/invoke/clarify", methods=["POST"])
def clarify():
    data = request.json
    question = data.get("question")
    return jsonify({"response": question})

if __name__ == "__main__":
    app.run(port=8000)


```


And here's the corresponding MCP client, which handles communication between the MCP host (ShoppingAgent) and the server:


```
class MCPClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def get_tools(self):
        response = requests.get(f"{self.base_url}/tools")
        response.raise_for_status()
        return response.json()

    def invoke(self, tool_name, arguments):
        url = f"{self.base_url}/invoke/{tool_name}"
        response = requests.post(url, json=arguments)
        response.raise_for_status()
        return response.json()


```


Now let's refactor our `ShoppingAgent` (the MCP Host) to first retrieve the list of available tools from the MCP server, and then invoke the appropriate function using the MCP client.


```
class ShoppingAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.mcp_client = MCPClient(os.getenv("MCP_SERVER_URL"))
        self.tool_schemas = self.mcp_client.get_tools()

    def run(self, user_message: str, conversation_history: List[dict] = None) -> str:
        if self.is_intent_malicious(user_message):
            return "Sorry! I cannot process this request."

        try:
            tool_call = self.decide_next_action(user_message, conversation_history or [])
            result = self.mcp_client.invoke(tool_call["name"], tool_call["arguments"])
            return str(result["response"])

        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

    def decide_next_action(self, user_message: str, conversation_history: List[dict]):
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *conversation_history,
                {"role": "user", "content": user_message}
            ],
            tools=[{"type": "function", "function": tool} for tool in self.tool_schemas],
            tool_choice="auto"
        )
        tool_call = response.choices[0].message.tool_call
        return {
            "name": tool_call.function.name,
            "arguments": tool_call.function.arguments.model_dump()
        }
    
        def is_intent_malicious(self, message: str) -> bool:
            pass

```


## Conclusion


Function calling is an exciting and powerful capability of LLMs that opens the door to novel user experiences and development of sophisticated agentic systems. However, it also introduces new risks—especially when user input can ultimately trigger sensitive functions or APIs. With thoughtful guardrail design and proper safeguards, many of these risks can be effectively mitigated. It's prudent to start by enabling function calling for low-risk operations and gradually extend it to more critical ones as safety mechanisms mature.


---
