#垂直运动
#垂直运动的物体, 高度由s = -16*t**2 + 96*t + 112给出,
#(a)当t = 0时物体的速度
#(b)物体的最大高度以及何时达到
#(c)当s=0时物体的速度

def s(t):
    return -16*t**2 + 96*t + 112

def v(t):
    return -32*t + 96

def a(t):
    return -32 + 0*t

x = linspace(0,7, 1000)
y = s(x)
yd= v(x)
ydd= a(x)

plot([0, 7], [0, 0], '-k')
plot(x, y, '-r', x, yd, '-g', x, ydd, '-b')

a = v(0)
zero_v_t = 3
b = s(zero_v_t)
zero_s_t = 7
c = v(zero_s_t)

print 'a:%f, b:%f(t=%f), c:%f' % (a, b, zero_v_t, c)

