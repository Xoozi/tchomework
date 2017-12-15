'''
平面曲线的法线

(a)证明n(t) = -g'(t)i + f'(t)j 和 -n(t) = g'(t)i - f'(t)j, 在点(f(t), g(t))正交于曲线r(t) = f(t)i + g(t)j

v(t) = f'(t)i + g'(t)j

dot(v(t), n(t)) = -f'(t) g'(t) + f'(t) g'(t) = 0
dot(v(t), -n(t)) = 0

而切单位向量T(t) = v(t) / |v(t)|
故T(t)和v(t)是同一方向的
股n(t)和-n(t)都与T(t)正交,

为对特殊的平面直线得到N, 我们可以选择n或-n中指向曲线的凹的一侧的一个, 并把它们归一化, 用这个方法求下列的N
'''

'''
(b) r(t) = ti + e**(2t)j

    f(t) = t,       f'(t) = 1
    g(t) = e**(2t), g'(t) = 2e**(2t)


    n(t) = -g'(t)i + f'(t)j = -2e**(2t)i + j
    -n(t) = g'(t)i - f'(t)j = 2e**(2t)i - j'''

'''
def bRX(t):
    return t

def bRY(t):
    return e**(2*t)

t = linspace(-10, 10, 10000)

x = bRX(t)
y = bRY(t)

plot(x, y, '-r')'''

'''观察了一下n(t)是指向凹测的
    于是
    N(t) = n(t) / |n(t)| 
    = (-2e**(2t)/sqrt(1 + 4e**(4t)))i + (1/sqrt(1 + 4e**(4t)))j'''

'''
(c) r(t) = sqrt(4 - t²)i + tj,  -2 <= t <= 2

    f(t) = sqrt(4 - t²),    f'(t) = t/sqrt(4 - t²)
    g(t) = t,               g'(t) = 1

    n(t) = -g'(t)i + f'(t)j = -i + t/sqrt(4 - t²) j
    -n(t)= g'(t)i - f'(t)j = i - t/sqrt(4 - t²) j
'''

def cRX(t):
    return sqrt(4 - t**2)

def cRY(t):
    return t

t = linspace(-2, 2, 10000)
x = cRX(t)
y = cRY(t)

plot(x, y, '-g')

'''观察了一下n(t)是指向凹侧的
    于是N(t) = n(t) / |n(t)|
'''
