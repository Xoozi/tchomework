#有空气阻力的自由落体
#一个物体从直升机上自由落下, 物体下落越来越快, 但其加速度
#由于空气阻力逐渐减小, 加速度在下落5秒内每秒记录一次
#  t  │ 0       1       2       3       4       5
#─────┼─────────────────────────────────────────────
#  a  │32.00    19.41   11.77   7.14    4.33    2.63
#
#(a)求t=5时速率的过剩估计
#(b)求t=5时速率的不足估计
#(c)求t=3时下落距离的过剩估计
def iv_fun_cnt(val_a, step, cnt):
    iv_sum = 0
    i = 0
    while(i < cnt):
        iv_sum += (val_a[i] * step)
        i = i + 1
    return iv_sum

def iv_fun(val_a, step):
    iv_sum = 0
    i = 0
    cnt = size(val_a)
    iv_array = []
    while(i < cnt):
        iv_sum += (val_a[i] * step)
        i = i + 1
        iv_array.append(iv_sum)
    return (iv_sum, iv_array)

a_left = [32.0, 19.41, 11.77, 7.14, 4.33]
a_right = [19.41, 11.77, 7.14, 4.33, 2.63]

(ia_left, iv_left)= iv_fun(a_left, 1.0)
(ia_right, iv_right)= iv_fun(a_right, 1.0)
v_left = iv_fun_cnt(iv_left, 1.0, 3)

print "result = (%f, %f, %f)" % (ia_left, ia_right, v_left)
