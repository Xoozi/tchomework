
#探究sin(kx)/x
#把y = sin(x)/x, y = sin(2x)/x, y= sin(4x)/x, 在-2<= x <=2上的图形画在一起.
#每个图形在何处看似要穿过y轴------x=0 y=k处
#该图形真的穿过y轴吗--------------并不, 因为x=0处函数无定义
#你认为在x->0时, y = sin(5x)/x和y = sin(-3x)/x的图形会怎样
#y = sin(5x)/x无限接近(0, 5)
#y = sin(-3x)/x无限接近(0, -3)
#对其他k值, y = sin(kx)/x的图形会怎样,(0, k)

def f(x, k):
    return sin(k*x)/x

def draw_f(s, e, k, style):

    x = linspace(s, e, 100)
    y = f(x, k)

    xlabel('x')
    ylabel('y')
    plot(x, y, style)


s = -2
e = -0.01
draw_f(s, e, 1, 'r-')
draw_f(s, e, 2, 'g-')
draw_f(s, e, 4, 'b-')

s = 0.01
e = 2
draw_f(s, e, 1, 'r--')
draw_f(s, e, 2, 'g--')
draw_f(s, e, 4, 'b--')


