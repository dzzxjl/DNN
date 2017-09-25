from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/Users/dzzxjl/data/MNIST_data", one_hot=True)

print("Training data size: ", mnist.train.num_examples)