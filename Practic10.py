import numpy as np
import datetime


def knff(a, b, c):
    part1 = np.logical_or(np.logical_or(a, b), c)
    part2 = np.logical_or(np.logical_or(np.logical_not(a), b), c)
    part3 = np.logical_or(np.logical_or(a, np.logical_not(b)), c)
    part4 = np.logical_or(np.logical_or(a, b), np.logical_not(c))
    return np.logical_and(part1, np.logical_and(part2, np.logical_and(part3, part4)))


def knff2(a, b, c):
    part1 = np.logical_or(np.logical_or(a, b), c)
    part2 = np.logical_or(np.logical_or(np.logical_not(a), np.logical_not(b)), np.logical_not(c))
    return np.logical_and(part1, part2)

def knff3(a, b, c):
    part1 = np.logical_or(np.logical_or(a, b), c)
    part2 = np.logical_or(np.logical_or(np.logical_not(a), np.logical_not(b)), np.logical_not(c))
    part3 = np.logical_or(np.logical_or(a, np.logical_not(b)), c)
    part4 = np.logical_or(np.logical_or(a, b), np.logical_not(c))
    part5 = np.logical_or(np.logical_or(np.logical_not(a), b), c)
    part6 = np.logical_or(np.logical_or(a, np.logical_not(b)), np.logical_not(c))
    part7 = np.logical_or(np.logical_or(np.logical_not(a), b), np.logical_not(c))
    part8 = np.logical_or(np.logical_or(np.logical_not(a), np.logical_not(b)), c)
    return np.logical_and(part1, np.logical_and(part2, np.logical_and(part3, np.logical_and(part4,np.logical_and(part5, np.logical_and(part6, np.logical_and(part7, part8)))))))

if __name__ == '__main__':
    a = np.array([False, False, False, False, True, True, True, True])
    b = np.array([False, False, True, True, False, False, True, True])
    c = np.array([False, True, False, True, False, True, False, True])
    t1=datetime.datetime.now()
    knf = knff3(a, b, c)
    print(datetime.datetime.now()-t1)
    print(knf)

    indexes = np.where(knf==True)
    print(indexes)
    if len(indexes[0])==0:
        print('not exist')
    else:
        print('exist')





