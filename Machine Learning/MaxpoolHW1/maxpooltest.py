import tensorflow as tf
x=tf.constant([[1,2,3],[4,5,6],[7,8,9]])
print(x)
mp2d=tf.keras.layers.MaxPooling2D(pool_size=(2,2),padding='valid')
print(mp2d(x))

