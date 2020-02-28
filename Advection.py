"""
Advection Equation

Anthony Ivakhnenko
"""

import matplotlib.pyplot as plt
import numpy as np

#Setting up the grid
Ngrid = 50
Nsteps = 5000
dx = 1
dt = 1

v = -0.1
alpha = v*dt/2/dx

x = np.arange(Ngrid)*dx

#Initial conds:
f1 = np.copy(x)*1./Ngrid #for FTCS
f2 = np.copy(x)*1./Ngrid #for Lax-Friedrichs

#set up plot
plt.ion()
fig, axes = plt.subplots(1, 2)
axes[0].set_title("FTCS")
axes[1].set_title("Lax-Friedrichs")

#plot the initial state for reference
axes[0].plot(x, f1, 'k-')
axes[1].plot(x, f2, 'k-')

plt1, = axes[0].plot(x, f1, 'ro')
plt2, = axes[1].plot(x, f2, 'ro')

for ax in axes:
    ax.set_xlim([0, Ngrid])
    ax.set_ylim([0, 2])

fig.canvas.draw()

count = 0
while count < Nsteps:
    #FTCS
    f1[1:Ngrid-1] = f1[1:Ngrid-1] - alpha*(f1[2:] - f1[:Ngrid-2])
    #Lax-Fried
    f2[1:Ngrid-1] = 0.5*(f2[2:] + f2[:Ngrid-2]) - alpha*(f2[2:] - f2[:Ngrid-2])

    plt1.set_ydata(f1)
    plt2.set_ydata(f2)

    fig.canvas.draw
    plt.pause(0.001)
    count += 1
