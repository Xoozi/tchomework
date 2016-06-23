#可去间断
#试给出一个除x=2外在一切x值连续的函数f(x)的例子, 该函数在x = 2处有一个可去的间断, 试解释你怎么知道f在2有间断以及怎么知道这个间断是可去的
#在x=2时, 有f(x) != lim(x->2)f(x), 所以该点有间断
#而因为lim(x->2)f(x)是存在的, 所以该间断可去

#xoozi 可去间断和不可去间断, 还好做了此题, 否则这个概念就漏掉了

def f(x):
    if 2 == x:
        return 0
    else:
        return 2*x + 1

ff = frompyfunc(f, 1, 1)
x = linspace(-10, 10, 100)
y = ff(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
