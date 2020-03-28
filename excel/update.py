import pandas as pd
from read import read_vocabulary

def read_or_create():
  vocabulary = []
  try:
    vocabulary = read_vocabulary()
    return vocabulary
  except Exception as e:
    return []

def update_vocabulary():
  vocabulary = read_or_create()
  english_words = [word['English'] for word in vocabulary]
  excel_file = pd.ExcelFile('data/new.xlsx')
  data = excel_file.parse(excel_file.sheet_names[0])
  for i, row in data.iterrows():
    if row[0] == 'French' and row[1] == 'English' and row[3] not in english_words:
      word = {}
      word['French'] = row[2]
      word['English'] = row[3]
      word['Level'] = 0.1
      vocabulary.append(word)
  def sort_key(value):
    return value['Level']
  vocabulary.sort(key=sort_key, reverse=True)
  return vocabulary

def save_updated(vocabulary):
  df = pd.DataFrame(columns=['French', 'English', 'Level'])
  for word in vocabulary:
    df = df.append(word, ignore_index=True)
  df.to_excel("data/vocabulary.xlsx", sheet_name="vocabulary", index=False)

v = update_vocabulary()
save_updated(v)

print('Vocabulary updated successfully !')