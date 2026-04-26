
import numpy as np

#
#  define the matrix
#

a = np.array( [ [5 ,1 ,0 , 0] , [3 , 5 , 0 , 0], [1 ,0 , 1, 0],[0 , 1 , 0 , 1] ]  ) 

print(a)

b = np.array(   [ 12 , 24 , 5 , 5]   ) 

print(b)

#
#  Solve the matrix equation A * x = b 


x = np.linalg.solve(a, b)


print("Solution x = " , x)
