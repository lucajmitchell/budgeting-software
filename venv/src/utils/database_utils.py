import sqlite3

class Database:
  def __init__(self, path):
    self.path = path

  def _connect(self):
    return sqlite3.connect(self.path)

  def dropTable(self, table):
    conn = self._connect()
    cur = conn.cursor()
    cur.execute(f'DROP TABLE IF EXISTS {table}')
    conn.commit()
    conn.close()

  def createTable(self, name, fields):
    conn = self._connect()
    cur = conn.cursor()
    cur.execute(f'CREATE TABLE IF NOT EXISTS {name} ({', '.join(fields)})')
    conn.commit()
    conn.close()

  def insert(self, table, fields, values):
    fieldsString = ', '.join(fields)
    placeholders = ', '.join(['?'] * len(values))

    conn = self._connect()
    cur = conn.cursor()
    cur.execute(
      f'INSERT INTO {table} ({fieldsString}) VALUES ({placeholders})',
      values  
    )
    conn.commit()
    conn.close()

  def fetch(self, query, args=()):
    conn = self._connect()
    cur = conn.cursor()
    cur.execute(query, args)
    result = cur.fetchall()
    conn.close()
    return result

  def execute(self, query, args=()):
    conn = self._connect()
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    conn.close()