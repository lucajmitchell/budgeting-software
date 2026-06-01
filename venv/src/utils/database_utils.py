import sqlite3

class Database:
  def __init__(self):
    self.connection = sqlite3.connect('venv/src/database.db')
    self.cursor = self.connection.cursor()

  def dropTables(self, tables):
    tablesString = ', '.join(tables)
    self.cursor.execute(f'DROP TABLE IF EXISTS {tablesString}')

  def createTable(self, name, fields):
    fieldsString = ', '.join(fields)
    self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {name}({fieldsString})')

  def insert(self, table, fields, values):
    fieldsString = ', '.join(fields)
    valuesString = ', '.join(values)
    self.cursor.execute(f'INSERT INTO {table} ({fieldsString}) VALUES ({valuesString})')
    self.connection.commit()

  def fetch(self, query, args):
    response = self.cursor.execute(query, args)
    return response.fetchall()
