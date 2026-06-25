from .time import *
from .totals import *

def getIdealSpending(db, dates):
  return [(getBudgetTotal(db) / len(dates)) * dayNum for dayNum in dates]

def getActualSpending(db, year, month, dates):
  spending = []
  cumulativeSpending = 0
  for day in dates:
    currentDate = date(year, month, day).isoformat()
    cumulativeSpending += getSpending(db, currentDate)
    spending.append(cumulativeSpending)
  return spending

def getGraphData(db, year, month):
  dates = getDatesList(year, month)
  budget = getIdealSpending(db, dates)
  spending = getActualSpending(db, year, month, dates)
  return {
    'dates': dates,
    'budget': budget,
    'spending': spending
  }