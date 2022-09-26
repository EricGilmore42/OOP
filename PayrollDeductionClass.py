class payroll:

    def __init__(self,i_description,i_date,i_amt,i_id):
        self.__description = i_description 
        self.__date = i_date 
        self.__Amt = i_amt 
        self.__empID = i_id  

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_amt(self):
        return self.__Amt

    def get_empID(self):
        return self.__empID    