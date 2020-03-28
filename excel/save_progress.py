import pandas as pd

def save_progress_to_excel(vocabulary):
  df = pd.DataFrame(columns=['French', 'English', 'Level'])
  for word in vocabulary:
    df = df.append(word, ignore_index=True)
  df.to_excel("data/vocabulary.xlsx", sheet_name="vocabulary", index=False)
