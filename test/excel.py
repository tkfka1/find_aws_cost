import pandas as pd

sheet = pd.read_excel('example2.xlsx', engine='openpyxl')

NP= sheet.to_numpy()
print(NP)

