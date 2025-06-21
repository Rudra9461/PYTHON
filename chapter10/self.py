class Employee:
    language = "Python" 
    salary = 1200000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
      

    @staticmethod 
    def  greet():
        print("good  morning")
       

harry = Employee()
harry.getinfo()        
harry.greet()