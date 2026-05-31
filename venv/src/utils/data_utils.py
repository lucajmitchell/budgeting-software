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
  '''Consolidates all data from files stored in SOURCE_PREFIX folder to a single DataFrame and returns it.'''

  # Get list of all data sources
  data_files = os.listdir(SOURCE_PREFIX)

  # Extract all data from files into a list of dataframes
  dataframes = []
  for file in data_files:
    df = Data(file).getDf()
    dataframes.append(df)

  # Consolidate all data into a single dataframe
  concat_data = pd.concat(dataframes)

  return concat_data