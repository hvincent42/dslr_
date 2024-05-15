import pandas as pd

df = pd.read_csv("data/dataset_testeee copy.csv")

df = pd.DataFrame(df)

df['Hogwarts House'] = df['Hogwarts House'].apply(lambda x: '')

df.to_csv('modified_dataset.csv', index=False)