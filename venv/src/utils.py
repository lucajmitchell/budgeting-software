from config import SOURCE_PREPOSITION
import pandas as pd

class Data:
  def __init__(self, file):
    self.src = SOURCE_PREPOSITION + file
  
  def getDf(self):
    df = pd.read_csv(self.src)
    return df