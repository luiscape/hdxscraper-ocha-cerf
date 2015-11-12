#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Collects data from OCHA CERF.

'''
import os
import json
import requests
import xml.etree.cElementTree as ElementTree

import app.utilities.load as Load
import app.utilities.xml_dictionary as XML

from os.path import splitext
from urllib.parse import urlparse
from app.utilities.item import item
from app.collect.flat import makeFlat

def _extension(url):
    '''
    Return the filename extension from url string.

    '''
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext[1:]

def collectData(url):
  '''
  Collects data from a specific endpoint
  from OCHA CERF.

  '''
  print('{bullet} Collecting data from: {url}'.format(bullet=item('bullet'), url=url))
  r = requests.get(url)

  if _extension(url) == 'json':
    result = []
    for record in r.json():
      result.append(makeFlat(record))

  else:
    result = []
    tree = ElementTree.fromstring(r.content)
    for element in tree:
      record = XML.XmlDictConfig(element)
      result.append(makeFlat(record))

  return result
