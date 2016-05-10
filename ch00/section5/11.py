

#画f(x) = cot(2*x)的图像， 周期是多少， 有什么样的对称性
#cot(2*pi/pi*x), 我推测周期为pi/2

#xoozi 不能用tan的倒数来构造cot的函数， 这样会出现奇点

##def f(x):
##    return 1.0/tan(2*x)
def f(x):
    return cos(2*x)/sin(2*x)


#xoozi很有意思， 如果像下面这样取输入区间， 由于太靠近奇点， y轴拉伸的厉害， 仿佛一个方波
#x = linspace(-pi/2+0.000001, pi/2-0.000001, 100)
#xoozi 这样也不行， cot的范围应该是（0,pi）
#x = linspace(-pi/2+0.3, pi/2-0.3, 100)
#xoozi 总的来说我把输入区间又考虑错了， cot(2*x)的周期不是pi， 猜测为pi/2
#x = linspace(0.3, pi-0.3, 100)
x = linspace(0.1, pi/2.0-0.1, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
