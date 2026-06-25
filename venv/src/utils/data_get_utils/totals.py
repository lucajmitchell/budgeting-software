def getBudgetTotal(db):
  return db.fetch('''
    SELECT COALESCE(SUM(Budget), 0)
    FROM Categories
  ''')[0][0]

def getIncome(db, start, end=False):
  if end == False:
    end = start

  return db.fetch('''
    SELECT COALESCE(SUM(Amount), 0)
    FROM Transactions
    LEFT JOIN Aliases ON Transactions.AliasId = Aliases.Id
    WHERE Amount > 0
    AND Date BETWEEN ? AND ?
    AND COALESCE(Aliases.Ignore, 0) != 1
  ''', (start, end))[0][0]

def getSpending(db, start, end=False):
  if end == False:
    end = start

  return db.fetch('''
    SELECT COALESCE(ABS(SUM(Amount)), 0)
    FROM Transactions
    LEFT JOIN Aliases ON Transactions.AliasId = Aliases.Id
    WHERE Amount < 0
    AND Date BETWEEN ? AND ?
    AND COALESCE(Aliases.Ignore, 0) != 1
  ''', (start, end))[0][0]