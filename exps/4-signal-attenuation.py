'''
EXP 3: To compute overall signal attenuation, signal attenuation (dB/km), and
attenuation with splices.
'''
from math import log10

Pi = float(input('[+] Pi : '))
Po = float(input('[+] Po : '))
L = float(input('[+] L (km): '))
single_splice_att = 1


# aplha (dB)
sig_att = 10*log10(Pi/Po)

# aplha (dB/km)
sig_att_per_len = sig_att/L

# splice attenuation
splice_att = (L-1) * single_splice_att

# overall attenuation
overall_att = sig_att + splice_att

print(f'''
α (dB): {sig_att}
α (dB/km): {sig_att_per_len}
α splice (dB): {splice_att}
overall signal attentuation: {overall_att}
''')