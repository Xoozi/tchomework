#容器中水的体积
#一个形状为半径8米的半球形容器盛了深度4米的水
#(a)通过8个内接圆柱逼近求水体积的一个估计
#(b)你将在4.5练习43中看到水的体积是320*pi/3, 求百分比误差

def cross_radiu(r, x):
    return sqrt(r**2 - x**2)

def vol_cy(r, h):
    return pi*h*r**2

def vol_true(r):
    return 320*pi/3.0

def vol_hemishere(r, sample_cnt):
    result = 0.0
    err = 0.0
    rate = 0.0
    step = (r-4.0)/sample_cnt
    sample_radiu = 0.0
    i = 0
    vv = 0.0
    while(i < sample_cnt):
        sample_radiu = cross_radiu(r, 4.0+i*step)
        result += vol_cy(sample_radiu, step)
        i += 1
    vv = vol_true(r)
    err = vv - result
    rate = err*100.0/vv
    print "cnt:%d, result:%.1f, err:%.1f rate:%.1f%%" % (sample_cnt, result, err, rate)

vol_hemishere(8.0, 8)

