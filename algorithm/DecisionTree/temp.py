from numpy import loadtxt

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

file = '/Users/dzzxjl/Desktop/' + 'pima-indians-diabetes.csv'

dataset = loadtxt(file, delimiter=",")



print(dataset)
print(type(dataset))


X = dataset[:,0:8]
Y = dataset[:,8]
