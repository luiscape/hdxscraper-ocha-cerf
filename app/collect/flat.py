#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Function that flattens a dictionary.

'''
def makeFlat(dictionary, delimiter='_'):
  '''
  Internal function to flattens dictionaries.
  Recursive.

  Returns: dict

  '''
  restart = True
  while restart:
    restart = False
    dout = { k:v for k,v in dictionary.items() }
    keys = dout.keys()
    for key in keys:

      if type(dictionary.get(key)) == type({}):
        for k in dictionary[key].keys():
          dictionary[key + delimiter + k] = dictionary[key][k]

        dictionary.pop(key)
        restart = True

      if type(dictionary.get(key)) == type([]):
        if len(dictionary.get(key)) > 0:
          dictionary[key] = dictionary[key][0]
          restart = True
        else:
          dictionary[key] = None
          restart = True

      if restart:
        break

  return dictionary
