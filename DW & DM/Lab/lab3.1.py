import time
import numpy as np
matrix1=np.random.rand(100,100)
matrix2=np.random.rand(100,100)  
#using for np.dot() 
start=time.time()  
result=np.dot(matrix1,matrix2)
end=time.time()  
print("Time taken by np.dot() is ",end-start)
result=np.zeros((100,100))  
#using for loop start=time.time()  
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j]+=matrix1[i][k]*matrix2[k][j]
end=time.time()
print("Time taken by for loop is ",end-start)  
