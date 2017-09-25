# Create first network with Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
from keras.utils import plot_model

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
# Sequential是一系列网络层按顺序构成的栈
model = Sequential()
# 第一层拥有初始输入
# units为神经单元个数
# 如Dense，支持通过指定其输入维度input_dim来隐含的指定输入数据shape
model.add(Dense(units=12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(units=8, init='uniform', activation='relu'))
model.add(Dense(units=4, init='uniform', activation='relu'))
model.add(Dense(units=1, init='uniform', activation='sigmoid'))
# Compile model 编译模型


# multi-class问题损失函数定义为categorical_crossentropy
# 指明损失函数和优化器
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=150, batch_size=10,  verbose=2)
# calculate predictions
predictions = model.predict(X)
# round predictions
rounded = [numpy.round(x) for x in predictions]
print(rounded)

plot_model(model, to_file='model.png', show_shapes=True)

