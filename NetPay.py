import EmployeeClass as e 
import PayrollDeductionClass as p

def main(): 
    name = 'Jimmy Smith'
    i_ID = 58475
    department = 'Information Systems'
    title = 'Developer'
    salary = 6800.00

    emp = e.Employee(name,i_ID,department,title,salary)
    paytable = []
    paytable.append(p.payroll('food court','8/14/2022',22.50,39119))
    paytable.append(p.payroll('gift contribution','8/12/2022',25.00,58475))
    paytable.append(p.payroll('food court','8/17/2022',15.25,21547))
    paytable.append(p.payroll('vending machine','8/22/2022',3.00,58475))
    paytable.append(p.payroll('vending machine','8/22/2022',2.75,58475))
       
    netpay = emp.get_salary()
    
    for record in paytable:
        if record.get_empID() == emp.get_id():
            netpay = netpay - record.get_amt()


    print('*** Employee Pay ***')
    print('Name: ',emp.get_name())
    print('ID Number: ',emp.get_id())
    print('Department: ',emp.get_department())
    print('Gross Pay: ',emp.get_salary())
    print('Net Pay: ','$'+str(format(netpay,',.2f')))
main()