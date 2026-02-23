import numpy as np
from numpy import linalg

# αποφυγή επιστημονικής σημειογραφίας
np.set_printoptions(suppress=True)

A = np.array([[1, 2], [3, 4]])
print("A:\n", A)

# χρήση από το subpackage numpy.linalg
inv_A = linalg.inv(A)
print("A^-1:\n", inv_A)

I = A @ inv_A  # το γινόμενο A * A^-1 με τον τελεστή @
print("A x A^-1:\n", I)
