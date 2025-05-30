class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self.__age =age
        self.__gender=gender

    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, value):
        self.__name = value 
    
    @staticmethod
    def print_name(self):
        print(self._name)
    
    
person = Person("arash", 28, "male")

print(person._name)