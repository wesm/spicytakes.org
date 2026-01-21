---
title: "A quick one: Testing log messages"
date: 2011-12-28
url: https://www.elidedbranches.com/2011/12/quick-one-testing-log-messages.html
word_count: 260
---

I'm writing a talk on unit testing for work, and it reminded me of one of the coolest things I learned from the ZK code base with respect to testing: testing log messages.
You probably don't want to rely too heavily on log messages for testing, but sometimes it's the only indication you have that a certain condition happened. So how do you test it?
Layout layout = Logger.getRootLogger().getAppender("CONSOLE")
.getLayout();
ByteArrayOutputStream os = new ByteArrayOutputStream();
WriterAppender appender = new WriterAppender(layout, os);
appender.setImmediateFlush(true);
appender.setThreshold(Level.INFO);
Logger zlogger = Logger.getLogger("org.apache.zookeeper");
zlogger.addAppender(appender);
try {
...
} finally {
zlogger.removeAppender(appender);
}
os.close();
LineNumberReader r = new LineNumberReader(new StringReader(os
.toString()));
String line;
Pattern p = Pattern.compile(".*Majority server found.*");
boolean found = false;
while ((line = r.readLine()) != null) {
if (p.matcher(line).matches()) {
found = true;
break;
}
}
Assert.assertTrue(
"Majority server wasn't found while connected to r/o server",
found);
}
From
[ReadOnlyModeTest](http://svn.apache.org/viewvc/zookeeper/trunk/src/java/test/org/apache/zookeeper/test/ReadOnlyModeTest.java?revision=1195854&view=markup)
.
Kudos to Patrick Hunt (@phunt)
,
the original author.
12/29 Edit:
Some folks have found this cringe-worthy. I agree. This is not a testing method that should be common in any code base, and for goodness sakes if you can find a different way to ensure something happened, do so. But there are a few times when this kind of test splits the difference between expedience and coverage (ie, I'd rather write a test to validate a log statement then just make the change and observe the log, or refactor the code base to expose some fact that the conditions causing the log were met in order to be able to test it).