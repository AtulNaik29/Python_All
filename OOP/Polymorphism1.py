# Method Overloading
class Bank:
    def rate_of_intrest(self):
        return 0

class ICICI(Bank):
    def rate_of_intrest(self):
        return 10.5

obj= ICICI()
print(obj.rate_of_intrest())

obj1=Bank()
obj1.rate_of_intrest()