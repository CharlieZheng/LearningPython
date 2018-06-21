# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
'''
二元一次方程组
x1 = np.arange(-4, 4, 0.1)
x2 = 3 - 2 * x1
x3 = x1
x4 = (3 - x1) / 2
plt.plot(x1, x2, color="red", linewidth="1.2", linestyle="-")
plt.plot(x3, x4)
plt.show()
'''

'''
# https://wenku.baidu.com/view/f9687a1986c24028915f804d2b160b4e777f8140.html
temp = 0.5
a  = np.mat(np.array([[ 2, 2, 2],[2, 2,2], [2, 2,2]]))
print("原矩阵：")
print(a)
# 缩放变换
i  = np.mat(np.array([[ temp,0 , 0],[0,temp,0], [0, 0,temp]]))
b = a*i
print("缩放为原来的"+str(temp)+"倍：")
print(b)
# 反射变换
i  = np.mat(np.array([[ -1,0 , 0],[0,1,0], [0, 0,-1]]))
b = a*i
print("反射变换：")
print(b)
'''


# https://wenku.baidu.com/view/80024ec50408763231126edb6f1aff00bed57091.html
import math
import numpy as np
x =np.array([1,2,3,4,5,6])
y = np.array([2.5,3.51,4.45,5.52,6.47,7.51])
y = np.array([2.5,3.51,4.45,5.52,6.47,10])


lenx =len(x)
if lenx == len(y) :
    sumx =np.sum(x)
    sumy = np.sum(y)
    sumxx = 0
    sumxy = 0
    for ix in range(lenx):
        sumxy += x[ix]*y[ix]
        sumxx += x[ix]*x[ix]

    # 公式一（https://wenku.baidu.com/view/80024ec50408763231126edb6f1aff00bed57091.html）：
    a = ((sumx * sumy)/lenx - sumxy) /(sumx*sumx/lenx-sumxx)
    b= (sumy-a*sumx)/lenx
    # 公式二（https://wenku.baidu.com/view/f9687a1986c24028915f804d2b160b4e777f8140.html）：
    a =( lenx*sumxy- sumx *sumy)/(lenx * sumxx - sumx*sumx)
    b = sumy /lenx - a/lenx *sumx

    liney = a*x +b
    print(a)
    print(b)
    print(x)
    print(y)
    plt.xlabel ( 'y = '+str(a)+' * x + '+str(b))
    plt.title ( '最小二乘法')
    plt.plot(x, y, 'or')
    plt.plot(x, liney)
    plt.show()

    
