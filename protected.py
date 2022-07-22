# protected variable

class A:
    def __init__(self):
        self ._a=14
class B(A):
    def __init__(self):
        A.__init__(self)
        print(self._a)
ob=B()