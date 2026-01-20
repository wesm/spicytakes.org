---
title: "Ursa Labs January 2019 Report"
date: 2019-02-05T00:00:00
tags: ["ursa labs", "work"]
slug: ursa-labs-january-2019
word_count: 2242
source_file: blog/ursa-labs-january-2019/index.qmd
content_type: blog
---

Ursa Labs had a busy January that went by too quickly. After a high-intensity 3
months of development, we helped release [Apache Arrow 0.12][1] on January
20th. A good chunk of our time was spent fighting fires (in packaging and
builds) related to the continued expansion of the project in recent months.

The 0.12 release contains a new [merged documentation site][2] where you can
expect more project-level documentation to appear this year.

## Upcoming Focus Areas

The team is working in a number of areas in the near future:

* Building out the gRPC-based Flight RPC system
* Computational kernels in C++ in support of a future Arrow-native in-memory
  query engine
* Parquet file performance and memory use improvements. We also plan to work on
  support for reading and writing nested types, which currently have only
  limited support
* Reading line-delimited JSON datasets to the Arrow format
* Automation and bot-based job triggering in our physical build cluster. We're
  hoping to have GitHub bots that we can ask to run various builds in Arrow
  pull requests
* Packaging Gandiva (LLVM expression compiler) and gRPC in conda and wheel
  Python packages
* Work toward getting the R Arrow package on CRAN

## C++ highlights

We made many improvements to our build system and developer tools. Outside of
some of these esoteric details, some highlights include:

* Improve columnar array builder performance
* Gandiva LLVM compiler support on Windows
* Refactoring in Parquet C++ to eventually permit direct-to-categorical reads
  for pandas users
* Toolchain improvements to support the gRPC-based Flight initiative
* Alpine Linux support

Hardening the new Flight RPC system for production and making it available to
C++, Python, and Java developers is a major area of upcoming development
interest.

## Python highlights

In Python we are working with the Ray, TensorFlow, and PyTorch communities to
resolve some packaging issues related to the manylinux1 standard for wheel
binary packages. The outcome there is as yet uncertain.

Some other highlights include:

* Bindings for buffered input and output stream classes for better performance
  with high latency file systems like S3 and Google Cloud
* Support for pandas 0.24.x

## R highlights

After a very busy fall, January was a lighter month for R:

* Bindings for the Arrow C++ CSV parser
* Multithreaded conversions from `arrow::Table` to R `data.frame.`
* Bindings for compressed input and output streams, which can be used in many
  contexts

We are working on a plan to get Arrow into CRAN to make it easier for R users
to install the software. There are some hurdles including getting the Arrow C++
libraries into Debian, Fedora, and Homebrew. If you could like to help with
packaging, we would appreciate the assistance.

## Ursa Labs Development Infrastructure

Thanks to generous donations of hardware from NVIDIA, Ursa Labs now has 2 DGX
Station machines hosted in Nashville, Tennessee, for the team to develop
on. Each has a 20-core Xeon processor, 4 GPUs, and 256 GB of RAM. NVIDIA has
also donated a Jetson TX2 dev kit for development and testing on Aarch64.

Our build cluster is growing and we intend to use this hardware to make the
Apache Arrow community more productive.

## Conference Talks, Blog Posts, and other reading

Wes spoke at two conferences

* [Ursa Labs and Apache Arrow 2019][3] at PyData Miami 2019
* The same talk, tailored for the R community, at RStudio Conference 2019

We also published a blog post about some work in Arrow 0.12

* [Reducing Python String Memory Use in Apache Arrow 0.12][4]

## Apache Arrow community notes

As Apache Arrow approaches its third birthday as a top-level Apache project, we
have surpassed 3000 stars on GitHub with over 240 unique contributors.

There is a discussion happening about building a benchmark database to test the
different Arrow libraries on many different kinds of hardware, including
different CPU and GPU architectures

We are just receiving the donation of a Rust-based in-memory query engine,
DataFusion.

## Team Changelog

The team had 86 commits merged into Apache Arrow in January. You
can click on the ASF JIRA links to learn more about the discussion on a
particular issue or the commit hash to see each patch.

* 2019-01-01: [ARROW-3910][101]: [Python] Set date_as_objects=True as default in to_pandas methods ([9376d8][102] by [wesm][100])
* 2019-01-03: [ARROW-4148][104]: [CI/Python] Disable ORC on nightly Alpine builds ([6ca8fc][105] by [kszucs][103])
* 2019-01-03: [ARROW-4009][107]: [CI] Run Valgrind and C++ code coverage in different builds ([7f1fbf][108] by [pitrou][106])
* 2019-01-04: [ARROW-3760][110]: [R] Support Arrow CSV reader ([fba4f3][111] by [romainfrancois][109])
* 2019-01-04: [PARQUET-690][112]: [C++] Reuse Thrift resources when serializing metadata structures ([4057b5][113] by [wesm][100])
* 2019-01-04: [ARROW-4150][114]: [C++] Ensure allocated buffers have non-null data pointer ([1ff797][115] by [pitrou][106])
* 2019-01-04: [ARROW-4157][116]: [C++] Fix clang documentation warnings on Ubuntu 18.04 ([161d00][117] by [wesm][100])
* 2019-01-04: [ARROW-4149][118]: [CI/C++] Parquet test misses ZSTD compression codec in CMake 3.2 nightly builds ([1e9a23][119] by [kszucs][103])
* 2019-01-04: [ARROW-4158][120]: Allow committers to set ARROW_GITHUB_API_TOKEN for merge script, better debugging output ([c322ae][121] by [wesm][100])
* 2019-01-07: [ARROW-4179][122]: [Python] Use more public API to determine whether a test has a pytest mark or not ([1aecb9][123] by [wesm][100])
* 2019-01-07: [ARROW-4125][124]: [Python] Don't fail ASV if Plasma extension is not built (e.g. on Windows) ([b92b1f][125] by [wesm][100])
* 2019-01-08: [ARROW-4178][126]: [C++] Fix TSan and UBSan errors ([4f2f53][127] by [pitrou][106])
* 2019-01-08: [ARROW-4200][128]: [C++/Python] Enable conda_env_python.yml to work on Windows, simplify python/development.rst ([090a8c][129] by [wesm][100])
* 2019-01-08: [ARROW-4186][130]: [C++] BitmapWriter shouldn't clobber data when length == 0 ([326015][131] by [pitrou][106])
* 2019-01-09: [ARROW-3233][132]: [Python] Add prose documentation for CUDA support ([bcfaca][133] by [pitrou][106])
* 2019-01-09: [ARROW-4118][134]: [Python] Fix benchmark setup for asv run"" ([3330d6][135] by [pitrou][106])
* 2019-01-09: [ARROW-3997][136]: [Documentation] Clarify dictionary index type ([6b496f][137] by [pitrou][106])
* 2019-01-09: [ARROW-4138][138]: [Python] Fix setuptools_scm version customization on Windows ([84b221][139] by [wesm][100])
* 2019-01-09: [ARROW-4177][140]: [C++] Add ThreadPool and TaskGroup microbenchmarks ([b29ecd][141] by [pitrou][106])
* 2019-01-09: [ARROW-2968][142]: [R] Multi-threaded conversion from Arrow table to R data.frame ([3b6134][143] by [romainfrancois][109])
* 2019-01-09: [ARROW-3126][144]: [Python] Make Buffered* IO classes available to Python, incorporate into input_stream, output_stream factory functions ([7fcad2][145] by [kszucs][103])
* 2019-01-10: [Release/Java] Disable Flight test case ([76618f][146] by [kszucs][103])
* 2019-01-10: [ARROW-4216][147]: [Python] Add CUDA API docs ([5a502d][148] by [pitrou][106])
* 2019-01-10: [ARROW-4210][149]: [Python] Mention boost-cpp directly in the conda meta.yaml for pyarrow ([fc7b41][150] by [kszucs][103])
* 2019-01-10: [ARROW-3819][151]: [Packaging] Update conda variant files to conform with feedstock after compiler migration ([9d342e][152] by [kszucs][103])
* 2019-01-11: [ARROW-4229][153]: [Packaging] Set crossbow target explicitly to enable building arbitrary arrow repo ([d7a683][154] by [kszucs][103])
* 2019-01-12: [ARROW-4238][155]: [Packaging] Fix RC version conflict between crossbow and rake ([38a628][156] by [kszucs][103])
* 2019-01-12: [ARROW-4237][157]: [Packaging] Fix CMAKE_INSTALL_LIBDIR in release verification script ([06de47][158] by [kszucs][103])
* 2019-01-12: [ARROW-4241][159]: [Packaging] Disable crossbow conda OSX clang builds ([9178ad][160] by [kszucs][103])
* 2019-01-12: [ARROW-4243][161]: [Python] Fix test failures with pandas 0.24.0rc1 ([3e97ca][162] by [kszucs][103])
* 2019-01-14: [ARROW-4256][163]: [Release] Fix Windows verification script for 0.12 release ([cf047f][164] by [wesm][100])
* 2019-01-15: [CI] Temporary fix for conda-forge migration (#3406) ([143558][165] by [kszucs][103])
* 2019-01-15: [ARROW-4258][166]: [Python] Safe cast fails from numpy float64 array with nans to integer ([18c0e8][167] by [kszucs][103])
* 2019-01-15: [ARROW-4260][168]: [Python] NumPy buffer protocol failure ([09d349][169] by [kszucs][103])
* 2019-01-15: [ARROW-4246][170]: [Plasma][Python][Follow-up] Ensure plasma::ObjectTableEntry always has the same size regardless of whether built with CUDA support ([87ac6f][171] by [wesm][100])
* 2019-01-15: [ARROW-4266][172]: [Python][CI] Disable ORC tests in dask integration test ([5a7507][173] by [kszucs][103])
* 2019-01-16: [ARROW-4270][174]: [Packaging][Conda] Update xcode version and remove toolchain builds ([a1a922][175] by [kszucs][103])
* 2019-01-16: [Release] Update CHANGELOG.md for 0.12.0 ([6c8c0c][176] by [kszucs][103])
* 2019-01-16: [Release] Update .deb/.rpm changelogs for 0.12.0 ([db508e][177] by [kszucs][103])
* 2019-01-16: [Release] Update versions for 0.12.0 ([6fcd91][178] by [kszucs][103])
* 2019-01-16: [maven-release-plugin] prepare release apache-arrow-0.12.0 ([8ca413][179] by [kszucs][103])
* 2019-01-19: [ARROW-4273][180]: [Release] Fix verification script to use cf201901 conda-forge label ([7a918b][181] by [kszucs][103])
* 2019-01-19: [Release] Build C++ unit tests in verify-release-candidate.bat ([87abfe][182] by [wesm][100])
* 2019-01-19: [ARROW-4254][183]: [C++][Gandiva] Build with Boost from Ubuntu Trusty apt ([2e8d38][184] by [wesm][100])
* 2019-01-19: [Release] Update versions for 0.13.0-SNAPSHOT ([e52c8f][185] by [kszucs][103])
* 2019-01-19: [Release] Update .deb package names for 0.13.0 ([808178][186] by [kszucs][103])
* 2019-01-19: [CI] Manually patch version in java/gandiva/pom.xml pending fix for ARROW-4301 ([7489d3][187] by [wesm][100])
* 2019-01-19: [maven-release-plugin] prepare for next development iteration ([a486db][188] by [kszucs][103])
* 2019-01-20: [ARROW-4123][190]: [C++] Enable linting tools to be run on Windows ([a665b8][191] by [bkietz][189])
* 2019-01-20: [ARROW-4252][193]: [C++] Fix missing Status code and newline ([9855e9][194] by [fsaintjacques][192])
* 2019-01-20: [Docs] Minor fixes to documentation build instructions ([349a95][195] by [wesm][100])
* 2019-01-21: [ARROW-4306][196]: [Release] Update website, write blog post for 0.12.0 release ([02864f][197] by [wesm][100])
* 2019-01-21: [Website] Add link to top-level documentation to nav dropdown ([304224][198] by [wesm][100])
* 2019-01-22: [ARROW-4312][199]: [C++] Only run 2 * os.cpu_count() clang-format instances at once ([4d6d7d][200] by [bkietz][189])
* 2019-01-22: [ARROW-4321][201]: [CI] Setup conda-forge channel globally in docker containers ([5a75bb][202] by [kszucs][103])
* 2019-01-22: [ARROW-4307][203]: [C++] Fix Doxygen warnings ([688f1e][204] by [pitrou][106])
* 2019-01-23: [ARROW-4281][205]: [CI] Use Ubuntu Xenial VMs on Travis-CI ([1b8a7b][206] by [pitrou][106])
* 2019-01-23: [ARROW-4234][207]: [C++] Improve memory bandwidth test ([d5fe8e][208] by [fsaintjacques][192])
* 2019-01-23: [ARROW-4323][209]: [Packaging] Fix failing OSX clang conda forge builds ([372137][210] by [kszucs][103])
* 2019-01-23: [ARROW-4031][211]: [C++] Refactor bitmap building ([d15cb4][212] by [bkietz][189])
* 2019-01-24: [ARROW-4346][213]: [C++] Fix class-memaccess warning on gcc 8.x ([9460bb][214] by [wesm][100])
* 2019-01-24: [ARROW-4349][215]: [C++] Add static linking option for benchmarks, fix Windows benchmark build failures ([75c835][216] by [wesm][100])
* 2019-01-25: [ARROW-4262][218]: [Website] Preview to Spark with Arrow and R improvements ([ae4ed3][219] by [javierluraschi][217])
* 2019-01-25: [ARROW-4373][220]: [Packaging] Travis fails to deploy conda packages on OSX ([9a6480][221] by [kszucs][103])
* 2019-01-26: [ARROW-4364][222]: [C++] Fix CHECKIN warnings ([90eeb4][223] by [fsaintjacques][192])
* 2019-01-26: [ARROW-4381][224]: [CI] Update linter container build instructions ([5043d1][225] by [wesm][100])
* 2019-01-26: [ARROW-4351][226]: [C++] Fix CMake errors when neither building shared libraries nor tests ([59c69a][227] by [wesm][100])
* 2019-01-26: [ARROW-4375][228]: [CI] Sphinx dependencies were removed from docs conda environment ([bcc100][229] by [kszucs][103])
* 2019-01-26: [ARROW-3367][230]: [INTEGRATION] Port Spark integration test to the docker-compose setup ([23475e][231] by [kszucs][103])
* 2019-01-27: [ARROW-4330][232]: [C++] More robust discovery of pthreads ([b42786][233] by [wesm][100])
* 2019-01-28: [ARROW-4368][234]: [Docs] Fix install document for Ubuntu 16.04 or earlier ([3bb244][235] by [kszucs][103])
* 2019-01-28: [ARROW-4399][236]: [C++] Do not use extern template class with NumericArray<T> and NumericTensor<T> ([823dd4][237] by [wesm][100])
* 2019-01-28: [ARROW-4408][238]: [CPP/Doc] Remove outdated Parquet documentation ([93d101][239] by [kszucs][103])
* 2019-01-28: [ARROW-4401][240]: [Python] Alpine dockerfile fails to build because pandas requires numpy as build dependency ([1ba029][241] by [kszucs][103])
* 2019-01-28: [ARROW-4336][242]: [C++] Change default build type to RELEASE ([0ce39c][243] by [fsaintjacques][192])
* 2019-01-28: [ARROW-3761][244]: [R] Bindings for CompressedInputStream, CompressedOutputStream ([f576c3][245] by [romainfrancois][109])
* 2019-01-29: [PARQUET-1508][246]: [C++] Read ByteArray data directly into arrow::BinaryBuilder and BinaryDictionaryBuilder. Refactor encoders/decoders to use cleaner virtual interfaces ([3d435e][247] by [wesm][100])
* 2019-01-29: [ARROW-4417][248]: [C++] Fix doxygen build ([c4c108][249] by [pitrou][106])
* 2019-01-30: [ARROW-4414][250]: [C++] Stop using cmake COMMAND_EXPAND_LISTS because it breaks package builds for older distros ([6626c0][251] by [kszucs][103])
* 2019-01-30: [PARQUET-1519][252]: [C++] Hide TypedColumnReader implementation behind virtual interfaces, remove use of extern template class"" ([27f60b][253] by [wesm][100])
* 2019-01-30: [ARROW-4407][254]: [C++] Cache compiler for CMake external projects ([ea6323][255] by [fsaintjacques][192])
* 2019-01-30: [ARROW-4268][256]: [C++] Native C type TypeTraits ([012f77][257] by [fsaintjacques][192])
* 2019-01-31: [ARROW-4198][258]: [Gandiva] Added support to cast timestamp ([641c69][259] by [pitrou][106])
* 2019-01-31: [ARROW-4431][260]: [C++] Fixes for gRPC vendored builds ([36e26f][261] by [wesm][100])
* 2019-01-31: [ARROW-4430][262]: [C++] Fix untested TypedByteBuffer<T>::Append method ([e59bf7][263] by [bkietz][189])
* 2019-01-31: [ARROW-3846][264]: [Gandiva][C++] Build Gandiva C++ libraries and get unit tests passing on Windows ([48de82][265] by [wesm][100])

[100]: https://github.com/wesm
[101]: https://issues.apache.org/jira/browse/ARROW-3910
[102]: https://github.com/apache/arrow/commit/9376d85c409f4b9b272297b3acb6a0f70dcedc32
[103]: https://github.com/kszucs
[104]: https://issues.apache.org/jira/browse/ARROW-4148
[105]: https://github.com/apache/arrow/commit/6ca8fcdeccc54a80ce90711441a41ec6ffbd216b
[106]: https://github.com/pitrou
[107]: https://issues.apache.org/jira/browse/ARROW-4009
[108]: https://github.com/apache/arrow/commit/7f1fbf83284b745ee9215f6722e114ee467bdeb8
[109]: https://github.com/romainfrancois
[110]: https://issues.apache.org/jira/browse/ARROW-3760
[111]: https://github.com/apache/arrow/commit/fba4f32001386b2ed593a69ec6d546a104eb45ba
[112]: https://issues.apache.org/jira/browse/PARQUET-690
[113]: https://github.com/apache/arrow/commit/4057b5f2f1402026c5853e53a038db8371650fbd
[114]: https://issues.apache.org/jira/browse/ARROW-4150
[115]: https://github.com/apache/arrow/commit/1ff79785e62855d003f4b5f0c054cbfd155160c1
[116]: https://issues.apache.org/jira/browse/ARROW-4157
[117]: https://github.com/apache/arrow/commit/161d00fbeeb2f1992da8d8ac0e96fb14de51b646
[118]: https://issues.apache.org/jira/browse/ARROW-4149
[119]: https://github.com/apache/arrow/commit/1e9a23612d258cd51a20b9eccf7a13bd5be52007
[120]: https://issues.apache.org/jira/browse/ARROW-4158
[121]: https://github.com/apache/arrow/commit/c322aecd82c93f96a6d8b8852c8336a750ebfbb1
[122]: https://issues.apache.org/jira/browse/ARROW-4179
[123]: https://github.com/apache/arrow/commit/1aecb987790bb78c084a2c8f4ce224acc2dfd13b
[124]: https://issues.apache.org/jira/browse/ARROW-4125
[125]: https://github.com/apache/arrow/commit/b92b1f5b08a64004c8b35db24a34ac71de7bd0e3
[126]: https://issues.apache.org/jira/browse/ARROW-4178
[127]: https://github.com/apache/arrow/commit/4f2f53336f2293eea33235e86e41aa9f08e98a1a
[128]: https://issues.apache.org/jira/browse/ARROW-4200
[129]: https://github.com/apache/arrow/commit/090a8c020611b2f75ec0e36d765cc6d48adbe9a7
[130]: https://issues.apache.org/jira/browse/ARROW-4186
[131]: https://github.com/apache/arrow/commit/326015cfc66e1f657cdd6811620137e9e277b43d
[132]: https://issues.apache.org/jira/browse/ARROW-3233
[133]: https://github.com/apache/arrow/commit/bcfacaafcb181a39d43dbb3d0540c018a5afe157
[134]: https://issues.apache.org/jira/browse/ARROW-4118
[135]: https://github.com/apache/arrow/commit/3330d660643a034168b472b52aebfe0fea84b8cf
[136]: https://issues.apache.org/jira/browse/ARROW-3997
[137]: https://github.com/apache/arrow/commit/6b496f7c1929a0a371fe708ae653228a9e722150
[138]: https://issues.apache.org/jira/browse/ARROW-4138
[139]: https://github.com/apache/arrow/commit/84b221dd864af8385ac626fc753875416e840ff0
[140]: https://issues.apache.org/jira/browse/ARROW-4177
[141]: https://github.com/apache/arrow/commit/b29ecdce6e096618aeb110878367906b3b4b48a5
[142]: https://issues.apache.org/jira/browse/ARROW-2968
[143]: https://github.com/apache/arrow/commit/3b61349b3c16d43003e493c7e2aec9348e7e7343
[144]: https://issues.apache.org/jira/browse/ARROW-3126
[145]: https://github.com/apache/arrow/commit/7fcad2c29e3c3ac99b2f6c1f1fddc91c05b7f2b3
[146]: https://github.com/apache/arrow/commit/76618f66ee8ce75cbe09d1d1a8c313dad3d94127
[147]: https://issues.apache.org/jira/browse/ARROW-4216
[148]: https://github.com/apache/arrow/commit/5a502d281545402240e818d5fd97a9aaf36363f2
[149]: https://issues.apache.org/jira/browse/ARROW-4210
[150]: https://github.com/apache/arrow/commit/fc7b414faa5c187770ef8e28c26319f416ad7018
[151]: https://issues.apache.org/jira/browse/ARROW-3819
[152]: https://github.com/apache/arrow/commit/9d342ec4ffe2441ab0b072c90a4f652aa2678dc8
[153]: https://issues.apache.org/jira/browse/ARROW-4229
[154]: https://github.com/apache/arrow/commit/d7a68335cca4dd996ed6c9d2967f01601f15d5e0
[155]: https://issues.apache.org/jira/browse/ARROW-4238
[156]: https://github.com/apache/arrow/commit/38a628dff6fcd5f3c7e6b402f5ceb35cc8bd52c8
[157]: https://issues.apache.org/jira/browse/ARROW-4237
[158]: https://github.com/apache/arrow/commit/06de47afcb7532a9646089ca23bd7d1e62eddc10
[159]: https://issues.apache.org/jira/browse/ARROW-4241
[160]: https://github.com/apache/arrow/commit/9178ad8c3c9ea371c3b7edb3fcee3073f5082bdc
[161]: https://issues.apache.org/jira/browse/ARROW-4243
[162]: https://github.com/apache/arrow/commit/3e97ca1c207cacfb5340940bc86f95107849cbcc
[163]: https://issues.apache.org/jira/browse/ARROW-4256
[164]: https://github.com/apache/arrow/commit/cf047fc67698fe3655471da64ced8d9335668dc4
[165]: https://github.com/apache/arrow/commit/143558e1726d6468f4d624ad53d707f9df8a02a5
[166]: https://issues.apache.org/jira/browse/ARROW-4258
[167]: https://github.com/apache/arrow/commit/18c0e8241b5af5b98d7238e64753e44e43a598a8
[168]: https://issues.apache.org/jira/browse/ARROW-4260
[169]: https://github.com/apache/arrow/commit/09d34964996a718beb2def4e4173974f8a3d862e
[170]: https://issues.apache.org/jira/browse/ARROW-4246
[171]: https://github.com/apache/arrow/commit/87ac6fddaf21d0b4ee8b8090533ff293db0da1b4
[172]: https://issues.apache.org/jira/browse/ARROW-4266
[173]: https://github.com/apache/arrow/commit/5a7507c9f28f5175c367f483accc072891f53905
[174]: https://issues.apache.org/jira/browse/ARROW-4270
[175]: https://github.com/apache/arrow/commit/a1a9221cf6522b4c9bc26a9ebf4a459f6217050e
[176]: https://github.com/apache/arrow/commit/6c8c0c1211ce1b4999184560d6fe4d83b25745e7
[177]: https://github.com/apache/arrow/commit/db508eee05ec50ddf786e24b94d025c3852f8230
[178]: https://github.com/apache/arrow/commit/6fcd910aa01b1c1923779bff29f162ce40caa98d
[179]: https://github.com/apache/arrow/commit/8ca41384b5324bfd0ef3d3ed3f728e1d10ed73f0
[180]: https://issues.apache.org/jira/browse/ARROW-4273
[181]: https://github.com/apache/arrow/commit/7a918b3343c7068500f4e5d2d1994a829a3aaa95
[182]: https://github.com/apache/arrow/commit/87abfef33c9d018000a29e934df56d37bb855f8e
[183]: https://issues.apache.org/jira/browse/ARROW-4254
[184]: https://github.com/apache/arrow/commit/2e8d389b0de2ca34f79f0fbda6acc452ac5d1a2c
[185]: https://github.com/apache/arrow/commit/e52c8f11703cbda962ce65767823f5123a1d9d32
[186]: https://github.com/apache/arrow/commit/8081786402ddc418375d19ad4512a93b9b4e42dd
[187]: https://github.com/apache/arrow/commit/7489d3bac5e499039d3a97333dd3fc8e196f9b0e
[188]: https://github.com/apache/arrow/commit/a486db8c1476be1165981c4fe22996639da8e550
[189]: https://github.com/bkietz
[190]: https://issues.apache.org/jira/browse/ARROW-4123
[191]: https://github.com/apache/arrow/commit/a665b829124ffa3850b30c6b2753088785471ac5
[192]: https://github.com/fsaintjacques
[193]: https://issues.apache.org/jira/browse/ARROW-4252
[194]: https://github.com/apache/arrow/commit/9855e9479889c9f6af7a076657183be2fa706761
[195]: https://github.com/apache/arrow/commit/349a957ad9e46a300d8b46c018013fada6bce094
[196]: https://issues.apache.org/jira/browse/ARROW-4306
[197]: https://github.com/apache/arrow/commit/02864fdacfb76bb16cebf84c3b0d2dd2b958c965
[198]: https://github.com/apache/arrow/commit/30422478cae9b55cb79b29115c43be683b9eb277
[199]: https://issues.apache.org/jira/browse/ARROW-4312
[200]: https://github.com/apache/arrow/commit/4d6d7d50835a8f634aae040c75f10f374790a781
[201]: https://issues.apache.org/jira/browse/ARROW-4321
[202]: https://github.com/apache/arrow/commit/5a75bb264da58454d3790f1c19fd0137f60f7a34
[203]: https://issues.apache.org/jira/browse/ARROW-4307
[204]: https://github.com/apache/arrow/commit/688f1eeb0f5f7127c50f52552813d545946c0b3b
[205]: https://issues.apache.org/jira/browse/ARROW-4281
[206]: https://github.com/apache/arrow/commit/1b8a7bc3baa4bce660c18a13934115d55f8733df
[207]: https://issues.apache.org/jira/browse/ARROW-4234
[208]: https://github.com/apache/arrow/commit/d5fe8e5c6789e1eac484d6a6d4d8c487ec89e126
[209]: https://issues.apache.org/jira/browse/ARROW-4323
[210]: https://github.com/apache/arrow/commit/372137611606fd54c41b34f829b956f9c0c3ccf5
[211]: https://issues.apache.org/jira/browse/ARROW-4031
[212]: https://github.com/apache/arrow/commit/d15cb454402204ba3b2825afb71853b35a81a886
[213]: https://issues.apache.org/jira/browse/ARROW-4346
[214]: https://github.com/apache/arrow/commit/9460bb733a9fc7802e31c35d3c70e74c0928959c
[215]: https://issues.apache.org/jira/browse/ARROW-4349
[216]: https://github.com/apache/arrow/commit/75c83578ced6de80015f3b93c1d290b9e74430e5
[217]: https://github.com/javierluraschi
[218]: https://issues.apache.org/jira/browse/ARROW-4262
[219]: https://github.com/apache/arrow/commit/ae4ed30d668387fcc01bb23421a2ba59f9d6837b
[220]: https://issues.apache.org/jira/browse/ARROW-4373
[221]: https://github.com/apache/arrow/commit/9a6480586593221cd5f48c8e8a1dd30507a06066
[222]: https://issues.apache.org/jira/browse/ARROW-4364
[223]: https://github.com/apache/arrow/commit/90eeb4a2d3daebf1626d2b25f7d2b44d28772e2e
[224]: https://issues.apache.org/jira/browse/ARROW-4381
[225]: https://github.com/apache/arrow/commit/5043d1ed1903a75991733a38e64afc025d7de91d
[226]: https://issues.apache.org/jira/browse/ARROW-4351
[227]: https://github.com/apache/arrow/commit/59c69aa2ec377e03388ff509eb7742e4fd625e01
[228]: https://issues.apache.org/jira/browse/ARROW-4375
[229]: https://github.com/apache/arrow/commit/bcc1003f976fd209d908616c27f7f58d7ee2e6a1
[230]: https://issues.apache.org/jira/browse/ARROW-3367
[231]: https://github.com/apache/arrow/commit/23475eeddacfc3b4bea9cacc7e431db434c7223a
[232]: https://issues.apache.org/jira/browse/ARROW-4330
[233]: https://github.com/apache/arrow/commit/b4278641a6a56c56d2007469b0eb840d52cc007d
[234]: https://issues.apache.org/jira/browse/ARROW-4368
[235]: https://github.com/apache/arrow/commit/3bb244fdc7733be017c299788fb8bc6b8c561220
[236]: https://issues.apache.org/jira/browse/ARROW-4399
[237]: https://github.com/apache/arrow/commit/823dd43e0ca95f74ef110ecefd70c66d76e48cc9
[238]: https://issues.apache.org/jira/browse/ARROW-4408
[239]: https://github.com/apache/arrow/commit/93d1012b1f7d7ba2addab4ca13d4761d5ae2bf8e
[240]: https://issues.apache.org/jira/browse/ARROW-4401
[241]: https://github.com/apache/arrow/commit/1ba029cad7a064c90bcbb7706562e53238ac5712
[242]: https://issues.apache.org/jira/browse/ARROW-4336
[243]: https://github.com/apache/arrow/commit/0ce39c6d3d029d80165d03c1e5ae49453890b3f7
[244]: https://issues.apache.org/jira/browse/ARROW-3761
[245]: https://github.com/apache/arrow/commit/f576c3ebe9159099eeef5c7229bb7041888109f6
[246]: https://issues.apache.org/jira/browse/PARQUET-1508
[247]: https://github.com/apache/arrow/commit/3d435e4f8d5fb7a54a4a9d285e1a42d60186d8dc
[248]: https://issues.apache.org/jira/browse/ARROW-4417
[249]: https://github.com/apache/arrow/commit/c4c108b2112b9809e0342e3d714fcd0ab2c9053b
[250]: https://issues.apache.org/jira/browse/ARROW-4414
[251]: https://github.com/apache/arrow/commit/6626c009ac19be2fdf5815b70eabbdfdf2b0e434
[252]: https://issues.apache.org/jira/browse/PARQUET-1519
[253]: https://github.com/apache/arrow/commit/27f60ba2f6cff9372261f4cedd721b0f982808fd
[254]: https://issues.apache.org/jira/browse/ARROW-4407
[255]: https://github.com/apache/arrow/commit/ea63231110c07010df7090518dc678c0a37d1ea6
[256]: https://issues.apache.org/jira/browse/ARROW-4268
[257]: https://github.com/apache/arrow/commit/012f77a96880cff49f588ae1ff2f65d5105ee433
[258]: https://issues.apache.org/jira/browse/ARROW-4198
[259]: https://github.com/apache/arrow/commit/641c6990cdc702c736921c78448cf3a175c97863
[260]: https://issues.apache.org/jira/browse/ARROW-4431
[261]: https://github.com/apache/arrow/commit/36e26fe473ab776982a52861bbc6875431abae7c
[262]: https://issues.apache.org/jira/browse/ARROW-4430
[263]: https://github.com/apache/arrow/commit/e59bf777bb8babc2fbef4cc881370478acfb8f97
[264]: https://issues.apache.org/jira/browse/ARROW-3846
[265]: https://github.com/apache/arrow/commit/48de821ea79bdf4d0480a2f6b377300ddc5bbd9a
[1]: http://arrow.apache.org/release/0.12.0.html
[2]: http://arrow.apache.org/docs/
[3]: https://www.slideshare.net/wesm/ursa-labs-and-apache-arrow-in-2019
[4]: http://arrow.apache.org/blog/2019/02/05/python-string-memory-0.12/