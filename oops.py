# # class man:
# #     def __init__ (self,name,age):
# #         self.name=name
# #         self.age=age
# # s=man("sunil",22)
# # print(s.name)
# # print(s.age)
# #
# # class sun:
# #     def __init__ (self,name,age):
# #         self.name=name
# #         self.age=age
# #     def myfunc(self):
# #         print(f"my name is ",self.name)
# #         print(f"i am ",self.age)
# # a=sun("sunil",22)
# # a.age=24
# # a.myfunc()
# #
# # class man:
# #     def __init__ (self,name,age,gender):
# #         self.name=name
# #         self.age=age
# #         self.gender=gender
# #     def myfunc(self):
# #         print(f"my name is ",self.name)
# #         print(f"i am ",self.age)
# #         print(f"and i am a ",self.gender)
# # a=man("sunil",22,"male")
# # a.myfunc()
#
# # class person:
# #     def __init__ (self):
# #         self.name=str(input("enter the name:"))
# #         self.age=int(input("enter the age:"))
# #     def myfunc(self):
# #         print(f"my name is ",self.name)
# #         print(f"i am ",self.age)
# #     def myfuncc(self):
# #         print(f"my name is ", self.name)
# #         print(f"i am ", self.age)
# # a=person()
# # a.myfunc()
# # a.myfuncc()
# #
# class sunny:
#     def __init__ (self):
#         self.a=int(input("enter the num1:"))
#         self.b=int(input("enter the num2:"))
#     def addition(self):
#         self.c=self.a+self.b
#         print(self.c)
#     def sub(self):
#         self.c=self.a-self.b
#         print(self.c)
# class bunty(sunny):
#     def __init__ (self):
#         self.a = int(input("enter the num1:"))
#         self.b = int(input("enter the num2:"))
#     def mul(self):
#         self.c = self.a * self.b
#         print(self.c)
#     def div(self):
#         self.c = self.a / self.b
#         print(self.c)
# z=sunny()
# z.addition()
# z.sub()
# x=bunty()
# x.addition()
# x.sub()
# x.mul()
# x.div()
#
# class sunny:
#     def __init__ (self):
#         self.a=int(input("enter the num1:"))
#         self.b=int(input("enter the num2:"))
#     def addition(self):
#         self.c=self.a+self.b
#         print(self.c)
#     def sub(self):
#         self.c=self.a-self.b
#         print(self.c)
# z=sunny()
# z.addition()
# z.sub()

#MULTI INHERITENCE

# class A:
#     def p(self):
#         print("this is from class A")
#         self.a=int(input("enter a num1:"))
#         self.b=int(input("enter a num2:"))
#         print(self.a,self.b)
# class B(A):
#     def r(self):
#         print("this is from class B")
#         self.c = str(input("enter a name1:"))
#         self.e = str(input("enter a name2:"))
#         print(self.c,self.e)
# class Z(B):
#     def l(self):
#         print("this is from class Z")
#         self.f = str(input("enter a vill:"))
#         self.g = str(input("enter a dist:"))
#         print(self.f, self.g)
# # x=A()
# # x.p()
# # d=B()
# # d.p()
# # d.r()
# k=Z()
# k.p()
# k.r()
# k.l()

# MULTIPLE LEVEL
#
# class A:
#     def p(self):
#         print("this is from class A")
#         self.a=int(input("enter a num1:"))
#         self.b=int(input("enter a num2:"))
#         print(self.a,self.b)
# class B:
#     def r(self):
#         print("this is from class B")
#         self.c = str(input("enter a name1:"))
#         self.e = str(input("enter a name2:"))
#         print(self.c,self.e)
# class Z(A,B):
#     def l(self):
#         print("this is from class Z")
#         self.f = str(input("enter a vill:"))
#         self.g = str(input("enter a dist:"))
#         print(self.f, self.g)
# # x=A()
# # x.p()
# # d=B()
# # d.p()
# # d.r()
# k=Z()
# k.p()
# k.r()
# k.l
#
# HEIERARICAL LEVEL
#
# class A:
#     def p(self):
#         self.a=int(input("enter a num:"))
#         self.b=int(input("enter a num:"))
#         print(self.a,self.b)
# class B(A):
#     def q(self):
#         self.a = str(input("enter a name1:"))
#         self.b = str(input("enter a name2:"))
#         print(self.a,self.b)
# class C(A):
#     def r(self):
#         self.a = int(input("enter a age1:"))
#         self.b = int(input("enter a age2:"))
#         print(self.a,self.b)
# class D(A):
#     def s(self):
#         self.a = str(input("enter a vill:"))
#         self.b = str(input("enter a dist:"))
#         print(self.a,self.b)
# X=B()
# X.p()
# X.q()
# Y=C()
# Y.r()
# Z=D()
# Z.s()

# HYBRID LEVEL

# class A:
#     def d(self):
#         self.a=int(input("enter a num1:"))
#         self.b=int(input("enter a num1:"))
#         print(self.a,self.b)
#
# class B(A):
#     def e(self):
#         self.a = int(input("enter a age:"))
#         self.b = int(input("enter a age:"))
#         print(self.a, self.b)
#
# class C(A):
#     def f(self):
#         self.a = str(input("enter a name1:"))
#         self.b = str(input("enter a name2:"))
#         print(self.a, self.b)
#
# class D(B,C):
#     def g(self):
#         self.a = str(input("enter a vill:"))
#         self.b = str(input("enter a dist:"))
#         print(self.a, self.b)
#
# x=D()
# x.d()
# x.e()
# x.f()
# x.g()

#POLYMORPHISM

# class Child1:
#     def __init__ (self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("took")
# class Child2:
#     def __init__ (self,bus,car):
#         self.bus=bus
#         self.car=car
#     def move(self):
#         print("take")
# class Child3:
#     def __init__ (self,hot,cool):
#         self.hot=hot
#         self.cool=cool
#     def move(self):
#         print("taken")
# x=Child1("automac","super model")
# y=Child2("palle velugu","rtc")
# z=Child3("tea","ice")
# # x.move()
# # y.move()
# # z.move()
# for a in (x,y,z):
#     a.move()


# class person:
#     def __init__ (self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print(f"my name is ", self.name)
#         print(f"i am ", self.age)
# x=person("sunil",22)
# x.myfunc()

# class sunny:
#     def __init__ (self):
#         self.a=int(input("enter the num1:"))
#         self.b=int(input("enter the num2:"))
#     def add(self):
#         self.c=self.a+self.b
#         print(self.c)
#     def sub(self):
#         self.d=self.a-self.b
#         print(self.d)
# class person(sunny):
#     def multi(self):
#         self.e = self.a * self.b
#         print(self.e)
#     def divi(self):
#         self.f = self.a / self.b
#         print(self.f)
#
# # x=sunny()
# # x.add()
# # x.sub()
# y=person()
# y.multi()
# y.add()
# y.sub()
# y.divi()

# class vehicle:
#     def __init__ (self,name,speed,milage):
#         self.name=name
#         self.speed=speed
#         self.milage=milage
#     def show(self):
#         print("details:", self.name,self.speed,self.milage)
#     def maxspeed(self):
#         print("max speed of vehicle is",self.speed)
#     def maxmilage(self):
#         print("max milage of vehicle is",self.milage)
# class car(vehicle):
#     def maxspeed(self):
#         print("max speed of vehicle is 220")
#     def maxmilage(self):
#         print("max milage of vehicle is 18")
# Car=car("bike",200,50)
# Car.show()
# Car.maxspeed()
# Car.maxmilage()
#
# Vehicle=vehicle("bus",150,10)
# Vehicle.show()
# Vehicle.maxspeed()
# Vehicle.maxmilage()

# class ferrari:
#     def fuel_type(self):
#             print("petrol")
#     def speed(self):
#             print("max speed 390")
# class bmw:
#     def fuel_type(self):
#         print("diesel")
#     def speed(self):
#         print("max speed 250")
# Ferrari=ferrari()
# Bmw=bmw()
# for car in (Ferrari,Bmw):
#     car.fuel_type()
#     car.speed()

# for i in range(5):
#     print(i,end=", ")
# print()
# for j in range(5,10):
#     print(j,end=", ")
# print()
# for i in range(1,15,3):
#     print(i,end=", ")
# print()


# a=['sunil','sravan','santhosh']
# for i in reversed("sunil naikoti"):
#     print(i,end="")
# print('\n')
# for j in reversed(a):
#     print(j,end=",")
#
# class shape:
#     def area(self,a,b=0):
#         if b > 0:
#             print("area of rectangla is",a * b)
#         else:
#             print("area of square is ",a**2)
# square=shape()
# square.area(4)
#
# rectangle=shape()
# rectangle.area(5,4)

# class Book:
#     def __init__(self, pages):
#         self.pages = pages
#     def __add__(self, other):
#         return self.pages + other.pages
#
# b1 = Book(400)
# b2 = Book(300)
# print("Total number of pages: ", b1 + b2)

# class square:
#     def __init__ (self,side):
#         self.side=side
#     def area(self):
#         print(self.side * self.side)
# class cube(square):
#     def area(self):
#         face_side=self.side * self.side
#         print(face_side * 5)
#     def volume(self):
#         face_side=self.side * self.side
#         print(face_side * self.side)
# a=cube(5)
# a.area()
# a.volume()


# class person:
#     def __init__ (self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         self.c=self.a+self.b
#         print(self.c)
# class man:
#     def sub(self):
#         self.d=self.a-self.b
#         print(self.d)
# class men(person,man):
#     def multi(self):
#         self.e=self.a*self.b
#         print(self.e)
# mad=men(5,4)
# mad.add()
# mad.sub()
# mad.multi()

