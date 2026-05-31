from config import SOURCE_PREFIX, DATA_COLUMN_TITLES, ALIASES
import pandas as pd
import os

class Data:
  def __init__(self, file):
    self.src = SOURCE_PREFIX + file
  
  def getDf(self):
    # Create dataframe and add column titles
    df = pd.read_csv(filepath_or_buffer=self.src, names=DATA_COLUMN_TITLES)

    # Replace long names with aliases
    df["Payee"] = df["Payee"].replace(ALIASES, regex=True)

    return df
  
def getConsolidatedData():
  '''Returns a single DataFrame consolidating all data from SOURCE_PREFIX folder'''

  # Get list of data sources
  dataFiles = os.listdir(SOURCE_PREFIX)

  # Extract data from files into list of dataframes
  dataframes = []
  for file in dataFiles:
    df = Data(file).getDf()
    dataframes.append(df)

  # Consolidate data into a single dataframe
  concat_data = pd.concat(dataframes)

  return concat_data