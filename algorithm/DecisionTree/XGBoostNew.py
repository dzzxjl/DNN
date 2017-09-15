from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
from xgboost import plot_importance
from matplotlib import pyplot

'''
使用XGBoost提供的二分器作为模型进行预测
用 Xgboost 做一个简单的二分类问题，以下面这个数据为例，
来判断病人是否会在 5 年内患糖尿病，
这个数据前 8 列是变量，最后一列是预测值为 0 或 1
'''



file = '/Users/dzzxjl/Desktop/' + 'pima-indians-diabetes.csv'

dataset = loadtxt(file, delimiter=",")

X = dataset[:,0:8]
Y = dataset[:,8]


seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)


# 使用XGBoost模型，预测准确率，Accuracy: 77.95%
# xgboost 有封装好的分类器和回归器，可以直接用 XGBClassifier 建立模型
# model = XGBClassifier()
# model = XGBClassifier()
# eval_set = [(X_test, y_test)]
# model.fit(X_train, y_train, early_stopping_rounds=10, eval_metric="logloss", eval_set=eval_set, verbose=True)

# plot_importance(model)
# pyplot.show()

# 使用XGBoost模型，预测准确率，Accuracy: 71.65%
model = tree.DecisionTreeClassifier()


model.fit(X_train, y_train)
y_pred = model.predict(X_test)


predictions = [round(value) for value in y_pred]

accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))