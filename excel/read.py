import pandas as pd

def read_vocabulary():
  excel_file = pd.ExcelFile('data/vocabulary.xlsx')
  data = excel_file.parse(excel_file.sheet_names[0])
  vocabulary = []
  for i, row in data.iterrows():
    word = {}
    word['French'] = row[0]
    word['English'] = row[1]
    word['Level'] = row[2]
    vocabulary.append(word)
  return vocabulary