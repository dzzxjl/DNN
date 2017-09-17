# Create first network with Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
# 设置初始种子值，使每次实验的结果相同
seed = 7
numpy.random.seed(seed)

# load pima indians dataset
file = '/Users/dzzxjl/Desktop/' + 'pima-indians-diabetes.csv'
dataset = numpy.loadtxt(file, delimiter=",")


# split into input (X) and output (Y) variables
# X取0至8列，第8列不取
X = dataset[:, 0:8]
# Y取第8列
Y = dataset[:, 8]

# print(X)
# create model
# 定义连续模型
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, nb_epoch=150, batch_size=10,  verbose=2)
# calculate predictions
predictions = model.predict(X)
# round predictions
rounded = [round(x) for x in predictions]
print(rounded)