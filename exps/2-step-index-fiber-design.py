'''
Exp 2: To design step index fiber
'''

from math import sqrt, asin, cos, degrees, pi

n1 = float(input('[+] n1: '))
n2 = float(input('[+] n2: '))
lam = float(input('[+] wavelength (in micro-meters): '))

NA = sqrt(n1**2 - n2**2)
print(f'NA: {NA}')

theta_a = degrees(asin(NA))
print(f'acceptance angle (degrees): {theta_a}')

solid_angle = pi * (theta_a**2)
print(f'solid angle (steradian): {solid_angle}')

beta = (2*pi*n1/lam)*cos(theta_a)
print(f'propogation constant (deg/mm): {beta}')

# [+] n1: 1.48
# [+] n2: 1.46
# [+] wavelength (in micro-meters): 1.5
# NA: 0.2424871130596432
# acceptance angle (degrees): 14.033378410321736
# solid angle (steradian): 618.691778531737
# propogation constant (deg/mm): 0.6422730530064061
