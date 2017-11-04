
#(a) 求点P1和P2之间的距离
#(b) 向量P1P2的方向
#(c) 线段P1P2的中点

def vecPP(start, end):
    return (end[0] - start[0], end[1] - start[1], end[2] - start[2])


def dot(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

def norm(v):
    return sqrt(dot(v, v))

def normalize(v):
    n = norm(v)
    return (v[0]/n, v[1]/n, v[2]/n)

def mid(start, end):
    return ((end[0]+start[0])/2.0, (end[1]+start[1])/2.0, (end[2]+start[2])/2.0)


def work(lable, start, end):
    v = vecPP(start, end)
    n = norm(v)
    nv = normalize(v)
    m = mid(start, end)

    print "%s. P1:(%.1f, %.1f, %.1f), P2:(%.1f, %.1f, %.1f), distance:%.2f, direction:(%.1f, %.1f, %.1f), mid:(%.1f, %.1f, %.1f)" % (lable, start[0], start[1], start[2], end[0], end[1], end[2], n, nv[0], nv[1], nv[2], m[0], m[1], m[2])


work("43", (-1.0, 1.0, 5.0), (2.0, 5.0, 0.0))
work("45", (3.0, 4.0, 5.0), (2.0, 3.0, 4.0))

