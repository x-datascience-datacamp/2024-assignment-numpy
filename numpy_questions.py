"""Assignment - using numpy and making a PR.

The goals of this assignment are:
    * Use numpy in practice with two easy exercises.
    * Use automated tools to validate the code (`pytest` and `flake8`)
    * Submit a Pull-Request on github to practice `git`.

The two functions below are skeleton functions. The docstrings explain what
are the inputs, the outputs and the expected error. Fill the function to
complete the assignment. The code should be able to pass the test that we
wrote. To run the tests, use `pytest test_numpy_question.py` at the root of
the repo. It should say that 2 tests ran with success.

We also ask to respect the pep8 convention: https://pep8.org.
This will be enforced with `flake8`. You can check that there is no flake8
errors by calling `flake8` at the root of the repo.
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
    i = 0
    j = 0

    # TODO
    # Checking the input
    if not isinstance(X, np.ndarray):
        raise ValueError('The input is not a numpy array.')
    if len(X.shape) != 2:
        raise ValueError('The input is not a 2D matrix.')

    # Finding the row and column index of the maximum
    max_value = X[i, j]
    n_rows, n_cols = X.shape
    for i0 in range(n_rows):
        for j0 in range(n_cols):
            if X[i0, j0] > max_value:
                max_value = X[i0, j0]
                i = i0
                j = j0

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
    """
    # XXX : The n_terms is an int that corresponds to the number of
    # terms in the product. For example 10000.

    # Checking the input
    if not isinstance(n_terms, int):
        raise ValueError('The input is not an integer.')

    # Base case
    if n_terms == 0:
        return 2.
    # Iterative computation
    pi_approx = 2.
    for n in range(1, n_terms + 1):
        pi_approx *= 4 * n**2 / (4 * n**2 - 1)

    return pi_approx
