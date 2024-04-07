#num=int(input("enter a number : "))
#max=num
#min=num
#while(num<100 or num>999):
#    if(max<num):
#        max=num
#    if(min>num):
#        min=num
#    num=int(input("enter a number : "))
#if(max<num):
#    max=num
#if(min>num):
#    min=num

#print(max, min)    





import random
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m",
        "n","o","p","q","r","s","t","u","v","w","x","y","z"]
hatspan=["a","b","c","d","e","f","g","h","i","j","k","l","m",
        "n","o","p","q","r","s","t","u","v","w","x","y","z"]
swapcount=random.randint(22,66)
for i in range(swapcount):
    idx1=random.randint(0,len(letters)-1)
    idx2=random.randint(0,len(letters)-1)
    ezer=hatspan[idx1]
    hatspan[idx1]=hatspan[idx2]
    hatspan[idx2]=ezer
print(hatspan)

text="bokertov"
newtext=[""]*len(text)
for i in range(len(text)):
    idx= ord(text[i])-ord('a')
    newtext[i]=hatspan[idx]
print(newtext)



'''
['a', 's', 't', 'v', 'd', 'r', 'i', 'x', 'u',
'k', 'h', 'l', 'w', 'n', 'j', 'f', 'm', 'y',
'q', 'g', 'p', 'o', 'b', 'z', 'c', 'e']
['s', 'j', 'h', 'd', 'y', 'g', 'j', 'o']
'''

['n','m','b','t','c','z','q','g','r','j','v','k','o',
  'y','h','l','p','i','u','f','w','s','d','x','a','e']
print()
  

# left=[
#     [2,5,4,6],    
#     [9,3,1,4],    
# ]
# right=[
#     [4,7,9],    
#     [1,2,3],    
#     [9,6,7],    
#     [3,2,3],    
# ]
# m=[
#     [0,0,0],
#     [0,0,0],
#   ]
# for r in range(len(left)):
#     for c in range(len(right[0])):
#         for i in range(len(left[0])):
#             m[r][c]=m[r][c] + left[r][i]*right[i][c]
# print(m[0])            
# print(m[1])  





#'''
#                   4 7 9                    
#                   1 2 3
#2 5 4 6            9 6 7
#9 3 1 4            3 2 3
                   
                   
#67  ?   ?
#?   ?   ?

#   2*4+5*1+4*9+6*3 =   67
#'''


#a=[4,2,8]
#b=[7,3,5,1]
#c=[0]*len(a)
#sumb=0
#for i in range(len(b)):
#    sumb+=b[i]
#for i in range(len(a)):
#    c[i]=a[i]*sumb
#print(c)


 # c[0]=4*7+4*3+4*5+4*1  =   4*(7+3+5+1)
 # c[1]=2*7+2*3+2*5+2*1  =   2*(7+3+5+1)
 # c[2]=8*7+8*3+8*5+8*1  =   8*(7+3+5+1)
 # c=[64,32,128]






#a=[4,2,8]
#b=[7,3,5,1]
#c=[0]*len(a)
#for i in range(len(a)):
#    for k in range(len(b)):
#       c[i]=c[i]+a[i]*b[k]
#print(c)


#c[0]=4*7+4*3+4*5+4*1  =   4*(7+3+5+1)
#c[1]=2*7+2*3+2*5+2*1  =   2*(7+3+5+1)
#c[2]=8*7+8*3+8*5+8*1  =   8*(7+3+5+1)
#c=[64,32,128]


#a=[
#    [1,2,3,4,5],
#    [2,3,4,5,9],
#    [9,8,7,6,5],
#    [8,7,6,5,0],
#    [3,4,5,9,8]
#]
#for c in range(len(a[0])):
#    for r in range(len(a)):
#        print(a[r][c], end=" ")
#    print()
   
#'''
#1 2 9 8 3
#2 3 8 7 4
#3 4 7 6 5
#4 5 6 5 9
#5 9 5 0 8
#'''



#a=[
#    [-4,-6,-1,-2,-9,-60],  
#    [5,6,7,8,9,1],  
#    [7,6,5,4,3,2],  
#]
#for r in range(len(a)):
#    max=a[r][0]
#    print(a[r][0], end=" ")
#    for c in range(1, len(a[r])):
#        print(a[r][c], end=" ")
#        if(max<a[r][c]):
#            max=a[r][c]
#    print("    ", max)

#'''
#-4 -6 -1 -2 -9 -60      -1
#5 6 7 8 9 1      9
#7 6 5 4 3 2      7
#'''









#a=[
#    [4,6,1,2,9,0],  
#    [5,6,7,8,9,1],  
#    [7,6,5,4,3,2],  
#]
#for r in range(len(a)):
#    sum=0
#    for c in range(len(a[r])):
#        print(a[r][c], end=" ")
#        sum=sum+a[r][c]
#    print("    ", sum)

#'''
#4 6 1 2 9 0      22
#5 6 7 8 4 1      36
#7 6 5 4 3 2      27
#'''

#a=[
#    [4,6,1,2,9,0],  
#    [5,6,7,8,9,1],  
#    [7,6,5,4,3,2],  
#]
##a=[[4,6,1,2,9,0],[5,6,7,8,9,1],[7,6,5,4,3,2]]
#for r in range(len(a)):
#    for c in range(len(a[r])):
#        print(a[r][c], end=" ")
#    print()





####################################################################################
################################################################################
#mekan Elazar

#num=int(input("Enter a Number:"))
#a=num
#b=num
#while(num>999 or num<100):
#    if num>a:
#        a=num
#    if num<b:
#        b=num
#    num=int(input("Enter a Number:"))   
#print(a)
#print(b)

#left=[
#    [2,5,4,6],
#    [9,3,1,4],
#    ]
#right=[
#    [4,7,9],
#    [1,2,3],
#    [9,6,7],
#    [3,2,3],
#    ]
#m=[
#    [0,0,0],
#    [0,0,0],
#    ]
#for r in range(len(left)):
#    for c in range(len(right[0])):
#        for i in range(len(left[0])):
#            m[r][c]=m[r][c]+left[r][i]*right[i][c]
#print(m[0])
#print(m[1])


#a=[4,2,8]        ????
#b=[7,3,5,1]
#c=[0]*len(a)
#i=0
#while(i<len(a)):
#    s=0
#    while(s<len(b):
#       c[i]=c[i]+a[i]*b[s]
#       s+=1
#       i+=1
#print(c)    ????


#a=[
#    [4,5,6,7,8,9],
#    [8,4,9,1,0,8],
#    [9,2,5,4,8,6],
#    ]
#for c in range(len(a[0])):
#    for r in range(len(a)):
#        print(a[r][c], end="")
#    print()





#a=[
#    [4,5,6,7,8,9],
#    [8,4,9,1,0,8],
#    [2,2,5,4,8,6],
#    ]
#for r in range(len(a)):
#    max=0
#    for c in range(len(a[r])):
#        print(a[r][c], end="")
#        if (max<a[r][c]):
#            max=a[r][c]
#    print("   ", max)


#a=[
#    [4,5,6,7,8,9],
#    [8,4,9,1,0,8],
#    [9,2,5,4,8,6],
#    ]
#for r in range(len(a)):
#    sum=0
#    for c in range(len(a[r])):
#        print(a[r][c], end="")
#        sum=sum+a[r][c]
#    print("   ", sum)
