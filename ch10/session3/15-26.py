
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

##求下列平面的方程
p15 = panel((0, 2, -1), (3, -2, -1))
print "15--过(0, 2, -1), 垂直于n = 3i - 2j - k的平面:(%f, %f, %f, %f)" % p15


a = (1, 1, -1)
b = (2, 0, 2)
c = (0, -2, 1)
u = sub(a, b)
v = sub(a, c)
n = cross(u, v)
p17 = panel(a, n)
print "17--过(1, 1, -1), (2, 0, 2) 和(0, -2, 1)的平面:(%f, %f, %f, %f)" % p17


p19 = panel((2, 4, 5), (1, 3, 4))
print "19--过(2, 4, 5), 垂直于直线x=5+t, y=1+3t, z=4t的平面:(%f, %f, %f, %f)" % p19


#21联立解得交点的t = 0, s = -1
#由于方程组是超定的不确定两直线是否相交, 代入验证一下:
#代入直线方程1 x = 1, y = 2, z = 3
#代入直线方程2 x = 1, y = 2, y = 3
#说明两直线是相交的, 从而得知它们共面
v1 = (2, 3, 4)
v2 = (1, 2, -4)
n = cross(v1, v2)
p21 = panel((1, 2, 3), n)
print "21题的平面为:(%f, %f, %f, %f)" % p21

#23 联立解得交点的 t = 0, s = 1/2
#由于方程组是超定的, 代入验证一下:
#代入直线方程1 x = -1, y = 2, z = 1
#代人直线方程2 x = -1, y = 2, z = 1
#说明两直线是相交的, 从而得知它们共面
v1 = (1, 1, -1)
v2 = (-4, 2, -2)
n = cross(v1, v2)
p23 = panel((-1, 2, 1), n)
print "23题的平面为:(%f, %f, %f, %f)" % p23


#25 求过点(2, 1, -1), 并且垂直于两平面2x + y - z = 3和x + 2y + z = 2的交线的平面
n1 = (2, 1, -1)
n2 = (1, 2, 1)
n = cross(n1, n2)
p25 = panel((2, 1, -1), n)
print "25题的平面为:(%f, %f, %f, %f)" % p25
