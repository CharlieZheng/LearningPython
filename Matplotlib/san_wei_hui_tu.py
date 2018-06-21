#!/usr/bin/env python
# encoding: utf-8

from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
print(shape(X))
X, Y = np.meshgrid(X, Y)
print(shape(X))
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
Z = X ** 2
# 开始 a
a = [[1, 2],[3, 4]]
print(a)
print(shape(a))
a =np.meshgrid(a)
print(a)
print(shape(a))


# 结束 a
print(type(X))
print(type(Y))
print(type(Z))
# 开始 b
print("开始 b")
b = [1, 2,3, 4]

print(b)
print(shape(b))
b =np.meshgrid(b)
print(b)
print(shape(b))

print("结束 b")
# 结束 b

# 开始 给数组赋值
shuzu=[2]
shuzu .append(9)
print("shuzu: "+str(shuzu))
# 结束 给数组赋值
def getZ(default, X, Y):
    if (len(X) != len(Y)):
        return default
    size = len(X)

    size = len(Y)
    print("size: "+str(size))
    result = []
    print(X)
   
    for i in range(size):
        print(shape(X))
        print(shape(X[i]))
        print(shape(Y[i]))
        if default < X[i]:
            result.append( 0)
        if default > Y[i]:
            if default > 0:
                result.append(  Y[i])
            else:
                result.append( -Y[i])
        result.append( default)
    return result

print("len(X): "+str(len(X)))
#Z = getZ(60, X[0], Y[0])

print(type(X))
print(type(Y))
print(type(Z))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.hot)
#ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cm.hot)
ax.set_zlim(-2, 2)

savefig('figure/plot3d_ex.png', dpi=48)
show()
