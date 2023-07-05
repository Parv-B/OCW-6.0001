#state vars
annual_salary = 120000
semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000
portion_down_payment = 0.25
months = 36

down_payment = total_cost*portion_down_payment

high = 10000
low = 0

current_savings = 0
steps = 0

portion_saved = (high + low) // 2

while abs(current_savings - down_payment) > 100:
    steps += 1
    ann_sal = annual_salary
    current_savings = 0
    mon_sal = annual_salary/12

