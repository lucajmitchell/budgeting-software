def getTransactionsDuring(db, start, end=False):
  '''Returns a list of transactions within the given date range, or on the given date if no end date provided'''

  # Assumes end date is same as start date if no end date provided
  if not end:
    end = start

  # Dates must have times attached to make both sides inclusive
  start += ' 00:00:00'
  end += ' 00:00:00'

  return db.fetch(
    '''
      SELECT * FROM Transactions
      WHERE Date BETWEEN ? AND ?;
    ''', (start, end)
  )

def getIncomeDuring(db, start, end=False):
  '''Retuns income in the given date range, or on the given date if no end date provided'''
  transactions = getTransactionsDuring(db, start, end)
  positiveTransactionAmounts = [t[3] for t in transactions if t[3]>0]
  return sum(positiveTransactionAmounts)

def getExpensesDuring(db, start, end=False):
  '''Retuns expenses in the given date range, or on the given date if no end date provided'''
  transactions = getTransactionsDuring(db, start, end)
  negativeTransactionAmounts = [t[3] for t in transactions if t[3]<0]
  return sum(negativeTransactionAmounts)

def getCategories(db):
  return db.fetch('SELECT DISTINCT Category FROM Transactions', ())

def getIncomeByCategoryDuring(db, category, start, end=False):
  '''Retuns income in the given date range and category, or on the given date if no end date provided'''
  transactions = getTransactionsDuring(db, start, end)
  positiveTransactionAmounts = [t[3] for t in transactions if t[3]>0 and t[4]==category]
  return sum(positiveTransactionAmounts)

def getExpensesByCategoryDuring(db, category, start, end=False):
  '''Retuns expenses in the given date range and category, or on the given date if no end date provided'''
  transactions = getTransactionsDuring(db, start, end)
  negativeTransactionAmounts = [t[3] for t in transactions if t[3]<0 and t[4]==category]
  return sum(negativeTransactionAmounts)

def getCounterparties(db):
  return db.fetch('SELECT DISTINCT Counterparty FROM Transactions', ())
  
def getIncomeByCounterpartyDuring(db, counterparty, start, end=False):
  '''Retuns income in the given date range for the given counterparty, or on the given date if no end date provided'''
  transactions = getTransactionsDuring(db, start, end)
  positiveTransactionAmounts = [t[3] for t in transactions if t[3]>0 and t[2]==counterparty]
  return sum(positiveTransactionAmounts)

def getExpensesByCounterpartyDuring(db, counterparty, start, end=False):
  '''Retuns expenses in the given date range for the given counterparty, or on the given date if no end date provided'''
  transactions = getTransactionsDuring(db, start, end)
  negativeTransactionAmounts = [t[3] for t in transactions if t[3]<0 and t[2]==counterparty]
  return sum(negativeTransactionAmounts)