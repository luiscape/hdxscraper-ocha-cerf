#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for testing the flattening functions.

'''
import os
import json
import unittest
import app.collect.flat as Flat

class TestCollect(unittest.TestCase):
  '''
  Unit tests for the collect functions.

  '''
  def setUp(self):
    self.folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
    self.file = os.path.join(self.folder, 'mock_project_data.json')

  def test_type(self):
    '''
    collect.flatdict:  Tests for the resulting types of the collect function.
    '''
    with open(self.file) as f:
      data = json.load(f)

    result = Flat.makeFlat(dictionary=data, delimiter='_')
    for record in result:
      self.assertIsNot(type(record), type({}))
      self.assertIsNot(type(record), type([]))
