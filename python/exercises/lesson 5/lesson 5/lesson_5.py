import random
i=0
s=0
while(i<39):
    n=random.randint(100,999)
    if(n%2==0):
        print(n%10 + (n//10)%10 + n//100)
    s=s+n
    i+=1
print(s/39)


n=random.randint(10, 99)
while(n%2==0):
    print(n)
    n=random.randint(10, 99)
print(n)   



import random
n=random.randint(10, 99)
while(n%2==0):
    print(n)
    n=random.randint(10, 99)
print(n)    



#   q1 springA 2021
z=0
e=0
for i in range(4):
    num=int(input("Enter a number : "))
    if(num>99 and num<1000):
        print(num%10 + (num//10)%10 + num//100)
    if(num%2==0):
        z+=1
    else:
        e+=num
print(z)
print(e)
   


#   q1 summerA 2020
num=int(input("Enter a number : "))
c=0
z=0
p=0
s=0
while(num!=0):
    c+=1
    if(num%2==0):
        z+=1
    if(num>0):
        p+=1
        s+=num
    num=int(input("Enter a number : "))
print(c)    
print(z)    
print(s/p)    
   


def Mul(a, b): # 1 5   
    r=0
    while(a>0):
        r=r+b  # 5
        a-=1
    return r
def Hezka(x, y):
    t=1
    while(y>0):
        t=Mul(t,x) #5  25
        y=y-1
    return t

print(Hezka(5,4))
print(Hezka(10,3))
print(Hezka(6,2))
print(Hezka(7,1))




def F(x):
    r=0
    i=1
    #   1  -  2  +  3  -  4  +  5  -  6  +  7  =  4
    while(i<x):
        if(i%2==0):
            r=r-i
            print(i, " + ", end=" ")
        else:
            r=r+i
            print(i, " - ", end=" ")
        i+=1
    if(x%2==0):
        r=r-x
    else:
        r=r+x
    print(x, " = ", r)
    return r
   ###  nain ###
num=int(input("Enter a number : "))
v=F(num)
print(F(num))
#   1 - 2 + 3 - 4 + 5 = 3


def F(x):
    r=0
    i=1
    while(i<x):
        r=r+i
        i+=1
    return r+i

for i in range(3, 8):
    print(F(i))



def F(x):
    y=x*x
    return y

r=F(3)
print(r)
print(F(8))



import math
def IsPrime(x):
     if(x%2==0):
         print("no")
     else:
         sqrtX=int(math.sqrt(x)) + 1
         i=3
         while(i<sqrtX):
             if(x%i==0):
                 print("no")
                 break
             i+=2
         if(i>=sqrtX):
             print("YES")
       
IsPrime(100)        
IsPrime(101)        
IsPrime(49)        
IsPrime(80)        
       

import math
def ShowDeviders(x):
     sqrtX=int(math.sqrt(x))
     for i in range(2, sqrtX, 1):
         if(x%i==0):
             print(i, "  ", x//i, end="  ")
     if(sqrtX*sqrtX==x):
         print(sqrtX)
     else:
         i+=1
         if(x%i==0):
             print(i, x//i)
     print()

 ###    MAIN    ####

num=int(input("Enter a number : "))
ShowDeviders(num)


   2   4   5   10
   50  25  20      



   100     2 4 5 10 20 25 50



########################################################################
########################################################################
 makan elazar

import random
from xml.etree.ElementPath import prepare_child
i=0
s=0
while(i<39):

   n=random.randint(100,999)
   if(n%2==0):
      print(n%10  )
    n=random.randint(10,99)
print(n)



num=int(input("enter a number:"))
for i in range(40):
    c=0
    if(num>99 and num<1000):
       c=c+(num%10)
       num=num//10






def Mul(a,b):
    r=0
    while(a>0):
        r=r+b
        a-=1
    return r
def Hezka(x,y):
    ??
if( Mul(7,3)> Mul(2,8)):
    print(("YYY"))
else:
    print(("NNN"))



from ast import Return


def f(x):
    r=0
    i=1
    while(i<x):
        r=r+i
        i+=1
    return r+i

for i in range(3,8):
    print(f(i))







import math
def IsPrime(x):
     if(x%2==0):
          print("NO")
     else:
          sqrtx=int(math.sqrt(x))+1
     i=3
     while(i<sqrtx):
         if(x%i==0):
              print("NO")
              break
         i+=2
         if
  ##  nain ###
num=int(input("enter a number :" ))
showDoeviders(num)



import math
def showDoeviders(x):
      sqrtx=int(math.sqrt(x))+1
      for i in range (3,sqrtx,2):
           if(x%i==0):
               print("NO")
               break
           else:
               print("YES")
               break
      #if(x%sqrtx==0):
      #    print(sqrtx)
      #else:
      #    print(x//sqrtx)
      print()
  ###  nain ###
num=int(input("enter a number :" ))
showDoeviders(num)



import math
def showDoeviders(x):
      sqrtx=int(math.sqrt(x))+1
      for i in range (2,sqrtx,1):
           if(x%i==0):
               print(i," ",x//i,end=" ")
      if(x%sqrtx==0):
          print(sqrtx)
      else:
          print(x//sqrtx)
      print()
  ###  nain ###
num=int(input("enter a number :" ))
showDoeviders(num)




import math
def showDoeviders(x):
      sqrtx=int(math.sqrt(x))+1
      for i in range (2,sqrtx,1):
           if(x%i==0):
               print(i," ",x//i,end=" ")
      print()
  ###  nain ###
num=int(input("enter a number :" ))
showDoeviders(num)


def kefel(a,b):
    r=0
    while(a>0):
        r=r+b
        a-=1
    return r
print(kefel (5, 4))
