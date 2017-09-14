from sklearn import tree
import numpy as np

X = np.array([[-1,-1],[-2,-1],[1,1],[2,1]])
y = np.array([1,1,2,2])

#
# X = [[0, 0], [1, 1]]
# Y = [0, 1]


clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X, y)
clf = clf.fit(X, y)

print(clf)

print(clf.predict([[-0.8,-1]]))
print(clf.predict([[5,6]]))