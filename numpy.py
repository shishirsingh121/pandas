import numpy as np
np1=np.array([2,3,4,5,6,7,34,44,22])
print(np1)
for i in np1:
    print(i)

np2=np.arange(10)
print(np2)
a=np.array([[1,2,3,4],[5,6,7,8]],dtype=np.float64)#convert into float
print(a.ndim)
print(a.shape)
print(a.reshape(8,1))
print(a.itemsize)
print(a.min())
print(a.max())
print(a.sum(axis=0))
print(np.sqrt(a))
a1=np.array([[1,2,3,4],[5,6,7,8]],dtype=np.complex128)
print(a1)
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[3,6,7],[1,3,5]])
print(np.concatenate((a,b)))
z=np.array([0,1,2,3,4,5,6,7,8])
print(z[:5])
print(z[:-1])
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[3,6,7],[1,3,5]])
print(a[1,2])
print(a)
print(a[:,0:2])
for cell in a.flat:
    print(cell)
print(np.vstack((a,b)))  
print(np.hstack((a,b)))  
a=np.array([[ 0,1,  2,  3],[ 4, 5, 6, 7],[ 8,9,10,11]])
b=a>5
print(b)   
print(a[b])
a=np.array([[ 0,1,  2,  3],[ 4, 5, 6, 7],[ 8,9,10,11]])
for row in a:
    for cell in row:
         print(cell)
for cell in a.flatten():
    print(cell)
    
for x in np.nditer(a,order='c'):
    print(x)

    
for x in np.nditer(a,order='f'):
    print(x)
