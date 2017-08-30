import numpy as np
import pandas as pd


def test_numpy():
    array_a = np.array([1, 4, 9])
    array_b = np.sqrt(array_a)
    array_c = np.arange(3)
    print(np.convolve(array_b, array_c))

    mat_a = np.matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    mat_b = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(mat_a * mat_b)


def test_pandas():
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df2 = pd.DataFrame([1, 1, 1])
    df.append(df2)
    print(df)


def test_both():
    df = pd.DataFrame(np.random.randn(6, 4))
    del df[0]
    df.append(pd.DataFrame(np.random.randn(6, 4)))
    print(df)


if __name__ == '__main__':
    print("test")
    test_numpy()
    test_pandas()
    test_both()
