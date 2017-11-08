
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

def panel(p, n):
    return (n[0], n[1], n[2], dot(p, n))


#27 求点s到过点p且平行于向量v的直线的距离
#(a)证明PS垂直于该直线的分量为|PS| sin θ
#   这个太显然了, 设θ为PS和v的夹角, PS垂直于v的分量就是|PS| sin θ
#(b)距离公式, 证明从s到过p平行于v的直线的距离是d = |PS x v|/|v|
#   根据叉积定义的推论有 |PS x v| = |PS|*|v|*sin θ
#   故|PS| sin θ = |PS x v|/|v|
def dist2line(line, s):
    p = (line[0], line[1], line[2])
    v = (line[3], line[4], line[5])
    ps = sub(s, p)
    return norm(cross(ps, v))/norm(v)


print "29 distance:%f" % (dist2line(line((2, 1, 3), (2, 6, 0)), (2, 1, 3)))
