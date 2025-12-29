# Name: OSUNDIJI BENEDICT
# Matric No: BU24SEN1070
# Department: SOFTWARE ENGINEERING

print("TAX COLLECTOR ")
print("0 - Single")
print("1 - Married Filing Jointly")
print("2 - Married Filing Separately")
print("3 - Head of Household")

status = int(input("Enter filing status (0-3): "))
income = float(input("Enter taxable income: $"))

# Tax brackets: [upper limit, rate] for each status
BRACKETS = [
    [8350, 33950, 82250, 171550, 372950, float('inf')],      # Single
    [16700, 67900, 137050, 208850, 372950, float('inf')],    # Joint
    [8350, 33950, 68525, 104425, 186475, float('inf')],      # Separate
    [11950, 45500, 117450, 190200, 372950, float('inf')]     # Head of Household
]

RATES = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]  # Same for all statuses

if not 0 <= status <= 3:
    print("Invalid status!")
else:
    tax = 0.0
    prev = 0.0
    limits = BRACKETS[status]
    
    for i in range(len(limits)):
        limit = limits[i]
        rate = RATES[i]
        
        if income <= prev:
            break
        if income < limit:
            tax += (income - prev) * rate
            break
        else:
            tax += (limit - prev) * rate
            prev = limit
    
    print(f"Your 2009 federal income tax is: ${tax:,.2f}")