#一个排球在离地面4英尺距6英尺高的网12英尺处被击打. 
#它离开击打点时的初速率是35英尺/秒, 角度是27度,
#由于对方未触到球, 球落下

def deg2Radian(d):
    return pi*d/180.0

g = 32.0
v0 = 35.0
y0 = 4.0
alpha = deg2Radian(27)



#(a)求排球路径的向量方程
#可以视为从(x0, y0) = (0, 4)发射
#r = (v0 cos α t)i + (y0 + v0 sin α t - gt²/2)j

#(b)排球飞行多高? 何时排球达到最大高度
#排球的y分量 y = y0 + v0 sin a t - gt²/2
#dy/dt = v0 sin α - gt
#达到最大高度时, 速度y方向分量为0
#故0 = v0 sin α - gt => t = v0 sinα/g
def tYMax(v0, alpha, g):
    return v0 * sin(alpha) / g

def yMax(y0, v0, alpha, g):
    t = tYMax(v0, alpha, g)
    return y0 + v0 * sin(alpha) * t - g * t * t/2.0

def rx(v0, alpha, t):
    return v0 * cos(alpha) * t

tymax = tYMax(v0, alpha, g)
ymax = yMax(y0, v0, alpha, g)

print 'Height max:%f, time:%f' % (ymax, tymax)

#(c)求它的射程和飞行时间
#排球的y分量 y = y0 + v0 sin a t - gt²/2
#到达其射程处y = 0, 解方程
#0 = y0 + v0 sin α t - gt²/2
p1 = poly1d([-g/2.0, v0*sin(alpha), y0])
Rt1= roots(p1)[0]
R1= rx(v0, alpha, Rt1)
print 'R :%f, R time:%f' % (R1, Rt1)

#(d)何时排球在地面以上7英尺处? 在这个高度排球离落点(地面距离)多远
#排球的y分量 y = y0 + v0 sin a t - gt²/2
#当y = 7解方程 0 = y0-7 + v0 sin α t - gt²/2
p2 = poly1d([-g/2.0, v0*sin(alpha), y0-7.0])
Rt2 = roots(p2)
R2 = [rx(v0, alpha, Rt2[0]), rx(v0, alpha, Rt2[1])]
print 'When %f sec and %f sec, at %f ft and %f ft, ball height is 7ft' % (Rt2[0], Rt2[1], R1 - R2[0], R1 - R2[1])


#(e)假定网升高到8英尺, 情况是否改变
#会改变, 因为无法过网了
