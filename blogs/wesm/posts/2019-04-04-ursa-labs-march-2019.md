---
title: "Ursa Labs March 2019 Report"
date: 2019-04-04T00:00:00
tags: ["ursa labs", "work"]
slug: ursa-labs-march-2019
word_count: 1647
source_file: blog/ursa-labs-march-2019/index.qmd
content_type: blog
---

The first quarter of 2019 has now wrapped up. In March we spent a good amount
of time focused on getting the 0.13.0 Apache Arrow release out of the door. I
will mention a few development highlights from the month and provide the full
changelog of patches later in the post.

## Development Highlights

We are continuing to set up our **physical build and test cluster** which we'll
use to run integration tests, GPU-enabled builds, benchmark comparisons, and
other automated tests to help with Arrow development.

Some highlights from our work in the Apache Arrow codebase:

* **C++ CMake Revamp**: we collaborated with Uwe Korn, Kouhei Sutou, and other
  parts of the Arrow community on a major revamp of the CMake build system for
  C++, with associated improvements and fixes to the downstream packages
* **C++ expression algebra**: we have begun prototyping an expression algebra
  to use for query engine development in C++. This work is loosely modeled
  after our prior work in the [Ibis project][241].
* **Arrow Flight**: the C++ build dependencies (including gRPC) for the new
  Arrow Flight messaging and RPC framework are now available in conda-forge. We
  have also added a URI library for file paths to our build toolchain to help
  describe network locations and protocols for Flight. We have been working
  closely with Two Sigma and Dremio on this important effort.
* **C++ Query Engine Discussions**: we wrote a [10-page discussion
  document][242] for the design of an embeddable Arrow-native analytical query
  engine in C++
* **R packaging support**: we are working to get the Arrow R package submitted
  to CRAN for R users
* **Gandiva packaging**: Gandiva (LLVM expression compiler) is now shipped in
  the Arrow 0.13.0 Python wheels

We have much work ahead of us and look forward to seeing you on GitHub, JIRA,
and the `dev@arrow.apache.org` developer mailing list.

## Sponsor Acknowledgements

We are grateful to the support of our sponsors:

* RStudio
* NVIDIA AI Labs
* ODSC Conference
* Two Sigma Investments

If you or your company would be interested in sponsoring the work of Ursa Labs,
please contact us at **info@ursalabs.org**.

## Team Changelog

The team had 68 commits merged into Apache Arrow in March. You
can click on the ASF JIRA links to learn more about the discussion on a
particular issue or the commit hash to see each patch.

* 2019-03-01: [ARROW-4297][101]: [C++] Fix build error with MinGW-w64 32-bit ([d4931c][102] by [javierluraschi][100])
* 2019-03-02: [ARROW-4696][104]: Better CUDA detection in release verification script ([503502][105] by [fsaintjacques][103])
* 2019-03-04: [ARROW-4707][107]: [C++] moving BitsetStack to BitUtil:: ([4e8e07][108] by [bkietz][106])
* 2019-03-04: [ARROW-3123][109]: [C++] Implement Count aggregate kernel ([1b30ab][110] by [fsaintjacques][103])
* 2019-03-04: [ARROW-4448][111]: [Java][Flight] Disable flaky TestBackPressure ([8724c1][112] by [fsaintjacques][103])
* 2019-03-05: [ARROW-3770][113]: [C++] Validate schema for each table written with parquet::arrow::FileWriter ([bf7ed4][114] by [bkietz][106])
* 2019-03-05: [ARROW-4766][115]: [C++] Fix empty array cast segfault ([f1bc19][116] by [fsaintjacques][103])
* 2019-03-07: [ARROW-3550][117]: [C++] use kUnknownNullCount for the default null_count argument ([09466c][118] by [bkietz][106])
* 2019-03-07: [ARROW-4710][120]: [C++][R] New linting script skip files with cpp" extension" ([0249f1][121] by [romainfrancois][119])
* 2019-03-08: [ARROW-4782][123]: [C++] Prototype array and scalar expression types to help with building an deferred compute graph ([08ca13][124] by [wesm][122])
* 2019-03-08: [ARROW-4774][125]: [C++] Fix FileWriter::WriteTable segfault ([ef9938][126] by [fsaintjacques][103])
* 2019-03-08: [ARROW-4699][127]: [C++] remove json chunker's requirement of null terminated buffers ([4afd2e][128] by [bkietz][106])
* 2019-03-11: [ARROW-4790][130]: [Python/Packaging] Update manylinux docker image in crossbow task ([3db579][131] by [kszucs][129])
* 2019-03-12: [ARROW-4837][132]: [C++] Support c++filt on a custom path in the run-test.sh script ([0fb9e5][133] by [kszucs][129])
* 2019-03-12: [ARROW-4664][134]: [C++] Do not execute expressions inside DCHECK macros in release builds ([082aa4][135] by [wesm][122])
* 2019-03-12: [ARROW-4789][136]: [C++] Deprecate and and later remove arrow::io::ReadableFileInterface ([7a539f][137] by [wesm][122])
* 2019-03-13: [ARROW-4834][138]: [R] Feature flag when building parquet ([95d62c][139] by [javierluraschi][100])
* 2019-03-13: [ARROW-1639][140]: [Python] Serialize RangeIndex as metadata via Table.from_pandas instead of converting to a column of integers ([86f480][141] by [wesm][122])
* 2019-03-13: [ARROW-4776][142]: [C++] Add DictionaryBuilder constructor which takes a dictionary array ([65d0e1][143] by [bkietz][106])
* 2019-03-13: [ARROW-4811][144]: [C++] Fix misbehaving CMake dependency on flight_grpc_gen ([e7713a][145] by [wesm][122])
* 2019-03-13: [ARROW-4831][146]: [C++] CMAKE_AR is not passed to ZSTD thirdparty dependency ([0c4f85][147] by [kszucs][129])
* 2019-03-13: [ARROW-4850][148]: [CI] Ensure integration_test.py returns non-zero on failures ([4fefff][149] by [fsaintjacques][103])
* 2019-03-14: [ARROW-3364][150]: [Docs] Add docker-compose integration documentation ([9198f6][151] by [fsaintjacques][103])
* 2019-03-14: [ARROW-4251][152]: [C++][Release] Add option to set ARROW_BOOST_VENDORED environment variable in verify-release-candidate.sh ([954e3f][153] by [wesm][122])
* 2019-03-14: [ARROW-4866][154]: [C++] Fix zstd_ep build for Debug, static CRT builds. Add separate CMake variable for propagating compiler toolchain to ExternalProjects ([431fc1][155] by [wesm][122])
* 2019-03-14: [ARROW-4673][156]: [C++] Implement Scalar::Equals and Datum::Equals ([548e19][157] by [fsaintjacques][103])
* 2019-03-15: [ARROW-4878][158]: [C++] Append \Library to CONDA_PREFIX when using ARROW_DEPENDENCY_SOURCE=CONDA ([d65503][159] by [wesm][122])
* 2019-03-15: [ARROW-4751][160]: [C++] Add pkg-config to conda_env_cpp.yml now that it's available on Windows ([be8f94][161] by [wesm][122])
* 2019-03-15: [ARROW-4056][162]: [C++] Unpin boost-cpp in conda_env_cpp.yml ([b601a6][163] by [wesm][122])
* 2019-03-15: [ARROW-4873][164]: [C++] Clarify documentation about how to use external ARROW_PACKAGE_PREFIX while also using CONDA dependency resolution ([359ba4][165] by [wesm][122])
* 2019-03-16: [ARROW-4867][166]: [Python] Respect ordering of columns argument passed to Table.from_pandas ([76e8fe][167] by [wesm][122])
* 2019-03-17: [ARROW-4339][168]: [C++][Python] Developer documentation overhaul for 0.13 release ([d94a9f][169] by [wesm][122])
* 2019-03-18: Fix markdown syntax in python's and rust's readme (#3964) ([377104][170] by [kszucs][129])
* 2019-03-18: [ARROW-4855][171]: [Packaging] Generate default package version based on cpp tags in crossbow.py ([71c529][172] by [kszucs][129])
* 2019-03-18: [ARROW-4909][173]: [CI] Use hadolint to lint Dockerfiles ([410752][174] by [kszucs][129])
* 2019-03-18: [ARROW-3824][175]: [R] Add basic build and test documentation ([7a495e][176] by [fsaintjacques][103])
* 2019-03-19: [ARROW-4961][177]: [C++] Add documentation note that GTest_SOURCE=BUNDLED is current required on Windows ([8abed5][178] by [wesm][122])
* 2019-03-19: [ARROW-4640][179]: [Python] Add docker-compose configuration to build and test the project without pandas installed ([50bc9f][180] by [kszucs][129])
* 2019-03-19: [ARROW-4413][182]: [Python] Fix pa.hdfs.connect() on Python 2 ([8281a5][183] by [pitrou][181])
* 2019-03-19: [ARROW-4869][184]: [C++] Fix gmock usage in compute/kernels/util-internal-test.cc ([8d5733][185] by [bkietz][106])
* 2019-03-19: [ARROW-4928][186]: [Python] Fix Hypothesis test failures ([ee59aa][187] by [pitrou][181])
* 2019-03-19: [ARROW-4954][188]: [Python] Fix test failure with Flight enabled ([af8686][189] by [pitrou][181])
* 2019-03-19: [ARROW-4637][190]: [Python] Conditionally import pandas symbols if they are used. Do not require pandas as a test dependency ([286bf7][191] by [wesm][122])
* 2019-03-20: [ARROW-4697][192]: [C++] Add URI parsing facility ([ca2351][193] by [pitrou][181])
* 2019-03-20: [ARROW-4969][194]: [C++] Set RPATH in correct order for test executables on OSX ([bd00f8][195] by [kszucs][129])
* 2019-03-20: [ARROW-549][196]: [C++] Add arrow::Concatenate function to combine multiple arrays into a single Array ([43f2a3][197] by [bkietz][106])
* 2019-03-20: [ARROW-3208][198]: [C++] Fix Cast dictionary to numeric segfault ([37f898][199] by [fsaintjacques][103])
* 2019-03-21: [ARROW-4951][200]: [C++] Turn off cpp benchmarks in cpp docker images ([50e9f6][201] by [kszucs][129])
* 2019-03-21: [ARROW-4862][202]: [C++] Fix gcc warnings in CHECKIN ([ad1697][203] by [fsaintjacques][103])
* 2019-03-21: [ARROW-4881][204]: [C++] remove references to ARROW_BUILD_TOOLCHAIN ([3bf1e3][205] by [bkietz][106])
* 2019-03-21: [Release] Apache Arrow JavaScript 0.4.1 ([e9cf83][206] by [kszucs][129])
* 2019-03-24: [ARROW-4989][207]: [C++] Find re2 on Ubuntu if asked to ([3cd5df][208] by [pitrou][181])
* 2019-03-24: [ARROW-4688][209]: [C++][Parquet] Chunk binary column reads at 2^31 - 1 byte boundaries to avoid splitting chunk inside nested string cell ([fc7d07][210] by [wesm][122])
* 2019-03-24: [ARROW-3843][211]: [C++][Python] Allow a degenerate" Parquet file with no columns" ([080c83][212] by [wesm][122])
* 2019-03-25: [ARROW-4250][213]: [C++] adding explicit epsilon for ApproxEquals and corresponding assert macro ([d0626c][214] by [bkietz][106])
* 2019-03-25: [ARROW-5006][215]: [R] parquet.cpp does not include enough Rcpp ([537bfb][216] by [romainfrancois][119])
* 2019-03-25: [ARROW-5003][217]: [R] remove dependency on withr ([0536ef][218] by [romainfrancois][119])
* 2019-03-26: [ARROW-5012][219]: [C++] Install testing headers ([fd8887][220] by [pitrou][181])
* 2019-03-26: [ARROW-4872][221]: [Python] Keep backward compatibility for ParquetDatasetPiece ([f70dbd][222] by [wesm][122])
* 2019-03-26: [ARROW-5011][223]: [Release] Add support in source release script for custom git hash ([52ca07][224] by [fsaintjacques][103])
* 2019-03-26: [ARROW-5010][225]: [Release] Fix source release docker ([eb8bc6][226] by [fsaintjacques][103])
* 2019-03-26: [ARROW-4995][227]: [R] Support for winbuilder for CRAN checks ([c43a7f][228] by [javierluraschi][100])
* 2019-03-26: [ARROW-4645][229]: [C++/Packaging] Ship Gandiva with OSX and Windows wheels ([9c174f][230] by [kszucs][129])
* 2019-03-26: [ARROW-4952][231]: [C++] Floating-point comparisons should consider NaNs unequal ([d2b5b3][232] by [pitrou][181])
* 2019-03-27: [ARROW-4646][233]: [C++/Packaging] Ship gandiva with the conda-forge packages ([4e3c73][234] by [kszucs][129])
* 2019-03-28: [ARROW-5041][235]: [C++] add GTest_SOURCE=BUNDLED to verify-release-candidate.bat ([b5f842][236] by [bkietz][106])
* 2019-03-28: [ARROW-5031][237]: [Dev] Run CUDA Python tests in release verification script ([4b325d][238] by [pitrou][181])
* 2019-03-28: [ARROW-5029][239]: [C++] Fix compilation warnings in release mode ([97abab][240] by [pitrou][181])

[100]: https://github.com/javierluraschi
[101]: https://issues.apache.org/jira/browse/ARROW-4297
[102]: https://github.com/apache/arrow/commit/d4931c92b3a75934d2146572b6fdd16be8b1114f
[103]: https://github.com/fsaintjacques
[104]: https://issues.apache.org/jira/browse/ARROW-4696
[105]: https://github.com/apache/arrow/commit/5035027d2e954d78cf8c6d37b74bf756dda4a8cb
[106]: https://github.com/bkietz
[107]: https://issues.apache.org/jira/browse/ARROW-4707
[108]: https://github.com/apache/arrow/commit/4e8e072eaa9d46d2a69031d22e81914da504ba0d
[109]: https://issues.apache.org/jira/browse/ARROW-3123
[110]: https://github.com/apache/arrow/commit/1b30ab5c5126f94270db48ff93e16282895f5842
[111]: https://issues.apache.org/jira/browse/ARROW-4448
[112]: https://github.com/apache/arrow/commit/8724c1ec6010937041139a2895780e7154cad888
[113]: https://issues.apache.org/jira/browse/ARROW-3770
[114]: https://github.com/apache/arrow/commit/bf7ed4562b7bce3d94267f65af041553d5cdcd74
[115]: https://issues.apache.org/jira/browse/ARROW-4766
[116]: https://github.com/apache/arrow/commit/f1bc19ec1cbf2b33ec0016107f199b8169cee553
[117]: https://issues.apache.org/jira/browse/ARROW-3550
[118]: https://github.com/apache/arrow/commit/09466ce0c143c7676c140b4e5cc4c1151056875e
[119]: https://github.com/romainfrancois
[120]: https://issues.apache.org/jira/browse/ARROW-4710
[121]: https://github.com/apache/arrow/commit/0249f19eeea9fca2f7dfe1f4e56071732074691b
[122]: https://github.com/wesm
[123]: https://issues.apache.org/jira/browse/ARROW-4782
[124]: https://github.com/apache/arrow/commit/08ca13f83f3d6dbd818c4280d619dae306aa9de5
[125]: https://issues.apache.org/jira/browse/ARROW-4774
[126]: https://github.com/apache/arrow/commit/ef993877ac05bc840aa4670d6e9aa2da9f4eb8d6
[127]: https://issues.apache.org/jira/browse/ARROW-4699
[128]: https://github.com/apache/arrow/commit/4afd2eec89de5b9d07d291cab8f55bc3c8439e41
[129]: https://github.com/kszucs
[130]: https://issues.apache.org/jira/browse/ARROW-4790
[131]: https://github.com/apache/arrow/commit/3db5797171616f1387ef8ce8ed1183e96e68dcdf
[132]: https://issues.apache.org/jira/browse/ARROW-4837
[133]: https://github.com/apache/arrow/commit/0fb9e58a30ee14cfeac6a627b6f5abbcc7d84443
[134]: https://issues.apache.org/jira/browse/ARROW-4664
[135]: https://github.com/apache/arrow/commit/082aa4061c72a7f0571d97eb1a315a95904a7ce4
[136]: https://issues.apache.org/jira/browse/ARROW-4789
[137]: https://github.com/apache/arrow/commit/7a539f3383bc6229a0a5648f1730ae75600317d8
[138]: https://issues.apache.org/jira/browse/ARROW-4834
[139]: https://github.com/apache/arrow/commit/95d62caff4c352dba848221454d55c21b8857448
[140]: https://issues.apache.org/jira/browse/ARROW-1639
[141]: https://github.com/apache/arrow/commit/86f480a2a246f0c885031aff8d21f68640dbd72a
[142]: https://issues.apache.org/jira/browse/ARROW-4776
[143]: https://github.com/apache/arrow/commit/65d0e1959a3a2a52acae85e9f5b465f345585476
[144]: https://issues.apache.org/jira/browse/ARROW-4811
[145]: https://github.com/apache/arrow/commit/e7713aa67c5d8aab07e5a123258699bbb00d2e6a
[146]: https://issues.apache.org/jira/browse/ARROW-4831
[147]: https://github.com/apache/arrow/commit/0c4f857e89b82369eb57ee9296c3ecd7a39f8850
[148]: https://issues.apache.org/jira/browse/ARROW-4850
[149]: https://github.com/apache/arrow/commit/4fefff3aeeb22e1c4e082122b3ee7c49c6071def
[150]: https://issues.apache.org/jira/browse/ARROW-3364
[151]: https://github.com/apache/arrow/commit/9198f630663e7f8ddaecbd4d9f037f61e5b450d3
[152]: https://issues.apache.org/jira/browse/ARROW-4251
[153]: https://github.com/apache/arrow/commit/954e3f44c8753e548c7b24f2269135716a2429cd
[154]: https://issues.apache.org/jira/browse/ARROW-4866
[155]: https://github.com/apache/arrow/commit/431fc13011cd959ecd3ea57b960436e960256f91
[156]: https://issues.apache.org/jira/browse/ARROW-4673
[157]: https://github.com/apache/arrow/commit/548e1949d527717d7821a4ab2f09ff7c39882152
[158]: https://issues.apache.org/jira/browse/ARROW-4878
[159]: https://github.com/apache/arrow/commit/d655035f5a1d8e42303eb61d2a6b698792e481e5
[160]: https://issues.apache.org/jira/browse/ARROW-4751
[161]: https://github.com/apache/arrow/commit/be8f9413b8af9480b2ebc05b5de90e9dda54f0a5
[162]: https://issues.apache.org/jira/browse/ARROW-4056
[163]: https://github.com/apache/arrow/commit/b601a63e4f5a03394dad58ede6b3dfddef58abbd
[164]: https://issues.apache.org/jira/browse/ARROW-4873
[165]: https://github.com/apache/arrow/commit/359ba42d83d3a89ff8fb891d74cdff3002339171
[166]: https://issues.apache.org/jira/browse/ARROW-4867
[167]: https://github.com/apache/arrow/commit/76e8fe98d9d61a58ed706c448697e8474fabd30f
[168]: https://issues.apache.org/jira/browse/ARROW-4339
[169]: https://github.com/apache/arrow/commit/d94a9fcee801d9e185f36f767bb5b70566df70ff
[170]: https://github.com/apache/arrow/commit/3771045a4d63061bab84a389b40d43138e98421d
[171]: https://issues.apache.org/jira/browse/ARROW-4855
[172]: https://github.com/apache/arrow/commit/71c529fa779f33fca03e88766a3c1d841970e2e3
[173]: https://issues.apache.org/jira/browse/ARROW-4909
[174]: https://github.com/apache/arrow/commit/4107529a53ae13686e09bda636737e2f4c0797aa
[175]: https://issues.apache.org/jira/browse/ARROW-3824
[176]: https://github.com/apache/arrow/commit/7a495e7800ed2f184da1d5ffc4efde7d6c4abcac
[177]: https://issues.apache.org/jira/browse/ARROW-4961
[178]: https://github.com/apache/arrow/commit/8abed593b5c574a1f24ed6e75f73a3c0cadc5eb6
[179]: https://issues.apache.org/jira/browse/ARROW-4640
[180]: https://github.com/apache/arrow/commit/50bc9f49671afb56594910f49b9bf34e080a70e7
[181]: https://github.com/pitrou
[182]: https://issues.apache.org/jira/browse/ARROW-4413
[183]: https://github.com/apache/arrow/commit/8281a5d7481efe0ecfeae1fe2f75e04671f6c11b
[184]: https://issues.apache.org/jira/browse/ARROW-4869
[185]: https://github.com/apache/arrow/commit/8d573322a4eccbab0b3dedf75505d4b693a430c1
[186]: https://issues.apache.org/jira/browse/ARROW-4928
[187]: https://github.com/apache/arrow/commit/ee59aaf011ae9b35d536bda67d4bec865d5fb6cd
[188]: https://issues.apache.org/jira/browse/ARROW-4954
[189]: https://github.com/apache/arrow/commit/af86869ceb1d8dd352d39d81c19ee5ac05d251cd
[190]: https://issues.apache.org/jira/browse/ARROW-4637
[191]: https://github.com/apache/arrow/commit/286bf7c9d343cb972691c32ea8128390aed39119
[192]: https://issues.apache.org/jira/browse/ARROW-4697
[193]: https://github.com/apache/arrow/commit/ca2351363ba1724de17eda3dd8ef334d7231f4f8
[194]: https://issues.apache.org/jira/browse/ARROW-4969
[195]: https://github.com/apache/arrow/commit/bd00f80abf6192fdf25159f0868063029290ef24
[196]: https://issues.apache.org/jira/browse/ARROW-549
[197]: https://github.com/apache/arrow/commit/43f2a31d3dd31cb2d5d6f0be72dba13a7a4e1e1f
[198]: https://issues.apache.org/jira/browse/ARROW-3208
[199]: https://github.com/apache/arrow/commit/37f898f9ca7d76448223407d436aeee6a81a8f7d
[200]: https://issues.apache.org/jira/browse/ARROW-4951
[201]: https://github.com/apache/arrow/commit/50e9f640d8fdf4e855909fe022f4b5152389bfc9
[202]: https://issues.apache.org/jira/browse/ARROW-4862
[203]: https://github.com/apache/arrow/commit/ad1697e5d25eeaff5630421f55b0120f45cf0ce1
[204]: https://issues.apache.org/jira/browse/ARROW-4881
[205]: https://github.com/apache/arrow/commit/3bf1e391bb7b1c85c93b0b78a8981aa9663f23ff
[206]: https://github.com/apache/arrow/commit/e9cf83c48b9740d42b5d18158e61c0962fda59c1
[207]: https://issues.apache.org/jira/browse/ARROW-4989
[208]: https://github.com/apache/arrow/commit/3cd5df2eb33a22f0b29803fd284c6a87243bd19f
[209]: https://issues.apache.org/jira/browse/ARROW-4688
[210]: https://github.com/apache/arrow/commit/fc7d07b2bfb04615be095606ac1a5f54ceb04cf5
[211]: https://issues.apache.org/jira/browse/ARROW-3843
[212]: https://github.com/apache/arrow/commit/080c83daf78676195c5658d41aab78b26407297a
[213]: https://issues.apache.org/jira/browse/ARROW-4250
[214]: https://github.com/apache/arrow/commit/d0626c05179cacd3d33e3c3efd4bedd710d71925
[215]: https://issues.apache.org/jira/browse/ARROW-5006
[216]: https://github.com/apache/arrow/commit/537bfb52030f941387fbefaf211770646d32a0a9
[217]: https://issues.apache.org/jira/browse/ARROW-5003
[218]: https://github.com/apache/arrow/commit/0536ef8174982a7a13a251174cc38701e8663b68
[219]: https://issues.apache.org/jira/browse/ARROW-5012
[220]: https://github.com/apache/arrow/commit/fd8887bf8134ecaa67417ba00c048f3c51ad9bfc
[221]: https://issues.apache.org/jira/browse/ARROW-4872
[222]: https://github.com/apache/arrow/commit/f70dbd1dbdb51a47e6a8a8aac8efd40ccf4d44f2
[223]: https://issues.apache.org/jira/browse/ARROW-5011
[224]: https://github.com/apache/arrow/commit/52ca0788c8636894bd9a6e592e8ee0c4c828a09a
[225]: https://issues.apache.org/jira/browse/ARROW-5010
[226]: https://github.com/apache/arrow/commit/eb8bc60e749c0a866fe5a288162dffd911f65ff3
[227]: https://issues.apache.org/jira/browse/ARROW-4995
[228]: https://github.com/apache/arrow/commit/c43a7f276313b7914c8f414bd326df6d29ac7eaf
[229]: https://issues.apache.org/jira/browse/ARROW-4645
[230]: https://github.com/apache/arrow/commit/9c174f44b73bb5c3b9ccf2bca9e0396a2592efae
[231]: https://issues.apache.org/jira/browse/ARROW-4952
[232]: https://github.com/apache/arrow/commit/d2b5b3bab0097c2bff6ce98e2bc64b030e993db8
[233]: https://issues.apache.org/jira/browse/ARROW-4646
[234]: https://github.com/apache/arrow/commit/4e3c73374ecebd3036ed3b1fd689a3051c2f04aa
[235]: https://issues.apache.org/jira/browse/ARROW-5041
[236]: https://github.com/apache/arrow/commit/b5f8426cce36ee97be149b28e356300688d3463d
[237]: https://issues.apache.org/jira/browse/ARROW-5031
[238]: https://github.com/apache/arrow/commit/4b325d83a928e7b38fc1d7960c3e349e4c3be239
[239]: https://issues.apache.org/jira/browse/ARROW-5029
[240]: https://github.com/apache/arrow/commit/97abab50d5d09d55e050ea59b7751b1a5a42ed5b
[241]: https://docs.ibis-project.org/
[242]: https://docs.google.com/document/d/10RoUZmiMQRi_J1FcPeVAUAMJ6d_ZuiEbaM2Y33sNPu4/edit?usp=sharing