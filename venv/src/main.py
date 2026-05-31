from utils.data_utils import getConsolidatedData
from utils.monthly_utils import getMonthlyData, getMonthlyIncome, getMonthlyExpenses

data = getConsolidatedData()

monthlyData = getMonthlyData(allData=data)
print(monthlyData)

monthlyIncome = getMonthlyIncome(monthlyData=monthlyData)
print(monthlyIncome)

monthlyExpenses = getMonthlyExpenses(monthlyData=monthlyData)
print(monthlyExpenses)