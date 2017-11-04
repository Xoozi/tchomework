#求
#(a) dot(v, u), norm(v), norm(u)
#(b) v和u之间夹角的余弦
#(c) v在方向u的数量分量
#(d) 向量proj(v, u)

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1] + v[2]*u[2]

def norm(v):
    return sqrt(dot(v, v))

def normalize(v):
    n = norm(v)
    return (v[0]/n, v[1]/n, v[2]/n)

def scale(v, f):
    return (v[0]*f, v[1]*f, v[2]*f)

def proj(v, u):
    f = (dot(v, u)/(norm(v)**2))
    return scale(v, f)


def work(lable, v, u):
    print '%s' % (lable)
    dvu = dot(v, u)
    nv = norm(v)
    nu = norm(u)
    print '\tdot(v, u):%f, norm(v):%f, norm(u):%f' % (dvu, nv, nu)

    ctheta = dvu/(nv * nu)
    theta = arccos(ctheta)
    print '\tctheta:%f, theta:%f' % (ctheta, theta)

    scaleVonU = nv*ctheta
    print '\tscaleVonU:%f' % (scaleVonU)

    projVU = proj(v, u)
    print '\tprojVU:(%f, %f, %f)' % projVU



work("01", (2.0, -4.0, sqrt(5)), (-2.0, 4.0, -sqrt(5)))
work("03", (10.0, 11.0, -2.0), (0.0, 3.0, 4.0))
work("05", (0.0, 5.0, -3.0), (1.0, 1.0, 1.0))

