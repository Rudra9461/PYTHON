# to print dictionary for 4 friends having diffrent languages

d={}
 
name = input("enter the name :")           #if we put same name of friend with diffrent language the update will take place and will update to the last value assinged 
lang = input("enter the language :")
d.update({name : lang})

 
name = input("enter the name :")
lang = input("enter the language :")
d.update({name : lang})

 
name = input("enter the name :")
lang = input("enter the language :")
d.update({name : lang})

 
name = input("enter the name :")
lang = input("enter the language :")
d.update({name : lang})

print(d)