#求对给定的t值的r, T, N, 和B, 然后求在该t值的密切, 法, 和次法平面的方程
#r(t) = (cos t)i + (sin t)j - k,     t = pi/4

#    v = (-sin t)i + (cos t)j
#    |v| = 1

#    T = v/|v| = (-sin t)i + (cos t)j


#    dT/dt = (-cos t)i + (-sin t)j
#    |dT/dt| = 1

#    N = dT/dt/|dT/dt| = (-cos t)i + (-sin t)j

#                |i          j           k|
#    B = T x N = |(-sin t)   (cos t)     0| = 0i + 0j + (sin²t + cos²t)k = k
#                |(-cos t)   (-sin t)    0|

#    r(pi/4) = sqrt(2)/2 i + sqrt(2)/2 j - k

def r(t):
    return (cos(t), sin(t), -1)

def T(t):
    return (-sin(t), cos(t), 0)

def N(t):
    return (-cos(t), -sin(t), 0)

def B():
    return (0, 0, 1)

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

def panel(p, n):
    return (n[0], n[1], n[2], dot(p, n))

pos = r(pi/4)
vT = T(pi/4)
vN = N(pi/4)
vB = B()



panelOsc = panel(pos, vB)
panelNormal = panel(pos, vT)
panelRect = panel(pos, vN)

print 'pos: (%f, %f, %f)' % pos
print 'vT: (%f, %f, %f)' % vT
print 'vN: (%f, %f, %f)' % vN
print 'vB: (%f, %f, %f)' % vB

print 'Osculating plane: (%f, %f, %f, %f)' % panelOsc
print 'Normal plane: (%f, %f, %f, %f)' % panelNormal
print 'Rectifying plane: (%f, %f, %f, %f)' % panelRect






