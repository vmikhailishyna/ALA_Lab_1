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
    X_copy = X.copy()
    X_st = (A @ X_copy.T).T
    return A, X_st

def shear(X,a,b):
    A = np.array([[1, a],
                  [b, 1]])
    X_copy = X.copy()
    X_sh = (A @ X_copy.T).T
    return A, X_sh

def reflection(X,a,b):
    A = (1/(pow(a, 2)+pow(b, 2))) * np.array([[pow(a, 2)-pow(b, 2), 2*a*b],
                                              [2*a*b, pow(b, 2)-pow(a, 2)]])
    X_copy = X.copy()
    X_ref = (A @ X_copy.T).T
    return A, X_ref

def rotation(X, theta):
    theta = np.deg2rad(theta)
    A = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    X_copy = X.copy()
    X_rot = (A @ X_copy.T).T
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

A, X_st = stretch(fox_arr,2,3)
print("Stretch matrix:\n", A)
plot_fox_2D(X_st)

A, X_sh = shear(fox_arr,4,6)
print("Shear matrix:\n", A)
plot_fox_2D(X_sh)

A, X_ref = reflection(fox_arr,0.25,1.5)
print("Reflection matrix:\n", A)
plot_fox_2D(X_ref)

A, X_rot = rotation(fox_arr, 30)
print("Rotation matrix:\n", A)
plot_fox_2D(X_rot)
