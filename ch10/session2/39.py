#求力F在螺栓的上施加的转矩的大小, 假定r = 8英寸, F = 30磅
#xoozi 这是坑爹的, r给8英寸, 答案要用英尺算, 无聊不无聊
#8英寸 = 8/12 = 2/3 英尺

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

def cross(u, v):
    return ((u[1]*v[2] - u[2]*v[1]), (u[2]*v[0] - u[0]*v[2]), (u[0]*v[1] - u[1]*v[0]))

def norm(v):
    return sqrt(dot(v, v))

theta = pi/3.0
f = (30*cos(theta), 30*sin(theta), 0.0)
r = (2.0/3.0, 0.0, 0.0)
fxr = cross(f, r)

print 'fxr:(%f, %f, %f)' % fxr
print 'torque:%f' % norm(fxr)
