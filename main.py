from Numeric_Analysis.RK import RK

rk = RK(0,1,lambda x : -2*x**3+12*x**2-20*x+8.5,0.5,n=5)
rk.solve(0.5)
rk.set_exact_expression(lambda x : -0.5*x**4+4*x**3-10*x**2+8.5*x+1)
rk.getAccuracy()
rk.plot(0,4,[0.1, .3, 0.5])
rk.plot(0,4)

