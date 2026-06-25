from flask import Flask, render_template, request, jsonify
from utils.database_utils import Database
from utils.data_load_utils import fillTransactions
import utils.data_get_utils as getUtils
from db_setup import setup

app = Flask(__name__)

# Setup database
db = Database('venv/src/database.db')
db.dropTable('Transactions')
db.dropTable('Aliases')
db.dropTable('Categories')

# Transactions may have an alias
# Multiple transactions can have the same alias
db.createTable(
  name='Transactions',
  fields=[
    'Id INTEGER PRIMARY KEY',
    'Date DATE NOT NULL',
    'Counterparty TEXT NOT NULL',
    'Amount FLOAT NOT NULL',
    'AliasId INTEGER'
  ]
)

# Aliases must have a category
# Multiple aliases can have the same category
db.createTable(
  name='Aliases',
  fields=[
    'Id INTEGER PRIMARY KEY',
    'Alias TEXT NOT NULL',
    'CategoryId INTEGER NOT NULL',
    'Ignore INTEGER NOT NULL'
  ]
)

db.createTable(
  name='Categories',
  fields=[
    'Id INTEGER PRIMARY KEY',
    'Name TEXT NOT NULL',
    'Budget FLOAT NOT NULL'
  ]
)

fillTransactions(db=db, dataFolder='venv/src/data')

# Fills database with temporary data for development purposes
setup(db)

# Render home page (default)
@app.route('/')
def home():
  return render_template('index.html')

# Returns JSON containing the years and months that have data
@app.route('/api/periods')
def getPeriods():
  periods = getUtils.getPeriods(db)
  return jsonify(periods)

# Returns JSON containing the total monthly budget
@app.route('/api/budget-total')
def getBudgetTotal():
  budget = getUtils.getBudgetTotal(db)
  return jsonify({ 'amount': budget })

# Returns JSON containing total spending for a given month
@app.route('/api/total-spending')
def getSpending():
  year, month = int(request.args.get('year')), int(request.args.get('month'))
  start, end = getUtils.getMonthBounds(year, month)
  spending = getUtils.getSpending(db, start, end)
  return jsonify({ 'amount': spending })

# Returns JSON containing total income for a given month
@app.route('/api/total-income')
def getIncome():
  year, month = int(request.args.get('year')), int(request.args.get('month'))
  start, end = getUtils.getMonthBounds(year, month)
  income = getUtils.getIncome(db, start, end)
  return jsonify({ 'amount': income })

# Returns JSON containing graph data
@app.route('/api/graph')
def getGraphData():
  graphData = getUtils.getGraphData(
    db=db,
    year=int(request.args.get('year')),
    month=int(request.args.get('month'))
  )
  return jsonify(graphData)

# Returns JSON containing categorised spending/budget data
@app.route('/api/budget')
def getBudget():
  budget = getUtils.getBudget(
    db=db,
    year=int(request.args.get('year')),
    month=int(request.args.get('month'))
  )
  return jsonify(budget)

# Returns JSON containing daily transaction data
@app.route('/api/daily-transactions')
def getDailyTransactions():
  dailyTransactions = getUtils.getDailyTransactions(
    db=db,
    year=int(request.args.get('year')),
    month=int(request.args.get('month'))
  )
  return jsonify(dailyTransactions)

# Returns JSON containing categorised transaction data
@app.route('/api/category-transactions')
def getCategoryTransactions():
  categoryTransactions = getUtils.getCategoryTransactions(
    db=db,
    year=int(request.args.get('year')),
    month=int(request.args.get('month'))
  )
  return jsonify(categoryTransactions)

if __name__ == '__main__':
  app.run(debug=True)