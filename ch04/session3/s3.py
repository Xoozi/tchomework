#估计半径为4的球体的体积
#半圆y = (16 - x**2)**(1/2), 绕x轴旋转描出一个球面
#实心球用以截面为底的圆柱逼近

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
        sample_radiu = cross_radiu(r, -r + (i+0.5)*step)
        result += vol_cy(sample_radiu, step)
        i += 1
    vv = vol_true(r)
    err = vv - result
    rate = err*100.0/vv
    print "cnt:%d, result:%.1f, err:%.1f rate:%.1f%%" % (sample_cnt, result, err, rate)

index = 4
while(index <= 256):
    vol_sh(4.0, index)
    index *= 2

