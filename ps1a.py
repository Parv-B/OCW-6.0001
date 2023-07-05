import math

#retrieve input
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

#initialize state vars
portion_down_payment = 0.25*total_cost
current_savings = 0.0
r = 0.04
months = 0

while(current_savings <= portion_down_payment):
    current_savings += (current_savings * r / 12) + (portion_saved * annual_salary/12)
    months += 1

#output
print("Number of months:",months)