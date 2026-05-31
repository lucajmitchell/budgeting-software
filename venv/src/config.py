SOURCE_PREFIX = 'venv/src/data/'

DATA_COLUMN_TITLES = ['Date', 'Payee', 'Amount']

ALIASES = {
  # Accounts
  '.*41647466.*': 'Savings',

  # Businesses
  '.*TESCO.*': 'Tesco',
  '.*JD WETHERSPOON.*': 'Wetherspoons',
  '.*MARKET PLACE FORUM EXETER.*': 'Forum',
  '.*Vinted.*': 'Vinted',
  '.*toogoodtogo.*': 'Too Good To Go',
  '.*PREMIER.*': 'Premier',

  # People
  '.*Liliana Cernecca.*': 'Lili',
  '.*Jac Jones.*': 'Jac',
}