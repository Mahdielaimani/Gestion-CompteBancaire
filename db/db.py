import pandas as pd

file_path = r'C:\Users\Mahdi Elaimani\Desktop\Projet Python & Scrum\db.xlsx'
data = pd.read_excel(file_path)

print(data)
print(data.head())
print(data.columns)
