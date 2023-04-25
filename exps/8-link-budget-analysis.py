'''
EXP 8: Link budget analysis
'''
# with jumper loss

print('[*] With Jumper Loss:\n\n')
# Pt = float(input('[+] Pt (dBm): '))
# Pr = float(input('[+] Pr (dBm): '))
# Lj = float(input('[+] Lj (dB): '))
# Lc = float(input('[+] Lc (dB): '))
# Af = float(input('[+] Af (dB): '))
# L = float(input('L (km): '))

Pt = -3
Pr = 30
Lj = 1.5
Lc = 2
Af = 1
L = 8

# Power loss of optical system dB
P = Pt - Pr
print('Power Loss of Optical System (dB):', P)

# Power Margin
Ms = P - (Af * L) - (2*Lc) - (2*Lj)
print('Power Margin (dB):', Ms)

# To calculate total power
for l in range(1,L+1):
    p = Lc + (Af * l) + Lj
    print(f'Total Power at {l} km: {p} (dB)')

print('\n\nWithout Jumper Loss:\n')

# Pt = -3
# Pr = 30
# Lj = 1.5
# Lc = 2
# Af = 1
# L = 8

# Power loss of optical system dB
P = Pt - Pr
print('Power Loss of Optical System (dB):', P)

# Power Margin
Ms = P - (Af * L) - (2*Lc) 
print('Power Margin (dB):', Ms)

# To calculate total power
for l in range(1,L+1):
    p = Lc + (Af * l)
    print(f'Total Power at {l} km: {p} (dB)')


# [*] With Jumper Loss:

# Power Loss of Optical System (dB): -33
# Power Margin (dB): -48.0
# Total Power at 1 km: 4.5 (dB)
# Total Power at 2 km: 5.5 (dB)
# Total Power at 3 km: 6.5 (dB)
# Total Power at 4 km: 7.5 (dB)
# Total Power at 5 km: 8.5 (dB)
# Total Power at 6 km: 9.5 (dB)
# Total Power at 7 km: 10.5 (dB)
# Total Power at 8 km: 11.5 (dB)


# Without Jumper Loss:

# Power Loss of Optical System (dB): -33
# Power Margin (dB): -45
# Total Power at 1 km: 3 (dB)
# Total Power at 2 km: 4 (dB)
# Total Power at 3 km: 5 (dB)
# Total Power at 4 km: 6 (dB)
# Total Power at 5 km: 7 (dB)
# Total Power at 6 km: 8 (dB)
# Total Power at 7 km: 9 (dB)
# Total Power at 8 km: 10 (dB)