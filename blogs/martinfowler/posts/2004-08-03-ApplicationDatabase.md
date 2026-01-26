---
title: "Application Database"
description: "I use the term Application Database for a database that is 	controlled and accessed by a single application, (in contrast to anIntegrationDatabase). Since only a single application 	accesses the datab"
date: 2004-08-03T00:00:00
tags: ["application integration", "database"]
url: https://martinfowler.com/bliki/ApplicationDatabase.html
slug: ApplicationDatabase
word_count: 233
---


I use the term Application Database for a database that is
	controlled and accessed by a single application, (in contrast to an
	[IntegrationDatabase](https://martinfowler.com/bliki/IntegrationDatabase.html)). Since only a single application
	accesses the database, the database can be defined specifically to
	make that one application's needs easy to satisfy. This leads to a
	more concrete schema that is usually easier to understand and often
	less complex than that for an [IntegrationDatabase](https://martinfowler.com/bliki/IntegrationDatabase.html).


To share data with other applications the controlling application
	may provide services. It also may provide a
	[ReportingDatabase](https://martinfowler.com/bliki/ReportingDatabase.html) for a wider range of read-only use.


One the great advantages of an application database is that it is
	easier to change since all its use is encapsulated by
	a single application. [Evolutionary
	database design and database refactoring](https://martinfowler.com/articles/evodb.html) can be used to make
	significant changes to an application database's design even after
	the database is put into production.


An application database schema is usually best designed and
	controlled by the application team themselves - often by having an
	experienced database professional as a member of the application
	team. This database professional needs to work very closely with the
	rest of the application developers to keep the database close to the
	needs of the rest of the application.


As people discuss Service Oriented Architecture a common term is
	that of an autonomous application - which seems to imply an
	application whose data is stored in an application database.
