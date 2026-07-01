from .time import *

def getCategories(db):
  categoriesList = db.fetch('''
    SELECT Id, Name
    FROM Categories
  ''')
  categoriesList.append((None, 'Uncategorised'))
  return categoriesList

def getFilterAndParamsFor(categoryId, year, month):
  start, end = getMonthBounds(year, month)

  if categoryId is None:
    categoryFilter = '''
      Aliases.Id IS NULL
    '''
    params = (start, end)

  else:
    categoryFilter = '''
      Aliases.CategoryId = ?
      AND Aliases.Ignore = 0
    '''
    params = (categoryId, start, end)

  return categoryFilter, params

def getIncomeAndSpendingFor(categoryId, db, year, month):
  categoryFilter, params = getFilterAndParamsFor(categoryId, year, month)

  income, spending = db.fetch(f'''
    SELECT
      COALESCE(SUM(
        CASE
          WHEN Transactions.Amount > 0
          THEN Transactions.Amount
          ELSE 0
        END
      ), 0),
      COALESCE(SUM(
        CASE
          WHEN Transactions.Amount < 0
          THEN -Transactions.Amount
          ELSE 0
        END
      ), 0)
    FROM Transactions
    LEFT JOIN Aliases ON Transactions.AliasId = Aliases.Id
    WHERE {categoryFilter}
    AND Transactions.Date BETWEEN ? AND ?
  ''', params)[0]

  return income, spending

def getTransactionsFor(categoryId, db, year, month):
  categoryFilter, params = getFilterAndParamsFor(categoryId, year, month)

  transactions = db.fetch(f'''
    SELECT
      CASE
        WHEN Aliases.Id IS NULL
        THEN Transactions.Counterparty
        ELSE Aliases.Alias
      END,
      SUM(
        CASE
          WHEN Transactions.Amount > 0
          THEN Transactions.Amount
          ELSE 0
        END
      ),
      SUM(
        CASE
          WHEN Transactions.Amount < 0
          THEN -Transactions.Amount
          ELSE 0
        END
      )
    FROM Transactions
    LEFT JOIN Aliases ON Transactions.AliasId = Aliases.Id
    WHERE {categoryFilter}
    AND Transactions.Date BETWEEN ? AND ?
    GROUP BY
      CASE
        WHEN Aliases.Id IS NULL
        THEN Transactions.Counterparty
        ELSE Aliases.Alias
      END
  ''', params)

  return transactions

def getCategoryTransactions(db, year, month):
    categoryData = []

    categories = getCategories(db)
    for categoryId, category in categories:

      income, spending = getIncomeAndSpendingFor(categoryId, db, year, month)
      transactions = getTransactionsFor(categoryId, db, year, month)

      categoryData.append({
        'category': category,
        'income': income,
        'spending': spending,
        'transactions': [{
            'counterparty': transaction[0],
            'income': transaction[1],
            'spending': transaction[2]
        } for transaction in transactions]
      })

    categoryData.sort(key=lambda x: x['spending'], reverse=True)
    return categoryData