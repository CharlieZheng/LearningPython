import numpy as np
import matplotlib.pyplot as plt
row = 3
col = 3
x = np.linspace(-5, 5, 20) # 1000个点
y1 = [1/(1+np.exp(-i)) for i in x]
y2 = x**2
plt.subplot(row, col, 1)
plt.plot(x, y1,'r-o',
x, y2, 'g-.', label='fe')
plt.legend()# 展示图例
plt.xlabel('Rads')
plt.ylabel('Amplitude')
plt.title('Sin and Cos Waves')
plt.subplot(row, col, 2)
plt.plot(x, y1, 'r-o', label='fe')


'散点图'
plt.subplot(row, col, 3)
plt.plot(x, y2, 'bo', label='fe')

plt.subplot(row, col, 4)
plt.scatter(x, y2)


'彩色映射散点图'
x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000) * 50
colour = np.random.rand(1000)
plt.subplot(row, col, 5)
plt.scatter(x, y, size, colour)
plt.colorbar()


'直方图'
x = np.random.randn(1000)
plt.subplot(row, col, 6)

plt.hist(x, 50)
















plt.show()