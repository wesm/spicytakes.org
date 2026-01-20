---
title: "Introducing vbench, new code performance analysis and monitoring tool"
date: 2011-12-18T00:00:00
tags: ["python", "benchmarks"]
slug: introducing-vbench-new-code-performance-analysis-and-monitoring-tool
word_count: 747
source_file: blog/introducing-vbench-new-code-performance-analysis-and-monitoring-tool/index.qmd
content_type: blog
---

Do you know how fast your code is? Is it faster than it was last week? Or a month ago? How do you know if you accidentally made a function slower by changes elsewhere? Unintentional performance regressions are extremely common in my experience: it's hard to unit test the performance of your code. Over time I have gotten tired of playing the game of "performance whack-a-mole". Thus, I started hacking together a little weekend project that I'm calling **<a href="http://github.com/pydata/vbench" title="vbench" target="_blank">vbench</a>**. If someone thinks up a cleverer name, I'm all ears.

<a href="http://pandas.sourceforge.net/vbench.html " title="vbench page" target="_blank">Link to pandas benchmarks page produced using vbench</a>

## What is vbench?

vbench is a super-lightweight Python library for running a collection of performance benchmarks over the course of your source repository's history. Since I'm a GitHub user, it only does git for now, but it could be generalized to support other VCSs. Basically, you define a benchmark:

```
common_setup = """
from pandas import *
import pandas.util.testing as tm
import random
import numpy as np
"""

setup = common_setup + """

N = 100000
ngroups = 100

def get_test_data(ngroups=100, n=N):
    unique_groups = range(ngroups)
    arr = np.asarray(np.tile(unique_groups, n / ngroups), dtype=object)

    if len(arr) < n:
        arr = np.asarray(list(arr) + unique_groups[:n - len(arr)],
                         dtype=object)

    random.shuffle(arr)
    return arr

df = DataFrame({'key1' : get_test_data(ngroups=ngroups),
                'key2' : get_test_data(ngroups=ngroups),
                'data' : np.random.randn(N)})
def f():
    df.groupby(['key1', 'key2']).agg(lambda x: x.values.sum())
"""
stmt2 = "df.groupby(['key1', 'key2']).sum()"
bm_groupby2 = Benchmark(stmt2, setup, name="GroupBy test 2",
                        start_date=datetime(2011, 7, 1))
```

Then you write down the information about your repository and how to build any relevant DLLs, etc., that vary from revision to revision:

```
REPO_PATH = '/home/wesm/code/pandas'
REPO_URL = 'git@github.com:wesm/pandas.git'
DB_PATH = '/home/wesm/code/pandas/gb_suite/benchmarks.db'
TMP_DIR = '/home/wesm/tmp/gb_pandas'
PREPARE = """
python setup.py clean
"""
BUILD = """
python setup.py build_ext --inplace
"""
START_DATE = datetime(2011, 3, 1)
```

Then you pass this info, plus a list of your benchmark objects, to the `BenchmarkRunner` class:

```
runner = BenchmarkRunner(benchmarks, REPO_PATH, REPO_URL,
                         BUILD, DB_PATH, TMP_DIR, PREPARE,
                         run_option='eod', start_date=START_DATE)
runner.run()
```

Now, the `BenchmarkRunner` makes a clone of your repo, then runs all of the benchmarks once for each revision in the repository (or some other rule, e.g. I've set `run_option='eod'` to only take the last snapshot on each day). It persists the results in a SQLite database so that you can rerun the process and it will skip benchmarks it's already run (this is key when you add new benchmarks, only the new ones will be updated). Benchmarks are uniquely identified by the MD5 hash of their source code.

This is the resulting plot over time for the above GroupBy benchmark related to some Cython code that I worked on late last week (where I made a major performance improvement in this case):

[<img src="https://wesmckinney.com/images/vbench_demo1.png" alt="" title="vbench_demo1" width="997" height="526" class="aligncenter size-full wp-image-383" />][1]

Here is a <a href="https://github.com/wesm/pandas/blob/5d4bf8febdad007d7804c2e91c5bead01ca92637/vb_suite/benchmarks.py" title="suite" target="_blank">fully-formed vbench suite</a> in the pandas git repository.

## Kind of like <a href="https://github.com/tobami/codespeed" title="codespeed" target="_blank">codespeed</a> and <a href="http://speed.pypy.org" title="speed.pypy.org" target="_blank">speed.pypy.org</a>?

Before starting to write a new project I looked briefly at codespeed and the excellent work that the PyPy guys have done with **speed.pypy.org**. But then I started thinking, you know, Django web application, JSON requests to upload benchmark results? Seemed like far too much work to do something relatively simple. The dealbreaker is that codespeed is just a web application. It doesn't actually (to my knowledge, someone correct me if I'm wrong?) have any kind of a framework for orchestrating the running of benchmarks throughout your code history. That is what this new project is for. I actually see a natural connection between vbench and codespeed, all you need to do is **write a script to upload your vbench results to a codespeed web app!**

At some point I'd like to build a simple web front end or wx/Qt viewer for the generated vbench database. I've never done any JavaScript, but it would be a good opportunity to learn. Knowing me, I might break down and hack out a stupid little wxPython app with an embedded matplotlib widget anyway.

Anyway, I'm really excited about this project. It's very prototype-y at the moment but I tried to design it in a nice and extensible way. I also plan to put all my git repo analysis tools in there (like code churn graphs etc.) so it should become a nice little collection of tools.

## Other ideas for extending

  * Dealing with API changes
  * Multiple library versions (e.g. NumPy) or Python versions

 [1]: https://wesmckinney.com/images/vbench_demo1.png