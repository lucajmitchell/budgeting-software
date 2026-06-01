from config import DATA_FOLDER, ALIASES, CATEGORIES
import pandas as pd
import os
from utils.database_utils import Database

class Data:
  def __init__(self, file):
    self.src = DATA_FOLDER + file
  
  def getDfFromStatement(self):
    '''Converts a bank statement to a clean DataFrame'''

    # Create dataframe and add column titles
    df = pd.read_csv(filepath_or_buffer=self.src, names=['Date', 'Counterparty', 'Amount'])

    # Convert dates from DD/MM/YYYY to YYYY-MM-DD
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

    # Replace long names with aliases
    df["Counterparty"] = df["Counterparty"].replace(ALIASES, regex=True)

    # Convert amounts to decimal
    df["Amount"] = (
      df["Amount"]
      .astype(str)
      .str.replace(",", "", regex=False)
      .str.strip()
      .astype(float)
    )

    # Add categories
    categoryMap = {
      counterparty: category
      for category, counterparties in CATEGORIES.items()
      for counterparty in counterparties
    }
    df["Category"] = df["Counterparty"].map(categoryMap)

    return df
  
def getConsolidatedData():
  '''Returns a single DataFrame consolidating all data from DATA_FOLDER folder'''

  # Get list of data sources
  dataFiles = os.listdir(DATA_FOLDER)

  # Extract data from files into list of dataframes
  dataframes = []
  for file in dataFiles:
    df = Data(file).getDfFromStatement()
    dataframes.append(df)

  # Consolidate data into a single dataframe
  concat_data = pd.concat(dataframes)

  return concat_data

def fillDatabase(db):
  '''Fills database with cleaned data from DATA_FOLDER folder'''

  # Get data
  df = getConsolidatedData()
  records = df.to_dict(orient='records')

  for transaction in records:

    # Extract transaction information
    date = transaction['Date']
    counterparty = transaction['Counterparty']
    amount = transaction['Amount']
    category = transaction['Category']

    # Create a new record in Transactions table
    # Add quotes around strings so they insert into database correctly
    db.insert(
      table='Transactions',
      fields=['Date', 'Counterparty', 'Amount', 'Category'],
      values=[f'"{date}"', f'"{counterparty}"', f'{amount}', f'"{category}"']
    )
