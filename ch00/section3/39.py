
# IPython log file
# 假定一个菌株开始时有一个细菌， 每隔半小时倍增其细菌数目， 24小时后该菌株共有多少细菌


def f(t):
    return 2**(t*2)

x = linspace(1, 24, 100)
y = f(x)

print 'after 24 hours there is %d ' % f(24)

xlabel('x')
ylabel('y')
plot(x, y, 'r-')
