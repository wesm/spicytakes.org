---
title: "This MCP Server Could Have Been a JSON File"
subtitle: "There's a lot of buzz around MCP. I'm not convinced it needs to exist."
date: 2025-09-11T10:03:17+00:00
url: https://materializedview.io/p/mcp-server-could-have-been-json-file
slug: mcp-server-could-have-been-json-file
word_count: 1003
---


Model context protocol (MCP)servers are very buzzy right now. The idea is simple: teachlarge language models (LLMs)how to interact with other software systems. In doing so, LLMs can learn from and affect the real world; they can call a web service to make a phone call, invoke acommand line interface (CLI)tool to add an item to a grocery list in a reminder app, and so on. To make such calls, LLMs must know what software it can call and how to do so. This is the problem that MCP solves: it informs LLMs of available software, teaches the LLM how to use it, and provides an avenue through which the LLM can call the software.


Developers write MCP servers that provideresources,prompts, andtoolsto the LLM. The MCP sitediscusses these concepts in detail, but theCore MCP Conceptssection provides a summary:


> Resources: File-like data that can be read by clients (like API responses or file contents)Tools: Functions that can be called by the LLM (with user approval)Prompts: Pre-written templates that help users accomplish specific tasks


These categories are arbitrary and confusing. At first blush, it seems resources are read-only and tools are write-only. But the MCP server documentation usessearchFlightsas their tool example—a read-only operation. Even more baffling, they later show flight searching as a resource. Here’s their tool definition:


```
{
  name: "searchFlights",
  description: "Search for available flights",
  inputSchema: {
    type: "object",
    properties: {
      origin: { type: "string", description: "Departure city" },
      destination: { type: "string", description: "Arrival city" },
      date: { type: "string", format: "date", description: "Travel date" }
    },
    required: ["origin", "destination", "date"]
  }
}
```


And here’s their resource definition:


```
{
  "uriTemplate": "travel://flights/{origin}/{destination}",
  "name": "flight-search",
  "title": "Flight Search",
  "description": "Search available flights between cities",
  "mimeType": "application/json"
}
```


Prompts are simplystatic JSON definitionsthat describe potential user activities.


The whole protocol feels off to me. Prompts are just static documentation, resources are static URL definitions, and tools look likeremote procedure call (RPC)definitions. I askedChatGPT 5 Thinkingto convert thesearchFlightstool definition to anOpenAPI definition(an actual RPC definition). Unsurprisingly,  it worked just fine:


```
openapi: 3.0.0
info:
  title: Flights API
  version: "1.0.0"
paths:
  /searchFlights:
    get:
      operationId: searchFlights
      summary: Search for available flights
      description: Search for available flights
      parameters:
        - in: query
          name: origin
          required: true
          description: Departure city
          schema:
            type: string
        - in: query
          name: destination
          required: true
          description: Arrival city
          schema:
            type: string
        - in: query
          name: date
          required: true
          description: Travel date
          schema:
            type: string
            format: date
      responses:
        "200":
          description: Search results
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
```


This begs the question: why do we need MCP for tool definitions? We already haveOpenAPI,gRPC, and CLIs. ChatGPT understands OpenAPI definitions. Millions of web services already provide OpenAPI definitions, too. And ChatGPT is actually better at CLIs than most humans—just watchCodexfly through sed, awk, and grep commands. A friend recently informed me that they successfully taught ChatGPT to usetmux.MCP vs CLI: Benchmarking Tools for Coding Agentsreflects this sentiment:


> MCP vs CLI truly is a wash: BothterminalcpMCP and CLI versions achieved 100% success rates. The MCP version was 23% faster (51m vs 66m) and 2.5% cheaper ($19.45 vs $19.95).


I’ve seenseveral argumentsmade to justify MCP’s existence:

1. LLMs have a limited context window. OpenAPI documentation takes up too much context space.
2. Many services are not well documented; they don’t come with an API spec.
3. LLMs need a way to discover what tools are available to it.


I’m skeptical. Perhaps MCP does allow us to squeeze a few more tools into the context window. Perhaps it does let models run a little faster. OpenAPI documents are indeed somewhat verbose. But for how long will this matter?


Last year we were talking about 1 million token models. Now, we have2 million token modelsinOpenRouter. Smaller models, fine tuning, and other research also continues apace. Viewed from this lens, MCP seems like a temporary kludge.


The final argument that many services have poor documentation is true for internal enterprise services.Jake Mannixmakes this point inhis recent thread. I hear that MCP is most widely adopted for this segment.


Customer-facing SaaS APIs are a different story. Mostareremarkablywelldocumented. Some are complex, but these are ofteninherent complexities(I can attest to this after working withWePay’s API).


Moreover, the argument seems to be that the same people that wrote the bad OpenAPI specs are going to write good MCP specs. I don’t buy it. (And again, even if theycoulddo this, why not write the endpoint as an OpenAPI endpoint or a CLI tool?)


![](https://substackcdn.com/image/fetch/$s_!HJgE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faded91f2-44a4-4e2b-a7f6-cb171417897f_684x196.png)

*View Post*


As for discovery, I accept that LLMs need to know where tools are and how to use them. But this is static content. We already haveAGENTS.md,.github/instructions,openapi.json, and so on.


Developersarewakingup to this.Bruin﹩ is using MCPjust to expose documentation; their tool calls are done through normal CLI commands.Donobu﹩ simply provides an OpenAPI spec. Both solutions work. Meanwhile, MCP’s Google trend looks bleak.


![](https://substackcdn.com/image/fetch/$s_!cMux!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd7b8f6f-0253-49e7-82c7-23309e34ad02_1142x704.png)

*Google Trends “mcp” Interest Over Time*


I don’t blame the MCP authors for this mess. Things happen fast in the AI ecosystem. MCP is a victim of its own success.MCP: An (Accidentally) Universal Plugin Systemdoes a good job explaining the situation.


We need to take a step back and think about what we’re trying to accomplish. There’s no law that LLMs need a new protocol to interact with software. In most cases, we have what we need. Where we don’t, we should write CLIs, web services, and documentation using existing standards.


> My takeaway? Maybe instead of arguing about MCP vs CLI, we should start building better tools. The protocol is just plumbing. What matters is whether your tool helps or hinders the agent's ability to complete tasks.—Mario Zechner,MCP vs CLI: Benchmarking Tools for Coding Agents


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
