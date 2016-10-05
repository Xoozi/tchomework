#心脏输出
#像例1一样, 附表给出了染料-稀释心脏-输出测定中的染料浓度.
#这次注射的染料总量是5毫克, 使用有限和估计患者的心脏输出
def iv_fun(val_a, step):
    iv_sum = 0
    i = 0
    cnt = size(val_a)
    while(i < cnt):
        iv_sum += (val_a[i] * step)
        i = i + 1
    return iv_sum

val = [0.3, 1.0, 2.05, 3.9, 3.95, 3.35, 2.3, 1.35, 0.75, 0.25]

iv = iv_fun(val, 2.0)

result = 5.0/iv * 60

print "result = %f" % (result)
