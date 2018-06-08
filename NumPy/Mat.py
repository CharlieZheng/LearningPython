'矩阵'
import numpy as np
from numpy import *

print("numpy的版本为："+np.__version__)
# array([0, 1, 2, 3, 4, 5, 6, 8, 9])
m = np.arange(10)

m = mat([1,2,3])
print(m)
m2 = mat([4, 5,6])
print(m*m2.T)

# 点乘
m3 =multiply(m, m2)
print(m3)

print(m *m3.T)

m = mat([[4, 3, 4],[2, 1, 3]])
m.sort()
print(m)
# 行数
print("行数："+str(m.shape[0]))
print("行数："+str(size(m , 0)))
# 列数

print("列数："+str(m.shape[1]))
print("列数："+str(size(m, 1)))

print(m)
m=tile(m , (2, 2)) # 行数扩展两倍，列数扩展两倍
print(m)