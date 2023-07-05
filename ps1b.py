import math

#retrieve input
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual raise, as a decimal: "))

#initialize state vars
portion_down_payment = 0.25*total_cost
current_savings = 0.0
r = 0.04
months = 0
monthly_sal = annual_salary/12

while(current_savings <= portion_down_payment):
    current_savings += (current_savings * r / 12) + (portion_saved * monthly_sal)
    months += 1
    if (months % 6 == 0):
        monthly_sal *= 1 + semi_annual_raise


#output
print("Number of months:",months)