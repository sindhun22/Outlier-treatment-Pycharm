import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# loading data
credit_data = pd.read_excel(r"C:\Users\Sindhu\Desktop\Codesrdata\Python class\credit_data.xls")
print(credit_data.head())

# Missing values
print(credit_data.isnull().any())
print(credit_data.isnull().sum())

credit_data['MonthlyIncome'] = credit_data['MonthlyIncome'].fillna(round(credit_data['MonthlyIncome'].mean()))
credit_data['NumberOfDependents'] = credit_data['NumberOfDependents'].fillna(round(credit_data['NumberOfDependents'].mean()))

print(credit_data.isnull().any())

# Outlier Treatment (Using Boxplots to check for outliers)

plt.figure(figsize=(22,7))
sns.boxplot(data=credit_data)
plt.show()

# For MonthlyIncome
q1 = credit_data["MonthlyIncome"].quantile(.25)
q3 = credit_data["MonthlyIncome"].quantile(.75)

print(q3-q1)

lb = q1-(q3-q1)*1.5
print(lb)

ub = q3+(q3-q1)*1.5
print(ub)

credit_data["MonthlyIncome"] = np.where(credit_data["MonthlyIncome"] < lb, lb, credit_data["MonthlyIncome"])
credit_data["MonthlyIncome"] = np.where(credit_data["MonthlyIncome"] > ub, ub, credit_data["MonthlyIncome"])

# Check outlier after Treatment

plt.figure(figsize = (20,5))
sns.boxplot(data = credit_data["MonthlyIncome"])
plt.show()

# for DebtRatio

q1 = credit_data["DebtRatio"].quantile(.25)
q3 = credit_data["DebtRatio"].quantile(.75)

print(q3-q1)

lb = q1-(q3-q1)*1.5
print(lb)

ub = q3+(q3-q1)*1.5
print(ub)

credit_data["DebtRatio"] = np.where(credit_data["DebtRatio"] < lb, lb, credit_data["DebtRatio"])
credit_data["DebtRatio"] = np.where(credit_data["DebtRatio"] > ub, ub, credit_data["DebtRatio"])


plt.figure(figsize = (20,5))
sns.boxplot(data = credit_data["DebtRatio"])
plt.show()

plt.figure(figsize=(22,7))
sns.boxplot(data=credit_data)
plt.show()