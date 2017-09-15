
##可微曲线间的夹角
##两条可微曲线的夹角是曲线在该点切线之间的夹角

def vec(x, y):
    return (x, y)

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1]

def norm(v):
    return sqrt(dot(v, v))

def angle(v, u):
    return arccos(dot(v, u)/(norm(v)*norm(u)))


'''
47. y= x**3, x = y**2

    作图观察第一个交点在原点(0, 0)

    曲线1的切线斜率为0
    曲线2的切线斜率为无穷大
    故他们夹角为pi/2

    第二个交点是y = x**3 和y = sqrt(x)的交点
    联立=> x = 1
    
    曲线1的切线斜率为3x**2 = 3
    曲线2的切线斜率为1/2 x**(-1/2) = 1/2

    '''

u1 = vec(1.0, 3.0)
u2 = vec(1.0, 0.5)
angle2 = angle(u1, u2)

print 'angle1:%f, angle2:%f' % (pi/2.0, angle2)
