#Picard方法
#用Picard方法解sqrt(x) = x可以求得解x = 1, 却求不出x = 0, 为什么?
#画出图就知道, sqrt(x) 在x = 0处斜率无穷大, 1处斜率小于1,
#Picard方法在斜率绝对值小于1时才会收敛

def f(x):
    return x

def g(x):
    return sqrt(x)

x = linspace(-2.0, 2.0, 10000)

fx = f(x)
gx = g(x)

plot(x, fx, 'r-', x, gx, 'g-')
