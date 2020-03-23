import pandas as pd
import numpy as np

excel_file = pd.ExcelFile('data/vocabulary03_23.xlsx')

data = excel_file.parse(excel_file.sheet_names[0], header=None)

def read_vocabulary():
  vocabulary = []
  for i, row in data.iterrows():
    if row[0] == 'French' and row[1] == 'English':
      word = []
      word.append(row[2])
      word.append(row[3])
      vocabulary.append(word)
  return vocabulary


def random_word(vocab):
  index = np.random.randint(0, len(vocab))
  word = vocab[index]
  return word

def learn():
  word = random_word(vocabulary)
  print(word[0])
  guess = input()
  while guess != word[1] and 'to ' + guess != word[1]:
    if guess == 'quit':
      print('Salut !')
      return
    if guess == '?':
      print(word[1])
      break
    print('No !')
    guess = input()
  learn()

vocabulary = read_vocabulary()

print('Bienvenue !')

learn()

print('END')