from .time import *
from .totals import *

def getTransactionsOn(db, date):
  return db.fetch('''
      SELECT
        COALESCE(Aliases.Alias, Transactions.Counterparty),
        SUM(
          CASE WHEN Transactions.Amount > 0
          THEN Transactions.Amount
          ELSE 0 END
        ) AS Income,
        SUM(
          CASE WHEN Transactions.Amount < 0
          THEN -Transactions.Amount
          ELSE 0 END
        ) AS Spending
      FROM Transactions
      LEFT JOIN Aliases
      ON Aliases.Id = Transactions.AliasId
      WHERE Transactions.Date = ?
      AND COALESCE(Aliases.Ignore, 0) != 1
      GROUP BY COALESCE(Aliases.Alias, Transactions.Counterparty)
      ORDER BY Spending DESC
    ''', (date,))

def getDailyTransactions(db, year, month):
  days = []

  dates = getDatesList(year, month)
  for day in dates:
    currentDate = date(year, month, day).isoformat()
    transactions = getTransactionsOn(db, currentDate)
    days.append({
      'date': currentDate,
      'income': getIncome(db, currentDate),
      'spending': getSpending(db, currentDate),
      'transactions': [{
        'counterparty': transaction[0],
        'income': transaction[1],
        'spending': transaction[2]
      } for transaction in transactions]
    })

  return days