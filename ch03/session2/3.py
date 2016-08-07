#检验函数s(t) = sqrt(t*(1-t), [0, 1] 是否满足中值定理的假设
#连续且可微, 自然满足
def s(t):
    return sqrt(t * (1-t))

x = linspace(0, 1, 100)
y = s(x)

plot(x, y, '-r')

