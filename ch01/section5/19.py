#变化率
#从塔楼丢下的物体
#一物体从100m高的塔楼丢下, 在t秒时它离地高度100 - 4.9 t**2, 丢下2秒后它速度多快
#位移函数 s(t) = 4.9 * t**2
#求位移变化率 lim(h->0)(s(t + h) - s(t)) / h
#= lim(h->0)(4.9*(t**2 + 2*t*h + h**2) - 4.9*t**2) / h
#= lim(h->0)(4.9*h*(2*t + h))/h
#= lim(h->0)(4.9*(2*t + h))
#= 9.8*t
#v(t) = 9.8*t
#2秒后其速度为19.6mps
