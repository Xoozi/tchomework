#切线
#求曲线 f(x) = 4 + cot(x) - 2*csc(x)
#(a)在P点(pi/2, 2)处的切线方程
#(b)斜率为0处的Q点的切线方程
#f(x) = 4 + cot(x) - 2*csc(x)
#fd(x) = -csc(x)**2 + 2*csc(x)*cot(x)
#fd(x) = 2 => sec(x)=±sqrt(2)
#=>1/cos(x) = ±sqrt(2)
#=>cos(x) = ±1/sqrt(2)
#=>x= ±pi/4
#xoozi 第一次用非解析的方法自己写程序求解, 很好玩呢
def csc(x):
    return 1/sin(x)

def cot(x):
    return cos(x)/sin(x)

def f(x):
    return 4 + cot(x) - 2*csc(x)

def fd(x):
    return -csc(x)**2 + 2*csc(x)*cot(x)

def draw_tangent_line(px, py, slop, sx, ex):
    sy = slop*(sx - px) + py
    ey = slop*(ex - px) + py
    plot([sx, ex], [sy, ey], 'g--')

def draw_work(s, e, a1x, a2x):

    x = linspace(s, e, 100)
    y = f(x)

    a1y = f(a1x)
    a2y = f(a2x)

    xlabel('x')
    ylabel('y')
    plot(x, y, 'r-', [a1x], [a1y], '*r', [a2x], [a2y], '*b')
    text(a1x, a1y, 'a1:%f' % (fd(a1x)))
    text(a2x, a2y, 'a2:%f' % (fd(a2x)))
    draw_tangent_line(a1x, a1y, fd(a1x), s, e)
    draw_tangent_line(a2x, a2y, fd(a2x), s, e)

x = 1.0
while(fd(x) > 0):
    x += 0.000001

print 'x = %f' % (x)

draw_work( 0.1, pi - 0.5, x, pi/2)
