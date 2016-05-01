# IPython log file
# 放射性衰减 磷-32的半衰期为14天， 一开始有6.6克
# (a)表示磷-32残余量的时间t的函数 xoozi 这个还真没想到是这样直白的写法
# (b)什么时候只剩下1克磷-32了

def f(t):
    return 6.6 * (0.5 ** (t/14))

ff = frompyfunc(f, 1, 1)
x = linspace(1, 100, 100)
y = ff(x)
xlabel('x')
ylabel('y')
plot(x, y, 'r-')
