
#求函数x->∞, x->-∞时的极限
#lim(x->∞)(2*x+3)/(5*x+7) = 
#lim(x->∞)(2+3/x)/(5+7/x) =
#(2+lim(x->∞)(3/x))/(5+lim(x->∞)(7/x)) =2/5

def f(x):
    return (2*x+3)/(5*x+7)

x = linspace(-1000, 1000, 1000)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
