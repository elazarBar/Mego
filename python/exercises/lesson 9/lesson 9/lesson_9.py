def Q3SummerB2021(s1, s2):
    if(len(s1)%len(s2)!=0):
        return False
    a=0
    while(a<len(s1)/len(s2)):
        b=0
        while(b<len(s2)):
            if(s1[a*(len(s2))+b]!=s2[b]):
              return False
            b+=1
        a+=1
    print()
    return True

x = "abc"    
y = "abcabcabc"  
print(Q3SummerB2021(y,x))



#import random
#def Show(a):
#    for r in range(len(a)):
#        for c in range(len(a)):
#            print(a[r][c], end=" ")
#        print()
           
#r=ord('a')
#s=""
#for i in range(30):
#    c=chr(random.randint(97,106))
#    s=s+c
#print(s)

#m= [[0 for x in range(10)] for y in range(10)]
#for i in range(len(s)-1):
#    sh=ord(s[i])-97
#    a=ord(s[i+1])-97
#    m[sh][a]+=1
#rMax=0
#cMax=0
#for r in range(len(m)):
#    for c in range(len(m)):
#        if(m[rMax][cMax]<m[r][c]):
#            rMax=r
#            cMax=c
#print(m[rMax][cMax])
#print(chr(rMax+97), chr(cMax+97))
#Show(m)    

 

#def S1InS2(s1, s2):
#    if(len(s1)>len(s2)):
#        return False
#    for i in range(len(s1)):
#        for k in range(len(s2)):
#            if(s1[i]==s2[k]):
#                break
#        if(s1[i]!=s2[k]):
#            return False
#    return True
#print(S1InS2("cea", "casv"))    
#print(S1InS2("cxea", "abcdef"))          
#print(S1InS2("cjea", "abcdef"))          
#print(S1InS2("cea", "cafehb"))    



#def S1InS2(s1, s2):
#    if(len(s1)>len(s2)):
#        return False
#    i=0
#    while(i<len(s1)):
#        k=0
#        while(k<len(s2)):
#            if(s1[i]==s2[k]):
#                break
#            k+=1
#        if(k==len(s2)):
#            return False
#        i+=1
#    return True
#print(S1InS2("cxea", "abcdef"))          
#print(S1InS2("cea", "bcdef"))
#print(S1InS2("ceav", "cae"))          
           



# #  fcea
# #  abcdef


#def CmpString(s1, s2):
#    l=len(s1)
#    if(len(s1)>len(s2)):
#        l=len(s2)
#    for i in range(l):
#        if(s1[i] != s2[i]):
#          return ord(s1[i]) - ord(s2[i])
#    return len(s1)-len(s2)
   
#names=["khimon", "oos ef", "gad", "yosef", "dan", "gadi"]          
#print(names)
#for niv in range(len(names)-1):
#    for bod in range(niv+1, len(names)):
#        if(CmpString(names[niv], names[bod])<0):
#            temp=names[bod]
#            names[bod]=names[niv]
#            names[niv]=temp
#print(names)          




#def CmpString(s1, s2):
#    l=len(s1)
#    if(len(s1)>len(s2)):
#        l=len(s2)
#    for i in range(l):
#        if(s1[i] != s2[i]):
#            return ord(s1[i]) - ord(s2[i])
#    return len(s1)-len(s2)
   
#print(CmpString("aaa", "bbb"))        
#print(CmpString("ccc", "bbb"))        
#print(CmpString("aaa", "abb"))        
#print(CmpString("axa", "aaaa"))        
#print(CmpString("aaaa", "aaa"))        
#print(CmpString("aaa", "aaaaaaaa"))        
           






#def CmpString(s1, s2):
#    l=len(s1)
#    if(len(s1)>len(s2)):
#        l=len(s2)
#    for i in range(l):
#        if(ord(s1[i]) < ord(s2[i])):
#          return -1
#        else:
#           if(ord(s1[i]) > ord(s2[i])):
#              return 1
#    if(len(s1)==len(s2)):
#        return 0
#    else:
#        return len(s1)-len(s2)   
   

#print(CmpString("aaa", "bbb"))        
#print(CmpString("ccc", "bbb"))        
#print(CmpString("aaa", "abb"))        
#print(CmpString("aaa", "aaaa"))        
#print(CmpString("aaaaa", "aaa"))        
           

#'''
#   reuven      levi        >0
#   levi        reuven      <0
#   levi        levi        ==0
#   levi        levin        <0
#   levin       levi        >0
#   levarov     levi        ==0
#   ran         binyamin

#   levin '/0'       levi '/0'
#'''

#import random
#def Show(a):
#    for r in range(len(a)):
#        for c in range(len(a)):
#            print(a[r][c], end=" ")
#        print()
           
#r=ord('a')
#s=""
#for i in range(100):
#    c=chr(random.randint(97,106))
#    s=s+c
#print(s)
#m=[
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0]
#    ]
##   s = "acfweedfaerfgafa
#for i in range(len(s)-1):
#    sh=ord(s[i])-97
#    a=ord(s[i+1])-97
#    m[sh][a]+=1
#Show(m)    

#################################################################
################################################################
#import random
#def Show(a):
#    for r in range(len(a)):
#        for c in range(len(a)):
#            print(a[r][c], end=" ")
#        print()
           

#s=""
#for i in range(100):
#    c=chr(random.randint(97,106))
#    s=s+c
#print(s)
#m=[
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0]
#    ]
##   s = "acfweedfaerfgafa
#for i in range(len(s)-1):
#    sh=ord(s[i])-97
#    a=ord(s[i+1])-97
#    m[sh][a]+=1
#Show(m)    

#def F(b):
#   r=0
#   for r in range(len(a)):
#        for c in range(len(a[0])):
#            if (r<(b[r][c])):
#                r=(b[r][c])


#def CmpString(s1, s2):
#    l=len(s1)
#    if(len(s1)>len(s2)):
#        l=len(s2)
#    for i in range(l):
#        if(s1[i] != s2[i]):
#           return ord(s1[i]) - ord(s2[i])
#    return len(s1)-len(s2)
   
#names=["shimon", "yosef", "gad", "dan", "gadi"]          
#print(names)

# def CmpString(s1, s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(s1[i] != s2[i]):
#            return ord(s1[i]) - ord(s2[i])
#     return len(s1)-len(s2)
   

# print(CmpString("aaa", "bbb"))        
# print(CmpString("ccc", "bbb"))        
# print(CmpString("aaa", "abb"))        
# print(CmpString("axa", "aaaa"))        
# print(CmpString("aaaa", "aaa"))        
# print(CmpString("aaa", "aaaaaaaa")) 
