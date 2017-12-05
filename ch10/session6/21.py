def sub(v, u):
    return (v[0] - u[0], v[1] - u[1], v[2] - u[2])

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

def cross(u, v):
    return ((u[1]*v[2] - u[2]*v[1]), (u[2]*v[0] - u[0]*v[2]), (u[0]*v[1] - u[1]*v[0]))

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

def plane(p, n):
    nn = normalize(n)
    return (nn[0], nn[1], nn[2], -dot(p, nn))

#椭圆
#(a)通过证明曲线 r(t) = (cos t)i + (sin t)j + (1 - cos t)k,  0 <= t <= 2pi是一个正圆柱和一个平面的交来证明这个曲线是椭圆. 并求柱面和平面的方程

#   观察可知柱面方程是 c(t) = (cos t)i + (sin t)j
#   对于r(t):
#       t = 0      时位置A = (1, 0, 0)
#       t = pi/2   时位置B = (0, 1, 1)
#       t = pi	   时位置C = (-1, 0, 2)
#       t = 3pi/2  ...
#       t = 2pi    ...

A = (1, 0, 0)
B = (0, 1, 1)
C = (-1, 0, 2)

AB = sub(B, A)
BC = sub(C, B)

n = cross(AB, BC)
nn = normalize(n)

print 'n:(%f, %f, %f)' % n
print 'nn:(%f, %f, %f)' % nn
#结果n = 2i + 2k
#当t不等于0和2pi时, R = r(t) = (cos t)i + (sin t)j + (1 - cos t)k
#与A(1, 0, 0)的差AR = (cos t - 1)i + (sin t)j + (1 - cos t)k
#dot(AR, n) = 2cos t - 2 + 2 - 2cos t = 0
#可知, 所有属于r(t)的点, 都在过A, 法向量为n的平面上

p = plane(A, n)
print 'plane:(%f, %f, %f, %f)' % p


#(b)在圆柱面上画椭圆, 并求t = 0, pi/2, pi, 3pi/2处的单位切向量
#v(t)   = (-sin t)i + (cos t)j + (sin t)k
#|v(t)| = sqrt(sin²t + cos²t + sin²t) = sqrt(1 + sin²t)
#T      = v(t)/|v(t)| = (-sin t/sqrt(1 + sin²t))i + (cos t/sqrt(1 + sin²t))j + (sin t/sqrt(1 + sin²t))k
def funT(t):
    return (-sin(t)/sqrt(1 + sin(t)**2), cos(t)/sqrt(1 + sin(t)**2), sin(t)/sqrt(1 + sin(t)**2))

T0 = funT(0)
T1 = funT(pi/2)
T2 = funT(pi)
T3 = funT(3*pi/2)
print 'T0:(%f, %f, %f)' % T0
print 'T1:(%f, %f, %f)' % T1
print 'T2:(%f, %f, %f)' % T2
print 'T3:(%f, %f, %f)' % T3

#(c)证明加速度向量总平行于该平面
#a(t) = (-cos t)i + (-sin t)j + (cos t)k
#dot(a, n) = -2cos t + 2cos t = 0
#于是可知加速度总是垂直于该平面的法向, 故平行于该平面

#(d)写出椭圆长度的积分, 不要试图求积分的值, 它不是初等的
#s = ∫(0, 2pi) |v(t)| dt = ∫(0, 2pi) sqrt(1 + sin²t) dt


#(e)估计椭圆长度, 用数值积分

sample = linspace(0, 2*pi, 10000)
sum = 0.0
i = 0
while i < 10000:
    sum += sqrt(1 + sin(sample[i])**2)
    i += 1
len = 2*pi*sum/10000
print 'len:%f' % (len)
#我写了一个土得不行的数值积分, 结果还可以

#xoozi 这个题真是有意思, 启发性的
























