---
title: "CityDesk Entity Classes"
date: 2003-01-03
url: https://www.joelonsoftware.com/2003/01/03/citydesk-entity-classes/
word_count: 745
---


*Comment: This article is Fog Creek Internal documentation, likely to be of interest only to hard core VB 6.0 geeks working with databases through DAO. Rather than use the DAO classes directly and scattering SQL syntax throughout our code, we try to isolate database access by using a thin layer which provides simple objects that map to underlying data. These objects are called “entities.”* *About 99% of what we do with databases consists of:*  *select one record* *enumerate records, possibly matching a query* *change a record* *add a new record* *The goal of entity classes is to make these things easy and consistent.* To isolate and simplify all access to the CityDesk database, all database access code goes through a set of classes called *entity classes*. These are VB user-defined classes, which are easily identified because the class names always start with the capital letter **E** followed by the name of the table. For example, you would use an entity class called **EArticle** to access the table **tblArticle**. There does not have to be an underlying *physical* table for each entity class. If you need to do a sophisticated query that joins multiple tables, this can be done inside an entity which still starts with **E** and has some sensible name but which does not correspond to a physical table. **Golden Rule:** Never let entity classes cause you to do something inefficient with the database. *Comment: A lot of times people using the entity classes forget about what’s involved in the underlying query, and end up writing code that’s ridiculously inefficient. For example, updating a table by looping through it and committing each change, rather than using a SQL UPDATE statement. This is explicitly forbidden.* Each entity class has public members for each of the columns in the table with the exact same names. For example, for tblArticle, EArticle has ixArticle, ixSet, ixLanguage, etc. These are *not* implement as property get/lets, that just makes the code ugly; they are implemented as plain members. There is ONE EXCEPTION: any large or blob type fields are implemented as property get/lets which defer the actual database access until you access *that particular field*. *Comment: CityDesk has a lot of tables containing a large blob field, for example, the table of articles. If you’re enumerating the articles in order to list them, you don’t want to spend any cycles extracting the blobs.* When you create a new entity object, name it with the same name as the table in lower case, for example: Dim article As EArticle : Set article = New EArticle Creating a new entity object initializes all the fields to something sensible and initializes the primary key ix field (e.g. ixArticle) to -1. Entity objects usually have these methods: .Load(ix)  Loads the object from a single record, where the primary key is ix.  Dim article As EArticle : Set article = New EArticle
article.Load 1 ‘ load article where ixArticle = 1
Debug.Print article.ixLanguage .Save  Commits any changes. If the primary key is still -1, this does an INSERT and **always returns the just inserted primary key** as a return value. If the primary key is not -1, this does an Update…Where and still returns the primary key.  ‘ Add new article:
Dim article As EArticle : Set article = New EArticle
article.ixLanguage = 1
‘ set all the other fields
Dim ixArticleNew: ixArticleNew = article.Save ‘ Now edit it:
article.Load ixArticleNew
article.ixLanguage = 2
article.Save *Comment: We always use autonumber/identity fields for primary keys. One of the most maddening things about SQL is the numerous, inconsistent and unreliable ways of getting the identity field you just inserted.* .List
.GetNext  Used for enumerating through the records. The plain version of List starts enumerating them all. *If there are zero matching records*, that is, if EOF is true immediately, List returns False, in case you want to have different code for that case. If you need to return any other kind of list, for example, all non-deleted, you use a variation of List like ListNonDeleted, which can take arguments. Then .GetNext loads the first record and returns true if not EOF.   ‘ List templates:
Dim template As ETemplate: Set template = New ETemplate
If template.List Then
    While template.GetNext
         Debug.Print template.Name
         ‘ No need to move next!
    Wend
Else
    Debug.Print “Nothing!”
End If *Comment: A common mistake in writing DAO code is forgetting the MoveNext at the bottom of your loop. This eliminates the need for it.* **
