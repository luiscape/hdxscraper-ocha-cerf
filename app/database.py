#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Configuring a database.
'''
import os
import scraperwiki

from app.utilities.item import item
from app.utilities.load import loadJSONFile

def createTables(instance='config/config.json'):
  '''
  Creates tables a database based on the
  tables specified in the configuration file.

  '''
  #
  # Loading database information
  # from config file.
  #
  database = loadJSONFile(instance)['database']

  #
  # Build each table.
  #
  for table in database:

    #
    # Construct SQL statement.
    #
    table_sql = ""
    for column in table['columns']:
      s = '%s %s, ' % (column['field_name'], column['type'])
      table_sql += s

    statement = 'CREATE TABLE IF NOT EXISTS "%s" (%sPRIMARY KEY (%s))' % (table['name'], table_sql, ", ".join(table['primary_key']))

    #
    # Send statements to the database.
    #
    try:
      scraperwiki.sql.execute(statement)
      print("%s table `%s` created." % (item('bullet'), str(table['name'])))

    except Exception as e:
      print('%s Table `%s` could not be created.' % (item('error'), table['name']))
      print(e)
      return False
