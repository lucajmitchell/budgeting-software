import sqlite3

class Database:
  def __init__(self, db_path='venv/src/database.db'):
    self.db_path = db_path

  def _connect(self):
    return sqlite3.connect(self.db_path)

  def dropTables(self, tables):
    tablesString = ', '.join(tables)

    conn = self._connect()
    cur = conn.cursor()
    cur.execute(f'DROP TABLE IF EXISTS {tablesString}')
    conn.commit()
    conn.close()

  def createTable(self, name, fields):
    fieldsString = ', '.join(fields)

    conn = self._connect()
    cur = conn.cursor()
    cur.execute(f'CREATE TABLE IF NOT EXISTS {name} ({fieldsString})')
    conn.commit()
    conn.close()

  def insert(self, table, fields, values):
      fieldsString = ', '.join(fields)
      valuesString = ', '.join(values)

      conn = self._connect()
      cur = conn.cursor()
      cur.execute(f'INSERT INTO {table} ({fieldsString}) VALUES ({valuesString})')
      conn.commit()
      conn.close()

  def fetch(self, query, args=()):
      conn = self._connect()
      cur = conn.cursor()
      cur.execute(query, args)
      result = cur.fetchall()
      conn.close()
      return result