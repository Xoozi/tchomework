#行进距离
#附表列出了模型机车沿轨道行进10秒的速度, 用长度为1的10个子区间
#(a)左端点值
#(b)中点值
#(c)右端点值
#的有限和估计机车的行进距离
def iv_fun(val_a, step):
    iv_sum = 0
    i = 0
    cnt = size(val_a)
    while(i < cnt):
        iv_sum += (val_a[i] * step)
        i = i + 1
    return iv_sum

val_left = [0.0, 12.0, 22.0, 10.0, 5.0, 13.0, 11.0, 6.0, 2.0, 6.0]
val_mid  = [6.0, 17.0, 16.0, 7.5, 9.0, 12.0, 8.5, 4.0, 4.0, 3.0]
val_right= [12.0, 22.0, 10.0, 5.0, 13.0, 11.0, 6.0, 2.0, 6.0, 0.0]

iv_left = iv_fun(val_left, 1.0)
iv_mid = iv_fun(val_mid, 1.0)
iv_right = iv_fun(val_right, 1.0)

print "result = (%f, %f, %f)" % (iv_left, iv_mid, iv_right)
