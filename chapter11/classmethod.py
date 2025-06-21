# class method is a method to dierectly acces the class 

class Employee:
    a=1

    @classmethod
    def show(clf):
        print(f"The class attribute od a is {clf.a}")

e =Employee()
e.a =45

e.show()

# if we want to show the attributes of class not of instance we use the @classmethod for calling
