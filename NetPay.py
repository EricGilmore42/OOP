import EmployeeClass as e 
import PayrollDeductionClass as p

def main(): 
    name = input('Enter full name: ')
    i_ID = input('Enter ID number: ')
    department = input('Eneter department name: ')
    title = input('Enter job title: ')
    salary = float(input('Enter monthly salary: '))

    emp = e.Employee(name,i_ID,department,title,salary)
    
    print()
    print('Name ','ID Number ','Department ','Job Title ','Monthly Salary ')
    print(emp.get_name(),' ',emp.get_id(),' ',emp.get_department(),' ',emp.get_job(),' ','$',emp.get_salary())
    print()
    description = input('Enter purchase description: ')
    date = input('Enter date in month/day/year format: ')
    amt = float(input('Enter charge amount: '))
    empID = input('Enter ID number: ')

    pay = p.payroll(description,date,amt,empID)
    
    print()
    print()
    print('Description','Date','Charge','EmployeeID')
    print(pay.get_description(),' ',pay.get_date(),' ',pay.get_amt(),' ',pay.get_empID())
    print()
    print()
    print('*** Employee Pay ***')
    print('Name: ',emp.get_name())
    print('ID Number: ',emp.get_id())
    print('Department: ',emp.get_department())
    print('Gross Pay: ',emp.get_salary())
    print('Net Pay: ',(emp.get_salary()-pay.get_amt()))
main()