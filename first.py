 # print("hello")
# a=b=c=8
# print(id(a))
# print(id(b))
# print(id(c))
# print(a,b,c)


#  #unpack 
# f=[5,6,7]
# a,b,c=f
# print(a,b,c)


#global variable
# def myfunc():
#     global x
#     x = "variable"
# myfunc()
# print (x)


#variable name-
# 1-camel style:- myVariable
# 2-snake style:- my_variable
# 3-pascal style:- MyVariable


# Numeric Data Type
# var1 = 1
# var2= True
# var3= 10.56
# var4= 20+3j
# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))

#  Output
# <class 'int'>
# <class 'bool'>
# <class 'float'>
# <class 'complex'>

# String Datatype
# print('hello')
# print("hello")
# a = """helloo world """
# b= '''helllllo '''
# print(a)
# print(b)

# # In used to check any word or letter is present in string or not
# print("world" in a) # True
# if "hello" in a:
#     print('yes')
# else:
#    print("no")
   
# print("java" not in a)   


  # Slicing of String
  # from start, end and index (numbering from 0 to n including space)
# str=" hello world "
# print(str[:]) # print string as it is  
# print(str[2:4])
# print(str[:4]) 
# print(str[-4:-2]) # in negative move from right side of the  last word 

# output
# hello world
# ll
# hell
# or


# Modification in String
# print(str.upper()) #HELLO WORLD
# print(str.lower()) # hello world
# print(str.strip()) #hello world

# a=" bhoomi "
# print(a.strip()) #removes spaces

# #replace
# print(a.replace("Hello","bhoomi"))

# a="Hello, world"
# print(a.split(","))  #['Hello', ' world']
# a="Hello world, bhoomi here"
# print(a.split(","))  #['Hello world', ' bhoomi here']
#here "," works as a seperator

#string concatenation
# a="hello"
# b="world"
# c=a+" "+b
# print(c)   #hello world

# #format-strings (F-string) to print variable and string in single print statement
# age=19
# t=f"my name is bhoomi,I am {age}"
# print(t)

# price=12.5567
# txt=f"the price is {price:.2f} dollar"
# print(txt)

# output
# my name is bhoomi,I am 19
# the price is 12.56 dollar

#Escape character-to insert characters that are illegal in a string(backlash-\)
#for eg- using double quote inside a string surrounded by double quote
# txt="we are the so-called \"vikings\" from the north."
# print(txt)    #we are the so-called "vikings" from the north.

#Boolean-(True or False)
# print(10>9)           # True
# print(10<9)           # False
# print(bool("hello"))  # True
# print(bool(10))       # True
# print(bool(0))        # False

# #function returning boolean
# def fun():
#     return True

# if fun():
#     print("yes")
# else:
#     print('no')

#SEQUENCE DATA TYPES- LIST , TUPLE , RANGE
 
#list
# l=["Dev",20,"5 march-2005","BTech"]
# tiny_l=["CSE",14]
# print(type(l))
# print(l)
# print(l[0])
# print(l[1:3])
# print(l[2:])
# print(tiny_l *2)
# print(l+tiny_l)
# #output
# <class 'list'>
# ['Dev', 20, '5v march-2005', 'BTech']
# Dev
# [20, '5 march-2005']
# ['5 march-2005', 'BTech']
# ['CSE', 14, 'CSE', 14]
# ['Dev', 20, '5 march-2005', 'BTech', 'CSE', 14]

#tuple
# tup=("abcd",789,4.56,"john",20+8j)
# tiny_tup=(123,"hello")
# print(type(tup))
# print(tup)
# print(tup[0])
# print(tup[1:3])
# print(tup[2:])
# print(tiny_tup *2)
# print(tup+tiny_tup)
# #output
# <class 'tuple'>
# ('abcd', 789, 4.56, 'john', (20+8j))
# abcd
# (789, 4.56)
# (4.56, 'john', (20+8j))
# (123, 'hello', 123, 'hello')
# ('abcd', 789, 4.56, 'john', (20+8j), 123, 'hello')

#range(start,stop,step)
# for i in range(5):
#     print(i)   #01234
# print("\n")
# for i in range(1,10,2):
#     print(i)   #13579
    
   
   
# Input
# n=int(input(""))
# print(n)
# print(type(n))

# If else,elif 
# a,b=5,10
# if (a>b):
#  print(a,"is greatest")
# elif a==b:
#  print("a=b")
# else:
#   print(b,"is greatest")
    
# #ShortHand
# a,b=5,10
# print(f"{a} is greater than {b}")if a>b else print(f"{b} is greater than {a}")
# print(f"{a} is greater than {b}") if a>b else print("=") if a==b 

# Match (work like Switch)
# month = 5 
# day =5
# match day:
#   case 1|2|3|4|5 if month == 5:
#     print("wednesday")
#   case _:  # default case "underscore is used"
#    print("weekend")
     
      
      
    # Program 
#  1. To find square of a number
# n=int(input(""))
# sqr=n**2
# print(sqr)

# 2. Print sum of two no.
# a=int(input())
# b=int(input())
# print(a+b)

# 3. swappping of two no.
# a=int(input(""))
# b=int(input(""))
# a=(a+b)-a
# b=(a+b)-b
# a,b=b,a
# print("value of a = ",a)
# print("value of b =",b)

# 4. Guess the no.
# no=4
# a=int(input(""))
# if(a==no):
#     print("you guessed it right the no. is - " ,no)
# else:
#     print("you guessed it wrong the no. is - " ,no)

# 5. EVEN/ODD
# no=int(input(""))
# if(no%2==0):
#    print(no,"is even")
# else:
#   print(no,"is odd")

# 6. temperature
# temp=int(input("enter a temp in Celcius"))
# print("teperature in F =",(temp*(9/5))+32)

# 7. type
# a=9
# b=3,4
# c="world"
# print(f"a variable type: {type(a)}\n" )

