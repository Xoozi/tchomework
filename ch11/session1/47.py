'''
Concorde的声震
地面上的人直接听到Concorde的而非空气中的层反射的声震的区域的宽度w是:
    T = 地面空气温度(Kelvin)
    h = Concorde的高度(km)
    d = 垂直温度梯度(Kelvin/km)

    的函数, w = 4(Th/d)**(1/2)

    从欧洲飞往Washington的Concorde在一个航线上飞临美国, 此航线在Nantucket岛以南, 飞机高度16.8km, 若地面温度为290K, 垂直温度梯度为5K/km
    飞机在Nantucket岛以南多少公里飞行才能保证它的声震层离开改岛

    相当于求w/2'''

d = 2*(290*16.8/5)**(0.5)

print 'distance:%f' % (d)
