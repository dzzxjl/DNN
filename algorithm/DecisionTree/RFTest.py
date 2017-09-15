from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.array([[-1,-1],[-2,-1],[1,1],[2,1]])
y = np.array([1,1,2,2])

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X, y)

print(clf)
# 预测结果
print(clf.predict([[-0.8,-1]]))
print(clf.predict([[5,6]]))