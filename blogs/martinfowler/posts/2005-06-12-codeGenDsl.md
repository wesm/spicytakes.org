---
title: "Generating Code for DSLs"
description: "When you build a Domain Specific Language (DSL), how do you go about making it executable. This is an easy question to answer for an internal DSL, since they are embedded into real languages. An exter"
date: 2005-06-12T00:00:00
tags: ["language workbench"]
url: https://martinfowler.com/articles/codeGenDsl.html
slug: codeGenDsl
word_count: 3064
---


I recently [wrote an
article](languageWorkbench.html) describing language oriented programming and the recent
evolution of a bunch of tools which I call language workbenches. In
that article I used a simple Domain Specific Language to illustrate my
points. Although I discussed what this DSL looked like in the article,
I didn't talk about how you would actually make that language
executable by generating code. It's useful to get an appreciation of
this because that can help you understand the nature of a language
workbench's abstract representation and how a language workbench's
generator works.


So in this article I'll take the [simple example](languageWorkbench.html#simpleExample) from
that article, and show some simple ways by which we could go about
generating code. This will lead from a simple single-pass approach to
ones that involve building up an abstract representation and using
templating to generate the code.


When thinking about the trade-offs in using DSLs, you don't
really need to understand how generation works. As I delve into how
language workbenches work, however, this will be handy.


I'll start with the custom language case. To refresh your
memory the custom language looks like:


```
mapping SVCL dsl.ServiceCall
  4-18: CustomerName
  19-23: CustomerID
  24-27 : CallTypeCode
  28-35 : DateOfCallString

mapping  USGE dsl.Usage
  4-8 : CustomerID
  9-22: CustomerName
  30-30: Cycle
  31-36: ReadDate
  

```


In order to get the custom case to work we need to transform it
into the equivalent of the internal DSL case.


```
public void Configure(Reader target) {
  target.AddStrategy(ConfigureServiceCall());
  target.AddStrategy(ConfigureUsage());
}
private ReaderStrategy ConfigureServiceCall() {
  ReaderStrategy result = new ReaderStrategy("SVCL", typeof (ServiceCall));
  result.AddFieldExtractor(4, 18, "CustomerName");
  result.AddFieldExtractor(19, 23, "CustomerID");
  result.AddFieldExtractor(24, 27, "CallTypeCode");
  result.AddFieldExtractor(28, 35, "DateOfCallString");
  return result;
}
private ReaderStrategy ConfigureUsage() {
  ReaderStrategy result = new ReaderStrategy("USGE", typeof (Usage));
  result.AddFieldExtractor(4, 8, "CustomerID");
  result.AddFieldExtractor(9, 22, "CustomerName");
  result.AddFieldExtractor(30, 30, "Cycle");
  result.AddFieldExtractor(31, 36, "ReadDate");
  return result;
}
```


The reader framework is very simple, there's just the reader
class that processes a file of events that has strategies for each
kind of event that may appear in the file. The reader reads each line,
extracts the event code, and hands off to the strategy for the
particular line. The job of configuration is to create the right
strategies and send them to the reader.


To encapsulate the code for creating the readers from an
external configuration file I that code is a separate reader builder
class. We'll explore a number of ways to do this as we go, so you'll
see several varieties of reader builder. The first one just simply
reads the custom configuration file and sets up the reader.


## Single Pass Builder


I create a builder by telling it which configuration file to
use. I then use it to configure a reader.


class ReaderBuilderTextSinglePass...


```
  public ReaderBuilderTextSinglePass(string filename) {
    _filename = filename;
  }
  private string _filename;
  public void Configure(Reader reader) {
    _reader = reader;
    using (TextReader input = File.OpenText(_filename)) {
      while ((_line = input.ReadLine()) != null)
        ProcessLine();
    }
  }
  private Reader _reader;
  private string _line = null;
```


To process a line of the custom configuration file, I test
the line with various regular expressions and react depending on what
kind of line I see. Blanks and comments are ignored.


class ReaderBuilderTextSinglePass...


```
  private void ProcessLine() {
    if (isBlank()) return;
    if (isComment()) return;
    else if (isNewMapping()) makeNewStrategy();
    else makeFieldExtract();
  }
  private bool isBlank() {
    Regex blankRE = new Regex(@"^\s*$");
    return blankRE.IsMatch(_line);
  }
  private bool isComment() {
    return _line[0] == '#';
  }
  private bool isNewMapping() {
    Regex blankRE = new Regex(@"\s*mapping");
    return blankRE.IsMatch(_line);
  }
```


When I see a mapping declaration I make a new strategy.


class ReaderBuilderTextSinglePass...


```
  private void makeNewStrategy() {
    string[] tokens = _line.Split(whitespace());
    _currentStrategy = new ReaderStrategy(tokens[1].Trim(whitespace()),
                                          Type.GetType(tokens[2]));
    _reader.AddStrategy(_currentStrategy);
  }
  private char[] whitespace() {
    char[] result = {' ', '\t'};
    return result;
  }
```


When I see a field declaration I add a new field extractor to
the strategy.


class ReaderBuilderTextSinglePass...


```
  private void makeFieldExtract() {
    string[] tokens1 = _line.Split(':');
    string targetProperty = tokens1[1].Trim(' ');
    string[] tokens2 = tokens1[0].Trim(whitespace()).Split('-');
    int begin = Int32.Parse(tokens2[0]);
    int end = Int32.Parse(tokens2[1]);
    _currentStrategy.AddFieldExtractor(begin, end, targetProperty);
  }
```


This is certainly not the prettiest parser that's been
written - even by me - but it's simple and does the job. Essentially
what I'm doing is parsing the configuration file and configuring the
reader as I go. For a simple example like this a single pass
transformation from custom DSL to framework is quick and easy.


## Two Pass Builder


Now let's look at a slightly different way of doing it. What
I'm going to do now is a two pass process. The parser reads the
configuration file and produces a data structure. A separate generator
then looks at this data structure to configure the reader.


![](configAST.gif)


Figure 1: The data structure for the abstract
representation of the language.


Figure 1 shows this data structure.
As you see it represents the abstract syntax of our mapping language.
People who remember their compiler classes will recognize this as an
Abstract Syntax Tree for the language.


Two classes manipulate this tree. The parser reads the text
input and creates the tree. The generator then reads the tree and
configures the reader object.


The parser is very similar to the parser we saw before. The
basic flow of control is identical.


class ReaderBuilderTextSinglePass...


```
  public ReaderBuilderTextSinglePass(string filename) {
    _filename = filename;
  }
  private string _filename;
  public void Configure(Reader reader) {
    _reader = reader;
    using (TextReader input = File.OpenText(_filename)) {
      while ((_line = input.ReadLine()) != null)
        ProcessLine();
    }
  }
  private Reader _reader;
  private string _line = null;
```


The only change in this start up code is to return the root
of the AST rather than a reader.


This decision making is entirely the same.


class BuilderParserText...


```
  private void ProcessLine() {
    if (isBlank()) return;
    if (isComment()) return;
    else if (isNewMapping()) makeMapping();
    else makeField();
  }
  private bool isBlank() {
    Regex blankRE = new Regex(@"^\s*$");
    return blankRE.IsMatch(_line);
  }
  private bool isComment() {
    return _line[0] == '#';
  }
  private bool isNewMapping() {
    Regex blankRE = new Regex(@"\s*mapping");
    return blankRE.IsMatch(_line);
  }
  private char[] whitespace() {
    char[] result = {' ', '\t'};
    return result;
  }
```


The changes occur in the actions once the parser has parsed
out the broad tokens. In this case the parser adds mapping objects to
the root of the AST when it sees the mapping line.


class BuilderParserText...


```
  private void makeMapping() {
    _currentMapping = new ReaderConfiguration.Mapping();
    _result.Mappings.Add(_currentMapping);
    string[] tokens = _line.Split(whitespace());
    _currentMapping.Code = tokens[1].Trim(whitespace());
    _currentMapping.TargetClassName = tokens[2].Trim(whitespace());
  }
```


Similarly when it sees fields it adds field objects.


class BuilderParserText...


```
  private void makeField() {
    ReaderConfiguration.Field f = new ReaderConfiguration.Field();
    string[] tokens1 = _line.Split(':');
    f.FieldName = tokens1[1].Trim(' ');
    string[] tokens2 = tokens1[0].Trim(whitespace()).Split('-');
    f.Start = Int32.Parse(tokens2[0]);
    f.End = Int32.Parse(tokens2[1]);
    _currentMapping.Fields.Add(f);
  }
}

```


The generator now reads this structure to configure the
framework. It's very simple class.


class BuilderGenerator...


```
  public void Configure(Reader result, ReaderConfiguration configuration) {
    foreach (ReaderConfiguration.Mapping mapping in configuration.Mappings)
      makeStrategy(result, mapping);
  }
  private void makeStrategy(Reader result, ReaderConfiguration.Mapping mapping) {
    ReaderStrategy strategy = new ReaderStrategy(mapping.Code, mapping.TargetClass);
    result.AddStrategy(strategy);
    foreach(ReaderConfiguration.Field field in mapping.Fields) 
      strategy.AddFieldExtractor(field.Start, field.End, field.FieldName);
  }
```


What's the advantage of separating the two stages? It does
cost us a bit of complexity - we have to add the AST classes. If we
were only reading and writing to a single format it's arguable whether
the AST is worth the effort - at least for this simple case. The real
advantage in the AST lies when we want to read or write multiple
formats.


Let's allow our DSL to be written in an XML concrete syntax
as well as the custom one. Again to save you running around this
document here's the XML version.


```
<ReaderConfiguration>
  <Mapping Code = "SVCL" TargetClass = "dsl.ServiceCall">
    <Field name = "CustomerName" start = "4" end = "18"/>
    <Field name = "CustomerID" start = "19" end = "23"/>
    <Field name = "CallTypeCode" start = "24" end = "27"/>
    <Field name = "DateOfCallString" start = "28" end = "35"/>
  </Mapping>
  <Mapping Code = "USGE" TargetClass = "dsl.Usage">
    <Field name = "CustomerID" start = "4" end = "8"/>
    <Field name = "CustomerName" start = "9" end = "22"/>
    <Field name = "Cycle" start = "30" end = "30"/>
    <Field name = "ReadDate" start = "31" end = "36"/>
  </Mapping>
</ReaderConfiguration>

```


To read this format all we have to do is write a new parser -
we can use the same generator.


class BuilderParserXml...


```
  ReaderConfiguration _result = new ReaderConfiguration();
  string _filename;
  public BuilderParserXml()
  {
  }
  public BuilderParserXml(string filename) {
    _filename = filename;
  }
  public void run() {
    XPathDocument doc = new XPathDocument(File.OpenText(_filename));
    XPathNavigator nav = doc.CreateNavigator();
    XPathNodeIterator it = nav.Select("//Mapping");
    while (it.MoveNext()) ProcessMappingNode(it.Current);
  }
  public ReaderConfiguration ReaderConfiguration {
    get { return _result; }
  }
  private void ProcessMappingNode(XPathNavigator nav) {
    ReaderConfiguration.Mapping currentMapping = new ReaderConfiguration.Mapping();
    _result.Mappings.Add(currentMapping);
    currentMapping.Code = nav.GetAttribute("Code", "");
    currentMapping.TargetClassName = nav.GetAttribute("TargetClass", "");
    XPathNodeIterator it = nav.SelectChildren("Field", "");
    while(it.MoveNext()) currentMapping.Fields.Add(ProcessFieldNode(it.Current));
  }
  private ReaderConfiguration.Field ProcessFieldNode(XPathNavigator nav) {
    ReaderConfiguration.Field result = new ReaderConfiguration.Field();
    result.FieldName = nav.GetAttribute("name", "");
    result.Start = Convert.ToInt16(nav.GetAttribute("start", ""));
    result.End = Convert.ToInt16(nav.GetAttribute("end", ""));
    return result;
  }
```


The XML parser is a bit easier to write, because the tools do
all the text munging for us, all we have to do is read the resulting
XML tree. It creates exactly the same objects as the custom text
parser, so the same generator will work the same. (A further advantage
of the two step process is that we test each step independently
too.)


Writing a parser like this by hand is okay for a language as
simple as this, but I wouldn't suggest it for more complicated
languages. Parser generator tools exist that can take a grammar
definition of a language and help you generate an AST. You don't have
to get much more complex than this example to make these tools
worthwhile. Although it takes a bit of effort to learn how to use
them, the results are much easier to deal with. (Essentially grammars
are a DSL for helping you parse languages into an abstract
representation.)


I won't discuss parser generators any more here because the
parsing part of the process isn't important for language workbenches.
In a language workbench, the abstract representation takes a much more
central role than it does in conventional programming - together with
the idea that you can have multiple human readable forms for the same
abstract representation.


## Using Templates for Generation


In the above examples, we used some procedural code to
generate the framework classes, which works very nicely in this case.
Another approach to the generator is to actually produce C# output
which can then be compiled in with the framework. This allows the
configuration files to be brought into the system at compile time
rather than runtime. Depending on the situation this can be a bane
rather than a boon, but it's worth exploring this approach here -
again because we'll see it again in language workbenches.


The idea behind templates is to edit your output file in its
final format, but with little markers to indicate where you want the
generator to insert code. The various server page technologies (PHP,
JSP, ASP) use templates to add dynamic content to web pages. In this
case we'll use templates to add generated content to a skeleton C#
file.


To demonstrate I'm going to use NVelocity. NVelocity is the
.NET port of the popular Java templating engine: Velocity. I like
Velocity because it's simple - many people like to use Velocity
instead of JSPs. NVelocity is still in development and as I used it I
found its documentation to be very limited. Fortunately the template
language (VTL) is the same as the Java version, and the documentation
there is usable.


Running NVelocity can be the tricky bit. Here I have a
velocity builder class that creates an instance of the velocity engine
which I can use to build the files I need.


class VelocityBuilder...


```
  public VelocityBuilder(string templateDir, string configDir, string targetDir) {
    engine = new VelocityEngine();  
    this.configDir = configDir;
    this.targetDir = targetDir;
    engine.SetProperty(RuntimeConstants_Fields.FILE_RESOURCE_LOADER_PATH, templateDir);
    engine.Init();
    config = new BuilderParserText(configDir + "ReaderConfig.txt").Run();
  }
  VelocityEngine engine;
  string configDir;
  string targetDir;
  ReaderConfiguration config;
```


When I'm doing templating I usually like to first write a
hard coded class for a single case, get that class working and
debugged, and then (as gradually as I can) replace the hard coded
elements with templated elements.


I'll show this two ways. First I'll use templating to
generate our C# configuration code from earlier on. This isn't
typically how you would do it, but it gives me a chance to demonstrate
templating on something familiar. The configuration code looks like
this.


```
public void Configure(Reader target) {
  target.AddStrategy(ConfigureServiceCall());
  target.AddStrategy(ConfigureUsage());
}
private ReaderStrategy ConfigureServiceCall() {
  ReaderStrategy result = new ReaderStrategy("SVCL", typeof (ServiceCall));
  result.AddFieldExtractor(4, 18, "CustomerName");
  result.AddFieldExtractor(19, 23, "CustomerID");
  result.AddFieldExtractor(24, 27, "CallTypeCode");
  result.AddFieldExtractor(28, 35, "DateOfCallString");
  return result;
}
private ReaderStrategy ConfigureUsage() {
  ReaderStrategy result = new ReaderStrategy("USGE", typeof (Usage));
  result.AddFieldExtractor(4, 8, "CustomerID");
  result.AddFieldExtractor(9, 22, "CustomerName");
  result.AddFieldExtractor(30, 30, "Cycle");
  result.AddFieldExtractor(31, 36, "ReadDate");
  return result;
}
```


The templated version of this looks like this.


```
public void Configure(Reader target) {
  #foreach( $map in ${config.Mappings})
  target.AddStrategy(Configure${map.TargetClassNameOnly}());
  #end
}
#foreach( $map in $config.Mappings)
private ReaderStrategy Configure${map.TargetClassNameOnly}() {
  ReaderStrategy result = new ReaderStrategy("$map.Code", typeof ($map.TargetClassName));
  #foreach( $f in $map.Fields)
  result.AddFieldExtractor($f.Start, $f.End, "$f.FieldName");
  #end
  return result;
}
#end
```


Since I won't assume you're familiar with VTL (Velocity
Template Language) I'll explain the elements I'm using.


The first bit is references to parameters. You can refer to a
parameter in VTL by using the syntax `$parameterName` or
`${parameterName}` (the latter is best when you are running
the parameter references directly against other text with no spaces).
Once you have the parameter you can call methods and access properties
on that parameter freely.


To set things so the parameter is accessible you need to put
the object into the context of the engine when you run the
mapping.


```
private void GenerateParameterized() {
  VelocityContext context = new VelocityContext();
  context.Put("config", this.config);
  using (TextWriter target = File.CreateText(targetDir + "ReflectiveTemplateBuilder.cs"))
    engine.MergeTemplate("ReflectiveTemplateBuilder.cs.vm", context, target);
}
```


(You'll notice I've defined a property
`TargetClassNameOnly` on Mapping. This returns the name of
the target class as `ServiceCall` rather than
`dsl.ServiceCall`, useful since I'm preserving the breakout
of methods in the generated configuration code. Although the AST is
mostly a dumb data structure there's no reason why you shouldn't move
useful behavior in there to avoid duplication.)


The second bit of VTL is
the looping directive `#foreach ($item in $collection). This
allows me to loop through the mappings and fields.`


The resulting generated code looks like this.


```
public void Configure(Reader target) {
        target.AddStrategy(ConfigureServiceCall());
        target.AddStrategy(ConfigureUsage());
      }
    private ReaderStrategy ConfigureServiceCall() {
  ReaderStrategy result = new ReaderStrategy("SVCL", typeof (dsl.ServiceCall));
        result.AddFieldExtractor(4, 18, "CustomerName");
        result.AddFieldExtractor(19, 23, "CustomerID");
        result.AddFieldExtractor(24, 27, "CallTypeCode");
        result.AddFieldExtractor(28, 35, "DateOfCallString");
        return result;
}
    private ReaderStrategy ConfigureUsage() {
  ReaderStrategy result = new ReaderStrategy("USGE", typeof (dsl.Usage));
        result.AddFieldExtractor(4, 8, "CustomerID");
        result.AddFieldExtractor(9, 22, "CustomerName");
        result.AddFieldExtractor(30, 30, "Cycle");
        result.AddFieldExtractor(31, 36, "ReadDate");
        return result;
}
```


The line formatting is a bit messed up, but other than that
it's pretty close to the original.


So this generates the same code that we wrote by hand - but
this isn't typically the way you'd work with a generator. What we've
done is generated the configuration of the runtime interpretor which
uses reflection to populate classes and fields. That's what you have
to do for a runtime interpreter, but when you use code generation you
can do it all with compile time constructs.


Instead of using a single strategy class that uses reflection
to do its work I can use multiple strategy classes, one for each kind
of event. These strategies can then call classes and methods directly.
Such a strategy might look like this.


```
public class InlineStrategy : IReaderStrategy  {
  public string Code {
    get { return "SVCL"; }
  }
  public object Process(string line)  {
    ServiceCall result = new ServiceCall();
    result.CustomerName = line.Substring(4,15);
    result.CustomerID = line.Substring(19,5);
    result.CallTypeCode = line.Substring(24,4);
    result.DateOfCallString = line.Substring(28,8);
    return result;
  }
}
```


Again I did this by writing this one case first, getting it
working and then turning it into a template. Here's the template.


```
public class $map.MapperClassName : IReaderStrategy
{
  public string Code {
    get { return "$map.Code"; }
  }

  public object Process(string line)  {
    $map.TargetClassName result = new ${map.TargetClassName}();
    #foreach( $f in $map.Fields)
    result.$f.FieldName = line.Substring($f.Start, $f.Length);
    #end
    return result;
  }
}
```


This produces two classes for our sample.


```
public class MapSVCL : IReaderStrategy
{
  public string Code {
    get { return "SVCL"; }
  }

  public object Process(string line)  {
    dsl.ServiceCall result = new dsl.ServiceCall();
          result.CustomerName = line.Substring(4, 15);
          result.CustomerID = line.Substring(19, 5);
          result.CallTypeCode = line.Substring(24, 4);
          result.DateOfCallString = line.Substring(28, 8);
          return result;
  }
}
```


```
public class MapUSGE : IReaderStrategy
{
  public string Code {
    get { return "USGE"; }
  }

  public object Process(string line)  {
    dsl.Usage result = new dsl.Usage();
          result.CustomerID = line.Substring(4, 5);
          result.CustomerName = line.Substring(9, 14);
          result.Cycle = line.Substring(30, 1);
          result.ReadDate = line.Substring(31, 6);
          return result;
  }
}
```


To hook these classes into a reader, we need to generate a
builder that will know about the classes we've just generated. Here's
the template for that


```
public class ReaderBuilderInline  {
  public void Configure(Reader target) {
    #foreach( $map in $config.Mappings)
    target.AddStrategy(new ${map.MapperClassName}());
    #end
  }
}
```


which generates


```
public class ReaderBuilderInline  {
  public void Configure(Reader target) {
          target.AddStrategy(new MapSVCL());
          target.AddStrategy(new MapUSGE());
        }
}
```


The resulting code is more voluminous, but usually that
doesn't matter much. You can now have the compiler check this code -
after all if you're using a statically typed language you might as
well the benefit of it. Often people find this kind of code easier to
follow than configuration code, at least once they get used to
manipulating VTL. It does stop you from modifying the configuration at
runtime, so this wouldn't be suitable for some scenarios. However
there's no reason why you can't use similar techniques to generate
scripts that can be executed at runtime. Indeed the lisp style of
language oriented programming is more like this, you write a generator
that generates lisp code that's executed at run time. This is where
lisp's macro capabilities shine.


## Closing Thoughts


This is a very simple example, but it does illustrate various
approaches in generating code from a DSL. In particular its useful to
understand the value in generating an AST to decouple generation from
parsing and how you can use a templating language to generate code
from the AST. Both of these techniques crop up in using language
workbenches.


---
