
#求
#(a)由点P, Q, R确定的三角形的面积
#(b)一个垂直于平面PQR的单位向量

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

def sub(v, u):
    return (v[0] - u[0], v[1] - u[1], v[2] - u[2])

def scale(v, f):
    return (v[0]*f, v[1]*f, v[2]*f)

def proj(v, u):
    f = (dot(v, u)/(norm(v)**2))
    return scale(v, f)


def work(lable, p, q, r):

    print '%s' % (lable)
    pq = sub(q, p)
    pr = sub(r, p)
    pqxpr = cross(pq, pr)

    print '\tP:(%f, %f, %f)' % p
    print '\tQ:(%f, %f, %f)' % q
    print '\tR:(%f, %f, %f)' % r
    print '\t(a) area of PQR:%f' % (norm(pqxpr)/2.0)
    print '\t(b) normal vec:(%f, %f, %f)' % normalize(pqxpr)





work("29", (1.0, -1.0, 2.0), (2.0, 0.0, -1.0), (0.0, 2.0, 1.0))
work("31", (2.0, -2.0, 1.0), (3.0, -1.0, 2.0), (3.0, -1.0, 1.0))
