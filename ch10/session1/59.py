

def vecPP(start, end):
    return (end[0] - start[0], end[1] - start[1], end[2] - start[2])


def dot(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

def norm(v):
    return sqrt(dot(v, v))

def normalize(v):
    n = norm(v)
    return (v[0]/n, v[1]/n, v[2]/n)

def scale(v, f):
    return (v[0] * f, v[1] * f, v[2] * f)

def add(v, u):
    return (v[0] + u[0], v[1] + u[1], v[2] + u[2])

def mid(start, end):
    return ((end[0]+start[0])/2.0, (end[1]+start[1])/2.0, (end[2]+start[2])/2.0)


# 三角形三顶点: A(4, 2, 0), B(1, 3, 0), C(1, 1, 3)
#(a) 求从C到AB中点M的向量
a = (4.0, 2.0, 0.0)
b = (1.0, 3.0, 0.0)
c = (1.0, 1.0, 3.0)

m = mid(a, b)
cm = vecPP(c, m)
print 'vec CM:(%.2f, %.2f, %.2f)' % cm

#(b) 求从C到 CM连线三分之二处的点的向量
stepcm = scale(cm, 2.0/3.0)
tar = add(c, stepcm)
ctar = vecPP(c, tar)
print 'ctar : (%.2f, %.2f, %.2f)' % ctar

#(c) 求薄板的质心
