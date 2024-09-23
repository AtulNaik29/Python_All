#Multiple inhheritance

class A:
    def add(self,a,b):
        self.a = a
        self.b = b
        res = self.a +self.b
        return res

    def sub(self,a,b):
        self.a = a
        self.b = b
        res = self.a -self.b
        return res


class B:
    def add(self,a,b):
        self.a = a
        self.b = b
        res = self.a +self.b
        return res


class C:
    def add(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        res = self.a +self.b+self.c
        return res

    def div(self,a,b):
        self.a = a
        self.b = b
        return  self.a/self.b



class D(B,A,C):
    # def mul(self,x,y):
    #     self.x = x
    #     self.y = y
    #     add = super().add(10,20,30)
    #     res= add*(self.x+self.y)
    #     return res

    def call(self):
        res = super().sub(10,20)+super().add(10,20)+super().div(10,2)
        return res



obj_d = D()
print(obj_d.call())
