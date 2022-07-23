import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from h5py import File
from keras.layers import Dense, Flatten
from keras.models import Sequential
from keras.utils import to_categorical
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score


def exp_decay(epoch):
    initial_lrate = 0.05
    k = 0.01
    lrate = initial_lrate * np.exp(-k*epoch)
    return lrate


_, x_test, y_test = File("data/test_catvnoncat.h5", "r").values()
_, x_train, y_train = File("data/train_catvnoncat.h5", "r").values()
x_train, y_train = x_train[()], y_train[()]
x_test, y_test = x_test[()], y_test[()]
x_train = x_train / 255
x_test = x_test / 255
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

num_classes = 2
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

lrate = tf.keras.callbacks.LearningRateScheduler(exp_decay)
callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=20)
modelo = Sequential()
modelo.add(Flatten())
modelo.add(Dense(200, kernel_initializer="random_uniform",
                 bias_initializer="random_uniform", activation="tanh"))
modelo.add(Dense(2, kernel_initializer="random_uniform",
                 bias_initializer="random_uniform", activation="softmax"))


opt = tf.keras.optimizers.SGD(momentum=0.1)
modelo.compile(optimizer=opt, loss="categorical_crossentropy", metrics=["accuracy"])

input_shape = x_train.shape
modelo.build(input_shape)

results = modelo.fit(x_train, y_train, validation_data=(x_test, y_test),
                     batch_size=64, epochs=400, callbacks=[callback, lrate], verbose=1)

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


y_test_pred = modelo.predict(x_test)
y_train_pred = modelo.predict(x_train)

print('\nAccuracy: {:.4f}\n'.format(accuracy_score(y_train.argmax(axis=1), y_train_pred.argmax(axis=1))))
ConfusionMatrixDisplay.from_predictions(y_train.argmax(axis=1), y_train_pred.argmax(axis=1))


print('\nAccuracy: {:.4f}\n'.format(accuracy_score(y_test.argmax(axis=1), y_test_pred.argmax(axis=1))))
ConfusionMatrixDisplay.from_predictions(y_test.argmax(axis=1), y_test_pred.argmax(axis=1))

plt.show()
