#CONSTANTS
BASE_HOURS = 40
OVERTIME_RATE = 1.5
HOLIDAY_RATE = 2.0

def get_requirements():
    print("\nDeveloper: Aliya Gamez")
    print("Payroll Calculator")
    print("\nProgram Requirements:"
          + "\n1. Must use float data type for user input."
          + "\n2. Overtime rate: 1.5 times hourly rate (hours over 40)"
          + "\n3. Holiday rate: 2.0 times hourly rate (all holiday hours)."
          + "\n4. Must format currency with dollar sign, and round to two decimal places."
          + "\n5. Create at least three functions that are called by the program:"
          + "\n\ta. main(): calls at least two other functions."
          + "\n\tb. get_requirements(): displays the program requirements."
          + "\n\tc. calculate_payroll(): calculates an individual one-week paycheck.\n")
    
def calculate_payroll():
    print("Input:")
    hours = float(input("Enter hours worked: "))
    holiday_hours = float(input("Enter holiday hours: "))
    pay_rate = float(input("Enter hourly pay rate: "))
    
    base_pay = BASE_HOURS * pay_rate
    overtime_hours = hours - BASE_HOURS
    
    if hours > BASE_HOURS:
        overtime_pay = overtime_hours * pay_rate * OVERTIME_RATE
        holiday_pay = holiday_hours * pay_rate * HOLIDAY_RATE
        gross_pay = BASE_HOURS * pay_rate + overtime_pay + holiday_pay
        print_pay(base_pay, overtime_pay, holiday_pay, gross_pay)
    else:
        overtime_pay = 0
        holiday_pay = holiday_hours * pay_rate * HOLIDAY_RATE
        gross_pay = hours * pay_rate + holiday_pay
        print_pay(base_pay, overtime_pay, holiday_pay, gross_pay)
        
def print_pay(base_pay, overtime_pay, holiday_pay, gross_pay):
    print("\nOutput:")
    print("{0:<10} ${1:,.2f}".format('Base', base_pay))
    print("{0:<10} ${1:,.2f}".format('Overtime', overtime_pay))
    print("{0:<10} ${1:,.2f}".format('Holiday', holiday_pay))
    print("{0:<10} ${1:,.2f}".format('Gross', gross_pay))
                      
    
    
    