#鼻锥的体积
#火箭的鼻锥是绕x轴旋转曲线y = sqrt(x), x ∈ [0, 5]
#生成的曲面, 为估计鼻锥的体积, 我们分割[0, 5]
#成5个等长子空间, 用在子区间左端点垂直于x轴
#的平面切割锥体, 构造高为1底为横截面的圆柱

#(a)求圆柱体积之和S5, S5是V的不足估计还是过剩估计
#(b)你将在4.5练习44中看到鼻锥的体积是25*pi/2, 求百分比误差

def cross_radiu(x):
    return sqrt(x)

def vol_cy(r, h):
    return pi*h*r**2

def vol_true():
    return 25*pi/2.0

def vol_paracone(sample_cnt):
    result = 0.0
    err = 0.0
    rate = 0.0
    step = 5.0/sample_cnt
    sample_radiu = 0.0
    i = 0
    vv = 0.0
    while(i < sample_cnt):
        sample_radiu = cross_radiu(i*step)
        result += vol_cy(sample_radiu, step)
        i += 1
    vv = vol_true()
    err = vv - result
    rate = err*100.0/vv
    print "cnt:%d, result:%.1f, err:%.1f rate:%.1f%%" % (sample_cnt, result, err, rate)

vol_paracone(5)
#从输出可见是不足估计
