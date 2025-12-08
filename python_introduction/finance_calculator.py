# Prompt for financial details and compute savings projection
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Helper to format money without unnecessary decimals
def _fmt(amount):
    if amount == int(amount):
        return f"${int(amount)}"
    return f"${amount:.2f}"

print(f"Your monthly savings are {_fmt(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: {_fmt(projected_savings)}")
