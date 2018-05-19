from sklearn import tree
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

# 尝试直接使用样本，代替样本提取出来的向量

X = ['beautiful', 'colorful', 'useful', 'action', 'vocation', 'worktion']
y = [0, 0, 0, 1, 1, 1]

# X = np.array([[-1,-1],[-2,-1],[1,1],[2,1]])

# y = np.array([1,1,2,2])

# 提取特征值
# X = [[0, 0], [1, 1]]
# y = [0, 1]


clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X, y)
clf = clf.fit(X, y)





print(clf)

print(clf.predict('hardful'))

# print(clf.predict([[-0.8,-1]]))
# print(clf.predict([[5,6]]))