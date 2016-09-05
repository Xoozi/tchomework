#求角度
#三角形的两边边长为a和b, 其夹角为θ. 什么样的θ值能使得三角形的面积最大
#a(x) = sin(x) * (a*b)/2
#在定义域(0, pi)上, a(x)在x=pi/2处取得极大值, 也是全局最大值

def a(x):
    return sin(x)

def ad(x):
    return cos(x)

def add(x):
    return -sin(x)


x = linspace(pi/6, 5*pi/6, 1000)
y = a(x)
yd= ad(x)
ydd= add(x)

plot([0, pi], [0, 0], '-k')
plot(x, y, '-r', x, yd, '-g', x, ydd, '-b')


