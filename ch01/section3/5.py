
#求函数x->∞时的极限
#lim(x->∞)(sin(2*x)/x) = lim(x->∞)2*(sin(2*x)/(2*x)) = lim(t->∞)2*(sin(t)/t)
# = lim(t->∞)2*(sin(t)/t) = 2 * lim(t->∞)sin(t)*lim(t->∞)1/t = 0

def f(x):
    return sin(2*x)/x

x = linspace(0, 1000, 1000)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
