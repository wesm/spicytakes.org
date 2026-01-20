---
title: "From pandas to Arrow: The Future of Data Infrastructure"
summary: "Podcast at Tech on the Rocks Podcast"
date: 2025-12-01T00:00:00
tags: ["podcast", "transcript"]
slug: tech-on-the-rocks-data-infrastructure
word_count: 5685
source_file: transcripts/2025-12-01-tech-on-the-rocks-data-infrastructure.md
content_type: transcript
event: "Tech on the Rocks Podcast"
video_url: "https://techontherocks.show/23"
---

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this wide-ranging 80-minute podcast with Kostas and Nitay, I cover the evolution of data infrastructure from pandas through Arrow to modern systems, along with thoughts on AI, open source sustainability, and the future of file formats.

### Career Arc and the Origins of Arrow

- Started pandas 17 years ago (2008), initially focused on user API and experience out of frustration with Excel
- Over time, naturally learned the systems side—performance, scalability, memory efficiency, file formats, database connectivity
- After pandas came Python for Data Analysis (2012), then Datapad with Chang Shu—a visual analytics company like what Hex is today
- At Datapad in 2013, pandas couldn't deliver the speed we needed for interactive SaaS analytics; DuckDB didn't exist yet
- Built a C library implementing a miniature query engine and a "Proto Arrow" file format for S3—this planted the seed for Arrow
- Gave the "Ten things I hate about pandas" talk at PyData NYC (November 2013) noting pandas wasn't designed as a database engine
- Datapad exited to Cloudera (end of 2014), where I worked with the Impala and Kudu teams—perfect environment to kick off Arrow
- Simultaneously started Ibis to decouple the DataFrame API from the compute engine; it's now 10 years old with surprising adoption

### What Arrow Actually Is

- A specification for representing tabular data in column-oriented format in memory
- Describes exactly how to arrange bytes for columns of float64s, strings, lists of int32s, etc.
- Handles missing data with a bit mask overlaid on columns
- Tables consist of "record batches"—collections of columns with contiguous data (hundreds to millions of rows)
- Two protocols for data transfer:
  - **IPC format**: Columns arranged end-to-end with a small metadata prefix (using FlatBuffers); enables zero-copy deserialization
  - **C Data Interface**: A C struct any language can construct via CFFI; enables zero-copy data passing across C function call sites
- Key innovation: deserialization cost is proportional to number of columns, not dataset size
- DuckDB can execute queries against Arrow data with completely zero copy via pointer swizzling

### Arrow vs Parquet

- Arrow wasn't designed for storage; Parquet was designed for an era of slow disks (200-300 MB/s) and 10 gigabit networking
- Parquet uses multiple encoding passes: dictionary encoding, run-length encoding, null collapsing, plus general-purpose compression (Snappy, Zstandard, LZ4)
- Arrow has no encoding—completely rehydrated data with predictable random access
- Today's hardware is 10-100x faster; Parquet's decoding overhead is now the bottleneck, not I/O transfer
- Arrow was designed for hyper-parallel, GPU-enabled contexts where serialization overhead kills performance

### The Future of File Formats

#### Parquet's Limitations

- Struggles with wide schemas (working rule: handles ~1,000-10,000 columns okay, but ML feature engineering can generate millions)
- Metadata overhead is expensive—file footer uses Apache Thrift
- Lacks advanced encodings for modern SIMD/GPU processing
- Relies on general-purpose compression that's inefficient on GPUs
- Can't predict memory requirements for GPU pre-allocation (strings need exact byte counts)
- Poor support for multimodal data (images, vectors)
- Research from TU Munich and CWI shows similar compression with much better random access using only lightweight encodings

#### New Approaches

- Vortex and F3 projects propose bundling WebAssembly implementations of new encodings in files—not as fast as native, but ensures compatibility
- Forward compatibility affordances so older implementations can skip unrecognized features safely
- Lance and Vortex specifically designed for multimodal data and mutable datasets
- Iceberg and Delta Lake integrating bleeding-edge formats so you're not locked to Parquet

### The "Big Metadata" Problem

- Tweeted in July 2016: "Forget big data. Let's start talking about big metadata."
- Hive Metastore was among the first open metastores; for massive tables (like Netflix), metadata interaction could add minutes of query planning overhead
- Running Spark jobs on massive Parquet datasets meant launching a Spark job just to read file footers
- Led to Iceberg, Delta Lake, and Hoodie providing more scalable metadata storage
- DuckDB built "DuckLake" (neo-hive-metastore)—simpler alternative for modest data lakes, pushback against "Iceberg-ification of everything"

### Scalability and the "No JVM Movement"

- Referenced "Scalability, But at What Cost" paper (same year Arrow started)—big data systems achieve scalability with massive overheads
- Original 2004 MapReduce paper described servers with one processor core; what was "big data" for Google then is one cloud machine now
- A terabyte isn't big data anymore; many distributed systems simply aren't needed
- Current "no JVM movement" rebuilding everything in Rust/native code reacts to frustration with operational complexity

### The DataFusion Ecosystem

- Rust-based, configurable query engine; started as Andy Groves' personal project, folded into Apache Arrow, now its own Apache project
- Like DuckDB but more customizable; DuckDB is batteries-included like SQLite
- Used by: Influx Data (next-gen query engine), LanceDB, SpiralDB, Arroyo (acquired by Cloudflare, powers their SQL data lake), Cube, DBT Fusion, Five Tran/Census/SQL Mesh
- Andrew Lamb's vision: "a thousand DataFusion companies"—we're on track
- If you're building a Rust startup needing a query engine, there's no reason to build your own

### Claude Code and AI Coding

- What clicked: "YOLO mode" with unbridled terminal access to Git, GH CLI tools feels streamlined
- Effective for investigation loops—can loop 20-30 times diagnosing bugs, adding debugging, recompiling, running tests
- Great for chore work: commit messages, GitHub tasks, CI/CD and DevOps tasks
- Canceled Windsurf subscription after a month because Claude Code replaced it
- Biggest risk is prompt injection—determined attackers could hijack and exfiltrate SSH keys

### Concerns About AI and Open Source

- AI labs benefit from 15-20 years of open source code on GitHub, Stack Overflow; ChatGPT and Claude are good at pandas because of incredible training data
- OpenAI should sponsor pandas maintainers—they don't; AI companies are "strip-mining" intellectual property from open source
- Worry about junior developers with "existential dread"—if 95% of their work comes from agents, will they develop the judgment that comes from hands-on experience?
- Code used to teach lessons the hard way; unsupervised agents make "gigantic messes" claiming to solve problems
- LLMs hallucinate with full confidence claiming code is "bug-free, production-ready"

### LLMs and Data: Need for a Data Context Protocol

- LLMs aren't data models—they're language models that struggle with tabular data
- Stuffing Arrow data in context windows doesn't work well for retrieval or analysis questions
- LLMs rely on tool calling for meaningful data work
- MCP with JSON isn't the best interface; need something like a "data context protocol" or "agent data context protocol"
- Research shows LLMs just aren't good at data, even with best formatting approaches
- Invested in Columner (Arrow-native, accelerating ADBC ecosystem); ADBC makes sense as JDBC/ODBC successor

## Key Quotes

> "Why isn't there a standardized, efficient in-memory format for tabular data that's portable across languages? This seed became Arrow in 2013." — Wes McKinney

> "In Arrow, deserialization cost isn't proportional to dataset size. You receive data with transfer cost, but once in process memory, constructing an arrow structure referencing it costs only what's proportional to the number of columns—very small." — Wes McKinney

> "Parquet's design constraints from 15 years ago are obsolete. I/O bandwidth isn't the bottleneck anymore; decoding performance is." — Wes McKinney

> "Forget big data. Let's start talking about big metadata." — Wes McKinney (2016 tweet)

> "What was big data for Google is just one machine in the cloud. Many distributed systems simply aren't needed. A terabyte isn't big data anymore." — Wes McKinney

> "Andrew Lamb, DataFusion's de facto leader, wants to create a world where there are a thousand DataFusion companies. We're probably on track for that." — Wes McKinney

> "AI companies are strip-mining intellectual property created by open source community and humanity generally." — Wes McKinney

> "Someone from school with 95% work from agents won't acquire the same judgment. There needs to be new emphasis on code literacy, reading and analyzing code." — Wes McKinney

> "Unsupervised agents without feedback make gigantic messes claiming to solve problems, generating totally incorrect code or unit tests introducing mocks pretending correctness when logic is wrong." — Wes McKinney

> "LLMs hallucinate, sometimes generating incorrect responses with full confidence claiming bug-free, production-ready shipping. Claude Code tells me daily 'production grade'—I open it saying not quite, let's fix things." — Wes McKinney

> "General recognition: LLMs aren't data models—they're language models. Providing datasets—stuffing arrow data in context windows—doesn't get good results for retrieval or analysis questions." — Wes McKinney

## Transcript

**Kostas:** Hello everyone, here we are at another episode of Tech on the Rocks and we have a special guest today, Wes McKinney. Wes, welcome. How are you today? And please give us a quick intro of yourself.

**Wes McKinney:** Thanks for having me. Most people know me as the creator of the Python pandas project, but I've also worked on Apache Arrow where I'm a co-creator, the Ibis project for Python, and done work on Apache Parquet. I've been involved in helping build the Python data science ecosystem. I have a book called Python for Data Analysis in its third edition. I'm also an entrepreneur and investor—I started Datapad, then Voltron Data, working on Arrow and GPU-accelerated data processing. I'm currently a software architect at Posit, where I've worked on the Positron data science IDE, particularly the data explorer. I also run Compose Ventures, a small venture fund where I've been active as an angel investor in seed and pre-seed rounds. Investing has given me a way to advise and be useful to entrepreneurs and open source developers beyond just building myself.

**Kostas:** It's impressive—you're like a full stack engineer but at the systems level, which is rare. People usually focus intensely on one thing because these systems are complicated.

**Wes McKinney:** I started building pandas 17 years ago in 2008, initially focused on the user API and experience. I was frustrated with Excel and other languages. As time went on, I naturally had to learn more about the system side—how to make things fast, scalable, and memory efficient. That led to file formats, database connectivity, and other work. It's been incremental over a long period. We solve one problem, make sure others can maintain it, then identify the next bottleneck. Open source maintenance is still difficult, though AI coding agents have helped with CI/CD and DevOps tasks I didn't enjoy. Still, open source has sustainability challenges—where does the money come from? I've tried creating synergistic relationships between open source and business. Posit is one of the rare companies building a sustainable business while investing half their R&D into open source.

**Kostas:** That's a topic worth multiple episodes. I've seen companies struggle balancing open source and business—Starburst with Trino, Rutherstack with their open source projects. How did you transition from pandas to the next thing?

**Wes McKinney:** What came directly after pandas was Python for Data Analysis, first edition in 2012. Then Chang Shu and I started Datapad, a visual analytics company at the intersection of Jupyter notebooks and business intelligence—something like what Hex is today, but more primitive when web technology was less mature. We needed fast interactive analytics in a SaaS environment, but pandas couldn't deliver the speed we wanted. In 2013, DuckDB didn't exist. This forced me to reconsider pandas' whole design since it wasn't designed like a database for large datasets or parallel processing. I gave a talk called "Ten things I hate about pandas" at PyData New York in November 2013, noting that pandas wasn't designed as a database engine. It had rough edges from relationships with NumPy, which was designed for numerical processing, not analytics. NumPy lacked good support for strings, non-numeric data, and structured types. While working on Datapad, I built a C library implementing a miniature query engine—a very primitive DuckDB version for cloud environments with data stored in S3. I created a file format similar to Arrow called Proto Arrow stored in S3. This led me to think: why isn't there a standardized, efficient in-memory format for tabular data that's portable across languages? This seed became Arrow in 2013. Datapad faced challenges—Looker dominated business intelligence in 2013-2014, making continued startup growth difficult. We found an opportune exit to Cloudera at the end of 2014. There I interacted with the Impala team building distributed data warehouses and the Kudu team building columnar storage supporting fast analytics and transactions. Coming from the Datapad experience wanting to redesign pandas internals more efficiently, it was the perfect environment to kick off Arrow. At the end of 2014, I began designing proto-Arrow as something Impala or Kudu could use for data transfer. Simultaneously, I wanted to decouple the data frame API from the compute engine, so I started building Ibis, a ten-year-old project now fairly mature with surprising use. I had two ideas: decoupling API from compute and storage, and creating an interoperable memory format for columnar data. The columnar project resonated more with the open source ecosystem and became ubiquitous. I've spent the last ten years making that happen, building technology and creating environments where people can be productive.

**Kostas:** Regarding Arrow, can you help us understand what Arrow is? How's it different from Parquet or ORC? And why is this decoupling important?

**Wes McKinney:** Arrow is multiple things. It started as a specification for representing tabular data in column-oriented format in memory, without concern for storage or interoperability. It describes exactly how to physically arrange bytes to represent a table at the individual column level—what a column of float64 values, strings, or lists of int32s looks like. It handles missing data with a bit mask—a separate memory chunk overlaid on a column. A group of named columns with types creates a schema, defining a table chunk. A table consists of record batches—collections of columns with contiguous data representing physical columns. Batches might be hundreds, thousands, or millions of rows. The idea is facilitating chunked data movement between processes, languages, and systems efficiently. We defined protocols for relocating data between processes in two modalities. One is the IPC (interprocess communication) format, arranging columns end-to-end like dominoes with a small metadata prefix. When received, you examine the prefix for byte offsets of memory buffers needed to reconstruct the batch without further copying or conversion. This enables zero-copy deserialization—you receive data over a socket, HTTP, or similar, pop it off your interface, look at the metadata prefix, and create an object with pointer offsets to memory locations, giving you a tabular view without moving every value into a different data structure. Compared with traditional database drivers, this is more efficient. Reading from Postgres, you'd receive SQL query data and immediately relocate all bytes into application-specific structures—expensive work proportional to dataset size. In Arrow, deserialization cost isn't proportional to dataset size. You receive data with transfer cost, but once in process memory, constructing an arrow structure referencing it costs only what's proportional to the number of columns—very small. There's also the C data interface, a C struct almost all languages can construct through CFFI or C function calling. This enables arrow data relocation across C function call sites without code sharing, only needing C headers. You can pass arrow data over C function calls without copying—DuckDB can execute queries against in-memory datasets with completely zero copy. DuckDB's internal pointer swizzling scans arrow data directly with minimal overhead.

**Nitay:** This is really cool—the native buffer swizzling work is amazing.

**Wes McKinney:** Each language's Arrow implementation has slightly different mechanics. Rust has unsafe pointer issues, so there are two Rust implementations—one allowing unsafe, another (Arrow2) being unsafe-free but less actively maintained. The metadata prefix uses Flat Buffers, minimizing even the metadata packet cost. If you send a payload with millions of columns, you aren't adding unnecessary overhead just examining structural information. Even Java, with complicated unsafe memory relationships, manages this. The C data interface, leveraging C function calling abilities available to most languages, lets people relocate arrow data structures across C function sites. For example, from Rust or Go to DuckDB, you can pass arrow data without copying. DuckDB's pointer swizzling scans arrow data directly with minimal overhead, though DuckDB's memory representation differs slightly from Arrow due to optimizations, but works well with Arrow with minimal overhead in embedded contexts.

**Kostas:** We have columnar data in Arrow, efficiently representing it in memory and transferring it with minimal cost. Parquet is another columnar format for disk storage. What's the difference? Why handle columnar data differently in storage versus memory?

**Wes McKinney:** Arrow wasn't designed for storage. When storing parquet, data goes through multiple encoding passes. Dictionary encoding works well for data with few unique values—you determine unique values and replace occurrences with integers referring to the dictionary, storing unique values once. Dictionary indices are further encoded with run-length encoding. Null values are collapsed. If a million-value column has only one non-null value, storage might be just tens of bytes. But decoding a parquet file requires expanding and rehydrating data to fit application data structures—multiple encoding passes create encoded columns, usually with general-purpose compression on top (Snappy, Zstandard, or LZ4). Reading parquet requires significant decoding and decompression. Parquet was created around 2011-2012 as a Twitter and Cloudera collaboration when spinning hard drives read 200-300 MB/second and networking was 10 gigabit, maybe terabit elsewhere. There was heavy focus on making files as compact as possible. Benefits of reduced transfer cost far outweighed decoding costs. Arrow has no encoding—completely rehydrated data. If you have int32s with nulls, four zero bytes replace nulls, enabling predictable random access. Arrow wasn't designed for storage compactness. We added general-purpose compression as a nice-to-have, not replacing parquet. Arrow was designed for a different era where disks are 10-100X faster and networking 10-100X or 1000X faster. Parquet's design constraints from 15 years ago are obsolete. I/O bandwidth isn't the bottleneck anymore; decoding performance is. Arrow was designed for hyper-parallel, GPU-enabled server contexts with minimal deserialization. Extra serialization would kill performance. We still need file formats. Replacing parquet with arrow company-wide would be problematic—arrow is too big on disk. There are applications where I/O bandwidth still matters, particularly GPU clusters where parquet decoding on GPU creates new complications that next-generation file formats address.

**Nitay:** What's the future of file formats? It seems like a never-ending problem—you think you've solved it, but resource constraints and workload bottlenecks shift.

**Wes McKinney:** Parquet is sticky; people just discovered it and started using it recently. Machine learning and AI papers use parquet for binary columnar format. People uncomfortable with parquet suddenly hearing we need new file formats might think "what the heck?" But parquet has challenges. It struggles with very large wide schemas—the working rule is parquet handles maybe a thousand to ten thousand columns okay, but overhead of interacting with parquet metadata—the file footer with structural information encoded in Apache Thrift—can be expensive, especially with wide schemas. Another problem is parquet lacks advanced encodings. Considering SIMD advances, multi-core systems, and GPUs, Parquet's encoding passes aren't advanced enough. It relies on general-purpose compression, not efficient to decompress on modern CPUs or GPUs. Design flaws include insufficient memory requirement predictability information. On CPUs this matters less, but as processing moves to GPUs, lacking pre-allocation hints in parquet files makes GPU decompression less efficient. You'd need exactly-sized byte knowledge for string expansion to reserve GPU memory efficiently. Without it, multiple decompression passes are necessary. Research from TU Munich, CWI (where DuckDB was created) shows you can achieve similar parquet compression levels with much better random access using only lightweight encodings without general-purpose compression. Research shows vastly greater decoding performance. The metadata problem means ideally a file format handles millions of columns, efficiently pulling ten from a million. Parquet struggles here. Machine learning datasets generate millions or tens of millions of columns through feature engineering, sometimes requiring storage. File formats not handling wide datasets are problematic. Additionally, parquet isn't good at multimodal data like images and vectors. Considering metadata, wide schemas, deserialization overhead, encoding performance, general-purpose compression, multimodal storage, and random access, building large data platforms at companies like Meta, Google, or Microsoft can measure data retrieval and deserialization costs. Continuing parquet use has material costs at large scale. This motivates new file formats without these limitations, more efficient to decode.

**Kostas:** It's clear why rethinking data storage is needed. Hardware changes and workload bottlenecks shift. These things are sticky—parquet isn't easy to replace. How do we make file formats future-proof so we don't wait another fifteen years for new designs?

**Wes McKinney:** One key thing is not repeating parquet's implementation fragmentation. Many parquet implementations exist across systems. New features and encodings were bolted on but not implemented consistently everywhere. Spark supported some features, not others. This fragmentation disincentivized implementing new bleeding-edge parquet features if you couldn't confidently make files interoperable with Spark. New encodings would create unreadable files elsewhere. One idea from Vortex and F3 projects is shipping new encodings or features implemented in WebAssembly, bundled in files. If an implementation encounters new encodings it doesn't know, it finds a bundled WebAssembly implementation. Not the most efficient compared to native code, but at least you have an implementation for compatibility—avoiding a situation where you receive unreadable files. Other metadata affordances can enable forward compatibility—if an older implementation receives a newer file, it can recognize unrecognized features and skip them safely, or error out. We don't want receiving files (especially untrusted user uploads) to cause crashes from unrecognized features. We've learned from parquet. Parquet is still improving. New file format projects have rejuvenated parquet development—there's great improvement in parquet performance in Data Fusion Rust implementations, motivated by "parquet can be much better." There's discussion of parquet 3.0. There's awkwardness around parquet 2.0 understanding. Healthy community dialogue exists, especially with open data lakes, Iceberg, and Delta Lake. Work integrates bleeding-edge file formats into Iceberg so you aren't forced to only use Parquet. In controlled environments with known generated files, you can safely choose the format making most sense for your application and computing engines. Building large data centers or cloud platforms with petabytes of data, why not choose the best-fitting file format? Multimodal datasets—images, videos, vectors—are ideal in formats like Lance and Vortex, specifically developed for better support. There's also the ability to modify datasets, add columns, and such.

**Kostas:** One last question—metadata complexity keeps coming up. Managing metadata across the whole stack sounds interesting. At what point does it become a problem or bottleneck? These table formats add metadata too. How does metadata interact across systems? Databases like Postgres handle this internally; we don't worry about encoding or paging. With data lakes and disaggregation between systems, people must get into details of each part. Tell me about metadata management.

**Wes McKinney:** I had a tweet from July 2016 that said "forget big data. Let's start talking about big metadata." I was joking, but it's real. The Hive Metastore was among the first open metastores facilitating multi-engine data access in distributed storage or HDFS. People found that for massive datasets like Netflix, interacting with metadata for really large, slow-moving tables could add minutes of planning overhead running queries. Another problem: running Spark jobs on massive parquet datasets meant launching a Spark job just to examine file metadata. That alone was significant computation just reading parquet file footers and considering what's in files—schema evolution, which columns you reference. You'd need to plan fetching specific byte ranges from all files in attached or cloud storage. Planning what data needs reading and deserialization could have massive overhead. This led to projects like Iceberg, Delta Lake, and Hoodie, providing more scalable metadata storage than Hive, designed for efficient metadata queries, enabling large-scale query planning and execution. Funny thing: Iceberg proliferation might be overkill for many data lakes. DuckDB recently built neo-hive-metastore—a way to store metadata in real databases, not flat parquet files in cloud storage, designed for modest data lakes, simpler and easier than Iceberg. It's called DuckLake—some pushback against "Iceberg-ification of everything," partly from DuckDB team frustration implementing all Iceberg features. The big metadata problem is real. I haven't done Iceberg development, but I know the team. It's there. The investment from the tech ecosystem is substantial. All major hyperscalers like AWS and Microsoft make massive investments because if you're managing people's data, collecting taxes on every petabyte stored is very profitable.

**Nitay:** Metadata catalogs started as basic Hive Metastores pointing to files. Over time, they're trying to do much more—hosting model catalogs, pointing to embeddings and multimodal data. What's the future? Also, I recall a research paper showing most workloads run faster on single machines, even single CPUs.

**Wes McKinney:** Yes—"Scalability, But at What Cost," written the same year we started Arrow. Frank McSherry and Microsoft Research folks found that big data systems achieve scalability with massive overheads. That line changes and tends to move opposite to expected directions.

**Nitay:** I found particularly interesting that even regardless of clock speeds, single CPUs handle more, just from distributed system overhead, and that line isn't fixed.

**Wes McKinney:** Interesting now, with the "no JVM movement," rebuilding everything in Rust or native code, everything should be easy to deploy—static binaries without bloated complexity. I think much happening now reacts to frustration with operational complexity and inefficiency. Recent talks mention the "computing hierarchy of needs." People focused on scaling; efficiency and operational ease were secondary. What's crazy—the original 2004 MapReduce paper described servers with one processor core. Now what was big data for Google is just one machine in the cloud. Many distributed systems simply aren't needed. Big data compared with twenty years ago has changed by thousand X. A terabyte isn't big data anymore.

**Nitay:** Fascinating. I want to shift gears slightly. You mentioned DataFusion and related Arrow ecosystem projects—DataFusion, Flight, ADBC. Give us a picture of the broader ecosystem and where it's moving.

**Wes McKinney:** DataFusion is a Rust-based, configurable, customizable query engine starting as Andy Groves' personal project, eventually folded into the Apache Arrow project. Think of it as slightly like DuckDB—more customizable and adaptable to specialized query processing systems. DuckDB is more batteries-included, like SQLite—drop it in as one gigantic C file. DataFusion is designed for customization. It's used by Influx Data's next-generation query engine and dozens of startups—LanceDB (Lance file format creator), SpiralDB (Vortex creator)—all using DataFusion. The community grew large enough to split from Arrow, creating Apache DataFusion with a growing community. It's cool—if you're building a Rust startup wanting a query engine, there's no motivation creating your own. Use DataFusion. It's meant to be picked up and customized for free. Example: Arroyo built a streaming SQL engine, got acquired by Cloudflare, now powering Cloudflare's SQL data lake offering, all using DataFusion. That's the intended use case. DataFusion is Arrow-native, written in Rust, accelerating the baseline platform for building new data processing solutions. Fifteen years ago, startups needed to build whole query engines from scratch. Now using DataFusion is a no-brainer for Rust work. It's exactly what we wanted.

**Kostas:** DataFusion's beauty is modularity—usually databases are monoliths where everything's super connected, changes are brittle. DataFusion's architecture lets you innovate where you want, take other parts off-the-shelf. Arroyo focused on streaming efficiency. DuckLake rebuilt everything in Rust. Everyone except Looker struggled in 2013-2014 business intelligence. Cube uses DataFusion for materialization and casting layers, taking non-IP parts off-the-shelf, building their stuff. DBT Fusion, the next DBT generation, uses DataFusion. Five Tran, Census, SQL Mesh are one company now. DataFusion and Arrow are central to enterprise data transformation.

**Wes McKinney:** Yeah, George Fraser from Five Tran is a professed Arrow fan. That being at the center of enterprise data transformation is really cool. Andrew Lamb, DataFusion's de facto leader, wants creating a world where there are a thousand DataFusion companies. We're probably on track for that.

**Nitay:** I've always believed in open source infrastructure—given a long timeline, open source always wins.

**Wes McKinney:** But not without blood, sweat, and tears. Huge bumps, roller coasters, unfortunate projects, unfortunate politics, companies trying to take over—Hollywood-level drama. Eventually open source wins.

**Nitay:** These data infrastructure projects like Arrow and DataFusion are among the most "AI resistant" technologies. Yes, you can use AI and agents coding more productively. But like, I don't see AI building projects like DataFusion autonomously anytime soon. Development will become more efficient and features faster with AI-assisted refactoring, handwritten kernel refactoring, and unit tests. But this domain needs smart people focused on it, collaborating to build solutions powering the next 20-30 years of data systems.

**Kostas:** One quick question—what about Claude Code is different from other IDEs that clicked for you?

**Wes McKinney:** I think because of what Simon Willison calls YOLO mode—dangerously skipping permissions—having unbridled access in a terminal environment to Git, GH CLI tools feels streamlined. I can watch it work, see what it's investigating. Sometimes I see it going down a dark path and hit escape saying no, that's not right. Here's the right approach. It's effective in loops investigating bugs or unit test failures. I can investigate, search, add debugging, recompile, run tests—it might loop twenty-thirty times diagnosing problems. I used Windsurf previously, canceled my subscription after a month with Claude Code because I wasn't using Windsurf anymore.

**Nitay:** I've seen people do full YOLO—sudo, do whatever—in codespace or Docker where you can blow away the entire machine. Let it run an hour implementing the whole thing autonomously.

**Wes McKinney:** Simon Willison gave a talk about sandboxing, running Claude Code inside Docker containers. There's a sandbox flag enabling pseudo and everything. I haven't done that sophistication, though I should—I probably expose myself to prompt injection risks half the time. I haven't seen Claude Code do anything uncomfortable on my side project, except once deleting my config directory without asking. Beyond that, very rarely have I seen safety issues. Prompt injection is biggest risk—determined attackers could hijack it, sending home directory contents, SSH keys—"keys to the kingdom." Very bad.

**Kostas:** What about open source maintainer burden with AI-generating PRs now?

**Wes McKinney:** Fortunately I'm not actively maintaining open source projects. People maintaining Arrow report increased submissions. They ask disclosing whether PRs are AI-assisted or fully AI-generated, creating maintainer burden. Bigger issue: AI labs benefit from fifteen-twenty years of open source code on GitHub, Stack Overflow. ChatGPT and Claude are good at pandas because there's incredible training data for pandas. You'd think OpenAI would sponsor maintainers supporting pandas. They don't. Essentially AI companies are strip-mining intellectual property created by open source community and humanity generally. Maybe AI becomes sophisticated enough generating next-generation libraries and training data continuing self-improvement. I don't know. Eventually the well might run more dry or hit limits—almost all internet code is AI-generated. The snake eats its tail. What happens to quality then? Another challenge: AI-induced laziness—people stopping solving problems their agents can't, limiting progress on new ideas. I'm happy Claude Code exists, making me productive. I'm fearful for future, especially junior developers with existential dread about jobs graduating. If people don't learn software development the old-fashioned way, will they acquire experience becoming senior principal engineers? I'm relying on twenty years software engineering experience giving Claude Code feedback judging its work. Someone from school with 95% work from agents won't acquire the same judgment. There needs new emphasis on code literacy, reading and analyzing code. Code used to teach lessons the hard way—building tangled, complicated software, learning design patterns, model-view-controller through refactoring and mess. Unsupervised agents without feedback make gigantic messes claiming solving problems, generating totally incorrect code or unit tests introducing mocks pretending correctness when logic is wrong. It's a minefield. LLMs hallucinate, sometimes generating incorrect responses with full confidence claiming bug-free, production-ready shipping. Claude Code tells me daily production grade—I open it saying not quite, let's fix things.

**Nitay:** I analogized early big data—to achieve scale, you forgo given standards—transactions, consistency. Same happening now—software must be consistent. Developers coming of age used to systems hallucinating, inconsistent, or down sometimes. That's how things are. We OGs think that's not how building systems works. Every technical breakthrough has disruptive capabilities but foregoes other stuff. Eventually people fix forgone things while keeping capability. NewSQL brought transactions back. I'm optimistic AI will retain productivity magic while getting to quality standards eventually.

**Wes McKinney:** Maybe not million, but bringing expectations to planet Earth—feet on ground—viewing LLMs as tools enhancing human productivity versus one great leap for mankind. I'm definitely optimistic about individual productivity impact and leverage for work, delegating mundane stuff bogging you down past. Chore work is prime AI work. Commit messages, GitHub chores—probably future AI work. There's still need for humans in loop, probably fewer humans. Less confident about mass unemployment narratives around coding agents.

**Nitay:** This has been fantastic. Summarizing—the data infrastructure space, resource changes, new file format needs—what's one top feature request you'd want the ecosystem working on?

**Wes McKinney:** Definitely under-investment bridging AI and current LLMs with data itself. General recognition LLMs aren't data models—they're language models. Providing datasets—stuffing arrow data in context windows—doesn't get good results for retrieval or analysis questions. LLMs rely on tool calling for meaningful data work. That needs work. How do we show LLMs tabular data, getting meaningful results? Some startups work on that. I'm advisor and investor in Columner, doing Arrow-native, accelerating ADBC ecosystem. It's an AI-resistant technology—everybody needs efficient database connection, simpler, faster. ADBC makes sense as JDBC and ODBC successor. There's MCP, JSON—not the best interface hooking LLMs to data. Maybe we need data context protocol or agent data context protocol more efficient, helping resolve general problems LLMs facing data. Research shows they just aren't good at it. Even formatting data—even the best approaches struggle.

**Nitay:** Relationships, types, underlying formulas between datasets—something needs different thinking than just token sequences from language perspective. Data-oriented MCP or similar standard sounds great. I'd love seeing that.

**Wes McKinney:** Absolutely.

**Nitay:** We'll wrap here, but not the end. We'd love having you continue conversations. Thank you for this great episode. I really enjoyed the conversation and thank you for your contributions. I personally use many of your projects and love them. Looking forward to continuing.

**Wes McKinney:** Great. Thanks for having me on.