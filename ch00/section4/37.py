
#求解方程， 做图
#ln(x) = 2*t + 4
#exp(ln(x)) = exp(2*t+4)
#x = exp(2*t+4)

def f(t):
    return exp(2*t+4)



x = linspace(0, 5, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
