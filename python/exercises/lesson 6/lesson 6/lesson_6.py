# #Q2SummerA2023
t=input("Enter tel number :")
c=0
while(True):
    c+=1
    if(len(t)==11 and t[0]=='0' and t[1]=='5' \
           and ord(t[2])<ord('9') \
           and ord(t[2])>=ord('0') \
           and t[3]=='-'):
        for i in range(4, 11):
            if(ord(t[i])<=ord('9') \
                    and ord(t[i])>=ord('0')):
                break
    t=input("Enter tel number :")
print(c)    

#Q1SummerA2023
def IsPerfect():
    for i in range(1 ,1000):
        sumDigits=0
        ezer=i
        while(ezer>0):
            sumDigits+=ezer%10
            ezer//=10
        if(i%sumDigits==0):
            print(i)
####    MAIN    ####
IsPerfect()        
       


def IsPalindrom(s):
    left=0
    right=len(s)-1
    while(left<right):
        if(s[left]!=s[right]):
            return False
        right-=1
        left+=1
    return True    

print(IsPalindrom("abcba"))


def F(s):
    q=""
    for i in range(len(s)):
        q=s[i] + q
    return q
   
e="wert"
print(F(e))
   


s="as"
s=s+"$$$"
print(s)
s="!!!" + s
print(s)


def StrToInt(s):
    t=0
    i=0
    while(i<len(s)):
        t=t*10+(ord(s[i])-48)
        i+=1
    return t
####    MAIN    ####
n="4321"
x=StrToInt(n)
x*=2
print(x)
'''
t=0
t=t*10+4        4
t=t*10+3        43
t=t*10+2        432
t=t*10+1        4321
'''



def IsSorted(a):
    for i in range(1, len(a)):
        if(a[i-1]>a[i]):
            return False
    return True

####    MAIN    ####
a=[4,6,15,21,32,48,59]
u=IsSorted(a)
print(u)
print(IsSorted(a))



def IsSorted(a):
    for i in range(1, len(a)):
        if(a[i-1]>a[i]):
            return 0
    return 1

####    MAIN    ####
a=[4,6,15,21,32,48,59]
u=IsSorted(a)
print(u)
print(IsSorted(a))



a=[4,6,5,1,2,8,9,7,11,55]
n=0
while(n<len(a)-1):
    b=n+1
    while(b<len(a)):
        if(a[n]>a[b]):
            temp=a[n]
            a[n]=a[b]
            a[b]=temp
        b+=1
    n+=1
print(a)

a=[3411,3653,41235,47,5,1268,98769,74]
#a=[4,4,5,2,1,4,5,2]
for i in range(0, len(a), 1):
    c=0
    while(a[i]>0):
        c+=1
        a[i]=a[i]//10
    a[i]=c
print(a)








a=[11,33,45,47,53,68,69,74]
b=[13,16,19,22,34,41,51]
c=[11]*(len(a)+len(b))
idxA=0
idxB=0
idxC=0
while(idxA<len(a) and idxB<len(b)):
    if(a[idxA]<b[idxB]):
        c[idxC]=a[idxA]
        idxA+=1
    else:
        c[idxC]=b[idxB]
        idxB+=1
    idxC+=1        
while(idxA<len(a)):
    c[idxC]=a[idxA]
    idxC+=1        
    idxA+=1
while(idxB<len(b)):
    c[idxC]=b[idxB]
    idxC+=1        
    idxB+=1
print(c)    
   
   


a=[22,44,77,99,11,43,67, 87, 12, 32,455,876]
print(a)        #      
for i in range(1,len(a), 2):
    if(a[i]>55):
        print(a[i])



##############################################################
##################################################
#MEKAN ELAZAR


#def IsPalindrob(s):
#    left=0
#    right=len(s)-1
#    while( left<right):
#        if()



#def F(s):
#    q=""
#    for i in range (len(s)):
#        q=s[i]+q
#    return q
### nain ##
#e="wert"
#print(F(e))


#def StrToInt(s):
#    t=0
#    i=0
#    while(i<len(s)): 
#        t=t*10+(ord(s[i])-48)
#        i+=1
#    return t

#### MAIN ###
#n="6234"
#x=StrToInt(n)
#x+=1
#print(x)



#def IsSorted(a):
#    for i in range(1, len(a)):
#        if (a[i-1]>a[i]):
#            return False
#    return True

#    ### MAIN ###
#a=[4,5,2,4,6,7,4,5,8]
#u=IsSorted(a)
#print(u)
#print(IsSorted(a))



#a=[4,6,5,1,2,7,6,9,11,55]
#n=0
#while(n<len(a)-1):
#    b=n+1
#    while(b<len(a)):
#        if(a[n]>a[b]):
#            temp=a[n]
#            a[n]=a[b]
#            a[b]= temp
#        b+=1
#    n+=1
#print(a)





#a=[746,39,4758,387549,876,76]
#for i in range (len(a)):
#    c=0
#    while(a[i]>0):
#        c+=1
#        a[i]=a[i]//10
#    a[i]=c
#print(a)






#a=[11,33,45,47,53,68,69,74]
#b=[11,16,19,22,34,41,51]
#c=[11]*(len(a)+len(b))
#idxA=0
#idxB=0
#idxC=0
#while(idxA<len(a) and idxB<len(b)):
#    if(a[idxA]<b[idxB]):
#        c[idxC]=a[idxA]
#        idxA+=1
#    else:
#        c[idxC]=b[idxB]
#        idxB+=1
#    idxC+=1
#while(idxA<len(a)):
#    c[idxC]=a[idxA]
#    idxC+=1
#    idxA+=1
#while(idxB<len(b)):
#    c[idxC]=b[idxB]
#    idxC+=1
#    idxB+=1
#print(c)



#a=[5456,847,987,98,8]

#print(a)

