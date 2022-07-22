# use of getter and setter

class A: 
    __value="a"
    def setvalue(self,value):
        self .__value=value
    def getvalue(self):
        return self .__value

ob=A()
ob.setvalue("abc")
print(ob.getvalue())