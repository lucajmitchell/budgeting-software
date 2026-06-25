from datetime import date
import calendar

def getMonthBounds(year, month):
  firstDay = date(year, month, 1)
  lastDayNum = calendar.monthrange(year, month)[1]
  lastDay = date(year, month, lastDayNum)
  return firstDay, lastDay

def getDaysInMonth(year, month):
  return calendar.monthrange(year, month)[1]

def getDatesList(year, month):
  numOfDates = getDaysInMonth(year, month)
  return list(range(1, numOfDates + 1))