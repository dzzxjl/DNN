from sklearn.svm import SVC
import numpy as np

X= np.array([[-1,-1],[-2,-1],[1,1],[2,1]])
y = np.array([1,1,2,2])

clf = SVC(kernel='linear')
clf.fit(X, y)
# 第一个打印出的是svc训练函数的参数
print(clf.fit(X, y))


# 预测结果
print(clf.predict([[-0.8,-1]]))
print(clf.predict([[5,6]]))

print(clf.coef_)