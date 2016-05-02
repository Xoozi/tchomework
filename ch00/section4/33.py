
#求解方程， 做图
#1.045**t = 2
#ln(1.045**t) = ln(2)
#t*ln(1.045) = ln(2)
#t = ln(2)/ln(1.045)

def f(x):
    return 1.045**x



x = linspace(0, 20, 100)
y = f(x)
t = log(2)/log(1.045)
yt = f(t)

print 't:%f, yt:%f' % (t, yt)

xlabel('x')
ylabel('y')
plot(x, y, 'r-')
