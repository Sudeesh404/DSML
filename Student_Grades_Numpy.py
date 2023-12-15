import numpy as np

#grades of students
grades = np.array([70,55,96,92,93,90,36,85,60])

#average grade
avg = np.mean(grades)
print(avg)

#students SCored above 90
abv_90 = np.count_nonzero(grades[grades>=90])
print(abv_90)

#standard deviation
sd = np.std(grades)
print(sd)
