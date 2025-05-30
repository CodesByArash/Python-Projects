from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_data():
        """ implement in child class """

class PersonSingleton(IPerson):
    __instance = None
    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name",0)
        return PersonSingleton.__instance
    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("singleton cannot be instantiated more than once")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}")
        print(f"Age: {PersonSingleton.__instance.age}")

