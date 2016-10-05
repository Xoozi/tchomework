#估计函数f(x) = x**3在区间[0, 2]上的平均值
def f(x):
    return x**3

def avg_f(start, end, cnt):
    x = linspace(start, end, cnt)
    y = f(x)
    return sum(y)/(cnt*1.0)

cnt = 2
while(cnt <= 65536):
    print 'cnt[%d], avg of f:%f' % (cnt, avg_f(0, 2, cnt))
    cnt *= 2
