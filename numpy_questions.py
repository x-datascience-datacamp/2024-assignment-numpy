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
    """Retourne les indices (i, j) de la valeur maximale dans une matrice 2D."""
    if not isinstance(X, np.ndarray):
        raise ValueError("X doit être un tableau numpy.")
    if X.ndim != 2:
        raise ValueError("X doit être une matrice 2D.")
    # Trouver l'indice aplati du maximum.
    flat_index = np.argmax(X)
    # Convertir en indices 2D.
    i, j = divmod(flat_index, X.shape[1])
    return i, j



def wallis_product(n_terms):
    produit = 1
    if n_terms==0:
        return(2)
    else:
        for i in range(1, n_terms+1):
            produit *= 4*i**2/(4*i**2 - 1)
    return(2*produit)
