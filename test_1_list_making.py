import numpy as np
# from . import movemont_function as mf
from movemont_function import *

END = np.array([
    [
        ['g1', 'g2', 'g3'],
        ['g4', 'g5', 'g6'],
        ['g7', 'g8', 'g9'],
    ], [
        ['r1', 'r2', 'r3'],
        ['r4', 'r5', 'r6'],
        ['r7', 'r8', 'r9'],
    ], [
        ['b1', 'b2', 'b3'],
        ['b4', 'b5', 'b6'],
        ['b7', 'b8', 'b9'],
    ], [
        ['o1', 'o2', 'o3'],
        ['o4', 'o5', 'o6'],
        ['o7', 'o8', 'o9'],
    ], [
        ['w1', 'w2', 'w3'],
        ['w4', 'w5', 'w6'],
        ['w7', 'w8', 'w9'],
    ], [
        ['y1', 'y2', 'y3'],
        ['y4', 'y5', 'y6'],
        ['y7', 'y8', 'y9'],
    ],
])

# front=red,index 1
# left=green,index 0
# right=blue, index 2
# up=white, index 4
# down=yellow, index 5
# back=orange, index 3
DIRECTION = ['LA', 'LC', 'FA', 'FC', 'RA', 'RC', 'BA', 'BC', 'UA', 'UC', 'DA', 'DC']

if __name__ == '__main__':
    new = move_front_a(END.copy())
    print()
    for n in new:
        for a in n:
            print(a)
        print()
