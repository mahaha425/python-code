# import numpy as np
# a = np.arange(8).reshape(2,4)
# print ('原数组：')
# print (a)
# # 默认按行
# print ('展开的数组：')
# print (a.flatten())
# print ('以 F 风格顺序展开的数组：')
# print (a.flatten(order = 'F'))

# import numpy as np
# a = np.arange(8).reshape(2,4)
# print ('原数组：')
# print (a)
# print ('调用 ravel 函数之后：')
# print (a.ravel())
# print ('以 F 风格顺序调用 ravel 函数之后：')
# print (a.ravel(order = 'F'))

# import numpy as np
# a = np.arange(12).reshape(3,4)
# print ('原数组：')
# print (a)
# print ('对换数组：')
# print (np.transpose(a))

import numpy as np
a = np.arange(12).reshape(3,4)
print ('原数组：')
print (a)
print ('\n')
print ('转置数组：')
print (a.T)