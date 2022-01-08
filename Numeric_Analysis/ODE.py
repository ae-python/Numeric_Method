"""
추가할 것
1. lambda y & lambda x, y
"""



import inspect
from types import LambdaType
from abc import *
import matplotlib.pyplot as plt

"""
Numerical Analysis for Ordinary Differential Equation
"""

class ODE(metaclass=ABCMeta):
    '''
    @param
    x0, y0 : initial value
    f : differential equation(explicit funtion) / Lambda type
    h : equidistant intervals (integer)
    '''
    def __init__(self,x0,y0,f,h=0.1, plot_precision=0.0001, n = 8):
        if not isinstance(x0 and y0 and h and plot_precision, (int, float)) :
            print("Put appropriate type")
            exit(1)
        if not isinstance(f,LambdaType) :
            print("Put appropriate type such as; lambda x:2*x**2+1")
            exit(1)
        self._x0 = x0
        self._y0 = y0
        self._h = abs(h)
        self._f = f
        self._numPara = len(inspect.getargspec(self._f).args)
        self._predicted_y = None
        self._target_x = None
        self._exact_expression = None
        self.plot_precision = plot_precision
        self._n = n

    # Initialize x0, y0 as user inputs
    def set_initial(func) :
        def wrapper(*args, **keyws) :
            init_x = args[0]._x0
            init_y = args[0]._y0
            result = func(*args, **keyws)
            args[0]._x0 = init_x
            args[0]._y0 = init_y
            return result
        return wrapper

    # Get numerical solution via _inner_solve()
    @set_initial
    def solve(self, target_x, print_on = True) :
        a = self._inner_solve(target_x, print_on)
        return a

    # _inner_solve() will differ by methods. Users only need to use solve().
    @abstractmethod
    def _inner_solve(self, target_x, print_on = True) :
        self._target_x = target_x

        if not isinstance(self._target_x,(int,float)) :
            print("'target_x' must be integer of float")
            exit(1)

        if abs(self._x0 - self._target_x) < abs(self._h) :
            print("h should be smaller than difference between x0 and target_x")
            print("Adjust target_x to x0")
            self._target_x = self._x0

        if self._target_x < self._x0 :
            self._h = - abs(self._h)
        else :
            self._h = abs(self._h)


    def _check_numPara(self, target_num) :
        if self._numPara == target_num :
            return True
        else :
            return False

    def _get_numPara(self, expression) :
        return len(inspect.getargspec(expression).args)

    def set_exact_expression(self, f) :
        if not isinstance(f, LambdaType) :
            print("Put appropriate type such as; lambda x:2*x**2+1")
            exit(1)
        if self._get_numPara(f) != self._numPara:
            print("Different number of variables.")
            exit(1)            
        self._exact_expression = f            

    @abstractmethod
    def getAccuracy(self) :
        if self._exact_expression is None:
            print("Use 'set_exact_expression()' method first.")
            exit(1)

        if not self._check_numPara(self._get_numPara(self._exact_expression)) :
            print("Different number of variables.")
            exit(1)

        if self._predicted_y is None :
            print("Please 'solve(target_x)' first.")
            exit(1)
        
        answer = self._exact_expression(self._target_x)
        print("=== ACCURACY ===")
        print("WARNING : This method doesn't know whether your exact y expression is right. You should double check yours.")
        print("Answer : y({}) = {}".format(self._target_x, answer))
        print("Predicted : y({}) = {:.{}f}".format(self._target_x, self._predicted_y, self._n))
        print("Accuracy : {:.{}f}%".format(100 - abs((answer - self._predicted_y) / answer) * 100, self._n))
        print()
        return 100 - abs(answer - self._predicted_y) / answer * 100
        # You can use accuracy value if you want

    def plot(self, x_start, x_end, h_list=None) :

        def range_generator(start, end, step) :
            num = start
            while num < end:
                yield num
                num += step

        old_target_x = self._target_x
        old_predicted_y = self._predicted_y

        if h_list is None : 
            h_list = [abs(self._h)]
            print("'h' is set to {}".format(self._h))
        if len(h_list) != len(set(h_list)):
            print("There are same h. Please input different h's.")
            exit(1)

        old_h = self._h
        for h in h_list :
            x_list = list(range_generator(x_start,x_end,abs(h)))
            self._h = h
            y_list = [self.solve(x) for x in x_list]
            plt.scatter(x_list,y_list,label="h = {}".format(self._h))

        if self._exact_expression is not None :
            exact_x = list(range_generator(x_start, x_end, self.plot_precision))
            exact_y = [self._exact_expression(x) for x in exact_x]
            plt.plot(exact_x, exact_y, 'r-', label='Exact')

        self._h = old_h
        plt.legend()
        plt.show()
        self._target_x = old_target_x
        self._predicted_y = old_predicted_y