from Numeric_Analysis.ODE import ODE

class Euler(ODE):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not super()._check_numPara(1) :
            print("the number of parameter should be one")
            exit(1)
        
    # Euler method
    def _inner_solve(self, target_x, print_on = True) :
        super()._inner_solve(target_x, print_on)

        x = self._x0
        y = self._y0
        
        for _ in range(int(abs(self._x0-self._target_x / self._h))):
            f = self._f(x)
            y += self._h * f
            x += self._h
        self._predicted_y = y

        if print_on :
            print("=== SOLVED ===")
            print("y({}) = {:.{}f}".format(x, self._predicted_y,self._n))
            print()
        return self._predicted_y

    def getAccuracy(self) :
        super().getAccuracy()
