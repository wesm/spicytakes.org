---
title: "Avoiding Undocumentation"
date: 2005-11-21
url: https://blog.codinghorror.com/avoiding-undocumentation/
slug: avoiding-undocumentation
word_count: 699
---

Have you ever noticed that much of the online MSDN .NET framework help is... not helpful? Take the the MSDN help for the IBindingList.AddIndex method, for example:


![](https://blog.codinghorror.com/content/images/2025/05/image-151.png)


Scott Swigart calls this **undocumentation**, and elaborates further in [his blog post](http://swigartconsulting.blogs.com/tech_blender/2005/07/the_undocumente.html):


> *This is an example where quacking like a duck doesn’t make you a duck. This looks like documentation. It shows up in the help alongside documentation, it’s indexed like documentation, but it’s not documentation. It doesn’t actually tell anyone anything they didn’t already know.
> Large swaths of the Framework are undocumented in exactly this way, and many v1.0 SDKs are, well, very undocumented.
> Honestly, my problem isn’t that lots of stuff is undocumented. It’s that Microsoft spent time writing this undocumentation, proof-reading this undocumentation, and putting this undocumentation through the same process as the real documentation. I don’t know how much time was spent undocumenting things, but I’m guessing that if you add it all up, it’s a lot.
> I guess on the documentation teams, there must be some law that no class, property, method, or event will show up in the help with a big, bold, “Undocumented.”
> **Can we stop pretending? Can you just mark everything as Undocumented until you get around to writing real documentation for it?** Maybe even include a “Click here to vote to have this documented.” For a simple test, if it doesn’t include a code example, it’s not documented. Just mark it as such and move on.*


What really scares me is that tools like [GhostDoc](https://submain.com/GhostDoc/) produce exactly this kind of useless undocumentation. Now, I understand that GhostDoc is just a tool intended to assist developers in producing real documentation. And like all tools, it can be used properly or abused. But whatever you do, **please don’t knowingly produce undocumentation for your applications**. Have some respect for your users and your fellow developers. Either take the time to write helpful documentation, or have the guts to acknowledge that *there simply is no documentation*.


I encounter undocumentation all the time when I’m rooting around for help on the .NET framework. For example, take a look at the MSDN [help for the PassportIdentity.SignOut method](http://msdn2.microsoft.com/en-us/library/system.web.security.passportidentity.signout.aspx).* This particular example of undocumentation is even more egregious, because *it actually includes code samples!* Utterly useless, one-line code samples. In each language.

kg-card-begin: html

```

' This example demonstrates how to sign a user out of Passport.
' local GIF file that the user is redirected to.
Dim signOutGifFile As String = "signout.gif"
' Signs the user out of their Passport Profile and displays the SignOut.gif file.
System.Web.Security.PassportIdentity.SignOut(signOutGifFile)

```

kg-card-end: html
kg-card-begin: html

```

// This example demonstrates how to sign a user out of Passport.
// local GIF file that the user is redirected to.
string signOutGifFile = "signout.gif";
// Signs the user out of their Passport Profile and displays the SignOut.gif file.
System.Web.Security.PassportIdentity.SignOut(signOutGifFile);

```

kg-card-end: html

But hey, at least the code samples are valid. As a Vertigo developer pointed out a few months ago, the code samples on the MSDN help page for IComparable.CompareTo aren’t even correct:

kg-card-begin: html

```

public class Temperature : IComparable
{
public int CompareTo(object obj) {
if(obj is Temperature)
{
Temperature temp = (Temperature) obj;
return m_value.CompareTo(temp.m_value);
}
throw new ArgumentException(
"object is not a Temperature");
}
protected int m_value;
public int Value
{
get { return m_value; }
set { m_value = value; }
}
public int Celsius
{
get { return (m_value-32) / 2; }
set { m_value = value * 2 + 32; }
}

```

kg-card-end: html

There are any number of websites documenting how to [convert Fahrenheit to Celsius](http://geography.about.com/c/ht/00/07/How_Convert_Fahrenheit_Celsius0962932698.htm) and vice-versa:

1. Take the temperature in Fahrenheit and subtract 32.
2. Divide by 1.8.
3. The result is degrees Celsius.


Oddly enough, the C++ sample on the same page is correct. I guess C++ developers really are smarter.


Grousing about all this undocumentation is funny, but it doesn’t magically produce useful documentation. Here’s something that might, though: **why not make the .NET framework documentation a Wiki?**


*Yes, we work on a few apps that use Microsoft Passport. God help us. God help us all.

[documentation](https://blog.codinghorror.com/tag/documentation/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[msdn](https://blog.codinghorror.com/tag/msdn/)
[.net framework](https://blog.codinghorror.com/tag/net-framework/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
