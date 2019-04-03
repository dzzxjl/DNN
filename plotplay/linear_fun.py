import numpy as np
import matplotlib.pylab as plt

x = np.linspace(-5, 5, 1000)  # 这个表示在-5到5之间生成1000个x值

y = [-1.5 * i + 0.032 for i in x]  # 对上述生成的1000个数循环用sigmoid公式求对应的y

plt.plot(x, y)  # 用上述生成的1000个xy值对生成1000个点

plt.show()  # 绘制图像
#
# import numpy as np
#
# import matplotlib.pyplot as plt
#
# x=np.linspace(-5,5,1000)  #这个表示在-5到5之间生成1000个x值
#
# y=[1/(1+np.exp(-i)) for i in x]  #对上述生成的1000个数循环用sigmoid公式求对应的y
#
# plt.plot(x,y)  #用上述生成的1000个xy值对生成1000个点
#
# plt.show()  #绘制图像
