---
title: "Ursa Labs February 2019 Report"
date: 2019-03-06T00:00:00
tags: ["ursa labs", "work"]
slug: ursa-labs-february-2019
word_count: 2034
source_file: blog/ursa-labs-february-2019/index.qmd
content_type: blog
---

The team had a busy 28 days this February. The Apache Arrow community is
discussing a 0.13 release toward the end of March, so we spent February helping
the project toward the next release milestone. We have been pushing projects on
multiple fronts and discuss some of those here.

The [Apache Arrow project just had its 3rd birthday][244], and we are pleased
to report that the community is thriving and growing fast after only a short
time as a top-level project in The Apache Software Foundation. We're really
looking forward to what the next few years will bring as the Arrow columnar
format and cross-language development platform becomes even more widely
adopted.

## Open Roles in the Team

We have open roles in the team for an [Engineering Manager][1] and [Senior
Software Engineer][2]. Ursa Labs is a rare opportunity to spend 100% of your
time on an ambitious and wide-reaching open source systems project. These are
full-time remote roles, so if you live in NYC or the Bay Area and would like to
move somewhere else ([I think Nashville is pretty great][3]) this could be your
chance.

## Sponsor Acknowledgements

We are grateful to the support of our sponsors:

* RStudio
* NVIDIA AI Lab
* ODSC Conference
* Two Sigma Investments

If you or your company would be interested in sponsoring the work of Ursa Labs,
please contact us at **info@ursalabs.org**.

## Development Highlights

One significant project not represented in the Apache Arrow open source project
is setting up a **physical build and test cluster** for Ursa Labs. NVIDIA has
provided us two DGX stations and a Jetson TX2 (Aarch64-based computer). To this
we have added a 2018 Mac Mini and will continue to add machines as needed. This
build cluster will be used for nightly tests and packaging builds as well as
performance benchmarking. The Arrow community has been discussion public daily
performance benchmarking and there is a [new SQL schema][243] for a proposed
benchmark database.

In Apache Arrow, we have been working in several areas:

* **Line-delimited JSON reader**: [an initial C++ implementation][197] of
  reading JSON files to the Arrow columnar format. We have more work to do
  here, but this work will form the basis of utilizing directories of JSON
  files as a data source for in-memory query processing
* **Arrow Flight, a new RPC / messaging system**: we have been collaborating
  with Two Sigma, one of our gracious sponsors, and Dremio on the development
  of this new gRPC-based Arrow-native messaging framework. We believe this will
  form the backbone of future distributed systems powered by Apache Arrow.
* **C++ Arrow Dataset Framework**: we have [proposed a general purpose C++
  framework][242] for interacting with large datasets stored in a number of
  different formats. This is an essential component for general-purpose
  in-memory query processing. This work will replace and generalize some of the
  pure Python code we have already for `pyarrow.parquet.ParquetDataset`
* **Computational Kernels**: to lay the foundations for an Arrow-native
  in-memory query engine, we have been implementing aggregation functions to
  enable parallel aggregation of Arrow datasets
* **Gandiva testing and packaging support**: we are working diligent to make it
  possible to ship Gandiva, our LLVM-based expression compiler (for
  projections and filters), in various package artifacts including Python
  wheels and conda packages
* **User-defined Extension Types in C++**: we have [proposed an initial C++
  API][218] for defining custom data types in C++ (eventually for Python,
  too) that are backed by one of the one of the built-in Arrow columnar data types
* **LLVM 7 migration**: we have upgraded the project, including the Gandiva, to
  use the stable LLVM 7 version

## Upcoming Focus Areas

In March one of our main priorities will be working with the Arrow community to
get the 0.13 release out the door. We will be focusing in several areas to
follow on with the above:

* Getting our build cluster up and running, to help make Arrow developers more
  productive, and helping set up automated daily performance benchmarks with
  the Arrow community
* Working toward getting initial Arrow Flight support into our packages (like
  conda packages and Python wheels)
* Continuing to develop and improve our computational kernels
* New data type additions to the Arrow format: the community is discussing a
  new-and-improved timedelta or interval type, as well as a "packed C struct"
  data type. We are interested in helping implement these new data types. See
  the Arrow developer mailing list for more

## Team Changelog

The team had 68 commits merged into Apache Arrow in February 2019. You can
click on the ASF JIRA links to learn more about the discussion on a particular
issue or the commit hash to see each patch.

(Note of the patches from early in the month have "February 8" commit date due
to a rebase)

* 2019-02-08: [ARROW-4431][101]: [C++] Fixes for gRPC vendored builds ([5d742d][102] by [wesm][100])
* 2019-02-08: [ARROW-4446][103]: [C++][Python] Run Gandiva C++ unit tests in Appveyor, get build and tests working in Python ([2b9155][104] by [wesm][100])
* 2019-02-08: [ARROW-4500][105]: [C++] Remove pthread / librt hacks causing linking issues in some Linux environments ([6f60e3][106] by [wesm][100])
* 2019-02-08: [ARROW-3606][107]: [Crossbow] Fix flake8 crossbow warnings ([5ad1ed][108] by [wesm][100])
* 2019-02-08: [ARROW-3422][109]: [C++] Uniformly add ExternalProject builds to the toolchain" target. Fix gRPC EP build on Linux" ([4c6e1c][110] by [wesm][100])
* 2019-02-08: [ARROW-3903][112]: [Python] Random array generator for Arrow conversion and Parquet testing ([d06c66][113] by [kszucs][111])
* 2019-02-08: [ARROW-3972][114]: [C++] Migrate to LLVM 7. Add option to disable using ld.gold ([40cfbc][115] by [wesm][100])
* 2019-02-08: [ARROW-4430][117]: [C++] Fix untested TypedByteBuffer<T>::Append method ([4a80fd][118] by [bkietz][116])
* 2019-02-08: [ARROW-4472][119]: [Website][Python] Blog post about string memory use work in Arrow 0.12 ([308c0d][120] by [wesm][100])
* 2019-02-08: [PARQUET-1521][121]: [C++] Use pure virtual interfaces for parquet::TypedColumnWriter, remove use of 'extern template class' ([490c6b][122] by [wesm][100])
* 2019-02-08: [ARROW-3239][124]: [C++] Implement simple random array generation ([fb23ed][125] by [fsaintjacques][123])
* 2019-02-08: [ARROW-4440][126]: [C++] Revert recent changes to flatbuffers EP causing flakiness ([b117a8][127] by [wesm][100])
* 2019-02-08: [ARROW-4469][128]: [CI] Pin conda-forge binutils version to 2.31 for now ([04ad21][129] by [wesm][100])
* 2019-02-08: [ARROW-3846][130]: [Gandiva][C++] Build Gandiva C++ libraries and get unit tests passing on Windows ([5232a4][131] by [wesm][100])
* 2019-02-08: [Website] Edits to Python string blog post ([65f37f][132] by [wesm][100])
* 2019-02-09: [ARROW-4124][133]: [C++] Draft Aggregate and Sum kernels ([9a10ba][134] by [fsaintjacques][123])
* 2019-02-11: [ARROW-4499][135]: [CI] Unpin flake8 in lint script, fix warnings in dev/ ([9db7a6][136] by [wesm][100])
* 2019-02-11: [ARROW-4498][138]: [Plasma] Fix building Plasma with CUDA enabled ([18f9e6][139] by [pitrou][137])
* 2019-02-11: [ARROW-3631][140]: [C#] Add Appveyor configuration ([62dd09][141] by [wesm][100])
* 2019-02-11: [ARROW-4434][142]: [Python] Allow creating trivial StructArray ([6b78fb][143] by [pitrou][137])
* 2019-02-11: [ARROW-331][144]: [Doc] Add statement about Python 2.7 compatibility ([4cf1c7][145] by [pitrou][137])
* 2019-02-11: [ARROW-4457][146]: [Python] Allow creating Decimal array from Python ints ([1d72a8][147] by [pitrou][137])
* 2019-02-11: [ARROW-4363][148]: [CI] [C++] Add CMake format checks ([fc7977][149] by [pitrou][137])
* 2019-02-12: [ARROW-4481][150]: [Website] Remove generated specification docs from site after docs migration ([b31845][151] by [wesm][100])
* 2019-02-12: [ARROW-4181][152]: [Python] Fixes for Numpy struct array conversion ([a5d8cc][153] by [pitrou][137])
* 2019-02-12: [ARROW-3292][154]: [C++] Test Flight RPC in Travis CI ([af60c2][155] by [pitrou][137])
* 2019-02-13: [ARROW-47][156]: [C++] Preliminary arrow::Scalar object model ([d831e2][157] by [wesm][100])
* 2019-02-13: [ARROW-4558][158]: [C++][Flight] Implement gRPC customizations without UB ([69d595][159] by [wesm][100])
* 2019-02-14: [ARROW-4340][160]: [C++][CI] Build IWYU for LLVM 7 in iwyu docker-compose job ([2571b0][161] by [fsaintjacques][123])
* 2019-02-14: [ARROW-4563][162]: [Python] Validate decimal128() precision input ([b9819e][163] by [pitrou][137])
* 2019-02-14: [ARROW-1896][164]: [C++] Do not allocate memory inside CastKernel. Clean up template instantiation to not generate dead identity cast code ([47ebb1][165] by [wesm][100])
* 2019-02-15: [ARROW-4529][166]: [C++] Add test for BitUtil::RoundDown ([10e894][167] by [fsaintjacques][123])
* 2019-02-15: [ARROW-4576][168]: [Python] Fix error during benchmarks ([bf138a][169] by [pitrou][137])
* 2019-02-15: [ARROW-3669][170]: [Python] Raise error on Numpy byte-swapped array ([40b0c8][171] by [pitrou][137])
* 2019-02-16: [ARROW-4341][172]: [C++] Refactor Primitive builders and BooleanBuilder to use TypedBufferBuilder<T> ([bbca71][173] by [bkietz][116])
* 2019-02-18: [ARROW-4546][174]: Update LICENSE.txt with parquet-cpp licenses ([d0d810][175] by [fsaintjacques][123])
* 2019-02-18: [ARROW-4531][176]: [C++] Support slices for SumKernel ([568004][177] by [fsaintjacques][123])
* 2019-02-18: [ARROW-4565][179]: [R] Fix decimal record batches with no null values ([aeb40e][180] by [javierluraschi][178])
* 2019-02-18: [ARROW-4420][181]: [INTEGRATION] Make spark integration test pass and test against spark's master branch ([76979c][182] by [kszucs][111])
* 2019-02-19: [ARROW-4624][183]: [C++] Fix building benchmarks ([707bac][184] by [pitrou][137])
* 2019-02-19: [ARROW-4347][185]: [CI][Python] Also run Python builds when Java affected. ([6fd507][186] by [wesm][100])
* 2019-02-19: [ARROW-4623][188]: [R] update Rcpp version ([bd5770][189] by [romainfrancois][187])
* 2019-02-19: [ARROW-4618][190]: [Docker] Makefile to build dependent docker images ([ef28f2][191] by [kszucs][111])
* 2019-02-19: [ARROW-4581][192]: [C++] Do not require googletest_ep or gbenchmark_ep for library targets ([09cfd4][193] by [wesm][100])
* 2019-02-20: [ARROW-4562][194]: [C++] Avoid copies when serializing Flight data ([6c4118][195] by [pitrou][137])
* 2019-02-20: [ARROW-694][196]: [C++] Initial parser interface for reading JSON into RecordBatches ([9c19bb][197] by [bkietz][116])
* 2019-02-20: [ARROW-3532][198]: [Python] Emit warning when looking up for duplicate struct or schema fields ([d3c5b8][199] by [pitrou][137])
* 2019-02-21: [ARROW-4559][200]: [Python] Allow Parquet files with special characters in their names ([671140][201] by [pitrou][137])
* 2019-02-21: [ARROW-3981][202]: [C++] Rename json.h ([a97725][203] by [pitrou][137])
* 2019-02-21: [ARROW-4372][204]: [C++] Embed precompiled bitcode in the gandiva library ([e8cc48][205] by [kszucs][111])
* 2019-02-21: [ARROW-3985][206]: [C++] Let ccache preserve comments ([345b09][207] by [pitrou][137])
* 2019-02-22: [ARROW-4654][208]: [C++] Explicit flight.cc source dependencies ([25b566][209] by [fsaintjacques][123])
* 2019-02-22: [ARROW-4643][210]: [C++] Force compiler diagnostic colors ([981460][211] by [fsaintjacques][123])
* 2019-02-23: [ARROW-4659][212]: [CI] ubuntu/debian nightlies fail because of missing gandiva files ([48f7b3][213] by [kszucs][111])
* 2019-02-25: [ARROW-4638][214]: [R] install instructions using brew ([1b78eb][215] by [romainfrancois][187])
* 2019-02-25: [ARROW-4192][216]: [CI] Fix broken dev/run_docker_compose.sh script ([a9a766][217] by [fsaintjacques][123])
* 2019-02-25: [ARROW-585][218]: [C++] Experimental public API for user-defined extension types and arrays ([a79cc8][219] by [wesm][100])
* 2019-02-26: [ARROW-4641][220]: [C++][Flight] Suppress strict aliasing warnings from unsafe" casts in client.cc" ([49f1ff][221] by [wesm][100])
* 2019-02-26: [ARROW-4520][222]: [C++] use voidified expr to ignore DCHECK() custom messages in NDEBUG ([37d9d3][223] by [bkietz][116])
* 2019-02-26: [ARROW-3816][224]: [R] nrow.RecordBatch method ([41fc38][225] by [romainfrancois][187])
* 2019-02-27: [ARROW-2392][226]: [C++] Check schema compatibility when writing a RecordBatch ([4a084b][227] by [pitrou][137])
* 2019-02-27: [ARROW-4672][228]: [CI] Fix clang-7 build entry ([e648a7][229] by [fsaintjacques][123])
* 2019-02-27: [ARROW-4657][230]: Don't build benchmarks in release verify script ([b3f3db][231] by [fsaintjacques][123])
* 2019-02-27: [ARROW-3361][232]: [R] Also run cpplint on Rcpp source files ([d092dd][233] by [wesm][100])
* 2019-02-27: [ARROW-4560][234]: [R] array() needs to take single input, not ... ([2a14c7][235] by [romainfrancois][187])
* 2019-02-27: [ARROW-2627][236]: [Python] Add option to pass memory_map argument to ParquetDataset ([f2fb02][237] by [wesm][100])
* 2019-02-27: [ARROW-3121][238]: [C++] Mean aggregate kernel ([29aa92][239] by [fsaintjacques][123])
* 2019-02-28: [ARROW-4687][240]: [Python] Stop Flight server on incoming signals ([05ce0a][241] by [pitrou][137])

[100]: https://github.com/wesm
[101]: https://issues.apache.org/jira/browse/ARROW-4431
[102]: https://github.com/apache/arrow/commit/5d742dd52a59803ba2d0cfb0fa4f886d41e7a8fa
[103]: https://issues.apache.org/jira/browse/ARROW-4446
[104]: https://github.com/apache/arrow/commit/2b9155a3f0ab5c8b15986aa683dcdcbeeec967ff
[105]: https://issues.apache.org/jira/browse/ARROW-4500
[106]: https://github.com/apache/arrow/commit/6f60e3fb441c97e45ee3bd808a2070509f20d884
[107]: https://issues.apache.org/jira/browse/ARROW-3606
[108]: https://github.com/apache/arrow/commit/5ad1ed880dda4677005c7a6cf920f972d219a1a2
[109]: https://issues.apache.org/jira/browse/ARROW-3422
[110]: https://github.com/apache/arrow/commit/4c6e1c8e4a6c18c23ea3d676bc507d2eb22210be
[111]: https://github.com/kszucs
[112]: https://issues.apache.org/jira/browse/ARROW-3903
[113]: https://github.com/apache/arrow/commit/d06c664a1966da682a2382e46fe148be96cca1aa
[114]: https://issues.apache.org/jira/browse/ARROW-3972
[115]: https://github.com/apache/arrow/commit/40cfbcabaab13300dd143f966416dedb4bbf93e5
[116]: https://github.com/bkietz
[117]: https://issues.apache.org/jira/browse/ARROW-4430
[118]: https://github.com/apache/arrow/commit/4a80fd970eba66a37090150bc282b4aa35bff451
[119]: https://issues.apache.org/jira/browse/ARROW-4472
[120]: https://github.com/apache/arrow/commit/308c0db86d325133267e68075e5a3411a25dd5e1
[121]: https://issues.apache.org/jira/browse/PARQUET-1521
[122]: https://github.com/apache/arrow/commit/490c6b8c746cc7fcfe71bfcc7a284932ff9ae25d
[123]: https://github.com/fsaintjacques
[124]: https://issues.apache.org/jira/browse/ARROW-3239
[125]: https://github.com/apache/arrow/commit/fb23ed8db5c48ea4b3b9bc062bb17a3211767c5c
[126]: https://issues.apache.org/jira/browse/ARROW-4440
[127]: https://github.com/apache/arrow/commit/b117a820673147a58589edb8644de4269307e7f4
[128]: https://issues.apache.org/jira/browse/ARROW-4469
[129]: https://github.com/apache/arrow/commit/04ad2140afad74a68a816d5e90b2781e23dd0418
[130]: https://issues.apache.org/jira/browse/ARROW-3846
[131]: https://github.com/apache/arrow/commit/5232a4cced3b43d3d21c7415c9b1e4d2663d8a81
[132]: https://github.com/apache/arrow/commit/65f37f7a7feb7468d32a4f27ed6b3a21a1da837d
[133]: https://issues.apache.org/jira/browse/ARROW-4124
[134]: https://github.com/apache/arrow/commit/9a10baed5580c330144d2d2807904c821798ad25
[135]: https://issues.apache.org/jira/browse/ARROW-4499
[136]: https://github.com/apache/arrow/commit/9db7a6144976cc618b085acbb633d9634a58e46e
[137]: https://github.com/pitrou
[138]: https://issues.apache.org/jira/browse/ARROW-4498
[139]: https://github.com/apache/arrow/commit/18f9e692f3bf588e4b062702e79884ca26882dbf
[140]: https://issues.apache.org/jira/browse/ARROW-3631
[141]: https://github.com/apache/arrow/commit/62dd09d642f0a75cb75914bd6f6ec71f29d9a145
[142]: https://issues.apache.org/jira/browse/ARROW-4434
[143]: https://github.com/apache/arrow/commit/6b78fba62b4a9d885c3518c9b61ddf99dfe1a5bc
[144]: https://issues.apache.org/jira/browse/ARROW-331
[145]: https://github.com/apache/arrow/commit/4cf1c7a093ed74caa6a16caa31ef06f8ad211d1b
[146]: https://issues.apache.org/jira/browse/ARROW-4457
[147]: https://github.com/apache/arrow/commit/1d72a89d49a98878086442d0567655aead544075
[148]: https://issues.apache.org/jira/browse/ARROW-4363
[149]: https://github.com/apache/arrow/commit/fc7977a670fae0d8e7b1418561d30f76df24ec02
[150]: https://issues.apache.org/jira/browse/ARROW-4481
[151]: https://github.com/apache/arrow/commit/b31845d23228f99543e6c7e403f311680c7e16c7
[152]: https://issues.apache.org/jira/browse/ARROW-4181
[153]: https://github.com/apache/arrow/commit/a5d8ccc3fc7671986c38cfe3558b77e0fe157053
[154]: https://issues.apache.org/jira/browse/ARROW-3292
[155]: https://github.com/apache/arrow/commit/af60c2e730236cfbbd207e1c0bd655bbb230bae1
[156]: https://issues.apache.org/jira/browse/ARROW-47
[157]: https://github.com/apache/arrow/commit/d831e2ce5931f520dc8be2ab3cf2d243999f85ed
[158]: https://issues.apache.org/jira/browse/ARROW-4558
[159]: https://github.com/apache/arrow/commit/69d595ae4c61902b3f2778e536fca6675350c88c
[160]: https://issues.apache.org/jira/browse/ARROW-4340
[161]: https://github.com/apache/arrow/commit/2571b03cf8dbe1c72e5cbe1ccd921fb07221685e
[162]: https://issues.apache.org/jira/browse/ARROW-4563
[163]: https://github.com/apache/arrow/commit/b9819e8e705932f28cb2f7b0115286bbd2bdefa9
[164]: https://issues.apache.org/jira/browse/ARROW-1896
[165]: https://github.com/apache/arrow/commit/47ebb1af1f6e1bcac95cf99f8258257f471f043b
[166]: https://issues.apache.org/jira/browse/ARROW-4529
[167]: https://github.com/apache/arrow/commit/10e8942990a48fe96ce87ac2faff12648cf2a307
[168]: https://issues.apache.org/jira/browse/ARROW-4576
[169]: https://github.com/apache/arrow/commit/bf138a848e6c52fc9372b3fc7c5001dbd7f70bab
[170]: https://issues.apache.org/jira/browse/ARROW-3669
[171]: https://github.com/apache/arrow/commit/40b0c88838b692518fec80835c70233629010e31
[172]: https://issues.apache.org/jira/browse/ARROW-4341
[173]: https://github.com/apache/arrow/commit/bbca7178adf1214425f95164a887989b018707f8
[174]: https://issues.apache.org/jira/browse/ARROW-4546
[175]: https://github.com/apache/arrow/commit/d0d810bc589253841571ef6d8d8919d6236dadba
[176]: https://issues.apache.org/jira/browse/ARROW-4531
[177]: https://github.com/apache/arrow/commit/5680042584cda6cebdf452a782e43a05ba9751d6
[178]: https://github.com/javierluraschi
[179]: https://issues.apache.org/jira/browse/ARROW-4565
[180]: https://github.com/apache/arrow/commit/aeb40ed8bdb939662f43c6a38fd960294542e01b
[181]: https://issues.apache.org/jira/browse/ARROW-4420
[182]: https://github.com/apache/arrow/commit/76979c924ef64da8a6fa2f5133e681cf0649c057
[183]: https://issues.apache.org/jira/browse/ARROW-4624
[184]: https://github.com/apache/arrow/commit/707bac28caab94b6aaa1951a91726cd66178a9ee
[185]: https://issues.apache.org/jira/browse/ARROW-4347
[186]: https://github.com/apache/arrow/commit/6fd5070db28001c1258628a58db78c575887c56d
[187]: https://github.com/romainfrancois
[188]: https://issues.apache.org/jira/browse/ARROW-4623
[189]: https://github.com/apache/arrow/commit/bd57703b702b00d5d2fdaac2f46314525f32fdad
[190]: https://issues.apache.org/jira/browse/ARROW-4618
[191]: https://github.com/apache/arrow/commit/ef28f201cf19001a8045f059a0936740c13bba7e
[192]: https://issues.apache.org/jira/browse/ARROW-4581
[193]: https://github.com/apache/arrow/commit/09cfd466746fa186e458b5134fb4119c2ed3e7a2
[194]: https://issues.apache.org/jira/browse/ARROW-4562
[195]: https://github.com/apache/arrow/commit/6c4118b274cadf044b2d0581401a018f0a438205
[196]: https://issues.apache.org/jira/browse/ARROW-694
[197]: https://github.com/apache/arrow/commit/9c19bb65c128f9e9a82e19b0c0caf575817e8fb2
[198]: https://issues.apache.org/jira/browse/ARROW-3532
[199]: https://github.com/apache/arrow/commit/d3c5b85e6881543f12378fd63c2921aead36cc5f
[200]: https://issues.apache.org/jira/browse/ARROW-4559
[201]: https://github.com/apache/arrow/commit/6711404a131f2ebf7d41f062d69eed6018108f71
[202]: https://issues.apache.org/jira/browse/ARROW-3981
[203]: https://github.com/apache/arrow/commit/a977250fbd542ddddb9d4d5b3b1956721a0c09c4
[204]: https://issues.apache.org/jira/browse/ARROW-4372
[205]: https://github.com/apache/arrow/commit/e8cc48b455251f4a8b6a8174d019669fe4a92d20
[206]: https://issues.apache.org/jira/browse/ARROW-3985
[207]: https://github.com/apache/arrow/commit/345b098efa2e5a83f9d6758d8a1d0c2234bc4386
[208]: https://issues.apache.org/jira/browse/ARROW-4654
[209]: https://github.com/apache/arrow/commit/25b566cbbc9eabbac63cb41c8240aaa51a3c0c98
[210]: https://issues.apache.org/jira/browse/ARROW-4643
[211]: https://github.com/apache/arrow/commit/9814605c25ab0e8736bae9ccad89c334647da660
[212]: https://issues.apache.org/jira/browse/ARROW-4659
[213]: https://github.com/apache/arrow/commit/48f7b360b138d7152e418021864e7b574f02458c
[214]: https://issues.apache.org/jira/browse/ARROW-4638
[215]: https://github.com/apache/arrow/commit/1b78eb7d24dfd36dc4149355ab2c4d4bdbf90798
[216]: https://issues.apache.org/jira/browse/ARROW-4192
[217]: https://github.com/apache/arrow/commit/a9a766bb66a3b7e99ea876bc998b5ec104b802d6
[218]: https://issues.apache.org/jira/browse/ARROW-585
[219]: https://github.com/apache/arrow/commit/a79cc809883192417920b501e41a0e8b63cd0ad1
[220]: https://issues.apache.org/jira/browse/ARROW-4641
[221]: https://github.com/apache/arrow/commit/49f1ff521b6e1b05ff85aac7b5a97161cf589cdf
[222]: https://issues.apache.org/jira/browse/ARROW-4520
[223]: https://github.com/apache/arrow/commit/37d9d3d1d781b37a65125b0c774d8ee0a4f0035b
[224]: https://issues.apache.org/jira/browse/ARROW-3816
[225]: https://github.com/apache/arrow/commit/41fc38f05afdf1cc4955216d744b2e17901d7882
[226]: https://issues.apache.org/jira/browse/ARROW-2392
[227]: https://github.com/apache/arrow/commit/4a084b79f9ab5c1f73658a5e5ff3581f5b875c42
[228]: https://issues.apache.org/jira/browse/ARROW-4672
[229]: https://github.com/apache/arrow/commit/e648a762586d1af3a294dd96054a78b90f6e71ec
[230]: https://issues.apache.org/jira/browse/ARROW-4657
[231]: https://github.com/apache/arrow/commit/b3f3dbc0fd58b28d109517f2fb7152be83dc1184
[232]: https://issues.apache.org/jira/browse/ARROW-3361
[233]: https://github.com/apache/arrow/commit/d092dd021e310b48bd9152c28696b9e18b534c8e
[234]: https://issues.apache.org/jira/browse/ARROW-4560
[235]: https://github.com/apache/arrow/commit/2a14c7ba47d106730adc6c154e74df8d21c45d55
[236]: https://issues.apache.org/jira/browse/ARROW-2627
[237]: https://github.com/apache/arrow/commit/f2fb02b82b60ba9a90c8bad6e5b11e37fc3ea9d3
[238]: https://issues.apache.org/jira/browse/ARROW-3121
[239]: https://github.com/apache/arrow/commit/29aa925683870d2644bb6334610d164aaeef6d10
[240]: https://issues.apache.org/jira/browse/ARROW-4687
[241]: https://github.com/apache/arrow/commit/05ce0a27ed5321b1646a397c5d2f6b97dd3d0954
[242]: https://lists.apache.org/thread.html/1f43d0d77d2fd2bcb3e1b5c68ff7e4f1925cf0e116a4429bc5c0e812@%3Cdev.arrow.apache.org%3E
[243]: https://github.com/apache/arrow/tree/master/dev/benchmarking
[244]: https://globenewswire.com/news-release/2019/02/19/1734042/0/en/The-Apache-Software-Foundation-Announces-Apache-Arrow-Momentum.html
[1]: https://t.co/Eta1VACtky
[2]: https://hire.withgoogle.com/public/jobs/rstudiocom/view/P_AAAAAACAAADN8HO470lz8Z
[3]: http://wesmckinney.com/blog/leaving-nyc-for-nashville/