import pandas as pd

df=pd.read_csv("cleaned_data.csv")



del df["Unnamed: 0"]




df.to_csv("cleaned_data.csv")