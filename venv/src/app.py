from flask import Flask, render_template, request, jsonify
from utils.database_utils import Database
from utils.data_utils import fillTransactions
from utils.api_utils import (
  getPeriods,
)

app = Flask(__name__)

# Setup database
db = Database('venv/src/database.db')
db.dropTable('Transactions')
db.createTable('Transactions', ['Date', 'Counterparty', 'Amount', 'CategoryId'])
db.createTable('Aliases', ['Contains', 'Alias', 'CategoryId'])
db.createTable('Categories', ['Id INTEGER PRIMARY KEY', 'Name', 'Budget'])
fillTransactions(db=db, dataFolder='venv/src/data')

# Render home page (default)
@app.route('/')
def home():
  return render_template('index.html')

# Returns JSON containing the years and months with available data
@app.route('/api/periods')
def api_getPeriods():
  periods = getPeriods(db)
  return jsonify(periods)

if __name__ == '__main__':
   app.run(debug=True)