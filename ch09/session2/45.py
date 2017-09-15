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
45. y= 3/2 - x**2, y = x**2

    先联立求交点
    x**2 = 3/2 - x**2
    2x**2 = 3/2
    x = ±sqrt(3)/2
    
    对于曲线1 dy/dx = -2x
    对于曲线2 dy/dx = 2x

    在交点1 曲线1的切线斜率为sqrt(3), 曲线2的切线斜率为-sqrt(3)
    构造两个向量分别为v1 = <1, sqrt(3)>, v2 = <1, -sqrt(3)>
    夹角为arccos(dot(v1, v2))

    在交点2 曲线1的切线斜率为-sqrt(3), 曲线2的切线斜率为sqrt(3)
    u1 = <1, -sqrt(3)>, u2 = <1, sqrt(3)>
    
    '''

v1 = vec(1.0, sqrt(3.0))
v2 = vec(1.0, -sqrt(3.0))
angle1 = angle(v1, v2)
u1 = vec(1.0, -sqrt(3.0))
u2 = vec(1.0, sqrt(3.0))
angle2 = angle(u1, u2)

print 'angle1:%f, angle2:%f' % (angle1, angle2)
