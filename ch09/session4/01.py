#一个抛射体以速率840米/秒和60度角发射. 它经过多长时间沿水平方向前进21千米.

g = 9.8

def rMax(v):
    return v*v/g

R = rMax(840.0)

print 'Range max:%f km' % (R/1000.0)

#检查了一下21千米没有超出最大射程
vh = 840.0*cos(pi/3.0)
t = 21000.0/vh

print 'Use %f sec, fly over 21km' % (t)

