#求三角形角的大小, 它的顶点是A = (-1, 0), B = (2, 1), C = (0, 3)

def vecPP(start, end):
    return (end[0] - start[0], end[1] - start[1])

def dot(v, u):
    return v[0]*u[0] + v[1]*u[1]

def norm(v):
    return sqrt(dot(v, v))

def angle(v, u):
    return arccos(dot(v, u)/(norm(v)*norm(u)))

def radian2Deg(r):
    return 360.0 * r/(2.0*pi)

posA = (-1.0, 0.0)
posB = (2.0, 1.0)
posC = (0.0, 3.0)

vAB = vecPP(posA, posB)
vBC = vecPP(posB, posC)
vCA = vecPP(posC, posA)
angleABC = angle(vAB, vBC)
angleBCA = angle(vBC, vCA)
angleCAB = angle(vCA, vAB)
print 'angle    ABC:%f, BCA:%f, CAB:%f' % (radian2Deg(angleABC), radian2Deg(angleBCA), radian2Deg(angleCAB))

vAB = vecPP(posA, posB)
vAC = vecPP(posA, posC)
angleBAC = angle(vAB, vAC)

vBA = vecPP(posB, posA)
vBC = vecPP(posB, posC)
angleCBA = angle(vBA, vBC)

vCA = vecPP(posC, posA)
vCB = vecPP(posC, posB)
angleACB = angle(vCA, vCB)

print 'angle BAC:%f, CBA:%f, ACB:%f' % (radian2Deg(angleBAC), radian2Deg(angleCBA), radian2Deg(angleACB))

#xoozi 这里可见, 如果要求绝对的夹角, 需要两向量起点相同, 否则可能求得的是其补角
