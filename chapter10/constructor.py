class Employee:
    language = "Python" 
    salary = 1200000
    
   # dunder method in python are automatically called and are called as the objec t is called   
    def __init__(self , name , salary , language):
        self.name = name 
        self.salary = salary
        self.language = language
        print("I am creating an object")
    

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
      

    @staticmethod 
    def  greet():
        print("good  morning")
       

harry = Employee("harry" , 13000000 , "JavaScript")
# harry.name = "Harry"
print(harry.name ,harry.salary , harry.language)