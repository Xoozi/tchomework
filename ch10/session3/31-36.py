
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


#31 按下列步骤求从点S到平面Ax + By + Cz = D的距离
#(a)求平面上一点P
#   P(x0, y0, z0), 有D = Ax0 + By0 + Cz0
#(b)求PS
#   PS = (x - x0)i + (y - y0)j + (z - z0)k
#(b)距离公式 证明距离是 d = |PS · n/|n||
#   设原点为O(0, 0, 0), 则SO = xi + yj + zk
#   SO在n方向的分量 = SO · n/|n|
#   此即为S在n方向到原点的距离
#   而D/|n|为平面到原点的距离
#   S到平面的距离可以表示为OS · n/|n| - D/|n| = (OS · n - D)/|n| = (Ax + By + Cz - Ax0 - By0 - Cz0)/|n|
#   = (A(x - x0)  + B(y - y0) + C(z - z0))/|n| = (n · PS)/|n|
#   这里就已经得证了
#
#   xoozi下面来看看工业化的办法, 使用齐次坐标, 点S表示为(x, y, z, 1), 平面表示为四维向量(A, B, C, -D)
#   四维內积dot4(S, Plane) = Ax + By + Cz - D = Ax + By + Cz - Ax0 - By0 - Cz0 = A(x - x0) + B(y - y0) + C(z - z0)
#   所以dot(S, Plane) / |n| 就可以求出距离了, 通常构造平面对象时会把n归一化, 跨域直接用dot4(S, Plane)来表示距离非常方便
#   无需像上面的公式去求P, 太绕了
#   
def dist2line(line, s):
    p = (line[0], line[1], line[2])
    v = (line[3], line[4], line[5])
    ps = sub(s, p)
    return norm(cross(ps, v))/norm(v)


print "29 distance:%f" % (dist2line(line((2, 1, 3), (2, 6, 0)), (2, 1, 3)))
