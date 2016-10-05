#一条路的长度
#你和同伴驾驶一辆车行进在一段蜿蜒的土路上, 车的速度计工作正常
#而里程计坏了, 为求这段路有多长, 记录了汽车10秒内的速度
#使用
#(a)左端点值
#(b)右端点值
#的有限和估计汽车的行进距离
def iv_fun(val_a, step):
    iv_sum = 0
    i = 0
    cnt = size(val_a)
    while(i < cnt):
        iv_sum += (val_a[i] * step)
        i = i + 1
    return iv_sum

val_left = [0.0, 44.0, 15.0, 35.0, 30.0, 44.0, 35.0, 15.0, 22.0, 35.0, 44.0, 30.0]
val_right = [44.0, 15.0, 35.0, 30.0, 44.0, 35.0, 15.0, 22.0, 35.0, 44.0, 30.0, 35.0]

iv_left = iv_fun(val_left, 10.0)
iv_right = iv_fun(val_right, 10.0)

print "result = (%f, %f)" % (iv_left, iv_right)
