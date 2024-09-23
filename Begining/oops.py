class ClassName:
    '''doc_string'''

    def method1(self):
        pass

class Student:

    def class_name(self):
        name = 'class 8'
        time = '10am to 4pm'
        return name,time

obj = Student()
print(obj.class_name())
print(dir(obj))

# class School:
#     def _init_(self,s_name,s_loc,s_total_no):
#         self.s_name = s_name
#         self.s_loc = s_loc
#         self.s_total_no = s_total_no
#
#     def batch_8_data(self,st_no):
#         self.st_no = st_no
#         rest_student = self.s_total_no-self.st_no
#         return f'School Name is:- {self.s_name}, batch 8 students :-{self.st_no}, rest studnets :- {rest_student} '



# obj = School('Sri Aurobindo','Khandagiri',634)
# print(obj.batch_8_data(100))

# First you have 1000 rupees create a const
#
# method 1 :- rupesh (-350) -- return how much rupesh take, and current amount(650)
#
# method 2 :- mahesh (+600) -return how much mahesh get, and current amount(1250)


# class MyMoney:
#
#     def _init_(self,current_amount):
#         self.current_amount = current_amount
#
#     def rupesh_debit(self,debit):
#         self.current_amount = self.current_amount-debit
#         return f'after rupesh debit current amont is :{self.current_amount}'
#
#     def mahesh_credit(self,credit):
#         self.current_amount = self.current_amount+credit
#         return f'after mahesh credit current amont is :{self.current_amount}'
#
# obj = MyMoney(1000)
# print(obj.rupesh_debit(350))
# print(obj.mahesh_credit(600))

# Create class ALG
#
#     in const pass two parametr
#
#     method 1 :- add two no. from _const
#     method 2 :- multple two no. const and restlt of add
#     method 3 :- div :- mul result / add two no.


class Alg:
    def _init_(self,num1,num2):
        self.num1= num1
        self.num2 = num2

    def  add(self):
        add_res = self.num1+self.num2
        return add_res

    def multiplication(self):
        mul = self.num1*self.num2*self.add()
        return mul