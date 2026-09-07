import pandas as pd

data = pd.read_csv('data(for_project).csv')

average_marks = data["Marks"].mean()

print(data)
print(data.describe())
print("Average marks:", average_marks)