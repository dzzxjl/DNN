from xgboost import XGBClassifier


from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
# print(iris)

rnf_clf = RandomForestClassifier(n_estimators=500, n_jobs=1)
# rnf_clf.fit(iris['data'], iris['target'])
rnf_clf.fit(iris['data'], iris['target'])

for name, score in zip(iris["feature_names"], rnf_clf.feature_importances_):
    print(name, score)


