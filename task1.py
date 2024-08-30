# thisdict=[{"name":"abc","age":21},{"a":1,"b":2},{"color":"red","fruits":"apple"}]
# b=thisdict[0]
# print(b)
# b=thisdict[1]
# print(b)
# b=thisdict[2]
# print(b)
# c=thisdict[1]
# print(c)
# print(thisdict[2]["fruits"])
# thisdict.append({"name1":"xyz"})
# print(thisdict)
# thisdict.append(100)
# print(thisdict)
# thisdict={"fruits":"apple","age":21,"name":"xyz"}
# thisdict["gender"]="abc"
# print(thisdict)
# x=thisdict.keys()
# print(x)
# y=thisdict.values()
# print(y)
# z=thisdict["age"]
# print(z)
# thisdict2=thisdict["name"]
# print(thisdict2)
# print(thisdict)
#
# thisdict={"name":"anil","age":21,"college":"abc"}
# x=thisdict.keys()
# print(x)
#
# y=thisdict.values()
# print(y)
#
# thisdict["class"]=12
# print(thisdict)
#
# thisdict["college"]="sri indhu"
# print(thisdict)
#
# print(thisdict["age"])
#
# x1=["fruit","vegetable","gender","name"]
# x2=["apple","potato","female","john"]
# y={}
# for i in range(len(x1)):
#     y[x1[i]]=x2[i]
# print(y)
#
# y=zip(x1,x2)
# print(y)
# z=dict(y)
# print(z)
#
# x=[1,2,3,4,5,6,7]
# x.insert(4,8)
# print(x)
#
# x.pop()
# print(x)
#
# x.append("anil")
# print(x)
#
# x.pop()
# print(x)
#
# x.remove(2)
# print(x)
#
#
# y=[1,2,3,4,8,6,7,9]
# z=(y[ :2])
 # x=(y[-2: ])
# print(x)
# z.extend(x)
# print(z)

# x=[1,2,3,4,5]
# y=[6,7,8,9,0]
# x.extend(y)
# print(x)
# print(len(x))

# s=[1,2,3,2,4,2,5,2,4,6,5,2]
# r=s.count(2)
# print(r)
# s.reverse()
# print(s)

# a=[10,20,80,40,22,33,54,100]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
#
# dict1={"name":"sunil","age":22,"gender":"male"}
# dict2={"name":"sravan","age":24,"class":"abc"}
# d3=dict1|(dict2)
# print(d3)
# d3.clear()
# print(d3)
#
# sports=["cricket","volleyball"]
# sports.append("chess")
# print(sports)
# sports.sort()
# print(sports)
# sports.sort(reverse=True)
# print(sports)
#
# sub=["telugu","hindi","english","social","maths","physics"]
# print(sub)
# a=str(input("enter a unwanted sub:"))
# # for x in sub:
# if a in sub:
#     sub.remove(a)
# print(sub)
#
# b=["apple","banana","cherry","mango","watermelon","kiwi"]
# print(b)
# y=str(input("remove unwanted fruit:"))
# for x in b:
#     if y in x:
#         b.remove(y)
# print(b)
#
#
# food={1:"idly",2:"dosa",3:"vada",4:"puri"}
# print(food)
# print("please consider above food as you liked")
# a=int(input("enter least like food:"))
# if a in food:
#     food.pop(a)
# print(food)
# #
# colors=["red","blue","green","yellow","orange","purpule","pink","brown","gray","black"]
# print(colors)
# a=colors[1:-1]
# print(a)
# print("enter any five colors(0-7)")
# d=[]
# for i in range(5):
#     r=int(input(f"enter colors no{i+1}:"))
#     d.append(r)
# z=[a[r] for r in d]
# # print("your selected colors are printed below")
# print(z)
# for x in z:
#     print(x)
#
# country=("india","chaina","pakisthan","srilanka","america")
# print(country)
# a=str(input("enter a country name:"))
# s=country.index(a)
# print(s)

#
# country=("india","chaina","pakisthan","srilanka","america")
# print(country)
# print("enter the country name according to their index num")
# user_input=input()
# try:
#     index=country.index(user_input)
#     print(f"the index of the {user_input} in the tuple is {index}")
# except:
#     print(f"{user_input} is not found")
#
# country=("india","chaina","pakisthan","srilanka","america")
# print(country)
# z=list(country)
# a=int(input("enter country no(0-4):"))
# r=z[a]
# print(r)
# #
# sports=["cricket","volleyball"]
# print(sports)
# a=str(input("enter any game to add the list:"))
# sports.append(a)
# sports.sort()
# print(sports)
#
# sub=["telugu","hindi","maths","social","english","physics"]
# print(sub)
# a=str(input("enter the unwanted sub:"))
# if a in sub:
#     sub.remove(a)
# print(sub)

# colors=["red","black","white","pink","yellow","purpule","gray","orange","brown","green"]
# print(colors)
# a=int(input("enter colors no(0-4):"))
# b=int(input("enter colors no(5-9):"))
# z=colors[a:b]
# print(z)
# #
# x1=[111,222,333,444]
# for x in x1:
#     print(x)
# a=int(input("enter the num:"))
# if a in x1:
#     z=x1.index(a)
#     print(z)
# else:
#     print("that num is not in the list")
#
# nums=[]
# for i in range(3):
#     a=int(input("enter a no:"))
#     nums.append(a)
#     print(nums)
# b=str(input("do you want to keep the last no(yes/no):"))
# if b =="no" and len(nums)>0:
#     nums.pop()
# print(nums)

# z="hello"
# a=str(input("enter your first name:"))
# print(a)
#
# fn=input("enter your name:")
# print("hello first name is ",fn)

# fn=input("enter your name:")
# sr=input("enter your surname:")
# z=fn+sr
# print(z)
#
# a=int(input("enter first num:"))
# b=int(input("enter second num:"))
# c=a+b
# print("the sum of no1,no2 is:",c)

# a=int(input("enter no1:"))
# b=int(input("enter no2:"))
# c=int(input("enter no3:"))
# z=a+b
# print("the sum of no1,no2 is:",z)
# x=z*c
# print("the multiplication of c and sum of z",x)

# ask=int(input("how many slices does your pizza have:"))
# print(f"my pizza contains{ask} slices")
# eat=int(input("how many slices have you ate?"))
# print(f"i ate{eat} pizza")
# a=ask-eat
# print(f"left over pizza slics are {a}")

# ask=input("what is your name:")
# age=int(input("what is your age:"))
# x = age + 1
# print(f"next birthday you will be {x}")

# bill=int(input("total amount:"))
# diners=int(input("how many people:"))
# total_diners = bill / diners
# print("each person must pay:",total_diners)

# a=int(input("enter first num:"))
# b=int(input("enter second num:"))
# if a > b:
#     print(b,a)
# else:
#     print(a,b)

# num=int(input("enter the num(1-3):"))
# if num == 1:
#     print("thank you")
# elif num == 2:
#     print("well done")
# elif num == 3:
#     print("correct")
# else:
#     print("error message")
#
# num1=int(input("enter the num(0-19):"))
# if num1 > 20:
#     print("too high")
# else:
#     print("thank you")
#
# num2=int(input("enter the num(10-20):"))
# if num2 > 10 and num2 < 20:
#     print("thank you")
# else:
#     print("incorrect")
#
# color=str(input("enter your favorite color:"))#.lower()
# if color.lower() == "red":
#     print("i like red too")
# else:
#     print(f"i dont like {color} i prefer red")

# a=str(input("there is raining?(yes/no):"))
# if a == "yes":
#     b=str(input("if it is windy?(yes/no):"))
#     if b == "yes":
#         print("it is too windy for an umbrella")
#     elif b == "no":
#         print("take an umbrella")
# else:
#     print("enjoy your day")
# age=int(input("enter your age:"))
# if age >= 18:
#     print("you can vote")
# elif age == 17:
#     print("you can learn to drive")
# elif age == 16:
#     print("you can buy a lottery ticket")
# else:
#     print("you can go to trickor treating")

#
# fn=str(input("enter your first name:"))
# print(fn)
# print(len(fn))
#
# a=str(input("enter your first name:"))
# b=str(input("enter your surname:"))
# c=a+" "+b
# print(c)
# print(len(c))

# a=str(input("enter your first name:"))
# b=str(input("enter your surname:"))
# c=a+" "+b
# x=c.upper()
# print(x)
#
# rhyme=str(input("enter a first line of rhyme:"))
# x=len(rhyme)
# print(x)
# a=int(input(f"enter starting num from{x}:"))
# b=int(input(f"enter ending num from{x}:"))
# y=rhyme[a:b]
# print(y)

# name=str(input("enter a name:"))
# x=name.upper()
# print(x)
#
# fn=str(input("enter your name:"))
# x=len(fn)
# if x < 5:
#     sr = str(input("enter your surename:"))
#     y=fn+sr
#     print(y.upper())
# else:
#     print(fn.lower())

# FOR LOOP :
#
# name=str(input("enter a name:"))
# for x in range(3):
#     print(name)
#
# name=str(input("enter your name:"))
# num=int(input())
# for x in range(num):
#     print(name)
#
# name=str(input("enter your name:"))
# for x in name:
#     print(x)
#
# name=str(input("enter a name:"))
# num=int(input("enter the num:"))
# for i in range(num):
#     for c in name:
#         print(c)

# a=int(input("enter a num between(1-12):"))
# for i in range(1,11):
#     x=a*i
#     print(x)

# #6
# name=str(input("enter your name:"))
# num=int(input("enter your num:"))
# if num < 10:
#     for x in range(num):
#         print(name)
# else:
#     for v in range(3):
#         print("too high")
#
# total=0
# for i in range(5):
#     a=int(input(f"enter a num{i+1}:"))
#     b=str(input("do you want add this num(yes/no):"))
#     if b == "yes":
#         total= total+a
#     elif b == "no":
#         continue
# print("total is :",total)
#
# z=[]
# ask=int(input("how may people invite to a party:"))
# if ask < 10:
#     for i in range(ask):
#         a=str(input(f"enter the name {i+1}:"))
#         print(f"{a} has been invited")
#         z.append(a)
# else:
#     print("too many people")
# print(z)

# WHILE LOOP:

# total=0
# while total < 50:
#     a=int(input("enter a num:"))
#     total=total+a
#     print("total is :",total)
# print("loop stopped")
#
# a=0
# while True:
#     a = int(input("enter a num:"))
#     if a >= 5:
#        print(f"the last num you entered was a {a} snd stoped the program.")
#        break
#
# num1=int(input("enter a num:"))
# num2=int(input("enter another num:"))
# a=num1+num2
# print(a)
# while True:
#     x=str(input("if you want add another num?(y/n):"))
#     if x == "y":
#         b=int(input("enter any num:"))
#         a=a+b
#         print(a)
#     elif x == "n":
#         break
# print(a)
#
# c=0
# ask=str(input("enter a name wants to invite to a party:"))
# a=(f"{ask} has now been invited")
# print(a)
# c=c+1
# while True:
#     d=str(input("if you want invite anybody?(y/n):"))
#     if d == "y":
#        x=str(input("enter a name:"))
#        print(f"{x} has been invited")
#        c=c+1
#     elif d == "n":
#         break
# print(c)

# c=0
# while True:
#     cn=int(input("enter a num to guess the num:"))
#     c=c+1
#     if cn < 50:
#         print("too low")
#     elif cn > 50:
#         print("too high")
#     elif cn == 50:
#         print(f"well done you took {c} attempts")
#         break
#
# user=int(input("enter the num between (10-20):"))
# while True:
#     if user < 10:
#         print("too low")
#         user=int(input("try again:"))
#     elif user > 20:
#         print("too high")
#         user=int(input("try again:"))
#     elif user > 10 and user < 20:
#         print("thankyou")
#         break