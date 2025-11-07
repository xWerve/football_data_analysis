import kagglehub
import pandas as pd
path = kagglehub.dataset_download("technika148/football-database")

apperances = pd.read_csv("../data/appearances.csv")
print(apperances.head())
