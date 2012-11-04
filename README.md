biz-news
========

Identify mentions of companies in a collection of rss feeds, using names and aliases in freebase.

Uses the new [regex python module](http://pypi.python.org/pypi/regex) to match a giant regular expression.

Expressed as a [mrjob](https://github.com/Yelp/mrjob) job so it can run locally, on a hadoop cluster or on EMR.

Intended as an experiment with mrjob and the new regex module, rather than for serious use.


preparation
-----------

* run `./get-biz.py` to fetch company names and aliases from freebase
* edit mrjob.conf with your details
* `pip install -r dependencies`
* `tar czvf modules.tar.gz businesses.py`

run locally
-----------

`MRJOB_CONF=mrjob.conf ./biz-news.py <sources >output`

run on your hadoop cluster
--------------------------

* make sure you have `python` and the modules in `dependencies` installed across your cluster
* `MRJOB_CONF=mrjob.conf ./biz-news.py -r emr <sources >output`

run on EMR
----------

`./runOnEMR`
