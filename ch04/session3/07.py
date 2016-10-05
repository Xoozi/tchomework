#球体的体积
#假定我们这样逼近例3中球的体积V, 把区间[-4, 4]分成长度为2的4个子区间
#并且用底为在子区间左端点处的横截面圆柱体
#(a)求各圆柱体积之和S4
#(b)求百分比误差

def cross_radiu(r, x):
    return sqrt(r**2 - x**2)

def vol_cy(r, h):
    return pi*h*r**2

def vol_true(r):
    return pi*r**3*4.0/3.0

def vol_sh(r, sample_cnt):
    result = 0.0
    err = 0.0
    rate = 0.0
    step = 2.0*r/sample_cnt
    sample_radiu = 0.0
    i = 0
    vv = 0.0
    while(i < sample_cnt):
        sample_radiu = cross_radiu(r, -r + i*step)
        result += vol_cy(sample_radiu, step)
        i += 1
    vv = vol_true(r)
    err = vv - result
    rate = err*100.0/vv
    print "cnt:%d, result:%.1f, err:%.1f rate:%.1f%%" % (sample_cnt, result, err, rate)

vol_sh(4.0, 4)

