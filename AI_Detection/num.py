import numpy as np

# Makes every other element in a 2d array a 0
# Patter arrangement


def numpy_ravel():
    orig = np.ones((5, 5), dtype=np.int16)
    rav = orig.ravel()

    for i in range(0, len(rav), 3):
        rav[i] = 0

    print(orig)
    print(orig.shape)


numpy_ravel()
