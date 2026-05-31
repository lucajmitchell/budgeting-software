from utils.data_utils import getConsolidatedData
from utils.monthly_utils import getMonthlyData

data = getConsolidatedData()
monthlyData = getMonthlyData(allData=data)
print(monthlyData)