import pandas as pd
import numpy as np

from excel.read import read_vocabulary
from excel.save_progress import save_progress_to_excel

from logic.learning_math import update_level, random_word
from logic.sort import sort_vocabulary

vocabulary = read_vocabulary()

def learn(vocabulary):
  word = random_word(vocabulary)
  print(word['French'])
  guess = input()
  correct = True
  while guess != word['English'] and 'to ' + guess != word['English']:
    if guess == 'quit':
      print('Saving progress ...')
      save_progress_to_excel(vocabulary)
      print('Salut !')
      return
    if guess == '?':
      correct = False
      print(word['English'])
      break
    word['Level'] = update_level(word['Level'], False)
    print('No !')
    guess = input()
  word['Level'] = update_level(word['Level'], correct)
  vocabulary = sort_vocabulary(vocabulary)
  learn(vocabulary)

print('Bienvenue !')

learn(vocabulary)

print('END')