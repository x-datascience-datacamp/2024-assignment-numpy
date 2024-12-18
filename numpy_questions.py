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

Exercise 1
"""
import numpy as np


def max_index(X):
   """
    Return the index of the maximum value in a 2D numpy array.

    Parameters
    ----------
    X : np.ndarray
        A 2D numpy array.

    Returns
    -------
    tuple
        A tuple (i, j) representing the row and column index of the maximum value.

    Raises
    ------
    ValueError
        If the input is not a 2D numpy array.
    """
    if not isinstance(X, np.ndarray):
        raise ValueError("Input has to be a numpy array.")
    if X.ndim != 2:
        raise ValueError("Input array must be 2D.")

    max_idx = np.argmax(X)  # Find the maximum value of the array
    i, j = divmod(max_idx, X.shape[1])  # Returns the indexes of the maximum

    return i, j


"""Exercise 2"""


def wallis_product(n_terms):
   """
    Compute an approximation of pi using the Wallis product.

    Parameters
    ----------
    n_terms : int
        The number of terms to compute in the Wallis product.

    Returns
    -------
    float
        The approximation of pi based on the Wallis product.

    Raises
    ------
    Exception
        If the input is not an integer.
    """
    if not isinstance(n_terms, int):
        raise Exception("Input has to be an integer.")
    if n_terms == 0:
        return 2.0  # By definition, return 2 for 0 terms
    product = 1.0
    for n in range(1, n_terms + 1):
        product *= (4 * n ** 2) / ((4 * n ** 2) - 1)

    return 2 * product
