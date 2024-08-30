# def check_balance():
#     print(f"your balance is {balance:.2f}:")
# def deposit():
#     amount=float(input("enter your amount:"))
#     if amount < 0:
#         print("amount must be greater than 0")
#         return 0
#     else:
#         print(f"{amount} has been credited")
#         return amount
# def withdraw():
#     amount=float(input("enter the amount:"))
#     if amount < 0:
#         print("amount must be greater than 0")
#         return 0
#     elif amount > balance:
#         print("insufficient balance")
#         return 0
#     else:
#         print(f"{amount} has been deducted")
#         return amount
#
#
# balance = 10000
# is_running = True
# while is_running:
#     print("WELL COME TO SBI")
#     print("1.check balance")
#     print("2.deposit")
#     print("3.withdraw")
#     print("4.exit")
#     a=int(input("choose the options from the above given:"))
#     if a == 1:
#         check_balance()
#     elif a == 2:
#         balance+=deposit()
#     elif a == 3:
#         balance-=withdraw()
#     elif a == 4:
#         is_running=False
#     else:
#         print("invalid operation")
# print("visit again")
#
#
# def myfunc():
#     a=int(input("enter any num:"))
#     fact=1
#     if a < 0:
#         print("a is greater than 0")
#     else:
#         for i in range(1,a+1):
#             fact=fact*i
#             print(fact)
# myfunc()
#
# def myfunc():
#     a=str(input("enter a naame:"))
#     y=len(a)
#     if y%2 == 0:
#         print("hello")
#     else:
#         x=y//2
#         print(a[x])
# myfunc()
#
# def myfunc():
#     a=int(input("enter the num:"))
#     for i in range(a):
#         if i%2 == 0:
#             print(i)
#         # else:
#         #     x=i//2
#         #     print(x)
# myfunc()
#
# def myfunc(*names):
#     print(list(names))
#     for i in names:
#         # print(i)
#         y=names.index(i)
#         print(i,y)
# myfunc("sunil","sravan","sai")
#
# def check_balance():
#     print(f"the bank balance if {balance:.2f}")
# def deposit():
#     b=float(input("enter the amount:"))
#     if b < 0:
#         print("b is must be greater than 0")
#         return 0
#     else:
#         return b
# def withdraw():
#     c=float(input("enter the amount you want:"))
#     if c < 0:
#         print("amount is must be greater than c")
#         return 0
#     elif c > balance:
#         print("insufficient balance")
#         return 0
#     else:
#         return c
#
#
# balance=0
# sunny=True
# while sunny:
#     print("WELL COME TO SBI")
#     print("1.check_balance")
#     print("2.deposit")
#     print("3.withdraw")
#     print("4.exit")
#     x=int(input("enter any num to banking:"))
#     if x == 1:
#         check_balance()
#     elif x == 2:
#         balance+=deposit()
#     elif x == 3:
#         balance-=withdraw()
#     elif x== 4:
#         print("visit again")
#     else:
#         print("incorrect operater")



# def check_balance():
#     print(f"the bank balance is {balance:.2f}")
# def deposit():
#     b=float(input("enter the amount want to deposit:"))
#     if b < 0:
#         print("the amount must be greater than 0")
#         return 0
#     else:
#         return b
# def withdraw():
#     c=float(input("enter the amount wants to deposit:"))
#     if c < 0:
#         print("amount must be greater than 0")
#         return 0
#     elif c > balance:
#         print("insufficient balance")
#         return 0
#     else:
#         return c
#
#
#
# balance=0
# is_running=True
# while is_running:
#     print("1.check_balance")
#     print("2.deposit")
#     print("3.withdraw")
#     print("4.exit")
#     x=int(input("enter the num:"))
#     if x == 1:
#         check_balance()
#     elif x == 2:
#         balance+=deposit()
#     elif x == 3:
#         balance-=withdraw()
#     elif x == 4:
#         print("visit again")
#     else:
#         print("incorrect opreator")
#         break
#
#
# class bankaccount:
#     def __init__ (self,account_holder,initial_balance):
#         self.account_holder=account_holder
#         self.balance=initial_balance
#
#     def check_balance(self):
#         print(f"account holder:{self.account_holder}")
#         print(f"current balance:{self.balance}")
#
#     def deposit(self):
#         a=int(input("enter the amout wants to deposit:"))
#         if a < 100:
#             print("amount must be greater  than 100")
#         else:
#             self.balance+=a
#             print(f"current balance:{self.balance}")

#     def withdraw(self):
#         c=int(input("enter the amount wants to withdraw:"))
#         if c < 100:
#             print("the amount must be greater than 100")
#             return 0
#         elif c > self.balance:
#             print("insufficeint balance")
#             return 0
#         else:
#             self.balance-=c
#             print(f"current balance:{self.balance}")
#
# bank=bankaccount("sunil",1000)
# bank.check_balance()
# bank.deposit()
# bank.withdraw()
#
#
# class employee:
#     def __init__ (self,name,base_salary):
#         self.name=name
#         self.base_salary=base_salary
#     def details(self):
#         print(f"employee name:{self.name},basic salary:{self.base_salary}")
#     def calculate_salary(self):
#         print(self.base_salary)
#
# class fulltimeemployee(employee):
#     def __init__ (self,name,base_salary,benefits):`
#         super().__init__(name,base_salary)
#         self.benefits=benefits
#     def details(self):
#         print(f"employee name:{self.name},basic salary:{self.base_salary},benefits:{self.benefits}")
#     def calculate_salary(self):
#         print(self.base_salary+self.benefits)
#
# class parttimeemployee(employee):
#     def __init__ (self,name,base_salary,hourly_wage,hours_work):
#         super().__init__(name,base_salary)
#         self.hourly_wage=hourly_wage
#         self.hours_work=hours_work
#     def details(self):
#         print(f"employee name:{self.name},basic salary:{self.base_salary},wage:{self.hourly_wage},hours working:{self.hours_work}")
#     def calculate_salary(self):
#         print(self.base_salary+(self.hourly_wage * self.hours_work))
#
# FULLTIME=fulltimeemployee("sunil",50000,2000)
# FULLTIME.details()
# FULLTIME.calculate_salary()
# PARTTIME=parttimeemployee("sravan",55000,1000,5)
# PARTTIME.details()
# PARTTIME.calculate_salary()

# class bankaccount:
#     def __init__ (self,owner,balance=0):
#         self.owner=owner
#         self.__balance=balance
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("hello")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("insufficient balance")
#     def get_balance(self):
#         return self.__balance
# bank=bankaccount("sunil")
# bank.deposit(1000)
# print(bank.get_balance())
# bank.withdraw(300)
# print(bank.get_balance())
#
# a=12
# b=10
# print(a&b)
#
# class car:
#     def __init__ (self,maxspeed,name):
#         self.__maxspeed=maxspeed
#         self.__name=name
#     def drive(self):
#         print("driving")
#         print(self.__maxspeed)
#     def dr(self,speed):
#         self.__maxspeed=speed
#         print(self.__maxspeed)
# redcar=car(200,"bmw")
# redcar.drive()
# redcar.dr(100)


# class A:
#     __name=" "
#     __age=" "
#     def __init__ (self):
#         self.__name="sunil"
#         self.__age=22
#     def get_details(self):
#         print("details")
#         print(self.__name)
#         print(self.__age)
#     def man(self,gender):
#         self.__gender=gender
#         print(self.__gender)
#
# b=A()
# b.get_details()
# b.man("male")
# print("sunil")