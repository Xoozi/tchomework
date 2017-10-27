#把每个向量表示成他的长度和方向的乘积

def vec(x, y, z):
    return (x, y, z)

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

def norm(v):
    return sqrt(dot(v, v))

def normalize(v):
    n = norm(v)
    return (v[0]/n, v[1]/n, v[2]/n)


def work(lable, x, y, z):
    v = vec(x, y, z)
    n = norm(v)
    nv = normalize(v)

    print '%s. v:(%.2f, %.2f, %.2f) = %.2f * (%.2f, %.2f, %.2f)' % (lable, x, y, z, n, nv[0], nv[1], nv[2])


work("33", 2.0, 1.0, -2.0)
work("35", 0.0, 0.0, 5.0)
work("37", 1/sqrt(6.0), -1/sqrt(6.0), -1/sqrt(6.0))

