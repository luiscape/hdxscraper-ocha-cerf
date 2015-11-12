# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# '''
# Unit tests for testing the collect module.

# '''
# import os
# import unittest
# import app.utilities.load as Load
# import app.collect.collect as Collect

# class TestCollect(unittest.TestCase):
#   '''
#   Unit tests for the collect functions.

#   '''
#   def setUp(self):
#     dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#     file = os.path.join(dir_name, 'config', 'config.json')
#     config = Load.loadJSONFile(file)
#     self.urls = []
#     for e in config['endpoints']:
#       self.urls.append(e['url'])

#   def test_type(self):
#     '''
#     collect:  Tests for the resulting types of the collect function.
#     '''
#     for url in self.urls:
#       result = Collect.collectData(url)
#       self.assertIs(type(result), type([]))

#   def test_records_exist(self):
#     '''
#     collect:  Tests that the dictionary contains records.
#     '''
#     for url in self.urls:
#       result = Collect.collectData(url)
#       self.assertNotEqual(len(result), 0)
