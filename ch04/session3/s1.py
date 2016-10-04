#面积和心脏输出
def iv_fun(val_a, step):
    iv_sum = 0
    i = 0
    cnt = size(val_a)
    while(i < cnt):
        iv_sum += (val_a[i] * step)
        i = i + 1
    return iv_sum

val = [1.4, 6.3, 7.5, 4.8, 2.8, 1.9, 1.1, 0.7, 0.5, 0.3, 0.2, 0.1]

iv = iv_fun(val, 2.0)

result = 5.6/iv * 60

print "result = %f" % (result)
