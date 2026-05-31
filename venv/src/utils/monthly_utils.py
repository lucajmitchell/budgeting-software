import pandas as pd

def getFormattedDate(date):
  '''Takes date in form DD/MM/YYY and returns it in the form MM_YYYY'''

  # Split date at every instance of '/'
  split_date = date.split('/')

  # Assemble date in format MM_YYYY
  month = split_date[1]
  year = split_date[2]
  formatted_date = f'{month}_{year}'

  return formatted_date

def getMonthlyData(allData):
  '''Returns a dict where each key holds transaction records for all transactions made that month'''

  monthlyData = {}

  # Convert DataFrame to records form
  records = allData.to_dict(orient='records')

  # Assigns record to a key based on date
  for record in records:
    formatted_date = getFormattedDate(record['Date'])
    if formatted_date in monthlyData:
      monthlyData[formatted_date].append(record)
    else:
      monthlyData[formatted_date] = [record]

  return monthlyData