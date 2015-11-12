#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for checking that the database
configuration is setup correctly.
'''

import os
import unittest
import app.utilities.load as Load

class TestDatabaseConfiguration(unittest.TestCase):
  '''
  Unit tests for the checking the database properties of
  the configuration files.
  '''
  def setUp(self):
    dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    self.folder = os.path.join(dir_name, 'config')
    self.files = [
        os.path.join(self.folder, 'config.json')
      ]

  def test_structure(self):
    '''
    database.configuration.file:  Test for the structure of configuration files.
    '''
    keys = ['name', 'primary_key', 'columns']
    for file in self.files:
      result = Load.loadJSONFile(file)
      for table in result['database']:
        for key in table.keys():
          self.assertIn(key, keys)


class TestTableConfiguration(unittest.TestCase):
  '''
  Unit tests for checking if the tables
  contain the right column names.
  '''
  def setUp(self):
    dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    self.folder = os.path.join(dir_name, 'config')
    self.files = [
        os.path.join(self.folder, 'config.json')
      ]
    self.tables = {
      'funding': [],
      'contributions': []
    }

  def test_column_names(self):
    '''
    database.configuration.tables:  Test that column names are correct.
    '''
    for file in self.files:
      database = Load.loadJSONFile(file)['database']
      for table in database:
        #
        # Don't test the 'test' table.
        #
        if table['name'] == 'test':
          continue
        else:
          for column in table['columns']:
            self.assertIn(column['field_name'], self.tables.get(table['name']))
