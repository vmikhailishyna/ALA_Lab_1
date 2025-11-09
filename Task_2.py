import numpy as np
import matplotlib.pyplot as plt

def modify_file():
    with open('fox_points.csv', 'r', encoding='utf-8') as f:
        fox_point = f.read().replace(',','.')
    with open('fox_points.csv', 'w', encoding='utf-8') as f:
        f.write(fox_point)
    fox_arr = np.loadtxt('fox_points.csv', delimiter=';')
    return fox_arr

def stretch(X,a,b):
    A = np.array([[a, 0],
                  [0, b]])
    X_st = (A @ X.T).T
    return A, X_st

def shear(X,a,b):
    A = np.array([[1, a],
                  [b, 1]])
    X_sh = (A @ X.T).T
    return A, X_sh

def rotation(X, theta):
    theta = np.deg2rad(theta)
    A = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    X_rot = (A @ X.T).T
    return A, X_rot

def plot_fox_2D(X):
    plt.scatter(X[:, 0], X[:, 1], color='pink')

    plt.gca().spines['left'].set_position('center')
    plt.gca().spines['bottom'].set_position('center')
    plt.gca().spines['right'].set_color('none')
    plt.gca().spines['top'].set_color('none')
    plt.axis('equal')
    plt.show()

fox_arr = modify_file()

plot_fox_2D(fox_arr)
copy_fox_arr_1 = np.copy(fox_arr)
copy_fox_arr_2 = np.copy(fox_arr)
copy_fox_arr_3 = np.copy(fox_arr)

A1, X_st = stretch(copy_fox_arr_1,2,3)
print("Stretch matrix:\n", A1)
plot_fox_2D(X_st)

A2, X_sh = shear(X_st,4,6)
print("Stretch -> Shear matrix:\n", A2 @ A1)
plot_fox_2D(X_sh)

A3, X_rot = rotation(X_sh, 30)
print("Stretch -> Shear -> Rotation matrix:\n", A3 @ A2 @ A1)
plot_fox_2D(X_rot)


A1, X_st = stretch(copy_fox_arr_2,2,3)
print("Stretch matrix:\n", A1)
plot_fox_2D(X_st)

A2, X_rot = rotation(X_st, 30)
print("Stretch matrix -> Rotation matrix:\n", A2 @ A1)
plot_fox_2D(X_rot)

A3, X_sh = shear(X_rot,4,6)
print("Stretch matrix -> Rotation matrix -> Shear matrix:\n", A3 @ A2 @ A1)
plot_fox_2D(X_sh)


A1, X_rot = rotation(copy_fox_arr_3,30)
print("Rotation matrix:\n", A1)
plot_fox_2D(X_rot)

A2, X_st  = stretch(X_rot, 2,3)
print("Rotation matrix -> Stretch matrix:\n", A2 @ A1)
plot_fox_2D(X_st)

A3, X_sh = shear(X_st,4,6)
print("Rotation matrix -> Stretch matrix -> Shear matrix:\n", A3 @ A2 @ A1)
plot_fox_2D(X_sh)

#When performing the second part of the first task, I noticed that
#the order of application of linear transformations (stretching, shifting and rotation)
#affects the final result.
#Because matrix multiplication is not a commutative operation,
#changing the order of operations resulted in different results.