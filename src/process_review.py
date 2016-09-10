import pandas as pd
import preprocess as pr

df = pd.read_csv("csv/train.csv")

i = 0
for text in df.Text:

df['Summary'] = df['Summary'].pipe(pr.preprocess_text, df['Summary'].str)
df['Text'] = df['Text'].pipe(pr.preprocess_text, df['Text'].str)

df.write_csv("csv/preprocessed_train.csv")
