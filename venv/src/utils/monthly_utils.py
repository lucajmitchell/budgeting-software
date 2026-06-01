import pandas as pd
from config import CATEGORIES

def formatDate(date):
  '''Returns date formatted from DD/MM/YYY to MM_YYYY'''

  # Split date at every instance of '/'
  dateSplit = date.split('/')

  # Assemble formatted date
  month = dateSplit[1]
  year = dateSplit[2]
  dateFormatted = f'{month}_{year}'

  return dateFormatted

def getMonthlyData(allData):
  '''Returns dictionary with transaction records organised by month'''

  monthlyData = {}

  # Convert DataFrame to records
  records = allData.to_dict(orient='records')

  # Assigns record to a key based on date
  for record in records:
    dateFormatted = formatDate(record['Date'])
    if dateFormatted in monthlyData:
      monthlyData[dateFormatted].append(record)
    else:
      monthlyData[dateFormatted] = [record]

  return monthlyData

def getMonthlyIncome(monthlyData):
  '''Returns total amount of money paid into account each month'''

  monthlyIncome = {}

  for month in monthlyData.keys():
    transactions = monthlyData[month]
    transactionAmounts = [transaction['Amount'] for transaction in transactions]
    income = sum([amount for amount in transactionAmounts if amount > 0 ])
    monthlyIncome[month] = income

  return monthlyIncome

def getMonthlyExpenses(monthlyData):
  '''Returns total amount of money paid out of account each month'''

  monthlyExpenses = {}

  for month in monthlyData.keys():
    transactions = monthlyData[month]
    transactionAmounts = [transaction['Amount'] for transaction in transactions]
    expenses = sum([amount for amount in transactionAmounts if amount < 0 ])
    monthlyExpenses[month] = abs(expenses)

  return monthlyExpenses

def getMonthlyIncomeByPayee(monthlyData):
  '''Returns dictionary with income from each payee for each month'''

  monthlyIncomeByPayee = {}

  for month in monthlyData.keys():
    income = {}
    transactions = monthlyData[month]

    for transaction in transactions:
      if transaction['Amount'] > 0:
        if transaction['Payee'] in income:
          income[transaction['Payee']] += transaction['Amount']
        else:
          income[transaction['Payee']] = transaction['Amount']

    monthlyIncomeByPayee[month] = income

  return monthlyIncomeByPayee

def getMonthlyExpensesByPayee(monthlyData):
  '''Returns dictionary with expenses for each payee for each month'''

  monthlyExpensesByPayee = {}

  for month in monthlyData.keys():
    expenses = {}
    transactions = monthlyData[month]

    for transaction in transactions:
      if transaction['Amount'] < 0:
        if transaction['Payee'] in expenses:
          expenses[transaction['Payee']] += abs(transaction['Amount'])
        else:
          expenses[transaction['Payee']] = abs(transaction['Amount'])

    monthlyExpensesByPayee[month] = expenses

  return monthlyExpensesByPayee

def getTransactionCategory(payee):
  '''Returns the category the payee belongs to, or "Miscellaneous" if they don't belong to any'''

  for key, value in CATEGORIES.items():
    if payee in value:
      return key

  return 'Miscellaneous'

def getMonthlyIncomeByCategory(monthlyData):
  '''Returns dictionary with income from each category for each month'''
  
  monthlyIncomeByCategory = {}

  for month in monthlyData.keys():
    income = {}
    transactions = monthlyData[month]

    for transaction in transactions:
      category = getTransactionCategory(transaction['Payee'])
      if transaction['Amount'] > 0:
        if category in income:
          income[category] += transaction['Amount']
        else:
          income[category] = transaction['Amount']

    monthlyIncomeByCategory[month] = income
  
  return monthlyIncomeByCategory

def getMonthlyExpensesByCategory(monthlyData):
  '''Returns dictionary with expenses for each category for each month'''
  
  monthlyExpensesByCategory = {}

  for month in monthlyData.keys():
    expenses = {}
    transactions = monthlyData[month]

    for transaction in transactions:
      category = getTransactionCategory(transaction['Payee'])
      if transaction['Amount'] < 0:
        if category in expenses:
          expenses[category] += transaction['Amount']
        else:
          expenses[category] = transaction['Amount']

    monthlyExpensesByCategory[month] = expenses

  return monthlyExpensesByCategory