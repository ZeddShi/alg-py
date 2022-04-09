# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 0:39
# @Author  : ziggy
# @File    : matrix_have_value.py

def matrix_have_value(matrix, value):
    """
    判断递增矩阵中是否有某个值
    :param matrix:
    :param value:
    :return:
    """
    if not matrix:
        return False

    m = len(matrix)
    n = len(matrix[0])

    point = (0, n - 1)
    while True:
        if point[0] >= m or point[1] < 0:
            break
        if matrix[point[0]][point[1]] == value:
            return True
        elif matrix[point[0]][point[1]] > value:
            point = (point[0], point[1] - 1)
        else:
            point = (point[0] + 1, point[1])
    return False


def matrix_have_value_from_left(matrix, value):
    """
    判断递增矩阵中是否有某个值
    :param matrix:
    :param value:
    :return:
    """
    if not matrix:
        return False

    m = len(matrix)
    n = len(matrix[0])

    point = (m - 1, 0)
    while True:
        if point[0] < 0 or point[1] >= n:
            break
        if matrix[point[0]][point[1]] == value:
            return True
        elif matrix[point[0]][point[1]] < value:
            point = (point[0], point[1] + 1)
        else:
            point = (point[0] - 1, point[1])
    return False


if __name__ == '__main__':
    matrix = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    print(matrix_have_value(matrix, 7))
    print(matrix_have_value_from_left(matrix, 7))
