
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 30), ylim=(-0.7, 0.7))
line, = ax.plot([], [], lw=2)

### set up the x-axis
x = np.linspace(0, 30, 1000)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially to generate the animation
def animate(i):
    ### Create an empty array of 1000 complex numbers that can be filled with the time-dependent wavefunction values
    psi_t = np.zeros(1000,dtype=complex)
    ### Creates an array of values of energy eigenstate 3 evaluated at 1000 x-values between 0 and L=30 atomic units
    space = PIB_Func(x, 3, 30.)
    ### Evaluate time-dependent part of current state at current time
    time = PIB_Time(3, 30, i)

    ### set array for time-dependent wavefunction equal to space * time
    psi_t = space*time

    ### define an array that will be the y-axis of the
    ### animation to be the real part of the psi_t wavefunction
    y = np.real(psi_t)
    ### define the current state of the animation object
    line.set_data(x, y)
    return line,

#### give a list of x-values between 0 and L, the length L, and the quantum numbner n
#### return a list of psi_n values between 0 and L
def PIB_Func(x, n, L):
    psi_n = np.sqrt(2./L)*np.sin(n*np.pi*x/L)
    return psi_n


### Give a quantum number n and a length L, return the energy 
### of an electron in a box of length L in state n
def PIB_En(n, L):
    En = (n*n * np.pi*np.pi)/(2*L*L)
    return En

### Give the quantum number and the current time, evaluate the time-dependent part of the wavefunction at current time
### and return its value
def PIB_Time(n, L, t):
    E = PIB_En(n, L)
    ci = 0.+1j
    phi_n_t = np.exp(-1*ci*E*t)
    return phi_n_t


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
	                               frames=10000, interval=20, blit=True)
        
plt.show()
