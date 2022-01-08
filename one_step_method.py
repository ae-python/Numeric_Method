import inspect

from types import LambdaType

# 변수명, 메서드의 접근제어자
# Public(누구나 접근 가능, _ 없음)
# private(자기 class 안에서만 사용(상속받아도 사용 불가), __ 2개) 
# protected(자기, 상속받은 class 안에서 사용(=접근) 가능, _ 한개)

# ODE로 바꿔보자~
class Initial_value:

    # init: 변수초기화, 적절한 변수인지만 체크
    def __init__(self,x0,y0,f,eps=10**(-8),h=0.01):

        # Type 검사. f에 lambda type만 들어올 수 있도록 제한하기
        if not isinstance(x0 and y0 and eps and h, (int, float)) :

            print("Put appropriate type")
        # exit(n) n에 따라 출력하는 문구가 다름
            exit(1)

        if not isinstance(f,LambdaType) :

            print("Put appropriate type")

            exit(1)

        self._x0 = x0

        self._y0 = y0

        self._eps = eps

        self._h = abs(h)

        self._f = f

        self._numPara = len(inspect.getargspec(self._f).args)



    def _check_numPara(self, target_num) :

        if self._numPara == target_num :

            return True

        else :

            return False



    def _get_numPara(self, expression) :

        return len(inspect.getargspec(expression).args)







class Euler:

    __predicted_y = None

    def __init__(self,x0,y0,target_x,f,h=0.01):

        # Initial_Value를 하나의 데이터 타입으로 취급해서 가져오기
        self.__var = Initial_value(x0,y0,f,eps,h)

        super().__init__(x0,y0,f,eps=10**(-8),h=0.01)

        self.__target_x = target_x


        if not super()._check_numPara(1) :

            print("the number of parameter should be one")

            exit(1)

        if abs(self._x0 - self.__target_x) < self._h :

            print("h is smaller than difference between x0 and target_x")

            exit(1)

        else :

            mul = abs(self._x0 - self.__target_x) / self._h

            if not isinstance(mul, int) :

                self._h = abs(self._x0 - self.__target_x) / int(mul)

            if self.__target_x < self._x0 :

                self._h = - self._h



    def solve(self) :

        for _ in range(0,int(abs((self._x0 - self.__target_x)/self._h))) :

            self._y0 += self._h * self._f(self._x0)

            self._x0 += self._h

       

        self.__predicted_y = self._y0

        print("=== SOLVED ===")

        # {:.5f} : 5D로 출력
        print("f({}) = {:.5f}".format(self.__target_x, self.__predicted_y))

        print()


    # 해석해를 구할 수 있는 경우 오차까지 제공하는 메서드
    def getAccuracy(self, expression) :

        if not isinstance(expression, LambdaType) :

            print("Input lambda type")

            exit(1)

        if super()._get_numPara(expression) != self._numPara :

            print("Different number of variables")

            exit(1)

        if self.__predicted_y is None :

            print("Please solve() first")

        answer = expression(self.__target_x)

        print("=== ACCURACY ===")

        print("Answer : f({}) = {}".format(self.__target_x, answer))

        print("Predicted : f({}) = {:.5f}".format(self.__target_x, self.__predicted_y))

        print("Accuracy : {:.5f}%".format(100 - abs(answer - self.__predicted_y) / answer * 100))

        print()

        return 100 - abs(answer - self.__predicted_y) / answer * 100