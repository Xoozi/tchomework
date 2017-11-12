#求两平面的交线的参数方程

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


#45. x + y + z = 1, x + y = 2
n1 = (1, 1, 1)
n2 = (1, 1, 0)
n = cross(n1, n2)
#令x = 0, 联立平面方程 y + z = 1, y = 2, 可知交线上一点为(0, 2, -1)
l = line((0, 2, -1), n)
print "45. line:(%f, %f, %f-%f, %f, %f)" % l


#47. x - 2y + 4z = 2, x + y - 2z = 5
n1 = (1, -2, 4)
n2 = (1, 1, -2)
n = cross(n1, n2)
#令y = 0, x + 4z = 2, x - 2z = 5 => 3x = 12 x = 4 => z = -1/2, 可知交线上一点为(4, 0, -1/2)
l = line((4, 0, -1/2), n)
print "47. line:(%f, %f, %f-%f, %f, %f)" % l
