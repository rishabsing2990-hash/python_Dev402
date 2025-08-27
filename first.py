print("hello")
a=b=c=8
print(id(a))
print(id(b))
print(id(c))
print(a,b,c)
 #unpack 
f=[5,6,7]
a,b,c=f
print(a,b,c)
#global variable
def myfunc():
    global x
    x = "variable"
myfunc()
print (x)