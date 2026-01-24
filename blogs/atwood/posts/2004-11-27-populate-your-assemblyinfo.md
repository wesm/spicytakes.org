---
title: "Populate your AssemblyInfo"
date: 2004-11-27
url: https://blog.codinghorror.com/populate-your-assemblyinfo/
slug: populate-your-assemblyinfo
word_count: 195
---

All too often, I download sample code with **AssemblyInfo** files that look like this:

kg-card-begin: html

```
//
// General Information about an assembly is controlled through the following
// set of attributes. Change these attribute values to modify the information
// associated with an assembly.
//
[assembly: AssemblyTitle("")]
[assembly: AssemblyDescription("")]
[assembly: AssemblyConfiguration("")]
[assembly: AssemblyCompany("")]
[assembly: AssemblyProduct("")]
[assembly: AssemblyCopyright("")]
[assembly: AssemblyTrademark("")]
[assembly: AssemblyCulture("")]
//
// Version information for an assembly consists of the following four values:
//
//      Major Version
//      Minor Version
//      Build Number
//      Revision
//
// You can specify all the values or you can default the Revision and Build Numbers
// by using the '*' as shown below:
[assembly: AssemblyVersion("1.0.*")]
```

kg-card-end: html

So, basically, **you’re compiling into an assembly DLL or EXE with nothing but crappy, default metadata and versioning**.


Please don’t do this.


If you’re going to the effort of making your code publicly available, take an additional 60 seconds to fill out the AssemblyInfo.


My only regret with assembly attributes is that they really should have included URL and email attributes by default. Instead we have to define custom attributes to get that...

[c#](https://blog.codinghorror.com/tag/c-2/)
[.net](https://blog.codinghorror.com/tag/net/)
[assemblyinfo](https://blog.codinghorror.com/tag/assemblyinfo/)
[versioning](https://blog.codinghorror.com/tag/versioning/)
