#圆的面积
#在半径为1的圆内内接一狗正n边形, 对下列n计算正多边形的面积
#(a)4
#(b)8
#(c)16
#(d)比较a,b,c的面积和圆面积
def area_n(n):
    angle = (2*pi)/(2*n)
    area_trangle = sin(angle)*cos(angle)/2.0
    return n*2.0*area_trangle

n= 2
while(n<= 65536*65536):
    print 'n[%d], area:%.20f/circle:%.20f' % (n, area_n(n), pi)
    n *= 2


