def annual_net_income(gross_salary):
    # complete your function implementation here...
    if gross_salary >= 45000:
        tax_rate = 0.5
    elif gross_salary >= 30000 and gross_salary < 45000:
        tax_rate = 0.3
    elif gross_salary < 30000:
        tax_rate = 0.15
    
    net_salary = gross_salary - (gross_salary * tax_rate)

    return net_salary

print(annual_net_income(20000))