import pandas as pd
import os
  
def statementToDf(path):
  df = pd.read_csv(filepath_or_buffer=path, names=['Date', 'Counterparty', 'Amount'])

  # Convert dates from DD/MM/YYYY to YYYY-MM-DD
  df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

  # Convert amounts to decimal
  df['Amount'] = (
    df['Amount']
    .astype(str)
    .str.replace(',', '')
    .str.strip()
    .astype(float)
  )

  return df
  
def getConsolidatedData(dataFolder):
  dataFiles = os.listdir(dataFolder)
  dataframes = [statementToDf(f'{dataFolder}/{dataFile}') for dataFile in dataFiles]
  consolidatedData = pd.concat(dataframes)
  return consolidatedData

def fillTransactions(db, dataFolder):
  df = getConsolidatedData(dataFolder)
  records = df.to_dict(orient='records')

  for transaction in records:

    # Extract data from record
    date = str(transaction['Date'])[:10]
    counterparty = transaction['Counterparty']
    amount = transaction['Amount']

    # Create new record in transactions
    db.insert(
      table='Transactions',
      fields=['Date', 'Counterparty', 'Amount'],
      values=(date, counterparty, amount)
    )
