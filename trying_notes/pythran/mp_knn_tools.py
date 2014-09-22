#pythran export knn_err_sum(float[], float[][])
import numpy as np

def knn_err_sum(x, X):
    return np.array([np.abs(X[:,i] - x[i]) for i in range(x.shape[0])]).T.sum(1)