try :
    a = int(input("Hey , Enter a number :"))
    print(a)

except ValueError as v:
    print("There is value error")
    print(v)

except Exception as e :
    print(e)    


print("Thank you")    
