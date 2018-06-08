from numpy import *
import numpy as np
a1 = array([1, 1, 1])
a2 = array([2,2,2])
print(a1+a2)
print(a1*2)

e =np.random.random((3,2,2)) *20
print(e)
'修改数组操作'
arr = np.arange(10)*3


out=np.where(arr%2==1, -1, arr) 
print(arr)

arr = arr[arr%2==1] # 取index满足条件的item组成新的数组
print(arr)
print(out)

'把1行10列的数组变成2行5列的数组'
out = arr.reshape(5, -1) # (5, -1)或(5, 1)
print(out)

arr = arr.reshape(1, -1)
'锤子拼接数组'
b = np.repeat(13, 5).reshape(1, 5)# .reshape(1, 5)后变成矩阵，不能与数组互操作
print('b：'+str(b))
# Method 1:
hb1 =np.concatenate([arr, b], axis =0)

# Method 2:
hb2=np.vstack([arr, b])
# Method 3:
hb3=np.r_[arr, b]

print('hb1：%s\nhb2：%s\nhb3：%s\n'%(str(hb1) ,str(hb2) ,str(hb3)))

'水平拼接数组'

# Method 1:
hb1 =np.concatenate([arr, b], axis =1)

# Method 2:
hb2=np.hstack([arr, b])
# Method 3:
hb3=np.c_[arr, b]

print('hb1：%s\nhb2：%s\nhb3：%s\n'%(str(hb1) ,str(hb2) ,str(hb3)))
'看效果'
arr =np.array([1, 2, 3])
print(np.r_[np.repeat(arr, 3), np.tile(arr, 3)])

'求交集'
arr =np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9,8])
print ('交集：'+str(np.intersect1d(arr, b)))
'求交集index'
print ('交集index：' +str(np.where(arr== b)))
'求相对于另一个数组元素完全不同的子集'
arr =np.array([1,2, 3, 4,5])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9,8])
print (np.setdiff1d(arr, b))


'筛选子集'
arr =np.arange(15)*1.2
# Method 1
index = np.where((arr>=5)&(arr<=10))
print(index)
print(arr[index])

# Method 2
index = np.where(np.logical_and(arr>=5, arr<=10))
print(index)
print(arr[index])

'行或列交换'
arr = np.arange(9).reshape(3, 3)
arr =arr[:, [2,1,0]] #列交换

print(arr)
arr = np.arange(9).reshape(3, 3)
arr =arr[[1,2,0], :] #行交换
print(arr)

'反转行或列'
arr = np.arange(9).reshape(3, 3)
arr =arr[:, ::-1] #列交换
print(arr)
arr = np.arange(9).reshape(3, 3)
arr =arr[ ::-1,:] #行交换或arr[ ::-1]
print(arr)


'5到10的二维数组'

# Solution Method 1:
bt = np.random.randint(low=5, high=10, size=(5, 3)) + np.random.random((5, 3))
print(bt)
# Solution Method 2:
bt = np.random.uniform(5, 10, size=(5, 3))
print(bt)
'截断'
bt=np.arange(100)
np.set_printoptions(threshold=6)
print(bt)
bt = np.arange(20)
'恢复'
np.set_printoptions(threshold=np.nan)
print(bt)

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object', encoding='utf-8')
names=('sepallength', 'sepallwidth', 'petallength', 'petallwidth', 'species')
print(iris.shape)
print(iris[:3])
species = np.array([row[4] for row in iris])
print(species.shape)
print(species[:5])

'27.如何将一维元组数组转换为二维numpy数组？'

# Solution Method 1:
species =np.array([row.tolist()[:4] for row in iris])
print(species.shape)
print(species[:4])
species = np.genfromtxt(url , delimiter=',', dtype='float', usecols=[0,1,2,3])
print(species.shape)
print(species[:4])

'28.如何计算numpy数组的平均值，中位数，标准差？'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)

print(mu, med, sd)
'29.如何标准化一个数组至0到1之间？'
Smax, Smin = sepallength.max(), sepallength.min()

S = (sepallength-Smin)/(Smax - Smin)
print(sepallength.shape)
print(S.shape)
print(sepallength)
print(S)