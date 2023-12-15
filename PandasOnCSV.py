import pandas as pd

df = pd.read_csv('student_data.csv')

#number of rows and columns in csv
num_rows, num_cols = df.shape
print("Rows = ",num_rows)
print("Colums = ", num_cols)

#total gpa
total_gpa = df['GPA'].sum()
print(total_gpa)

#20 years or older
age20 = df['Age']>20
df.where(age20,inplace=True)
print(df)

#descending order gpa
df.sort_values(['GPA'], ascending=True,inplace=True)
print(df)