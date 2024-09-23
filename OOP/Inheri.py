'class Alg:
    def _init_(self,num1,num2):
        self.num1= num1
        self.num2 = num2

    def  add(self):
        add_res = self.num1+self.num2
        return add_res

    def multiplication(self):
        mul = self.num1*self.num2*self.add()
        return mul


obj = Alg(10,20)
obj.num3 = 30
print(obj._dict_)
'''

#method
'''instance method
class method
static methdo

instance var
static var
local var'''

#inhheritance
# single inhheritance

class A:
    def _init_(self,l,b):
        self.l = l
        self.b = b

    def rec_peri(self):
        res = self.a*self.b
        return res


class B(A):
    def _init_(self,l,b,a):
        self.a = a
        super()._init_(l,b)

    def squre(self):
        res = super().rec_peri()+(self.a**2)
        return res

obj_b = B(100,200,150,250)
print(obj_b.sub())