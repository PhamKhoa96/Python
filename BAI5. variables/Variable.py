import numpy as np

k = 1.3
ten = "khoa"
h = 2
s = k + h
j, y, t = 12, "thao", 4.4
init = (20,1,5,8,8,5)

poolsize = (2,3,5)
print(s)
print(ten)
print(j,y,t)

print(type(j),type(y),type(t))
print(init[2:])
print(np.prod(poolsize))

filter_shape=(20, 1, 5, 5)
poolsize=(2, 2)
n_out = (filter_shape[0]*np.prod(filter_shape[2:])/np.prod(poolsize))
print(n_out)


image_shape = (10, 1, 28, 28)
print(image_shape)
ji= np.reshape(image_shape,(2,2))
print(ji)


#print(np.random.RandomState(20))
#print(np.random.rand(3))
np.random.seed(0)
print (np.random.permutation(10))
np.random.seed(1)
print (np.random.permutation(10))
np.random.seed(2)
print (np.random.permutation(10))

print("---------")

np.random.seed(42) 
print(np.random.randn(4))

print(np.random.randn(4))

print(np.random.randn(4))

np.random.seed(42)   #np.random.RandomState maintains the number just as before that have exacly the same seed
print(np.random.randn(4))

print("--------------")

import theano
import theano.tensor as T
from theano.tensor import shared_randomstreams

srng = shared_randomstreams.RandomStreams(np.random.RandomState(0).randint(999999))
print(srng)
