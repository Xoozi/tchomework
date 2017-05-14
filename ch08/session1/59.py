#求使得不等式对所有n > N成立的N,
#(0.9)**n < 10**(-3)

def f(n):
    return 0.9**(n)

i = 1

while f(i) > 0.001:
    i += 1

print 'n > %d' % (i)


#N = 66, 极限为0
