from config import *
from utils import Data

obj = Data(file='04_2026.csv')
df = obj.getDf()
print(df)