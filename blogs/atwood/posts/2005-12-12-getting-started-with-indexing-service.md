---
title: "Getting Started with Indexing Service"
date: 2005-12-12
url: https://blog.codinghorror.com/getting-started-with-indexing-service/
slug: getting-started-with-indexing-service
word_count: 1055
---

Microsoft’s ancient circa-1997 Indexing Service gets no respect. And that’s a shame, because it’s a surprisingly decent content indexing engine that supports [arbitrary metadata](https://blog.codinghorror.com/whatever-happened-to-the-meta-tag/). Sure, there may be better choices, but **Indexing Service’s saving grace is that it’s *completely free*.** It’s a default component of Windows 2000, Windows XP Pro, and Windows 2003 Server. And I’ll show you how you can programmatically query it from .NET, too.


First, let’s set us up the bomb a little Indexing Service catalog to play with:

1. In Computer Management, right click Indexing Service and select New, Catalog.
2. Give the new catalog a name. You’ll use this name in code to select the right catalog, so treat it like a variable name and use something that makes sense. I used **test**.
3. Select a location path for the catalog. Note that this is NOT the location of the content you want to index, but the physical location of the hidden **catalog.wci** index folder. I know, it’s confusing. I chose **c:test** as my location.
4. Expand the new Test catalog, and right click the Directories folder. Select New, Directory. You can ignore the UNC textbox unless you’re indexing content on a remote computer. Enter the path to the content you wish to index. I chose **c:testindex-me**.


Click OK, restart Indexing Service, and you end up with something like this:


![](https://blog.codinghorror.com/content/images/2025/03/image-375.png)


Now, if you plop files in the index-me folder, Index Server will automatically index them – assuming an [appropriate IFilter is installed](http://www.ifilter.org/default.htm). Click on the Indexing Service node to watch it happen; the total indexed and unindexed document counts are shown in real time.


![](https://blog.codinghorror.com/content/images/2025/03/image-374.png)


After you’ve added some documents, bring up the integrated query – click on the Query the Catalog node under your catalog – and verify that, indeed, you can find specific words in your documents. Ok, full text search works. That’s not very exciting... **until you add some custom metadata to the mix!** Plop this HTML file in the index-me folder:

kg-card-begin: html

```
<head><title>Html Test Page 2</title><!-- automatically maps to DocAuthor in Index Server --><meta name=“author” content=“John Doe” /><!-- automatically maps to DocKeywords in Index Server --><meta name=“keywords” content=“giraffe, elephant, mouse, aardvark” /><!-- automatically maps to DocSubject in Index Server --><meta name=“subject” content=“animal” /><!-- custom meta tags  --><meta name=“testing” content=“dos” /><meta name=“metacategory” content=“awesome” /><meta name=“metanumber” content=“two” /><meta name=“metainteger” content=“222” /></head><body>Jackdaws love my big sphinx of quartz.</body> 
```

kg-card-end: html

Once you do, you’ll notice that the Properties folder for your Catalog contains some interesting new properties that correspond to our <meta> tags:


![](https://blog.codinghorror.com/content/images/2025/03/image-373.png)


As noted in the HTML comments, a few of the <meta> tags automagically map directly to standard Index Server properties. You can query these properties directly using Indexing Service Query Language:

kg-card-begin: html

```

$DocAuthor John AND Doe
$DocKeywords mouse
$DocSubject animal
$DocTitle test

```

kg-card-end: html

That’s nice for free, but the truly custom properties require a bit more work. If you try “$testing dos,” you’ll get an unceremonious “No such property” message. The first thing we need to do is **mark the property cacheable**. Right click the “testing” property in the properties folder and check the “Cached” checkbox:


![](https://blog.codinghorror.com/content/images/2025/03/image-372.png)


Take note of the storage level drop-down as well, because it has a special meaning: **properties marked as primary storage can be returned in the search results.** This can be a big deal for performance, since you can have as many bits of metadata as you want coming back in the initial search results.


You’ll need to re-index once you mark a property cacheable. There are two ways to do that:

1. **The scorched earth way**: stop the service, delete the hidden catalog.wci file, then restart the service.
2. **The obscure UI way**: right click the directory in the Directories folder of your Catalog, select “All Tasks,” then select “Full Rescan” or “Incremental Rescan.”


Once we’ve cached the property and rescanned, we now need to map the friendly name “testing” to the GUID of the new property. You can either [map friendly names](https://web.archive.org/web/20051219043220/http://www.ifiltershop.com/friendly-names-iis.html) with a manually edited text file (see MSKB 1, MSKB 2), or you can do it in code at query time. We’ll do it through code.


Create a new ASP.NET project and **add a project reference to the ixsso COM object**:


![](https://blog.codinghorror.com/content/images/2025/03/image-371.png)


Next, place a TextBox, Button, and DataGrid on the default webpage. Add using statements for System.Data.OleDb and Cisso. Then paste this code in the Button1_Click event:

kg-card-begin: html

```

CissoQueryClass q = new CissoQueryClass();
CissoUtilClass util = new CissoUtilClass();
OleDbDataAdapter da = new OleDbDataAdapter();
DataSet ds = new DataSet(“IndexServerResults”);
q.Query = TextBox1.Text;
q.DefineColumn(“testing = d1b5d3f0-c0b3-11cf-9a92-00a0c908dbf1 testing”);
q.Catalog = “Test”;
q.SortBy = “rank[d]”;
q.Columns = “rank, path, size, testing”;
//q.MaxRecords = 1000;
util.AddScopeToQuery(q, @“c:testindex-me”, “deep”);
object o = q.CreateRecordset(“nonsequential”);
da.Fill(ds, o, “IndexServerResults”);
DataGrid1.DataSource = ds;
DataGrid1.DataBind();

```

kg-card-end: html

Entering a query of “$testing dos” returns the above HTML document, as we would expect. **The ability to query arbitrary metadata along with full-text search makes index server much more flexible and powerful than I had ever realized**. A set of custom generated HTML could easily index entirely database-driven websites, in tandem with the rich Indexing Service query language ([examples](https://web.archive.org/web/20050526083856/http://www.codeproject.com/asp/indexserver.asp)).


In general Indexing Services just works, but there are some non-obvious things I ran into while experimenting with it:

- Custom properties set to primary storage can be returned in the search results, but they are always returned as datatype “object,” which means the DataGrid can’t bind to them automatically.
- I couldn’t get pagination to work using the CissoQueryClass object properties. This means you’ll realistically need to limit the number of results with the MaxRecords property, which does work.
- There’s a hidden performance tuning option. Right click the Indexing Service node, then select “All Tasks” and “Tune Performance.”
- Be sure to turn on abstracts – short textual summaries – for your catalog. You can do this by right clicking the Catalog, selecting Properties, unchecking Inherit, then checking “Generate Abstracts.”
- The list of “stop words” for Indexing Services can be edited in c:windowssystem32noise.enu. See this [MSKB article](https://web.archive.org/web/20060302190255/http://support.microsoft.com/default.aspx?scid=kb;en-us;247561) for more details.
- If you are querying Indexing Services from ASP.NET, bear in mind that *your queries will only return documents that the ASP.NET process account has permissions to!* Don’t let this one bite you like it did me.

[indexing service](https://blog.codinghorror.com/tag/indexing-service/)
[.net](https://blog.codinghorror.com/tag/net/)
[windows](https://blog.codinghorror.com/tag/windows/)
[content indexing](https://blog.codinghorror.com/tag/content-indexing/)
[metadata](https://blog.codinghorror.com/tag/metadata/)
