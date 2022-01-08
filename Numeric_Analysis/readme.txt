@@@@@ HOW TO USE Numeric_Analysis @@@@@

This project implements numerical methods in <<Advanced Engineering Mathmatics>>, 10th, Erwin Kreyszig.

[Implemented methods and examples]

<ODE - Euler method (1st order method)>
"""
    from Numeric_Analysis.Euler import Euler

    euler = Euler(0,1,lambda x : -2*x**3+12*x**2-20*x+8.5,h=0.3,n=5)
        -> parameters are; (x0, y0, explicit y' with lambda, h(0.1 is default), plot_precision(x interval when plot exact solution), n(floating point, 8 is default))
    euler.solve(4)
        -> parameter is; (target x, False if you don't want to see result)
    euler.set_exact_expression(lambda x : -0.5*x**4+4*x**3-10*x**2+8.5*x+1)
        -> If you know exact solution, you can get accuracy and graph. parameter is; (explicit y which is the primitive function of y')
    euler.getAccuracy()
        -> Accuracy calculated with exact & numerical solution
    euler.plot(0,4,[0.3])
        -> You can plot vary cases with h's. parameters are; (x_start, x_end, h_list)
    euler.plot(0,4)
        -> You can also plot one case of h. If you used set_exact_expression(), exact graph would be get too.
"""

<ODE - RK method (4th order Runge-Kutta method)>
"""
    from Numeric_Analysis.RK import RK

    simmilar as Euler.
    rk = RK(...) 
    ...
"""