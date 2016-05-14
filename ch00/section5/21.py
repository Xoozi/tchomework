


#方程(2)
#s(x) = A*sin(2*PI/B(x-C)) + D
#	|A| 为振幅
#	|B| 为周期
#    C  为水平位移
#	 D  为垂直位移
#
#阿拉斯加的温度: 求一般正弦函数 f(x) = 37*sin((2*pi/365)*(x-101)) + 25 的ABCD
#A = 37
#B = 365
#C = 101
#D = 25
def f(x):
    return 37*sin((2*pi/365)*(x-101)) + 25



x = linspace(0, 365, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-');
