# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 20:27
# @Author  : dzzxjl@126.com

import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
print("X:", X)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

regr_1 = DecisionTreeRegressor(max_depth=4, criterion="mse")
# regr_1 = DecisionTreeRegressor()
regr_2 = DecisionTreeRegressor(max_depth=4, criterion="mae")
# regr_3 = DecisionTreeRegressor(max_depth=5)
# regr_4 = DecisionTreeRegressor(max_depth=10)

regr_1.fit(X, y)
regr_2.fit(X, y)
# regr_3.fit(X, y)
# regr_4.fit(X, y)

X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
# y_3 = regr_3.predict(X_test)
# y_4 = regr_4.predict(X_test)

plt.figure()
plt.scatter(X, y, s=20, edgecolors="black", c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=5 mse", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5 mae", linewidth=2)
# plt.plot(X_test, y_3, color="red", label="max_depth=5", linewidth=2)
# plt.plot(X_test, y_4, color="pink", label="max_depth=10", linewidth=2)

plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()

# import pydotplus
# dot_data = export_graphviz(regr_3, out_file=None)
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf('regr_3.pdf')