#把v写成平行于u的向量和垂直于u的向量之和

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

def norm(v):
    return sqrt(dot(v, v))

def normalize(v):
    n = norm(v)
    return (v[0]/n, v[1]/n, v[2]/n)

def scale(v, f):
    return (v[0]*f, v[1]*f, v[2]*f)

def add(v, u):
    return (v[0] + u[0], v[1] + u[1], v[2] + u[2])

def sub(v, u):
    return (v[0] - u[0], v[1] - u[1], v[2] - u[2])

def proj(v, u):
    f = (dot(v, u)/(norm(v)**2))
    return scale(v, f)


def work(lable, v, u):

    tv = proj(u, v)
    nv = sub(v, tv)
    av = add(tv, nv)
    print '%s:' % lable
    print '\ttanVec:(%f, %f, %f)' % tv
    print '\tnormalVec:(%f, %f, %f)' % nv
    print '\tadd:(%f, %f, %f' % av



work("07", (1.0, 1.0, 0.0), (0.0, 3.0, 4.0))
work("09", (1.0, 2.0, -1.0), (8.0, 4.0, -12.0))

#xoozi 和答案对不上, 但验算发现我是对的
