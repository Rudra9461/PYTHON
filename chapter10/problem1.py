class Programmer:
    company = "Microsoft"
    def __init__(self , name , salary , pin):  #hum log kya kya data save krwna cahate hai vo hum self me likhenge 
        self.name =name 
        self.salary = salary 
        self.pin = pin

p = Programmer("harry" , 120000 , 245001)
print(p.name ,p.salary , p.pin , p.company)
r = Programmer("Rohan" , 120000 , 245001)
print(r.name ,r.salary , r.pin , r.company)