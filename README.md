### OCHA CERF Collector
Collector for [OCHA's CERF](http://www.unocha.org/cerf/) funding data. Designed to work on [ScraperWiki](http://scraperwiki.com).

[![Build Status](https://travis-ci.org/luiscape/hdxscraper-ocha-cerf.svg)](https://travis-ci.org/luiscape/hdxscraper-ocha-cerf) [![Coverage Status](https://coveralls.io/repos/luiscape/hdxscraper-ocha-cerf/badge.svg?branch=master&service=github)](https://coveralls.io/github/luiscape/hdxscraper-ocha-cerf?branch=master)

### Usage
Make use of the `Makefile` instructions as follows:

```shell
$ git clone [THIS REPOSITORY]
$ cd [THIS REPOSITORY]
$ make setup && make test
$ make run
```

The results will be available in a `scraperwiki.sqlite` database in the repository's root path.
