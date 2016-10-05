#心脏输出
#像例1一样, 附表给出了染料-稀释心脏-输出测定中的染料浓度.
#这次注射的染料总量是10毫克, 使用有限和估计患者的心脏输出
def iv_fun(val_a, step):
    iv_sum = 0
    i = 0
    cnt = size(val_a)
    while(i < cnt):
        iv_sum += (val_a[i] * step)
        i = i + 1
    return iv_sum

val = [0.0, 0.05, 0.35, 1.3, 3.1, 5.25, 6.9, 7.7, 7.85, 6.95, 5.4, 4.1, 2.8, 1.4, 0.35]

iv = iv_fun(val, 2.0)

result = 10.0/iv * 60

print "result = %f" % (result)
