from abc import ABCMeta, abstractmethod
class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, employees):
        """implement in child class"""
    @staticmethod
    @abstractmethod
    def print_department():
        """implement in child class"""

class Accounting(IDepartment):
    def __init__(self,employees):
        self.employees = employees
    def print_department(self):
        print(f"Accounting Department: {self.employees}")

class Development(IDepartment):
    def __init__(self,employees):
        self.employees = employees
    def print_department(self):
        print(f"Development Department: {self.employees}")
    
class ParentDepartment(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []
    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees
    def print_department(self):
        print("Parent Department")
        print(f"Parent Departmrnt base employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total nunmber of employees:{self.employees}")

