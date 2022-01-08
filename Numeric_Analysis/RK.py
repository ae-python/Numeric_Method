from Numeric_Analysis.ODE import ODE

class RK(ODE):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not super()._check_numPara(1) :
            print("the number of parameter should be one")
            exit(1)
        
    # RK method
    def _inner_solve(self, target_x, print_on = True) :
        super()._inner_solve(target_x, print_on)

        x = self._x0
        y = self._y0
        h = self._h
        f = self._f
        
        for _ in range(int(abs(x-self._target_x / h))):
            k1 = h * f(x)
            k2 = h * f(x + 0.5 * h)
            k3 = h * f(x + 0.5 * h)
            k4 = h * f(x + h)
            y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
            x += self._h
        self._predicted_y = y

        if print_on :
            print("=== SOLVED ===")
            print("y({}) = {:.{}f}".format(x, self._predicted_y, self._n))
            print()
        return self._predicted_y

    def getAccuracy(self) :
        super().getAccuracy()
