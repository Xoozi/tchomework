#令人惊讶的图形
#画函数f(x) = sin(x) * sin(x+2) - sin(x+1)**2
#为什么这个函数的性态会是这样?
#f'(x) = cos(x) * sin(x+2) + sin(x)*cos(x+2) - 2*sin(x+1)*cos(x+1)
#      = sin(2*x+2) - sin(2*x+2)
#      = 0
#根据中值定理的推论1, 如果一个函数的导函数是0, 则该函数是常值函数
def f(x):
    return sin(x) * sin(x+2) - sin(x+1)**2

x = linspace(-2*pi, 2*pi, 100)
y = f(x)

plot(x, y, '-r')

#xoozi 因崔斯廷
