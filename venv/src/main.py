from utils.data_utils import getConsolidatedData
from utils.monthly_utils import getMonthlyData, getMonthlyIncome, getMonthlyExpenses, getMonthlyIncomeByPayee, getMonthlyExpensesByPayee
from misc.table import printTable

data = getConsolidatedData()
monthlyData = getMonthlyData(allData=data)
monthlyIncome = getMonthlyIncome(monthlyData=monthlyData)
monthlyExpenses = getMonthlyExpenses(monthlyData=monthlyData)
monthlyIncomeByPayee = getMonthlyIncomeByPayee(monthlyData=monthlyData)
monthlyExpensesByPayee = getMonthlyExpensesByPayee(monthlyData=monthlyData)

months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMEBR', 'DECEMBER']
for month in monthlyData.keys():
  income = monthlyIncome[month]
  expenses = monthlyExpenses[month]
  transactions = monthlyData[month]
  incomeByPayee = monthlyIncomeByPayee[month]
  expensesByPayee = monthlyExpensesByPayee[month]

  print()
  print('==============================')
  print(f'{months[int(month.split('_')[0])-1]} {month.split('_')[1]}')
  print('==============================')
  print()
  print(f'INCOME:    £{round(income, 2)}')
  print(f'EXPENSES:  £{round(expenses, 2)}')
  print()
  print('INCOME BY PAYEE:')
  for key, value in incomeByPayee.items():
    print(f'{key:<20}£{round(value, 2):<10}')
  print()
  print('EXPENSES BY PAYEE:')
  for key, value in expensesByPayee.items():
    print(f'{key:<20}£{round(value, 2):<10}')
  print()
  print('ALL TRANSACTIONS:')
  printTable(transactions)