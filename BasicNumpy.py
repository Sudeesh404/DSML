import numpy as np

#initializing an array
a1 = np.array([1,2,3,4,5])
print(a1)

#appending another list of objects to the a1 array
a1 = np.append(a1, [6,7,8,9])
print(a1)

#inserting elements to a pos
a1 = np.insert(a1,2,[10,10])
print(a1)

#delete elements from array
a1 = np.delete(a1,[4])
print(a1)

#unique elements in array
a1 = np.unique(a1)
print(a1)

#sorting
a1 = np.sort(a1)
print(a1)

#array to txt file
np.savetxt('a1.txt',a1)

#load data from txt
txt_a1 = np.loadtxt('a1.txt')
print(txt_a1)
