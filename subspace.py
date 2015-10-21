__author__ = 'dennis'

import numpy as np


def pca(X, y, num_components=0):
    n, p = X.shape
    if num_components <= 0 or num_components >= n:
        num_components = min(n, p)
    mu = X.mean(axis=0)
    X = X -mu
    W, eig, U = np.linalg.svd(X.T, full_matrices=False)
    idx = np.argsort(-eig)
    eig = eig[idx]
    W = W[:, idx]

    return eig[0:num_components].copy, W[:, 0:num_components].copy(), mu


def project(W, X, mu=None):
    if mu is None:
        return np.dot(X, W)
    return np.dot(X - mu, W)


def reconstruct(W, Y, mu=None):
    if mu is None:
        return np.dot(Y, W.T)
    return np.dot(Y, W.T) + mu





