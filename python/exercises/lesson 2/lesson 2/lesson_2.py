# 0  1  2  3  4  index
a=[33,11,66,55,77]
print(a)
t=a[len(a)-1]   #  t=77
i=len(a)-1      #  i=4
while(i>0):
    a[i]=a[i-1]
    i-=1
a[0]=t          #  =77
print(a[2])
"""
i=4      3   2   1     
a[i]=55  66  11  33 
output: a[77,33,11,66,55]
"""



# 0  1  2  3  4
a=[33,11,66,55,77]
p=0
while(p<len(a)):        #  p<5
    t=a[0]              #  t=33
    i=1
    while(i<len(a)):    #  i<5
        a[i-1]=a[i]
        i+=1 
    a[len(a)-1]=t
    p+=1
 """
 i=1        2   3   4   5
 a[i-1]=33  11  66  55
 a[i]=  11  66  55  77   (t)=33
 p=0  1

 a[11,66,55,77,33]
 t=11
 i=1        2   3   4   5
 a[i-1]=11  66  55  77  
 a[i]=66    55  77  33 (t)=11
 p=2

 a[66,55,77,33,11]
 c[55,77,33,11,66]
 p=3

 a[55,77,33,11,66]
 outcome: a[77,33,11,66,55]
 p=4

 a[77,33,11,66,55]
 outcome: a[33,11,66,55,77]
 p=5
"""

## 0  1  2  3  4  index
a=[33,11,66,55,77,]
t=a[0]              # t=33
i=1
while(i<len(a)):
    a[i-1]=a[i]
    i+=1
a[len(a)-1]=t
'''                     ??
    i   a
    1   33 11 66 55 77  ??
    2   11 11 66 55 77
    3   11 66 66 55 77
    4   11 66 55 55 77
    5   11 66 55 77 77
        11 66 55 77 33
'''



## 0  1  2  3  4  5  6  index
a=[33,11,66,55,77,22,99]
m=a[0]
i=1
while(i<len(a)):  #len(a) = 7
    if(m<a[i]):
        m=a[i]
    print(m)
    i+=1
print("sof")
"""
m=33        66      77       99
screen= 33  66  66  77  77   99  sof
i=1     2   3   4   5   6    7
"""

## 0  1  2  3  4  5  index
a=[33,11,66,55,77,88]
i=0
while(i<6):
    print(a[i])
    i+=1
print("sof")
"""
i=0      1   2   3   4   5
a[i]=33  11  66  55  77  88
"""


num=int(input("Enter a namber")) #1234
num=1234
t=0
while(num>0):
    t=t*10+(num%10)
    num=num//10
print(t)
"""
num=1234  123   12   1   0
t=0        4    43  432  4321
"""

r=int(input("enter a number:"))
while(r<1):
    r=int(input("ERROR!!!enter again:"))
t=0
while(r>0):
    t=t+(r%10)
    r=r//10
    print(r,t)
print(r,t)
print("sof")



r=int(input("enter a number:"))
t=0
if(r>0):
    while(r>0):
        t=t+(r%10)
        r=r//10
        #print(r,t)
    print(r,t)
else:
    print("wrong imput")
print("sof")


r=451
t=0
while(r>0):
    t=t+(r%10)
    r=r//10
    print(r, t)
print(r,t)
"""
r=451  45  4   0
t=0    1   6   10
"""

r=6231
t=0
while(r>0):
    t=t+(r%10)
    r=r//10
print(r, t) 
"""
# # r=6231  623   62   6   0
# # t=0      1    4    6   12
"""



 # y=x%10
 # y=x//10
x=7
z=x//10
y=x%10


# u=6475
# t=u//10


a=21
b=5
c=a//b     # c=4
d=a%b      #d=1
e=a/b  
a=21    #e=4.2

print(a)
print(b)
print(c)
print(d)
print(e)


mo=17
me=5
c=0
while(mo>=me):
    mo=mo-me
    c+=1
print(c, mo)

"""
 mo=17   12   7    2 
 c=0     1    2    3
 me=5
"""



r=26
st=1
while(r>0):
    sp=r-1
    while(sp>0):
        print(" " ,end="")
        sp=sp-1
    ko=st
    while(ko>0):
        print("*",end="")
        ko-=1    #  ko=ko-1
    print()
    r=1
    st+=1        #  st=st-1

