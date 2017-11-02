#求由u, v, w三个向量确定的平行六面体的体积

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

def cross(u, v):
    return ((u[1]*v[2] - u[2]*v[1]), (u[2]*v[0] - u[0]*v[2]), (u[0]*v[1] - u[1]*v[0]))

def box(u, v, w):
    return dot(cross(u, v), w)

def norm(v):
    return sqrt(dot(v, v))

def normalize(v):
    n = norm(v)
    if 0 == n:
        return (0.0, 0.0, 0.0)
    else:
        return (v[0]/n, v[1]/n, v[2]/n)

def sub(v, u):
    return (v[0] - u[0], v[1] - u[1], v[2] - u[2])

def scale(v, f):
    return (v[0]*f, v[1]*f, v[2]*f)

def proj(v, u):
    f = (dot(v, u)/(norm(v)**2))
    return scale(v, f)


def work(lable, u, v, w):

    print '%s' % (lable)
    uxvdotw = dot(cross(u, v), w)
    vxwdotu = dot(cross(v, w), u)
    wxudotv = dot(cross(w, u), v)

    print '\tuxvdotw:%f' % uxvdotw
    print '\tvxwdotu:%f' % vxwdotu
    print '\twxudotv:%f' % wxudotv
    print '\tvolume:%f' % uxvdotw


work("33", (2.0, 0.0, 0.0), (0.0, 2.0, 0.0), (0.0, 0.0, 2.0))
work("35", (2.0, 1.0, 0.0), (2.0, -1.0, 1.0), (1.0, 0.0, 2.0))
