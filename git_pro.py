class Person:
    name = ""
    age = 0

    def __init__(self) -> None:
        self.name = ""
        self.age = 0
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_name(self,name):
        self.name = name
    
    def set_age(self,age):
        self.age = age
    
    def __str__(self) -> str:
        print(self.name,self.age)
    

        

def hello():
    return "Hello dev!"
