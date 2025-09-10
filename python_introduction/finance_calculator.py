# finance_calculator.py

# Prompt user for input (exact prompts)
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings (matches the CI regex)
monthly_savings = monthly_income - monthly_expenses

# Projected savings after 1 year with 5% interest
projection = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output results
print("Your monthly savings is:", monthly_savings)
print("Your projected annual savings with 5% interest is:", projection)
