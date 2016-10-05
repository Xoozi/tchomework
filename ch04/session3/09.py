#半球的体积
#估计半径4的半球的体积V, 把区间[0, 4]分成长度为8个子区间
#并且用底为在子区间左端点处的横截面圆柱体
#(a)求各圆柱体积之和S8, 这是过剩估计还是不足估计
#(b)求百分比误差

def cross_radiu(r, x):
    return sqrt(r**2 - x**2)

def vol_cy(r, h):
    return pi*h*r**2

def vol_true(r):
    return pi*r**3*2.0/3.0

def vol_hemishere(r, sample_cnt):
    result = 0.0
    err = 0.0
    rate = 0.0
    step = r/sample_cnt
    sample_radiu = 0.0
    i = 0
    vv = 0.0
    while(i < sample_cnt):
        sample_radiu = cross_radiu(r, i*step)
        result += vol_cy(sample_radiu, step)
        i += 1
    vv = vol_true(r)
    err = vv - result
    rate = err*100.0/vv
    print "cnt:%d, result:%.1f, err:%.1f rate:%.1f%%" % (sample_cnt, result, err, rate)

vol_hemishere(4.0, 8)
#从输出看, 也很明显是过剩估计

