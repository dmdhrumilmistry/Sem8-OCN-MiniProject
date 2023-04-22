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
Ms = P - (Af * L) - (2*Lc) 
print('Power Margin (dB):', Ms)

# To calculate total power
for l in range(1,L+1):
    p = Lc + (Af * l)
    print(f'Total Power at {l} km: {p} (dB)')
