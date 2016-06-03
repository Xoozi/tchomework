#自由落体 一个水气球从高出地面很多的窗口掉下, t秒后的下落距离为y=4.9t**2, 求气球的

def dis(t):
    return 4.9*t**2
def va(t):
    return dis(t)/t

#(a)下落头3秒的平均速度
va3 = va(3)
print "average v of 3 sec:%f" % va3
#(b)瞬间t=3的速度
pv3 = (dis(3.000001) - dis(2.999999))/0.000002
print "p v of 3 sec:%f" % pv3
