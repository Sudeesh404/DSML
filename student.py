import pandas as pd
data=pd.read_csv("student_data.csv")


print("\n\nStudents who are 20 years old or older\n")
age_filter=data["Age"]>20
data.where(age_filter,inplace=True)
print(data)

#descending order of GPA
print("\n\n#descending order of GPA\n")
data.sort_values(["GPA"],ascending=True,inplace=True)
print(data)

#top 5 students with the highest GPAs.
print("\n\n#top 5 students with the highest GPAs")
data.sort_values(["GPA"],ascending=False,inplace=True)
print(data)
