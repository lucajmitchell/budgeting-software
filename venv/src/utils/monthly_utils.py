import pandas as pd

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