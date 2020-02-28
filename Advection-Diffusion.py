"""
Advection-Diffusion Equation

Anthony Ivakhnenko
"""


import matplotlib.pyplot as plt
import numpy as np

# function to create the tri diagonal Matrix A
def matrix(n, beta):
    a = np.eye(n) * (1. + 2. * beta) + np.eye(n, k=1) * -beta + np.eye(n, k=-1) * -beta
    a[0][0] = 1
    a[0][1] = 0
    a[-1][-1] = 1 + beta
    return a


# Setting up grid
Nsteps = 5000
Ngrid = 50
dt = 1
dx = 1

v = -0.1
alpha = v * dt / 2 / dx

D = [1, 5]
beta1 = D[0] * dt / (dx ** 2)
beta2 = D[1] * dt / (dx ** 2)

x = np.arange(Ngrid) * dx

# Initial conditions:
f1 = np.copy(x) * 1. / Ngrid
f2 = np.copy(x) * 1. / Ngrid

# Set up the plot:
plt.ion()
fig, axes = plt.subplots(1, 2)
s1 = "D = " + str(D[0])
s2 = "D = " + str(D[1])
axes[0].set_title(s1)
axes[1].set_title(s2)

#Inverse the matrix A to properly solve for f^n+1 terms
A1 = np.linalg.inv(matrix(Ngrid, beta1))
A2 = np.linalg.inv(matrix(Ngrid, beta2))

# Update grid with diffusion term:
f1 = np.linalg.solve(A1, f1)
f2 = np.linalg.solve(A2, f2)

# Plot the initial state:
axes[0].plot(x, f1, 'k-')
axes[1].plot(x, f2, 'k-')

plt1, = axes[0].plot(x, f1, 'ro')
plt2, = axes[1].plot(x, f2, 'ro')

fig.canvas.draw()

count = 0
while count < Nsteps:
    #Solve advection like in part 1
    f1[1:Ngrid - 1] = 0.5 * (f1[2:] + f1[:Ngrid - 2]) - alpha * (f1[2:] - f1[:Ngrid - 2])
    f2[1:Ngrid - 1] = 0.5 * (f2[2:] + f2[:Ngrid - 2]) - alpha * (f2[2:] - f2[:Ngrid - 2])
    plt1.set_ydata(f1)
    plt2.set_ydata(f2)
    fig.canvas.draw()
    plt.pause(0.001)
    count += 1