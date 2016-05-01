# IPython log file
# 如果利息按年复利率6.25%计算， 问需要多少时间使投资倍增

def f(p, y):
    return p * (1.0625**y)

x = linspace(1, 20, 100)
y = f(100, x)

k = -1
for i, e in enumerate(y):
    if e >= 200:
        k = i
        break

if k > 0:
    print 'double the input need %f years' % x[k]
else:
    print 'on right anwser'


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
