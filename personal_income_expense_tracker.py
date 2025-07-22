import pandas as pd
import numpy as np
from random import choice, randint, shuffle

# --- Configuration ---
start_date = "2025-01-01"
end_date = "2025-06-30"
num_income = 100
num_expense = 250

# Categories
income_categories = {
    "Salary": ["Monthly Salary", "Bonus", "Commission"],
    "Freelance": ["Design Project", "Writing Gig", "Consulting Work"],
    "Investments": ["Stock Dividends", "Mutual Funds", "Crypto Trading"],
    "Passive Income": ["Rental Income", "Royalties", "Affiliate Earnings"],
    "Other": ["Tax Refund", "Birthday Gift", "Lottery Winnings"]
}

expense_categories = {
    "Housing": ["Rent", "Mortgage", "Insurance", "Maintenance"],
    "Utilities": ["Electricity", "Water", "Internet", "Mobile Recharge"],
    "Food": ["Groceries", "Dining Out", "Coffee", "Zomato Order"],
    "Transport": ["Petrol", "Metro", "Uber", "Car Service"],
    "Shopping": ["Amazon", "Clothing", "Electronics", "Gifts"],
    "Health": ["Doctor", "Medicines", "Gym", "Yoga"],
    "Entertainment": ["Netflix", "Movie", "Concert", "Games"],
    "Education": ["Course", "Books", "Tuition", "Workshop"],
    "Travel": ["Flight", "Hotel", "Tour Guide"],
    "Care": ["Haircut", "Skincare", "Spa"],
    "Debts": ["Credit Card", "Loan EMI", "Student Loan"],
    "Misc": ["Charity", "Magazines", "Bank Fees"]
}

# Utility: Random date generator
def generate_date(start, end):
    return pd.to_datetime(start) + pd.to_timedelta(
        np.random.randint(0, (pd.to_datetime(end) - pd.to_datetime(start)).days), unit='D'
    )

# Income records
income_data = []
for _ in range(num_income):
    cat = choice(list(income_categories.keys()))
    desc = choice(income_categories[cat])
    income_data.append({
        "Date": generate_date(start_date, end_date).strftime("%d-%m-%Y"),
        "Amount": randint(3000, 50000),
        "Type": "Income",
        "Category": cat,
        "Description": desc
    })

# Expense records
expense_data = []
for _ in range(num_expense):
    cat = choice(list(expense_categories.keys()))
    desc = choice(expense_categories[cat])
    expense_data.append({
        "Date": generate_date(start_date, end_date).strftime("%d-%m-%Y"),
        "Amount": randint(100, 20000),
        "Type": "Expense",
        "Category": cat,
        "Description": desc
    })

# Combine and shuffle
raw_data = income_data + expense_data
shuffle(raw_data)

# Introduce imperfect column order (e.g., Description comes before Type)
df = pd.DataFrame(raw_data)[["Date", "Amount", "Description", "Type", "Category"]]

# Save
df.to_csv("raw_data.csv", index=False)
print("✅ raw_data.csv generated with mixed Income & Expense records.")
