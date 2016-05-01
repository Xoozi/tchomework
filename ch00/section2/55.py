
wavelength  = array([0.20, 0.65, 1.13, 2.55, 4.00, 5.75, 7.80, 10.20, 12.90, 16.00, 18.40])
speed       = array([1.8, 3.6, 5.4, 7.2, 9.0, 10.8, 12.6, 14.4, 16.2, 18.0, 19.8])

coefficient = polyfit(wavelength, speed, 6)

func = poly1d(coefficient.astype(float))
fspeed = func(wavelength)
x = linspace(0, 20, 100)
y = func(x)

xlabel('wavelength')
ylabel('speed')

plot(wavelength, speed, 'go', wavelength, fspeed, 'r-', x, y, 'b-')
