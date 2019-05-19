import numpy as np
import matplotlib.pyplot as plt

def rbf(d1, d2):
    return np.exp((-1 / 2)  * (d1-d2)**2)

def matrix(X, num_centers):
    M = np.zeros((X.shape[0], num_centers), float)
    
    for c_n, c in enumerate(centers):
        for x_n, x in enumerate(X):
            M[x_n,c_n] = self.function_rbf(c, x)
    return M

def centers_definition(X, shape_hidden):

    random_cent = np.random.choice(len(X), shape_hidden)
    centers = X[random_cent]
    return centers

def fit(X, Y):
    centers = centers_definition(X)

    M = matrix(X)

    W = np.dot(np.linalg.pinv(M), Y)


def predict(X, W):

    M = matrix(X)
    Y = np.dot(M, W)
    return Y


N = 100
X = np.random.uniform(0., 1., N)
X = np.sort(X, axis=0)
y =np.

num_centers = 3
rbf.fit(X, y)

y_pred = rbf.predict(X)

plt.plot(X, y, '-o', label='F-true', color = 'red')
plt.plot(X, y_pred, '-o', label='RBF', color = 'blue')
plt.legend()

plt.tight_layout()
plt.show()
