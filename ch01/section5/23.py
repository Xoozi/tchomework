#变化率
#火星上的自由落体
#火星表面自由落体方程: s(t) = 1.86 * t**2
#求落下1秒后的速度
# 不用求极限了 从19题类推, 变化率的函数v(t) = 2 * 1.86 * t
# 所以1秒后速度为3.72mps
#= lim(h->0)(4.9*(t**2 + 2*t*h + h**2) - 4.9*t**2) / h
#= lim(h->0)(4.9*h*(2*t + h))/h
#= lim(h->0)(4.9*(2*t + h))
#= 9.8*t
#v(t) = 9.8*t
#2秒后其速度为19.6mps