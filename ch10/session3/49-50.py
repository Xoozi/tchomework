

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

def add(u, v):
    return (u[0]+v[0], u[1]+v[1], u[2]+v[2])

def sub(u, v):
    return (u[0]-v[0], u[1]-v[1], u[2]-v[2])

def scale(v, f):
    return (v[0]*f, v[1]*f, v[2]*f)

def line(p, v):
    return (p[0], p[1], p[2], v[0], v[1], v[2])

def panel(p, n):
    return (n[0], n[1], n[2], dot(p, n))


FLT_ABS_ERROR  = 1e-6

def equ(u, v):

    if abs(u[0] - v[0]) > FLT_ABS_ERROR:
        return False
    if abs(u[1] - v[1]) > FLT_ABS_ERROR:
        return False
    if abs(u[2] - v[2]) > FLT_ABS_ERROR:
        return False

    return True


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


#给出三条直线, 一次取其中两条, 确定他们平行, 相交, 或相错, 如果相交, 求交点
#49.
#L1: x = 3 + 2t, y = -1 + 4t, z = 2 - t
#L2: x = 1 + 4s, y = 1 + 2s, z = -3 + 4s
#L3: x = 3 + 2r, y = 2 + r, z = -2 + 2r

def work(lable, l1, l2):
    v1 = (l1[3], l1[4], l1[5])
    v2 = (l2[3], l2[4], l2[5])

    print "%s:" % (lable)
    
    if equ(normalize(v1), normalize(v2)):
        print "\t两直线平行"
        return

    #到了这里说明两直线要么相交要么相错
    #已知同一平面上的非平行直线一定相交
    #故重点在于判断两直线是否共面
    #设, 两直线共面, 则必有交点p:(x, y, z)
    #设平面方程为Ax + By + Cz = D
    #我想了一种办法, 先用v1 x v2求得n1
    #再交换直线的首尾, 求两方向w1, w2
    #再求w1 x w2 得n2, 对n1, n2 可知两直线是否共线
    s1 = (l1[0], l1[1], l1[2])
    s2 = (l2[0], l2[1], l2[2])
    e1 = add(s1, v1)
    e2 = add(s2, v2)
    w1 = sub(e2, s1)
    w2 = sub(e1, s2)

    n1 = cross(v1, v2)
    n2 = cross(w1, w2)
    
    if equ(normalize(n1), normalize(n2)):
        print "\t两直线相交"
    else:
        print "\t两直线相错"

    return


#L1: x = 3 + 2t, y = -1 + 4t, z = 2 - t
#L2: x = 1 + 4s, y = 1 + 2s, z = -3 + 4s
#L3: x = 3 + 2r, y = 2 + r, z = -2 + 2r
l1 = line((3, -1, 2), (2, 4, -1))
l2 = line((1, 1, -3), (4, 2, 4))
l3 = line((3, 2, -2), (2, 1, 2))

work("L1 vs L2", l1, l2)
work("L1 vs L3", l1, l3)
work("L2 vs L3", l2, l3)

#xoozi 我以为我的办法够土了, 答案的比我还土, 用判断超定方程的局部解是否满足所有条件的办法
#其实有更好办法
'''
         * 非平行的情况可以用下面的公式解出两条直线最短距离的两点的参数
         * ┌  ┐                             ┌              ┐┌          ┐
         * │t1│               1             │-V2**2   V1·V2││(S2-S1)·V1│
         * │  │ = ───────────────────────── │              ││          │
         * │t2│   (V1·V2)**2 - V1**2*V2**2  │-V1·V2   V1**2││(S2-S1)·V2│
         * └  ┘                             └              ┘└          ┘
         *'''
#恩仔细一想, 这种办法其实更近于答案的办法, 比我的办法好在鲁棒性更佳
#只是说,我的办法, 和这种办法可以较容易地写成函数
#看来书还是不土























   
