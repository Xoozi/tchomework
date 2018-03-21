'''Least Squares and Regression Lines

When we try to fit a line y = mx + b, to a set of numerical data points
(x1, y1), (x2, y2),...,(xn, yn), we usually choose the line that
minimizes the sum of the squares of the vertical distances from the points
to the line. In theory, this mean finding the values of m and b
that minimizes the value of function

    w = (mx1 + b - y1)² + ... +(mxn + b - yn)²

    ######
        (mx1 + b - y1) * (mx1 + b - y1)
        = m²x1² + mbx1 - mx1y1 + mbx1 + b² - by1 - mx1y1 - by1 + y1²
        = m²x1² + 2mbx1 - 2mx1y1 - 2by1 + b² + y1²

    w = m²(∑xk²) + 2mb(∑xk) - 2m(∑xkyk) - 2b(∑yk) + ∑yk² + b²

    wm = 2m(∑xk²) + 2b(∑xk) - 2(∑xkyk)
    wb = 2m(∑xk) - 2(∑yk) + 2b

    0 = wm, 0 = wb
    => 
    
    
    ######

The values of m and b do this are found with the First and Second Derivative Test to be

    m = ((∑xk)(∑yk) - n∑xkyk) / ((∑xk)² - n∑xk²)
    
    b = (∑yk - m∑xk)/n'''


def leastSq(xlist, ylist):
    xxlist = xlist*xlist
    xylist = xlist*ylist
    xsum = xlist.sum()
    ysum = ylist.sum()
    xxsum = xxlist.sum()
    xysum = xylist.sum()
    n = xlist.size

    m = (xsum*ysum - n*xysum) / (xsum*xsum - n*xxsum)

    b = (ysum - m*xsum) / n

    return (m, b)

##57 (-1, 2), (0, 1), (3, -4)
xlist = array([-1.0, 0.0, 3.0])
ylist = array([2.0, 1.0, -4.0])
ret = leastSq(xlist, ylist)
print "57: m=%f, b=%f" % ret

##58 (-2, 0), (0, 2), (2, 3)
xlist = array([-2.0, 0.0, 2.0])
ylist = array([0.0, 2.0, 3.0])
ret = leastSq(xlist, ylist)
print "58: m=%f, b=%f" % ret

##59 (0, 0), (1, 2), (2, 3)
xlist = array([0.0, 1.0, 2.0])
ylist = array([0.0, 2.0, 3.0])
ret = leastSq(xlist, ylist)
print "59: m=%f, b=%f" % ret

##60 (0, 1), (2, 2), (3, 2)
xlist = array([0.0, 2.0, 3.0])
ylist = array([1.0, 2.0, 2.0])
ret = leastSq(xlist, ylist)
print "60: m=%f, b=%f" % ret
