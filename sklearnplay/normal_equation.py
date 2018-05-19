# -*- coding: utf-8 -*-
# @Time    : 2018/4/2 10:32
# @Author  : dzzxjl@126.com


import numpy as np
import matplotlib.pyplot as plt

X = 2 * np.random.rand(100, 1)
# print('X', X)
# print(X.shape)
y = 4 + 3 * X + np.random.rand(100, 1)
#
X_b = np.c_[np.ones((100, 1)), X]

# print(X_b)
# print(X_b.shape)
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)




print(theta_best)



X_new = np.array([[0], [2]])
print(X_new)
X_new_b = np.c_[np.ones((2, 1)), X_new]
print(X_new_b)
y_predict = X_new_b.dot(theta_best)


plt.plot(X_new, y_predict, 'r-')
plt.plot(X, y, 'b.')
plt.axis([0, 2, 0, 15])
plt.show()


import lightgbm as lgb

lgb = lgb.LGBMClassifier()
lgb.feature_importances_