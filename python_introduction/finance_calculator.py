# finance_calculator.py

# Prompt user for input
monthly_income = int(input("Enter your monthly income: "))
total_expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - total_expenses

# Projected savings after 1 year with 5% interest
projection = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output results
print("Your monthly savings is:", monthly_savings)
print("Your projected annual savings with 5% interest is:", projection)
