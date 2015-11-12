#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for the XML to dictionary utility.
This tests if the XML converter is creating
dictionaries correctly.

'''
import os
import unittest
import xml.etree.cElementTree as ElementTree
import app.utilities.xml_dictionary as XML

class TestUtilityXMLDictionary(unittest.TestCase):
  '''
  Unit tests for the loading of configuration files.
  '''
  def setUp(self):
    self.folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
    self.file = os.path.join(self.folder, 'mock_data.xml')

  def test_type(self):
    '''
    utilities.xml:  Test for the type of XML output is dictionary.
    '''
    tree = ElementTree.parse(self.file)
    root = tree.getroot()
    result = XML.XmlDictConfig(root)
    self.assertIs(type(dict(result)), type({}))
