"""This module implements functions for numpy-based operations.

It includes:
1. max_index: Returns the index of the maximum value in a 2D numpy array.
2. wallis_product: Computes an approximation of pi using the Wallis product.

The module is designed for practicing numpy, automated tools, and git workflows.
"""

import numpy as np


def max_index(X):
    """Return the index of the maximum in a numpy array.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The input array.

    Returns
    -------
    (i, j) : tuple(int)
        The row and column index of the maximum.

    Raises
    ------
    ValueError
        If the input is not a numpy array or
        if the shape is not 2D.
    """
    # Check whether input is a numpy array
    if not isinstance(X, np.ndarray):
        raise ValueError("Input array is not a numpy array.")

    # Check whether input is 2D array
    if X.ndim != 2:
        raise ValueError("Input array is not 2D.")

    # Initialize the max value and indices
    max_val = float('-inf')
    i, j = 0, 0

    for row in range(X.shape[0]):  # Iterate through all rows
        for col in range(X.shape[1]):  # Iterate through all columns
            if X[row, col] > max_val:
                max_val = X[row, col]  # Update the maximum value
                i, j = row, col  # Update the indices of the maximum

    return i, j


def wallis_product(n_terms):
    """Implement the Wallis product to compute an approximation of pi.

    See:
    https://en.wikipedia.org/wiki/Wallis_product

    Parameters
    ----------
    n_terms : int
        Number of steps in the Wallis product. Note that `n_terms=0` will
        consider the product to be `1`.

    Returns
    -------
    pi : float
        The approximation of order `n_terms` of pi using the Wallis product.

    Raises
    ------
    ValueError
        If n_terms is negative.
    """
    if n_terms < 0:
        raise ValueError("n_terms must be a non-negative integer.")
    # `n_terms=0` will consider the product to be 1
    product = 1.0
    # Iterate from 1 to n_terms
    for n in range(1, n_terms + 1):
        numerator = 4 * n**2
        denominator = 4 * n**2 - 1
        product *= numerator / denominator  # Compute each term in the product
    return 2 * product  # Multiply by 2 to compute pi
