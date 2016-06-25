'''工资谈判, 一位焊工的合同, 承诺4年里每年涨工资3.5%, 而Luisa的起始工资是36500美元
(a)说明Luisa的工资由y = 36500*(1.035)**y给出
(b)图示, 并说明哪些时候y是连续的
    每年中是连续的'''

def f(x):
    y = floor(x)
    return 36500*((1.035)**y)

x = linspace(0, 10, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
