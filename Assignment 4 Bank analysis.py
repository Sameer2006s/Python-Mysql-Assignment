import numpy as np
import pandas as pd

# Bank transaction data
transactions = np.array([
    [5000, 2000, 3000],
    [8000, 1500, 4000],
    [3000, 1000, 2500],
    [10000, 3000, 5000],
    [7000, 2500, 3500]
])


# 1. Total deposit amount
total_deposit = np.sum(transactions[:, 0])

print("Total deposit amount:")
print(total_deposit)


# 2. Total withdrawal amount
total_withdrawal = np.sum(transactions[:, 1])

print("\nTotal withdrawal amount:")
print(total_withdrawal)


# 3. Total investment amount
total_investment = np.sum(transactions[:, 2])

print("\nTotal investment amount:")
print(total_investment)


# 4. Net balance = Deposit - Withdrawal
net_balance = transactions[:, 0] - transactions[:, 1]

print("\nNet balance of each customer:")
print(net_balance)


# 5. Customer with highest deposit
highest_deposit = np.argmax(transactions[:, 0])

print("\nCustomer with highest deposit:")
print("Customer", highest_deposit + 1)
print("Deposit:", transactions[highest_deposit, 0])


# 6. Customer with highest withdrawal
highest_withdrawal = np.argmax(transactions[:, 1])

print("\nCustomer with highest withdrawal:")
print("Customer", highest_withdrawal + 1)
print("Withdrawal:", transactions[highest_withdrawal, 1])


# 7. Customers whose net balance is greater than 4000
above_4000 = np.where(net_balance > 4000)

print("\nCustomers with net balance greater than 4000:")
print(above_4000[0] + 1)


# 8. Average deposit
average_deposit = np.mean(transactions[:, 0])

print("\nAverage deposit:")
print(average_deposit)


# 9. Standard deviation of deposits
deposit_std = np.std(transactions[:, 0])

print("\nStandard deviation of deposits:")
print(deposit_std)


# 10. Classify customers based on net balance
status = np.where(
    net_balance >= 7000,
    "High",
    np.where(net_balance >= 4000, "Medium", "Low")
)

print("\nCustomer classification:")
print(status)


# 11. Convert final data into Pandas DataFrame
df = pd.DataFrame(
    transactions,
    columns=["Deposit", "Withdrawal", "Investment"]
)

df["Net Balance"] = net_balance
df["Status"] = status

print("\nFinal DataFrame:")
print(df)