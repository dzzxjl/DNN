import tensorflow as tf

# result是一个计算图


a = tf.constant([1.0,2.0], name="a")
b = tf.constant([3.0,4.0], name="b")

result = a + b

sess = tf.Session()

print(sess.run(result))
