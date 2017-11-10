

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

def cross(u, v):
    return ((u[1]*v[2] - u[2]*v[1]), (u[2]*v[0] - u[0]*v[2]), (u[0]*v[1] - u[1]*v[0]))

def norm(v):
    return sqrt(dot(v, v))

def normalize(v):
    n = norm(v)
    if 0 == n:
        return (0.0, 0.0, 0.0)
    else:
        return (v[0]/n, v[1]/n, v[2]/n)

def sub(u, v):
    return (u[0]-v[0], u[1]-v[1], u[2]-v[2])

def scale(v, f):
    return (v[0]*f, v[1]*f, v[2]*f)

def line(p, v):
    return (p[0], p[1], p[2], v[0], v[1], v[2])

def plane(p, n):
    nn = normalize(n)
    return (nn[0], nn[1], nn[2], -dot(p, nn))

def planeRaw(a, b, c, d):
    n = norm((a, b, c))
    return (a/n, b/n, c/n, -d/n)

#两平面夹角为各自法向量成的锐角
def planeAngle(p1, p2):
    n1 = (p1[0], p1[1], p1[2])
    n2 = (p2[0], p2[1], p2[2])
    return arccos(dot(n1, n2))


print "37 angle:%f" % (planeAngle(planeRaw(3, -6, -2, 15), planeRaw(2, 1, -2, 5)))

print "39 angle:%f" % (planeAngle(planeRaw(2, 2, -1, 3), planeRaw(1, 2, 1, 2)))

