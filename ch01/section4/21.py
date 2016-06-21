
#lim(x->pi)sin(x - sin(x))
#sin(x)在实数域连续
#x-t在实数域连续
#故复合函数连续

def f(x):
    return sin(x - sin(x))

x = linspace(-2*pi, 2*pi, 1000)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
