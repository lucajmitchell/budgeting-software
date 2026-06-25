from .time import *

def getCategorisedSpending(db, start, end):
  return db.fetch('''
    SELECT
      Categories.Name,
      COALESCE(ABS(SUM(
        CASE
          WHEN Transactions.Amount < 0
          THEN Transactions.Amount
        END
      )), 0) AS spending,
      Categories.Budget
    FROM Categories
    LEFT JOIN Aliases ON Aliases.CategoryId = Categories.Id AND Aliases.Ignore = 0
    LEFT JOIN Transactions ON Transactions.AliasId = Aliases.Id AND Transactions.Date BETWEEN ? AND ?
    GROUP BY Categories.Id
  ''', (start, end))

def getUncategorisedSpendingAmount(db, start, end):
  return db.fetch('''
    SELECT COALESCE(ABS(SUM(Amount)), 0)
    FROM Transactions
    WHERE AliasId IS NULL
    AND Amount < 0
    AND Date BETWEEN ? AND ?
  ''', (start, end))[0][0]

def budgetRecord(category, spending, budget):
  return {
    'category': category,
    'spending': spending,
    'budget': budget
  }

def getBudget(db, year, month):
  budgetData = []

  # Get data
  start, end = getMonthBounds(year, month)
  categorisedSpending = getCategorisedSpending(db, start, end)
  uncategorisedSpendingAmount = getUncategorisedSpendingAmount(db, start, end)

  # Add data to list
  for category, spending, budget in categorisedSpending:
    budgetData.append(budgetRecord(category, spending, budget))
  budgetData.append(budgetRecord('Uncategorised', uncategorisedSpendingAmount, 0))

  # Return data sorted by spending (greatest spend first)
  budgetData.sort(key=lambda x: x['spending'], reverse=True)
  return budgetData