marks = {
    "harry" : 50 ,
    "tanu" : 29 ,
    "john" : 45 ,
    "alice" : 38 ,
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update( { "harry" : 99 , "reena" : 57 })
print(marks)

print(marks.get("Hemant"))    # returs none
#  print(marks.get["harry"])      #returns error 
