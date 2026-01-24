---
title: "Custom wsdlHelpGenerator + webroot = error"
date: 2005-04-07
url: https://blog.codinghorror.com/custom-wsdlhelpgenerator-webroot-error/
slug: custom-wsdlhelpgenerator-webroot-error
word_count: 286
---

Why are the smallest bugs in the .NET framework always the most disproportionately frustrating? Take the wsdlHelpGenerator element, for example. Sure, it seems straightforward enough; you want to replace the default crappy, **random hash sorted list of Web Service methods with one that’s (shock!) in alphabetical order**. I know, it’s crazy talk, but bear with me. So you’d...

1. Make a copy of the file: `C:WINDOWSMicrosoft.NETFrameworkv1.1.4322CONFIGDefaultWsdlHelpGenerator.aspx`
2. Rename that file to `CustomWsdlHelpGenerator.aspx` and place it in the root of your Web Service solution
3. Open the file and make a simple one-line modification, replacing `Hashtable methodsTable` with `SortedList methodsTable`
4. Modify your `Web.config` to include the following:

kg-card-begin: html

```
<webServices>  
<wsdlHelpGenerator href="CustomWsdlHelpGenerator.aspx" />  
</webServices>
```

kg-card-end: html

And it works great! Well, as long as you deploy your Web Service to a subfolder under the webroot (e.g., http://staging.company.com/mywebservice/). However. If you deploy this very same code to a root URL (e.g., http://mywebservice.company.com/,) you get this exciting, ultra-fatal error:


> *Configuration Error
> **Description:** An error occurred during the processing of a configuration file required to service this request. Please review the specific error details below and modify your configuration file appropriately.
> **Parser Error Message:** Exception in configuration section handler.*


This makes deploying to production a lot more, uh, *thrilling* than it would otherwise be. Commenting the `wsdlHelpGenerator` line out “fixes” the problem. So does moving the webservice to a subfolder under the root.


This egregious bug in the .NET framework really pisses me off, particularly since it has persisted into 1.1 SP1. I can find lots of people complaining about this in Google Groups, but I can’t find *one single workaround*. Can you? Class? Bueller? Bueller?

[c#](https://blog.codinghorror.com/tag/c-2/)
[.net framework](https://blog.codinghorror.com/tag/net-framework/)
[web services](https://blog.codinghorror.com/tag/web-services/)
[web configuration](https://blog.codinghorror.com/tag/web-configuration/)
[wsdlhelpgenerator](https://blog.codinghorror.com/tag/wsdlhelpgenerator/)
