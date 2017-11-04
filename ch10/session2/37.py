
#设u = 5i - j + k, v = j - 5k, w = -15i + 3j - 3k, 其中哪些平行, 哪些正交

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

def cross(u, v):
    return ((u[1]*v[2] - u[2]*v[1]), (u[2]*v[0] - u[0]*v[2]), (u[0]*v[1] - u[1]*v[0]))


u = (5.0, -1.0, 1.0)
v = (0.0, 1.0, -5.0)
w = (-15.0, 3.0, -3.0)

udv = dot(u, v)
udw = dot(u, w)
vdw = dot(v, w)

ucv = norm(cross(u, v))
ucw = norm(cross(u, w))
vcw = norm(cross(v, w))

print 'udv:%f, udw:%f, vdw:%f' % (udv, udw, vdw)
print 'ucv:%f, ucw:%f, vcw:%f' % (ucv, ucw, vcw)
