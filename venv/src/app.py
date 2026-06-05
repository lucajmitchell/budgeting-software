from flask import Flask, render_template, request, jsonify
from utils.database_utils import Database
from utils.data_utils import fillDatabase

app = Flask(__name__)

db = Database()
db.dropTables(['Transactions'])
db.createTable('Transactions', ['ID INTEGER PRIMARY KEY', 'Date', 'Counterparty', 'Amount', 'Category'])
fillDatabase(db)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/api/periods')
def getPeriods():

  # Get years and months in form [('YYYY', 'MM,MM,MM,...'), ...]
  rows = db.fetch('''
    SELECT
      strftime('%Y', Date) AS year,
      GROUP_CONCAT(DISTINCT CAST(strftime('%m', Date) AS INTEGER)) AS months
    FROM Transactions
    GROUP BY year
    ORDER BY year
  ''', ())

  # Format to [{ 'year': YYYY, 'months': [MM, MM, MM, ...] }, ...]
  periods = []
  for year, months in rows:
    yearFormatted = int(year)
    monthsFormatted = [int(month) for month in months.split(',')]
    monthsFormatted.sort()

    periods.append({
      'year': yearFormatted,
      'months': monthsFormatted
    })

  return jsonify(periods)

if __name__ == '__main__':
   app.run(debug=True)