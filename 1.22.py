# import numpy as np
# a = np.arange(12).reshape(3,4)
# print ('第一个数组：')
# print (a)
# print ('未传递 Axis 参数。 在插入之前输入数组会被展开。')
# print (np.delete(a,5))
# print ('删除第二列：')
# print (np.delete(a,1,axis = 1))
# print ('包含从数组中删除的替代值的切片：')
# a = np.array([1,2,3,4,5,6,7,8,9,10])
# print (np.delete(a, np.s_[::2]))

# import numpy as np
# a = np.array([5,2,6,2,7,5,6,8,2,9])
# print ('第一个数组：')
# print (a)
# print ('第一个数组的去重值：')
# u = np.unique(a)
# print (u)
# print ('去重数组的索引数组：')
# u,indices = np.unique(a, return_index = True)
# print (indices)
# print ('我们可以看到每个和原数组下标对应的数值：')
# print (a)
# print ('去重数组的下标：')
# u,indices = np.unique(a,return_inverse = True)
# print (u)
# print ('下标为：')
# print (indices)
# print ('使用下标重构原数组：')
# print (u[indices])
# print ('返回去重元素的重复数量：')
# u,indices = np.unique(a,return_counts = True)
# print (u)
# print (indices)

# import numpy as np
#
# print('13 和 17 的二进制形式：')
# a, b = 13, 17
# print(bin(a), bin(b))
#
# print('13 和 17 的位与：')
# print(np.bitwise_and(13, 17))

# import numpy as np
# a,b = 13,17
# print ('13 和 17 的二进制形式：')
# print (bin(a), bin(b))
# print ('13 和 17 的位或：')
# print (np.bitwise_or(13, 17))

# import numpy as np
# print ('13 的位反转，其中 ndarray 的 dtype 是 uint8：')
# print (np.invert(np.array([13], dtype = np.uint8)))
# # 比较 13 和 242 的二进制表示，我们发现了位的反转
# print ('13 的二进制表示：')
# print (np.binary_repr(13, width = 8))
# print ('242 的二进制表示：')
# print (np.binary_repr(242, width = 8))

# import numpy as np
# print ('将 10 左移两位：')
# print (np.left_shift(10,2))
# print ('10 的二进制表示：')
# print (np.binary_repr(10, width = 8))
# print ('40 的二进制表示：')
# print (np.binary_repr(40, width = 8))
# # '00001010' 中的两位移动到了左边，并在右边添加了两个 0。

# import numpy as np
# print ('将 40 右移两位：')
# print (np.right_shift(40,2))
# print ('40 的二进制表示：')
# print (np.binary_repr(40, width = 8))
# print ('10 的二进制表示：')
# print (np.binary_repr(10, width = 8))
# # '00001010' 中的两位移动到了右边，并在左边添加了两个 0。

# import numpy as np
# print ('连接两个字符串：')
# print (np.char.add(['hello'],[' xyz']))
# print ('连接示例：')
# print (np.char.add(['hello', 'hi'],[' abc', ' xyz']))

# import numpy as np
# print (np.char.multiply('Runoob ',3))

# import numpy as np
# # np.char.center(str , width,fillchar) ：
# # str: 字符串，width: 长度，fillchar: 填充字符
# print (np.char.center('Runoob', 20,fillchar = '*'))

# import numpy as np
# a = np.array([1.0,5.55,  123,  0.567,  25.532])
# print  ('原数组：')
# print (a)
# print ('舍入后：')
# print (np.around(a))
# print (np.around(a, decimals =  1))
# print (np.around(a, decimals =  -1))

# import numpy as np
# a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
# print ('提供的数组：')
# print (a)
# print ('修改后的数组：')
# print (np.floor(a))

# import numpy as np
# a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
# print  ('提供的数组：')
# print (a)
# print ('修改后的数组：')
# print (np.ceil(a))

import numpy as np

a = np.array([0.25, 1.33, 1, 100])
print('我们的数组是：')
print(a)
print('\n')
print('调用 reciprocal 函数：')
print(np.reciprocal(a))