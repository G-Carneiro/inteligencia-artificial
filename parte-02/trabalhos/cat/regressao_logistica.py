import numpy as np
import matplotlib.pyplot as plt
import h5py
from sklearn.metrics import ConfusionMatrixDisplay


# funcao propagacao que calcula a funcao de custo do gradiente
def propagate(w, b, X, Y):
    m = X.shape[1]
    A = sigmoid(np.dot(w.T, X) + b)
    cost = (-1 / m) * np.sum((Y * np.log(A)) + ((1 - Y) * np.log(1 - A)))
    db = (1 / m) * (np.sum(A - Y))
    dw = (1 / m) * (np.dot(X, np.subtract(A, Y).T))
    assert (db.dtype == float)
    cost = np.squeeze(cost)
    assert (cost.shape == ())
    grads = {"dw": dw,
             "db": db}
    return grads, cost

##otimizacao da funcao
def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost=False):
    costs = []
    for i in range(num_iterations):
        grads, cost = propagate(w, b, X, Y)
        dw = grads["dw"]
        db = grads["db"]
        w = w - learning_rate * dw
        b = b - learning_rate * db
        if i % 100 == 0:
            costs.append(cost)
        if print_cost and i % 100 == 0:
            print(f"Cost after iteration {i}: {cost}")
    params = {"w": w,
              "b": b}
    grads = {"dw": dw,
             "db": db}
    return params, grads, costs


## calcular sigmoide
def sigmoid(z):
    s = 1 / (1 + np.exp(-z))
    return s


##funcao de previsao que vai prever se a imagem é um gato ou nao
##onde será 0 se o valor for <= 0,5
##e vai ser 1 se o valor for > 0,5
def predict(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)
    A = sigmoid(np.dot(w.T, X) + b)
    for i in range(A.shape[1]):
        if (A[0, i] <= 0.5):
            Y_prediction[0, i] = 0
        elif (A[0, i] > 0.5):
            Y_prediction[0, i] = 1
        pass
    assert (Y_prediction.shape == (1, m))
    return Y_prediction


##inicializando parametros com valores 0
def initialize_with_zeros(dim):
    w = np.zeros((dim, 1))
    b = 0
    assert (w.shape == (dim, 1))
    assert (isinstance(b, float) or isinstance(b, int))
    return w, b


##Carregando os dados
def load_dataset():
    with h5py.File('data/train_catvnoncat.h5', "r") as train_dataset:
        train_set_x_orig = np.array(train_dataset["train_set_x"][:])
        train_set_y_orig = np.array(train_dataset["train_set_y"][:])

    with h5py.File('data/test_catvnoncat.h5', "r") as test_dataset:
        test_set_x_orig = np.array(test_dataset["test_set_x"][:])
        test_set_y_orig = np.array(test_dataset["test_set_y"][:])
        classes = np.array(test_dataset["list_classes"][:])

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


##metodo principal
def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5, print_cost=False):
    w, b = initialize_with_zeros(X_train.shape[0])

    parameters, grads, costs = optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost)

    w = parameters["w"]
    b = parameters["b"]

    Y_prediction_test = predict(w, b, X_test)
    Y_prediction_train = predict(w, b, X_train)

    print("train accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
    print("test accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))
    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test,
         "Y_prediction_train": Y_prediction_train,
         "w": w,
         "b": b,
         "learning_rate": learning_rate,
         "num_iterations": num_iterations}
    return d


# ----------------------------PRE PROCESSAMENTO--------------------------------#

train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

## achatando a matriz de 4 dimensões
## imagens agora são representadas como vetores

train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T

## padronizar o conjunto de dados

train_set_x = train_set_x_flatten / 255.
test_set_x = test_set_x_flatten / 255.

# --------------------------FIM DO PRE PROCESSAMENTO---------------------------------------------------#

d = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations=2200, learning_rate=0.001, print_cost=False)

##funcao de custo do gradiente
costs = np.squeeze(d['costs'])
plt.plot(costs)
plt.ylabel('cost')
plt.xlabel('iterations (per hundreds)')
plt.title("Learning rate =" + str(d["learning_rate"]))
# plt.show()

from sklearn import metrics

##matriz de confusao de teste
c_matrixTeste = metrics.confusion_matrix(test_set_y[0].astype(int),d['Y_prediction_test'][0].astype(int))
disp = ConfusionMatrixDisplay(confusion_matrix=c_matrixTeste)

##matriz de confusao de treinamento
c_matrixTreinamento = metrics.confusion_matrix(train_set_y[0].astype(int),d['Y_prediction_train'][0].astype(int))
disp1 = ConfusionMatrixDisplay(confusion_matrix=c_matrixTreinamento)

disp.plot()
disp1.plot()
plt.show()
