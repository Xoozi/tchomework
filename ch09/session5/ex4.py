#r² = 4 cos α
#α 的范围为[-pi/2, pi/2]
#r = 2sqrt(cos α)或r = - 2sqrt(cos α)
def xPostive(theta, power):
    return (4*cos(theta))**(1.0/power) * cos(theta)

def xNegative(theta, power):
    return -(4*cos(theta))**(1.0/power) * cos(theta)

def yPostive(theta, power):
    return (4*cos(theta))**(1.0/power) * sin(theta)

def yNegative(theta, power):
    return -(4*cos(theta))**(1.0/power) * sin(theta)

def work(power, pattern):
    theta = linspace(-pi/2, pi/2, 1000)
    xP = xPostive(theta, power)
    xN = xNegative(theta, power)
    yP = yPostive(theta, power)
    yN = yNegative(theta, power)
    plot(xP, yP, pattern, xN, yN, pattern)

work(2.0, '-r')
work(4.0, '-g')
work(8.0, '-b')
