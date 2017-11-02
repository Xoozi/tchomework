
#求 u×v和 v×u

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


def scale(v, f):
    return (v[0]*f, v[1]*f, v[2]*f)

def proj(v, u):
    f = (dot(v, u)/(norm(v)**2))
    return scale(v, f)


def work(lable, u, v):

    print '%s' % (lable)
    uxv = cross(u, v)
    vxu = cross(v, u)
    nuxv = normalize(uxv)
    nvxu = normalize(vxu)
    print 'u x v direction:(%f, %f, %f)' % nuxv
    print 'u x v lenth:%f' % norm(uxv)

    print 'v x u direction:(%f, %f, %f)' % nvxu
    print 'v x u length:%f' % norm(vxu)




work("17", (2.0, -2.0, -1.0), (1.0, 0.0, -1.0))
work("19", (2.0, -2.0, 4.0), (-1.0, 1.0, -2.0))
work("21", (2.0, 0.0, 0.0), (0.0, -3.0, 0.0))
work("23", (-8.0, -2.0, -4.0), (2.0, 2.0, 1.0))
