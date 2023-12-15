import numpy as np

#initializing two 2x2 matrices
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

#matrix sum
matrix_sum = np.add(A,B)
print(matrix_sum)

#matrix product
matrix_product = np.multiply(A,B)
print(matrix_product)

#matrix dot product
dot_product = np.dot(A,B)
print(dot_product)

#Transpos of A
A_transpose = np.transpose(A)
print(A_transpose)

#determinent of B
det_B = np.linalg.det(B)
print(det_B)

#Eigen values and vectors of A
ei_val_A, ei_vector_a = np.linalg.eig(A)
print(ei_val_A)
print(ei_vector_a)

#svd od A
svd_A = np.linalg.svd(A)
print(svd_A)
