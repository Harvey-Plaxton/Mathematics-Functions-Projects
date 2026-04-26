##
##   Example python script to create a random stream of uniform
##  random numers
##

nsample = 8 ;

import numpy as np

# create a vector of nsample random numbers between 0 and 1
v = np.random.rand(nsample)

# loop over elements of vector v and create random 0 and 1
dim = len(v)
for i in range(0,dim) :
   print(i, round(v[i]) )


