


a=[325,7842,131,9]
print(a)
i=0
while(i<len(a)):
    if(a[i]%2==1):
        a[i]+=1
    i+=1      
print(a)


a=[4,5,8,7,9,2]
#print(a)
i=0
s=0
while(i<len(a)):
    if(a[i]%2==0):
        s=s+a[i]
    i+=1
print(s)



m=[3245,123,98,4587,3,99]
i=0
while(i<len(m)):
    e=0
    while(m[i]>0):
        e=e+m[i]%10
        m[i]=m[i]//10
    m[i]=e
    i+=1
print(m)



m=[324,123,98,4587,3,99]
print(m)
i=0
while(i<len(m)):
    while(m[i]>9):
        m[i]=m[i]//10
    i+=1
print(m)




m=[324,123,98,4587,3,99]
i=0
while(i<len(m)):
    while(m[i]>99):
        m[i]=m[i]//10
    i+=1
print(m)




m=[324,123,98,4587,3,99]
i=0
while(i<len(m)):
    x=int(input("enter a number : "))
    if((x-10)>m[i]  or (x+10)<m[i]):
        m[i]=x
    i+=1
print(m)


m=[230,65,345,98,87,2,8]
i=0
while(i<len(m)):
    x=int(input("enter a number":))
    if(m[i]>(x+10) or m[i]<(x-10)):
        m[i]=x
    i+=1
print(m)




m=[324,123,98,4587,3,99]
i=1
while(i<len(m)):
    print(m[i-1]-m[i],end=" ")
    i+=1
print("hafsaka")




w="boker tov"
print(w)
i=0
while(i<len(w)):
    print(w[i], ord(w[i]))
    i+=1








#  boker tov yosef balas
s=input("enter a message :")
i=0
while(i<len(s)):
    if(s[i]!=' '):
        print(s[i], end="")
    else:
        print()
    i+=1
print("sof")



s=input("enter a message :")
i=0
c=0
while(i<len(s)):
    if(ord(s[i])>=ord('A') and \
        ord(s[i])<=ord('Z')):
        c+=1
    i+=1
print(c)




s=input("enter a message :")
i=0
c=0
while(i<len(s)):
    if(ord(s[i])>=ord('A') and \
        ord(s[i])<=ord('Z')  or (ord(s[i])>=ord('a') \
       and ord(s[i])<=ord('z'))):
        c+=1
    i+=1
print(c)


# boker tov yosef balas
s=input("enter a message :")
i=0
c=0
while(i<len(s)):
    if(ord(s[i])>=ord('A') and \
        ord(s[i])<=ord('Z')):
        c+=1
    if(ord(s[i])>=ord('a') and \
        ord(s[i])<=ord('z')):
        c+=1
    i+=1
print(c)
print(len(s)-c)