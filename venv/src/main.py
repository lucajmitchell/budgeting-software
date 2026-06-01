from utils.data_utils import getConsolidatedData
from utils.monthly_utils import (
  getMonthlyData,
  getMonthlyIncome,
  getMonthlyExpenses,
  getMonthlyIncomeByPayee,
  getMonthlyExpensesByPayee,
  getMonthlyIncomeByCategory,
  getMonthlyExpensesByCategory,
  )
from misc.table import printTable

data = getConsolidatedData()
monthlyData = getMonthlyData(allData=data)
monthlyIncome = getMonthlyIncome(monthlyData=monthlyData)
monthlyExpenses = getMonthlyExpenses(monthlyData=monthlyData)
monthlyIncomeByPayee = getMonthlyIncomeByPayee(monthlyData=monthlyData)
monthlyExpensesByPayee = getMonthlyExpensesByPayee(monthlyData=monthlyData)
monthlyIncomeByCategory = getMonthlyIncomeByCategory(monthlyData=monthlyData)
monthlyExpensesByCategory = getMonthlyExpensesByCategory(monthlyData=monthlyData)

months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMEBR', 'DECEMBER']
for month in monthlyData.keys():
  income = monthlyIncome[month]
  expenses = monthlyExpenses[month]
  transactions = monthlyData[month]
  incomeByPayee = monthlyIncomeByPayee[month]
  expensesByPayee = monthlyExpensesByPayee[month]
  incomeByCategory = monthlyIncomeByCategory[month]
  expensesByCategory = monthlyExpensesByCategory[month]

  print()
  print('==============================')
  print(f'{months[int(month.split('_')[0])-1]} {month.split('_')[1]}')
  print('==============================')
  print()
  print(f'INCOME:    £{round(income, 2)}')
  print(f'EXPENSES:  £{round(expenses, 2)}')
  print()
  print('INCOME BY CATEGORY:')
  for key, value in incomeByCategory.items():
    print(f'{key:<30}£{round(value, 2):<10}')
  print()
  print('EXPENSES BY CATEGORY:')
  for key, value in expensesByCategory.items():
    print(f'{key:<30}£{round(value, 2):<10}')
  print()
  print('INCOME BY PAYEE:')
  for key, value in incomeByPayee.items():
    print(f'{key:<30}£{round(value, 2):<10}')
  print()
  print('EXPENSES BY PAYEE:')
  for key, value in expensesByPayee.items():
    print(f'{key:<30}£{round(value, 2):<10}')
  print()
  print('ALL TRANSACTIONS:')
  printTable(transactions)