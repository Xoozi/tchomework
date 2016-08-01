#区间上的绝对极值
#f(x)   = sin(x + pi/4),    0 <= x <= 7*pi/4
#f'(x)  = cos(x + pi/4),    在x=pi/4, 5/4 * pi时导数为0
#在区间端点处:
#sin(pi/4) = 1/sqrt(2), sin(2pi) = 0
#在临界点:
#sin(pi/2) = 1, sin(3/2*pi) = -1
#所以M = 1, m = -1
#xoozi 
def f(x):
    return sin(x + pi/4.0)

x = linspace(0, pi*7.0/4.0, 100)
y = f(x)

xlabel('x')
ylabel('y')
plot(x, y, 'r-')

