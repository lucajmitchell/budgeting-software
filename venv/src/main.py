from utils.database_utils import Database
from utils.data_utils import fillDatabase
from utils.get_utils import (
  getTransactionsDuring,
  getIncomeDuring,
  getExpensesDuring,

  getCategories,
  getIncomeByCategoryDuring,
  getExpensesByCategoryDuring,

  getCounterparties,
  getIncomeByCounterpartyDuring,
  getExpensesByCounterpartyDuring,
)

# Setup database
db = Database()
db.dropTables(['Transactions'])
db.createTable('Transactions', ['ID INTEGER PRIMARY KEY', 'Date', 'Counterparty', 'Amount', 'Category'])
fillDatabase(db)

# Display data
periods = [
  ['2026-04-01', '2026-04-30'],
  ['2026-05-01', '2026-05-31']
]
categories = getCategories(db)
counterparties = getCounterparties(db)

for period in periods:
  start = period[0]
  end = period[1]

  print(f'\n{start} > {end}')

  print('\n=== SUMMARY ===')
  print(f'Income: {getIncomeDuring(db, start, end)}')
  print(f'Expenses: {getExpensesDuring(db, start, end)}')

  print('\n=== INCOME (CATEGORIES) ===')
  for category in categories:
    category = category[0]
    print(f'{category:<20} {getIncomeByCategoryDuring(db, category, start, end)}')
  
  print('\n=== EXPENSES (CATEGORIES) ===')
  for category in categories:
    category = category[0]
    print(f'{category:<20} {getExpensesByCategoryDuring(db, category, start, end)}')
  
  print('\n=== INCOME (CONTERPARTIES) ===')
  for counterparty in counterparties:
    counterparty = counterparty[0]
    print(f'{counterparty:<20} {getIncomeByCounterpartyDuring(db, counterparty, start, end)}')

  print('\n=== EXPENSES (CONTERPARTIES) ===')
  for counterparty in counterparties:
    counterparty = counterparty[0]
    print(f'{counterparty:<20} {getExpensesByCounterpartyDuring(db, counterparty, start, end)}')

  print('\n=== ALL TRANSACTIONS ===')
  print(f'{"-"*10}-+-{"-"*20}-+-{"-"*20}-+-{"-"*20}-+-{"-"*20}')
  for transaction in getTransactionsDuring(db, start, end):
    print(f'{transaction[0]:<10} | {transaction[1]:<20} | {transaction[2]:<20} | {transaction[3]:<20} | {transaction[4]:<20}')
    print(f'{"-"*10}-+-{"-"*20}-+-{"-"*20}-+-{"-"*20}-+-{"-"*20}')
