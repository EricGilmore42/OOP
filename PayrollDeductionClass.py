class payroll:

    def __init__(self,i_description,i_date,i_amt,i_id):
        self.__description = i_description 
        self.__date = i_date 
        self.__Amt = i_amt 
        self.__empID = i_id  

    def set_description(self,i_description):
        self.__description = i_description

    def set_date(self,i_date):
        self.__date = i_date 

    def set_amt(self,i_amt):
        self.__Amt = i_amt

    def set_id(self,i_id):
        self.__empID = i_id 

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_amt(self):
        return self.__Amt

    def get_empID(self):
        return self.__empID    