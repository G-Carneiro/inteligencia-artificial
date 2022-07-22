import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# import seaborn as sns

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
from h5py import File

_, x_test, y_test = File("data/test_catvnoncat.h5", "r").values()
_, x_train, y_train = File("data/train_catvnoncat.h5", "r").values()
x_train, y_train = x_train[()], y_train[()]
x_test, y_test = x_test[()], y_test[()]

print(x_test.shape)
print(y_test.shape)

print(x_train.shape)
print(y_train.shape)

# plt.figure(figsize=(15, 15))
# for i in range(20):
#     ax = plt.subplot(4, 5, i + 1)
#     plt.imshow(x_train[i+10])
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
#
# plt.show()

num_classes = 2
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

model = Sequential()
model.add(layers.Flatten())
model.add(Dense(10, kernel_initializer="random_uniform",
                bias_initializer="random_uniform", activation="tanh"))
model.add(Dense(2, kernel_initializer="random_uniform",
                bias_initializer="random_uniform", activation="softmax"))

optimizer = keras.optimizers.SGD(learning_rate=0.005)
model.compile(optimizer=optimizer, loss="categorical_crossentropy", metrics=["accuracy"])
input_shape = x_train.shape
model.build(input_shape)
model.summary()

xtr, xval, ytr, yval = train_test_split(x_train, y_train)
num_train = np.size(xtr, 0)
print(num_train)

results = model.fit(xtr, ytr, validation_data=(xval, yval),
                    batch_size=64, epochs=450, verbose=1)

acc = results.history['accuracy']
val_acc = results.history['val_accuracy']
loss = results.history['loss']
val_loss = results.history['val_loss']
epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'b', label='Training accuracy')
plt.plot(epochs, val_acc, 'r', label='Validation accuracy')
plt.title('Training and Validation accuracy')
plt.legend()

plt.figure()
plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training and Validation loss')
plt.legend()

plt.show()
