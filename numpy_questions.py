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
    (i_max, j_max) : tuple(int)
        The row and columnd index of the maximum.

    Raises
    ------
    ValueError
        If the input is not a numpy array or
        if the shape is not 2D.
    """
    #handle exceptions
    if not isinstance(X, np.ndarray) :
        raise ValueError("The argument is not an np.array")
    if np.ndim(X) != 2 : 
        raise ValueError("The matrix's dimension is not 2")


    i_max = 0
    # TODO
    n_samples = X.shape[0]
    n_features = X.shape[1]

    max_per_line = []
    index = []
    for i in range(n_samples):
        j_max = 0
        for j in range(n_features-1):
            if X[i,j_max] < X[i,j+1] :
                j_max = j+1

        max_per_line.append(X[i,j_max])
        index.append(j_max)

    for i in range(n_samples-1) : 
        if max_per_line[i_max] < max_per_line[i+1] :
            i_max = i+1
    j_max = index[i_max]
    return i_max, j_max



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

    wallis = 1

    for i in range(1, n_terms+1): 
        wallis = wallis*(4*i**2/(4*i**2 -1))
    pi = 2*wallis
    
    return pi

A = [1,       2,3]