# import numpy as np
# import matplotlib.pyplot as plt
# from dask.optimization import inline
#
# # 生成从0到5的50个等间距的数值
# x = np.linspace(0,5,50)
# # 生成从0到5的50个等间距的数值，并调整形状以便进行广播操作
# y = np.linspace(0,5,50)[:,np.newaxis]
# # 计算复杂函数z的值
# z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
#
#
# # 绘制二维图像
# plt.imshow(z,origin='lower',extent = [0,5,0,5], cmap = 'viridis')
# # 显示颜色条
# plt.colorbar()
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# # 生成绘图数据
# x = np.linspace(0, 10, 100)
# y = np.cos(x)
#
# # 绘制图形
# plt.plot(x, y, label='cos(x)')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('y = cos(x)')
# plt.legend()
#
# # 显示图形
# plt.show()
# arr_1 = np.array([1, 2, 3, 4, 5])

# 类型字段名可以用于存取实际的 age 列
# import numpy as np
# dt = np.dtype([('age',np.int8)])
# a = np.array([(10,),(20,),(30,)], dtype = dt)
# print(a['age'])

# # 示例一
# import numpy as np
# # 使用标量类型
# dt = np.dtype(np.int32)
# print(dt)

# # 示例二
# import numpy as np
# # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
# dt = np.dtype('i4')
# print(dt)

# # 示例四
# #首先创建结构化数据类型
# import numpy as np
# dt = np.dtype([('age',np.int8)])
# print(dt)

# # 示例五
# # 将数据类型应用于 ndarray 对象
# import numpy as np
# dt = np.dtype([('age',np.int8)])
# a = np.array([(10,),(20,),(30,)], dtype = dt)
# print(a)

# # 示例六
# # 类型字段名可以用于存取实际的 age 列
# import numpy as np
# dt = np.dtype([('age',np.int8)])
# a = np.array([(10,),(20,),(30,)], dtype = dt)
# print(a['age'])

# # 示例七
# import numpy as np
# student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
# print(student)
# a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
# print(a['name'])

# # 示例八
# # 结构化数据类型可以用字典来创建
# import numpy as np
# student =np.dtype({'names':['name','age','marks'], 'formats':['S20','i1','f4']})
# a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
# print(a)

# array_1 = np.array([1,2,3])
# array_2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(array_1.flags)
# print(array_2.flags)

# import numpy as np
# # 创建一个 3x3 的二维数组
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # 创建一个与 arr 形状相同的，所有元素都为 0 的数组
# zeros_arr = np.zeros_like(arr)
# print(zeros_arr)

# import numpy as np
# x =  [1,2,3]
# a = np.asarray(x)
# print (a)

# import numpy as np
# x =  (1,2,3)
# a = np.asarray(x)
# print (a)

import numpy as np
x =  [(1,2,3),(4,5,0)]
a = np.asarray(x)
print (a)