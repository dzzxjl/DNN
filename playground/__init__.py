import nltk
import random
from nltk.corpus import names

nltk.download()
def gender_feature(name):
    return {'last_letter': name[-1]}

# 获取名字，性别数据列表
male_names = [(name, 'male') for name in names.words('male.txt')]
print('male_num*****', male_names.__len__())
female_names = [(name, 'female') for name in names.words('female.txt')]
print('female_num*****', female_names.__len__())

total_names = male_names + female_names
# 打乱数据集
random.shuffle(total_names)

# 生成性别特征集
feature_set = [(gender_feature(n), g) for (n, g) in total_names]

# 将特征集拆分为训练集和测试集
train_set_size = int(len(feature_set) * 0.6)
print(train_set_size)
train_set = feature_set[0:train_set_size]
test_set = feature_set[0:train_set_size]


classifier = nltk.NaiveBayesClassifier.train(train_set)

print(classifier.classify(gender_feature('Neo')))
