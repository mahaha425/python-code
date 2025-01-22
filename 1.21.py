# import numpy as np

# # 创建了三维的 ndarray
# a = np.arange(8).reshape(2, 2, 2)
#
# print('原数组：')
# print(a)
# print('获取数组中一个值：')
# print(np.where(a == 6))
# print(a[1, 1, 0])  # 为 6
# # print('\n')
#
# # 将轴 2 滚动到轴 0（宽度到深度）
#
# print('调用 rollaxis 函数：')
# b = np.rollaxis(a, 2, 0)
# print(b)
# # 查看元素 a[1,1,0]，即 6 的坐标，变成 [0, 1, 1]
# # 最后一个 0 移动到最前面
# print(np.where(b == 6))
# # print('\n')
#
# # 将轴 2 滚动到轴 1：（宽度到高度）
#
# print('调用 rollaxis 函数：')
# c = np.rollaxis(a, 2, 1)
# print(c)
# # 查看元素 a[1,1,0]，即 6 的坐标，变成 [1, 0, 1]
# # 最后的 0 和 它前面的 1 对换位置
# print(np.where(c == 6))
# # print('\n')

#import numpy as np

# # 创建了三维的 ndarray
# a = np.arange(8).reshape(2, 2, 2)
#
# print('原数组：')
# print(a)
# # print('\n')
# # 现在交换轴 0（深度方向）到轴 2（宽度方向）
#
# print('调用 swapaxes 函数后的数组：')
# print(np.swapaxes(a, 2, 0))

# import numpy as np

# x = np.array([[1], [2], [3]])
# y = np.array([4, 5, 6])
#
# # 对 y 广播 x
# b = np.broadcast(x, y)
# # 它拥有 iterator 属性，基于自身组件的迭代器元组
#
# print('对 y 广播 x：')
# r, c = b.iters
#
# # Python3.x 为 next(context) ，Python2.x 为 context.next()
# print(next(r), next(c))
# print(next(r), next(c))
# # print('\n')
# # shape 属性返回广播对象的形状
#
# print('广播对象的形状：')
# print(b.shape)
# # print('\n')
# # 手动使用 broadcast 将 x 与 y 相加
# b = np.broadcast(x, y)
# c = np.empty(b.shape)
#
# print('手动使用 broadcast 将 x 与 y 相加：')
# print(c.shape)
# # print('\n')
# c.flat = [u + v for (u, v) in b]
#
# print('调用 flat 函数：')
# print(c)
# # print('\n')
# # 获得了和 NumPy 内建的广播支持相同的结果
#
# print('x 与 y 的和：')
# print(x + y)

# import numpy as np
# a = np.arange(4).reshape(1,4)
# print ('原数组：')
# print (a)
# print ('调用 broadcast_to 函数之后：')
# print (np.broadcast_to(a,(4,4)))

# import numpy as np
# x = np.array(([1,2],[3,4]))
# print ('数组 x：')
# print (x)
# y = np.expand_dims(x, axis = 0)
# print ('数组 y：')
# print (y)
# print ('数组 x 和 y 的形状：')
# print (x.shape, y.shape)
# # 在位置 1 插入轴
# y = np.expand_dims(x, axis = 1)
# print ('在位置 1 插入轴之后的数组 y：')
# print (y)
# print ('x.ndim 和 y.ndim：')
# print (x.ndim,y.ndim)
# print ('x.shape 和 y.shape：')
# print (x.shape, y.shape)

# import numpy as np
# x = np.arange(9).reshape(1,3,3)
# print ('数组 x：')
# print (x)
# y = np.squeeze(x)
# print ('数组 y：')
# print (y)
# print ('数组 x 和 y 的形状：')
# print (x.shape, y.shape)

# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
# print ('第一个数组：')
# print (a)
# print ('第一个数组的形状：')
# print (a.shape)
# b = np.resize(a, (3,2))
# print ('第二个数组：')
# print (b)
# print ('第二个数组的形状：')
# print (b.shape)
# # 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了
# print ('修改第二个数组的大小：')
# b = np.resize(a,(3,3))
# print (b)

# import numpy as np
# a = np.array([[1,2,3],[4,5,6]])
#
# print ('第一个数组：')
# print (a)
# print ('向数组添加元素：')
# print (np.append(a, [7,8,9]))
# print ('沿轴 0 添加元素：')
# print (np.append(a, [[7,8,9]],axis = 0))
# print ('沿轴 1 添加元素：')
# print (np.append(a, [[5,5,5],[7,8,9]],axis = 1))

import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
print ('第一个数组：')
print (a)
print ('未传递 Axis 参数。 在删除之前输入数组会被展开。')
print (np.insert(a,3,[11,12]))
print ('传递了 Axis 参数。 会广播值数组来配输入数组。')
print ('沿轴 0 广播：')
print (np.insert(a,1,[11],axis = 0))
print ('沿轴 1 广播：')
print (np.insert(a,1,11,axis = 1))