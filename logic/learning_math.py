import numpy as np
import math

def correct_answer(x):
  return 0.75*x + 0.25

def wrong_answer(x):
  return 0.65*x

def update_level(x, correct):
  if correct:
    return correct_answer(x)
  return wrong_answer(x)

def random_index(length):
  # try working with various exponents
  exponent = 2.1
  index = np.random.random()
  index = -(1 - index)**exponent + 1
  index = math.floor(index*length)
  return index

def random_word(vocabulary):
  index = random_index(len(vocabulary))
  return vocabulary[index]
