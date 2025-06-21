def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a=int(input("enter number a "))    
b=int(input("enter number b "))  
c=int(input("enter number c "))      

print(f"greatest amobg three number is {greatest(a,b,c)}")