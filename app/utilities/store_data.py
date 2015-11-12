#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Function that stores records from a Python
dictionary into a SQLite database table.

'''
import os
import scraperwiki

from app.utilities.item import item
from app.utilities.load import loadJSONFile

def storeData(data, table):
  '''
  Store records in a SQLite database.

  '''
  #
  # Check no NULL values are passed.
  #
  # pops = []
  # for key in data.keys():
  #   if data.get(key) is None:
  #     pops.append(key)

  # for key in pops:
  #   data.pop(key)
  print('{bullet} Storing {n} records in database.'.format(bullet=item('bullet'), n=len(data)))
  for record in data:
    scraperwiki.sqlite.save(record.keys(), record, table_name=table)
