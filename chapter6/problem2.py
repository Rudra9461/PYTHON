marks1=int(input("enter 1st marks "))

marks2=int(input("enter 2nd marks "))

marks3=int(input("enter 3rd marks "))

total_percentage = (100)*(marks1 +marks2 +marks3)/300

if(total_percentage>=40):
    print("you are pass" , total_percentage)
else:
    print("you are fail" , total_percentage)    