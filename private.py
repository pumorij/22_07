# private variable

class A:
    def show(self):
        self.__a=20
        print(self.__a)
    def display(self):
        print("A")
        ob=A()
        ob .__show()

ob=A()
ob.show()