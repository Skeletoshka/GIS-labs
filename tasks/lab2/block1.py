import numpy as np


# Создание матрицы от 0 до 1 размером n*m
def createArr(n, m):
    return np.random.uniform(low=0, high=1, size=(n, m))


# Минимальный элемент матрицы
def minEl(arr):
    return np.min(arr)


# максимальный элемент матрицы
def maxEl(arr):
    return np.max(arr)


# Преобразует матрицу в массив и сортирует
def sortMatrixInArr(arr):
    return np.flip(np.sort(arr, axis=None)).reshape(len(arr), len(arr[0]))


def diffElMenCol(arr):
    avgEl = np.mean(arr, axis=0)
    print('Средние значения: ' + str(avgEl))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] -= avgEl[j]
    return arr
