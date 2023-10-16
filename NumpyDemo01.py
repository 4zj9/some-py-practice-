# Exercise01
# import numpy as np
#
# Exerciae02
# a=np.array([4,5,6])
# print(type(a),a.shape,a[0])
#
# Exercise03
# b=np.array([[4,5,6],[1,2,3]])
# print(b.shape,b[0,0],b[0,1],b[1,1])
#
# Exercise04
# a=np.zeros((3,3),dtype=int)
# b=np.ones((4,5),dtype=int)
# c=np.identity(4)
# d=np.random.randn(3,2)
# print(a)
# print(b)
# print(c)
# print(d)
#
# Exercise05
# a = np.arange(1,13).reshape(3,4)
# a
# print(a[2,3])
# print(a[0,0])
#
# Exercise06
# b = a[0:2, 1:3]
# b
# print(b[0,0])
#
# Exercise07
# c = a[1:3, :]
# c
# c[0][-1]
#
# Exercise08
# a = np.array([[1,2],[3,4],[5,6]])
# print(a[[0,1,2],[0,1,0]])
#
# Exercise09
# a = np.arange(1,13).reshape(4,3)
# b = np.array([0,2,0,1])
# print(a[[np.arange(4),b]])
#
# Exercise10
# a[[np.arange(4),b]] += 10
# print(a[[np.arange(4),b]])
#
# Exercise11
# x = np.array([1,2])
# print(x.dtype) # dtype('int32')
#
# Exercise12
# x =np.array([1.0,2.0])
# print(x.dtype)
#
# Exercise13
# x = np.array([[1, 2], [3, 4]], dtype=np.float64)
# y = np.array([[5, 6], [7, 8]], dtype=np.float64)
# np.add(x,y)
# print(x+y,np)
#
# Exercise14
# print(x-y,np.subtract(x,y))
#
# Exercise15
# print(x*y)
# print(np.multiply(x,y))
# print(np.dot(x,y))
#
# Exercise16
# print(x/y,np.divide(x,y))
#
# Exercise17
# print(np.sqrt(x))
#
# Exercise18
# print(x.dot(y))
# print(np.dot(x,y))
#
#
# Exercise19
# print(np.sum(x))
# print(np.sum(x,axis=0))
# print(np.sum(x,axis=1))
#
# Exercise20     平均数
# print(np.mean(x))
# print(np.mean(x,axis=0))
# print(np.mean(x,axis=1))
#
# Exercise21
# x.T
# print(x.T)
#
# Exercise22  e的指数
# print(np.exp(x))
#
# Exercise23    求值最大的下标
# print(np.argmax(x))
# print(np.argmax(x,axis=0))
# print(np.argmax(x,axis=1))
#
# Exercise24
# import matplotlib.pyplot as plt
# x = np.arange(0,100,0.1)
# y = x * x
# plt.figure(figsize=(6,6))  # 创建画布，并指定画布大小
# plt.plot(x,y)   # 在画布上画图
# plt.show()  # 展示画图结果
#
# Exercise25
# import matplotlib.pyplot as plt
# x=np.arange(0,3*np.pi,0.1)
# y1=np.sin(x)
# y2=np.cos(x)
# plt.figure(figsize=(10,6))
# plt.plot(x,y1,color="Red")
# plt.plot(x,y2,color="Blue")
# plt.legend(["Sin","Cos"])    #给线做标记
# plt.show()
#














