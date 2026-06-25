def createAlias(db, alias, categoryId, ignore=False):
  if categoryId == None:
    categoryId = 1

  db.insert(
    table='Aliases',
    fields=['Alias', 'CategoryId', 'Ignore'],
    values=(alias, categoryId, ignore)
  )

def createCategory(db, name, budget):
  db.insert(
    table='Categories',
    fields=['Name', 'Budget'],
    values=(name, budget)
  )
