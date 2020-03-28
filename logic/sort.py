def sort_key(value):
  return value['Level']

def sort_vocabulary(vocabulary):
  vocabulary.sort(key=sort_key, reverse=True)
  return vocabulary