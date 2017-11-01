
#求 向量v和u的夹角

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

def norm(v):
    return sqrt(dot(v, v))

def normalize(v):
    n = norm(v)
    return (v[0]/n, v[1]/n, v[2]/n)

def scale(v, f):
    return (v[0]*f, v[1]*f, v[2]*f)

def proj(v, u):
    f = (dot(v, u)/(norm(v)**2))
    return scale(v, f)


def work(lable, v, u):
    print '%s' % (lable)

    ctheta = dot(v, u)/(norm(v) * norm(u))
    theta = arccos(ctheta)
    print '\tctheta:%f, theta:%f' % (ctheta, theta)



work("11", (1.0, 2.0, -1.0), (2.0, 1.0, 0.0))
work("13", (sqrt(3.0), 1.0, -2.0), (sqrt(3.0), -7.0, 0.0))

