import matplotlib.pyplot as plt
import numpy as np

dt = 0.1
duration = 100
I = 200
V_th = -65
V_reset = -75
tau_m = 5
g_L = 10
V_init = -75
E_L = -75

time = np.arange(0, duration, dt)


def integrate(time_vector):
    V_mem = np.zeros(int(duration / dt))
    V_mem[0] = V_init
    t = 0
    for i in range(1, time_vector.size):
        V_mem[i] = V_mem[i - 1] + (((I / g_L) - (V_mem[i - 1] - V_reset)) / tau_m) * dt
    return V_mem


potential = integrate(time)
plt.plot(time, potential)
plt.xlabel("Time")
plt.ylabel("Membrane Potential (mV)")
plt.title("Simulation of a LIF neuron for 100s with dt=0.1s")
plt.show()
