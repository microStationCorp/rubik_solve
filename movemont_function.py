import numpy as np


# front=red,index 1
# left=green,index 0
# right=blue, index 2
# up=white, index 4
# down=yellow, index 5
# back=orange, index 3

# rotate face clockwise or anti-clockwise
def face_rotate(cube_side, clockwise=True):
    if clockwise:
        temp = cube_side[0, :].copy()
        cube_side[0, :] = np.flip(cube_side[:, 0])
        cube_side[:, 0] = cube_side[2, :]
        cube_side[2, :] = np.flip(cube_side[:, 2])
        cube_side[:, 2] = temp
    else:
        temp = cube_side[0, :].copy()
        cube_side[0, :] = cube_side[:, 2]
        cube_side[:, 2] = np.flip(cube_side[2, :])
        cube_side[2, :] = cube_side[:, 0]
        cube_side[:, 0] = np.flip(temp)
    return cube_side


def move_left_a(cube):
    # set green face
    cube[0] = face_rotate(cube[0].copy(), False)

    temp = cube[1][:, 0].copy()
    cube[1][:, 0] = cube[5][:, 0].copy()
    cube[5][:, 0] = np.flip(cube[3][:, 2].copy())
    cube[3][:, 2] = np.flip(cube[4][:, 0].copy())
    cube[4][:, 0] = temp
    return cube


def move_left_c(cube):
    # set green face
    cube[0] = face_rotate(cube[0].copy())

    temp = cube[1][:, 0].copy()
    cube[1][:, 0] = cube[4][:, 0].copy()
    cube[4][:, 0] = np.flip(cube[3][:, 2].copy())
    cube[3][:, 2] = np.flip(cube[5][:, 0].copy())
    cube[5][:, 0] = temp
    return cube
