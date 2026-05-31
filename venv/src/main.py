from utils.data_utils import getConsolidatedData
from utils.monthly_utils import getMonthlyData, getMonthlyIncome, getMonthlyExpenses
from misc.table import printTable

data = getConsolidatedData()
monthlyData = getMonthlyData(allData=data)
monthlyIncome = getMonthlyIncome(monthlyData=monthlyData)
monthlyExpenses = getMonthlyExpenses(monthlyData=monthlyData)

months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMEBR', 'DECEMBER']
for month in monthlyData.keys():
  income = monthlyIncome[month]
  expenses = monthlyExpenses[month]
  transactions = monthlyData[month]
  print()
  print('==============================')
  print(f'{months[int(month.split('_')[0])]} {month.split('_')[1]}')
  print('==============================')
  print()
  print(f'INCOME:    £{round(income, 2)}')
  print(f'EXPENSES:  £{round(expenses, 2)}')
  print()
  printTable(transactions)