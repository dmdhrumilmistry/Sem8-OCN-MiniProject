'''
Exp 5: To compute responsivity, received optical power,
number of photons, thermal noise, shot power, S/N ratio
for PIN diode.
'''
from matplotlib import pyplot as plt
import numpy as np

T = 40 + 273
B = 50e3
k = 1.38e-23
e = 1.6e-19
R1 = 2000

print('Temperature (K):', T)

# for Is = 2.k.T
#         -------
#          e.R1
Is = (2*k*T)/(e*R1)
print('Is:', Is)

# for recvd optical power
# Pr = Is
#     ----
#      R
R = 0.5
Pr = Is/R
print('Received Optical Power Pr:', Pr)

# For Thermal Noise Temperature
# Pnt = 4.k.T.B
Pnt = 4 * k * T * B
print('Thermal Noise Temperature Pnt:', Pnt)


# S/N =   Is
#      --------
#        4.e.B
s_n = Is/(4*e*B)
print('Signal to Noise Ratio (S/N):', s_n)

# Shot Noise Power
# Psn = 2.e.Is.B.R1
Psn = 2*e*Is*B*R1
print('Shot Noise Power Psn:', Psn)

# Responsivity
# R = n.e.lam
#    ---------
#       h.c
n = 50/100
lam = 0.9e-6
h = 6.6e-34
c = 3.8e8

R = (n * e * lam)/(h*c)
print('R:', R)

# For optical Power (Po)
Ip = 1e-6
Po = Ip/R
print('Received Optical Power (Po):', Po)

# for number of photons
# E = h.c
#    ------
#     lamb
#
# Np = Po
#     -----
#      E
E = h*c/lam
Np = Po/E
print('Number of photons (Np):', Np)

# For plot
plot_lambda = np.linspace(0,1000)
plot_po = np.linspace(0,0.3)

plt.plot(plot_lambda, plot_po)
plt.xlabel('Wavelength in nm')
plt.ylabel('Optical Power in micro meter')
plt.show()