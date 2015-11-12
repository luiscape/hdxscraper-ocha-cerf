#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
HDX Collector for OCHA CERF data.

'''
import os
import scraperwiki
import app.utilities.load as Load

from app.utilities.item import item
from app.collect.collect import collectData
from app.utilities.store_data import storeData

def main():
  '''
  Application wrapper.

  '''
  dir_name = os.path.dirname(os.path.realpath(__file__))
  file = os.path.join(dir_name, 'config', 'config.json')
  config = Load.loadJSONFile(file)

  for endpoint in config['endpoints']:
    data = collectData(endpoint['url'])
    storeData(data, endpoint['name'])


if __name__ == '__main__':
  main()
  # try:
  #   main()
  #   print('{success} Successully collected OCHA CERF data.'.format(success=item('success')))

  # except Exception as e:
  #   print('{failure} Failed to collected OCHA CERF data.'.format(failure=item('error')))

