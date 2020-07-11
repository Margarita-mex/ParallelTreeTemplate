import numpy as np


def knff(a, b, c):
    part1 = np.logical_or(np.logical_or(a, b), c)
    part2 = np.logical_or(np.logical_or(np.logical_not(a), b), c)
    part3 = np.logical_or(np.logical_or(a, np.logical_not(b)), c)
    part4 = np.logical_or(np.logical_or(a, b), np.logical_not(c))
    return np.logical_and(part1, np.logical_and(part2, np.logical_and(part3, part4)))


if __name__ == '__main__':
    print('Hello, world!')
    a = np.array([False, False, False, False, True, True, True, True])
    b = np.array([False, False, True, True, False, False, True, True])
    c = np.array([False, True, False, True, False, True, False, True])
    knf = knff(a, b, c)
    print(knf)
    indexes = np.where(knf==True)
    if len(indexes)==0:
        print('not exist')
    else:
        print('exist')





