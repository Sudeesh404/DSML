import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
marks = np.array([10,18,34,50,20,10,30,45,49,25,12,22])
fig ,ax = plt.subplots(figsize=(4,4))
ax.hist(marks,color='darkcyan',ec="black", lw=l)
plt.title("Exam Score")
plt.ylabel('No of students')
plt.xlabel('Score')
plt.figure(figsize=(4,4))
sns.boxplot(y=marks,color='red')
plt.title('Exam Score')
plt.ylabel('score')
plt.show()