import numpy as np


def max_index(X):
    # Raises
    if not isinstance(X, np.ndarray):
        raise ValueError("The input is not a numpy array")
    if X.ndim != 2:
        raise ValueError("The shape is not 2D")
    """ Return the index of the maximum in a numpy array
     (The row and columnd index of the maximum)"""
    i = 0
    j = 0
    max_index = np.argmax(X)
    i, j = np.unravel_index(max_index, X.shape)
    # I convert to int just to avoid show the type(int64) in the output
    return (int(i), int(j))


def wallis_product(n_terms):
    # So if n_terms = 0 -> product = 1
    product = 1.0
    for n in range(1, n_terms + 1):
        """In wiki the wallis product = the infinite product
        # representation of π 4*n^2/(4*n^2-1)"""
        term = (4 * np.square(n)) / (4 * np.square(n) - 1)
        product *= term
    pi = 2 * product
    return pi
