class Employee: 

    def __init__(self, i_name, i_ID, i_department, i_job, i_salary):
        self.__name = i_name
        self.__id = i_ID
        self.__department = i_department
        self.__job = i_job
        self.__salary = i_salary

    def set_name(self, i_name):
        self.__name = i_name

    def set_id(self,i_ID):
        self.__id = i_ID 
    
    def set_department(self,i_department):
        self.__department = i_department

    def set_job(self,i_job):
        self.__job = i_job
    
    def set_salary(self,i_salary):
        self.__salary = i_salary

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def get_job(self):
        return self.__job
    
    def get_salary(self):
        return self.__salary
