#枪以1200英尺每秒的弹速, 在水平以上8度发射, 求速度的水平分量和垂直分量


def deg2Radian(d):
    return pi*d/180.0

theta = deg2Radian(8)

vx = 1200.0*cos(theta)
vy = 1200.0*sin(theta)

print 'vx:%f, vy:%f' % (vx, vy)
