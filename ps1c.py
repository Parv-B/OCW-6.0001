import pdb

def calculate_savings(portion_saved, monthly_salary, semi_annual_raise, months):
    current_savings = 0 
    for i in range(1,months+1):
        current_savings += (current_savings * 0.04 / 12) + (portion_saved * monthly_salary)
        if (i % 6 == 0):
            monthly_salary *= 1 + semi_annual_raise
    return current_savings

#retrieve input
annual_salary = int(input("Enter the starting salary:  "))

#given information
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000

down_payment = total_cost*portion_down_payment

#bounds for binary search
high = 10000
low = 0
portion_saved = 5000

#state vars
current_savings = 0
steps = 0
months = 36
flag = True

while abs(current_savings - down_payment) > 100:
    steps += 1
    # print(portion_saved)
    current_savings = 0
    mon_sal = annual_salary/12
    months = 36
    current_savings = calculate_savings(portion_saved/10000, mon_sal, semi_annual_raise, months)
    # pdb.set_trace()
    pre_saved = portion_saved
    if (current_savings < down_payment):
        low = portion_saved
    else:
        high = portion_saved

    portion_saved = (high + low) // 2

    if pre_saved == portion_saved:
        flag == False
        break

if (flag):
    print("Best Savings Rate:", portion_saved/10000)
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to pay the down payment in three years.")