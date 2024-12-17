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
    """
    Return the indices (i, j) of the maximum value in a 2D matrix.

    Parameters:
    X (np.ndarray): A 2D numpy array.

    Returns:
    tuple: Indices (i, j) of the maximum value in the array.

    Raises:
    ValueError: If X is not a numpy array or not a 2D array.
    """
    if not isinstance(X, np.ndarray):
        raise ValueError("X must be a numpy array.")
    if X.ndim != 2:
        raise ValueError("X must be a 2D array.")

    # Find the flattened index of the maximum value
    flat_index = np.argmax(X)
    # Convert to 2D indices
    i, j = divmod(flat_index, X.shape[1])
    return i, j


def wallis_product(n_terms):
    """
    Approximate the value of pi using the Wallis product.

    Parameters:
    n_terms (int): The number of terms in the Wallis product.

    Returns:
    float: Approximation of pi.

    Raises:
    ValueError: If n_terms is negative.
    """
    if not isinstance(n_terms, int) or n_terms < 0:
        raise ValueError("n_terms must be a non-negative integer.")

    product = 1.0
    if n_terms == 0:
        return 2.0

    for i in range(1, n_terms + 1):
        product *= (4 * i**2) / (4 * i**2 - 1)

    return 2 * product
