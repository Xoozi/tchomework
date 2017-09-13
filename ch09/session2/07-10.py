#求向量之间的夹角


def dot(v, u):
    return v[0]*u[0] + v[1]*u[1]

def norm(v):
    return sqrt(dot(v, v))

def angle(v, u):
    return arccos(dot(v, u)/(norm(v)*norm(u)))

#7 v = 2i + j, u = i + 2j
v7 = (2.0, 1.0)
u7 = (1.0, 2.0)
angle7 = angle(v7, u7)

v9 = (sqrt(3.0), -7.0)
u9 = (sqrt(3.0), 1.0)
angle9 = angle(v9, u9)

print 'angle7:%f, angle9:%f' % (angle7, angle9)
