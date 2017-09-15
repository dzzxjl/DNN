import numpy as np

a = np.array([[0, 1, 2], [3, 4, 5]])

print(a)
# ndarray.shape 数组的维度。它是一个整数组成的tuple，表示各维度的长度。对于一个n行m列的矩阵，它的shape就是（n，m）

print(a.shape)
# 一个用来描述元素类型的numpy对象
print(a.dtype)
# 数组中数字的总数，也就是shape中的元素的乘积
print(a.size)

# print(matrix.context)
