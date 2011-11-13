# -*- coding: utf-8 -*-

"""
pylitvoc - lithuanian vocative library in python 

Copyright (C) 2011 Vilius Visockas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

def vocative(word):
  # Exceptions which do not follow rules
  exceptions = {'duktė': 'dukterie', 'sesuo': 'seserie'}

  # Transformation rules
  transforms = [
    ('tis', 'tie'), ('uo', 'enie')    ,
    ('čias', 'ty'), ('ėjas', 'ėjau'), ('as', 'e'), ('ys', 'y'),  ('is', 'i'), 
    ('ia', 'ia'), ('a', 'a'), ('i', 'i'), 
    ('ė', 'e'),
    ('us', 'au'),
  ]

  if len(word) == 0:
    return word

  # Lithuanian male name -as
  if word[0].isupper() and word.endswith('as'):
    return word[:-2] + 'ai'

  # One of exceptions
  if word.lower() in exceptions:
    return exceptions[word.lower()]

  # Apply first rule which fits
  for transform in transforms:
    if word.endswith(transform[0]):
      return word[:-len(transform[0])] + transform[1] 

  return word


# Apply vocative for each word in expression
def vocate(expression):
  return ' '.join(map(vocative, expression.split()))

if __name__ == "__main__":
  assert vocate('Vilius Visockas') == 'Viliau Visockai'
  assert vocate('vyras') == 'vyre'
  assert vocate('svečias') == 'svety'
  assert vocate('gaidys') == 'gaidy'
  assert vocate('brolis') == 'broli'
  assert vocate('galva') == 'galva'
  assert vocate('vyšnia') == 'vyšnia'
  assert vocate('marti') == 'marti'
  assert vocate('katė') == 'kate'
  assert vocate('sūnus') == 'sūnau'
  assert vocate('dantis') == 'dantie'
  assert vocate('vanduo') == 'vandenie'
  assert vocate('sesuo') == 'seserie'
  assert vocate('duktė') == 'dukterie'
  assert vocate('vėjas') == 'vėjau'   
