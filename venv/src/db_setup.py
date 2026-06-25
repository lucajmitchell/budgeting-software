from utils.data_create_utils import (
  createAlias,
  createCategory,
)

def autoAlias(db, contains, aliasId):
  db.execute('''
    UPDATE Transactions
    SET AliasId = ?
    WHERE Counterparty like '%' || ? || '%'
  ''', (aliasId, contains))

def setup(db):

  createCategory(db, 'Miscellaneous', 100)
  createCategory(db, 'Shopping', 100)
  createCategory(db, 'Food', 100)
  createCategory(db, 'Pub', 100)

  # 1
  createAlias(db, 'Savings', None, True)
  autoAlias(db, '41647466', 1)

  # 2
  createAlias(db, 'Corinium Partnership', None, False)
  autoAlias(db, 'Corinium Par', 2)

  # 3
  createAlias(db, 'Vinted', 2, False)
  autoAlias(db, 'Vinted', 3)

  # 4
  createAlias(db, 'Anna', None, False)
  autoAlias(db, 'Anna Ayres', 4)

  # 5
  createAlias(db, 'Tesco', 3, False)
  autoAlias(db, 'TESCO', 5)

  # 6
  createAlias(db, 'Spoons', 4, False)
  autoAlias(db, 'WETHERSPOON', 6)
