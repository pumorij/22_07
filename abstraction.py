# abstraction

from abc import ABC,abstractmethod

class A(ABC):
    def display(self):
        print("Hi")
    @abstractmethod
    def m1(self):
        pass

class B(A):
    def m1(self):
        print("Hello")

ob=B()
ob.m1()
ob.display()
