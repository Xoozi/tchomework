#一个直射入空气中的射弹速度是v(t) = 160 - 9.8*t
#用有限和技术来估计头三秒内射弹升高多少,
#和精确值435.9米比较的误差是多少
def v_fun(t):
    return 160 - 9.8*t
def v_height(sample_cnt):
    result_left = 0.0
    result_mid = 0.0
    result_right = 0.0
    err_left = 0.0
    err_mid = 0.0
    err_right = 0.0
    rate_left = 0.0
    rate_mid = 0.0
    rate_right = 0.0
    i = 0
    step = 3.0/sample_cnt
    sample = 0.0
    v = 0.0
    while(i < sample_cnt):
        sample = i*step
        v = v_fun(sample)
        result_left += (v*step)

        sample = (i+0.5)*step
        v = v_fun(sample)
        result_mid += (v*step)

        sample = (i+1.0)*step
        v = v_fun(sample)
        result_right += (v*step)
        i = i + 1

    err_left = 435.9 - result_left
    err_mid = 435.9 - result_mid
    err_right = 435.9 - result_right
    rate_left = abs(err_left)*100.0/435.9
    rate_mid = abs(err_mid)*100.0/435.9
    rate_right = abs(err_right)*100.0/435.9
    print "cnt:%d l:(%.1f, %.1f, %.1f%%) m:(%.1f, %.1f, %.1f%%) r:(%.1f, %.1f, %.1f%%)" % (sample_cnt, result_left, err_left, rate_left, result_mid, err_mid, rate_mid, result_right, err_right, rate_right)

index = 3
while(index <= 192):
    v_height(index)
    index *= 2
