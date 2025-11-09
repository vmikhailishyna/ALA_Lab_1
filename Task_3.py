import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def read_off():
    with open("cup_0080.off",'r') as f:
        if 'OFF' != f.readline().strip():
            raise ValueError('Not a valid OFF header')
        n_verts, n_faces, _ = map(int, f.readline().strip().split())

        verts = [list(map(float, f.readline().strip().split())) for _ in range(n_verts)]
        faces = [list(map(int, f.readline().strip().split()[1:])) for _ in range(n_faces)]

        return np.array(verts), faces

def rotate_xy(X, theta):
    theta = np.deg2rad(theta)
    A = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])
    X_copy = X.copy()
    rotate_xy = (A@X_copy.T).T
    return A, rotate_xy

def rotate_yz(X, theta):
    theta = np.deg2rad(theta)
    A = np.array([[1, 0, 0],
                  [0, np.cos(theta), -np.sin(theta)],
                  [0, np.sin(theta), np.cos(theta)]])
    X_copy = X.copy()
    rotate_yz = (A@X_copy.T).T
    return A, rotate_yz

def rotate_xz(X, theta):
    theta = np.deg2rad(theta)
    A = np.array([[np.cos(theta), 0, -np.sin(theta)],
                  [0, 1, 0],
                  [np.sin(theta), 0, np.cos(theta)]])
    X_copy = X.copy()
    rotate_xz = (A @ X_copy.T).T
    return A, rotate_xz


def plot_off(vertices, faces):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    mesh = Poly3DCollection([vertices[face] for face in faces], alpha=0.3)
    ax.add_collection3d(mesh)

    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s = 2, c='r')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.auto_scale_xyz(vertices[:, 0], vertices[:, 1], vertices[:, 2])

    plt.show()


vertices, faces = read_off()
plot_off(vertices, faces)

A_xy, X_xy = rotate_xy(vertices, 30)
print("Rotation matrix xy: \n", A_xy)
plot_off(X_xy, faces)
A_yz, X_yz = rotate_yz(vertices, 45)
print("Rotation matrix yz: \n", A_yz)
plot_off(X_yz, faces)
A_xz, X_xz = rotate_xz(vertices, 60)
print("Rotation matrix xz: \n", A_xz)
plot_off(X_xz, faces)
