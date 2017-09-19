#求行进路径, 一个质点于时刻t在平面上的位置
#r(t) = (1 - cos t) i + (t - sin t)j
#求质点沿路径从t = 0 到t = 2pi/3行进的路径长度

def rx(t):
    return 1.0 - cos(t)

def ry(t):
    return t - sin(t)


t = linspace(0, 2.0*pi/3.0, 1000)

x = rx(t)
y = ry(t)

plot(x, y, 'r-')

#s  = ∫(0, 2pi/3) sqrt((dx/dt)² + (dy/dt)²) dt
#   dx/dt = sin t
#   dy/dt = 1 - cos t
#s  = ∫(0, 2pi/3) sqrt(sin² t + 1 - 2cos t + cos² t) dt
#   = ∫(0, 2pi/3) sqrt(2 - 2cos t) dt 
#   = sqrt(2) ∫(0, 2pi/3) sqrt(1 - cos t) dt
#   = sqrt(2) ∫(0, 2pi/3) sqrt(2 sin² (t/2)) dt
#   = 2 ∫(0, 2pi/3) |sin (t/2)| dt
#       在该区间可以去掉绝对值符号
#   =  -4(cos(t/2))|(0, 2pi/3)
#   =  -4*(1/2 - 1)
#   = 2
