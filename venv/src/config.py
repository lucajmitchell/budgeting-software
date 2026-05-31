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
  '.*MYNIGHTOUT.*': 'My Night Out',
  '.*EFES.*': 'Efes',
  '.*DUKE OF YORK.*': 'Duke of York',
  '.*BLACK HORSE.*': 'Black Horse',
  '.*APPLE.COM.*': 'Apple',
  '.*TRAINLINE.*': 'Trainline',
  '.*Trainline.*': 'Trainline',
  '.*CENTRAL CONVENIENC CREWE.*': 'Corner Shop',
  '.*BOOTS.*': 'Boots',
  '.*FIXR.*': 'FIXR',
  ".*ST ANNE'S WELL.*": "St Anne's Well",
  '.*VICTORIA INN.*': 'Victoria Inn',
  '.*CHEVALIER INN.*': 'Wetherspoons',
  '.*THE STAND OFF.*': 'The Stand Off',
  '.*FlyingTiger.*': 'Tiger',
  '.*HM Exeter.*': 'H&M',
  '.*Old Fire House.*': 'Old Fire House',
  '.*Franco Manca.*': 'Franco Manca',
  '.*MAGDALEN STORES.*': 'Corner Shop',
  '.*TG Jones.*': 'WHSmith',
  '.*CIRCUIT GO.*': 'Circuit Laundry',
  '.*MARKS&SPENCER.*': 'M&S',
  '.*TIMEPIECE.*': 'Timepiece',
  '.*CORNWALL HOUSE.*': 'Laf Shop',
  '.*Corinium Par.*': 'Corinium Partnership',
  '.*GRADDON SONS.*': 'Vending Machine',
  '.*T G POP LT Brentwood.*': 'Stoke Arms',
  '.*STAGECOACH.*': 'Stagecoach',
  '.*SOSTRENE GRENE.*': 'Sostrene Grene',
  '.*The Crown.*': 'The Crown',
  '.*BURRITO MAMA.*': 'Burrito Mama',
  '.*Decathlon.*': 'Decathlon',
  '.*THE BEAR INN.*': 'The Bear Inn',
  '.*WEAREHOMESFOR.*': 'Printworks',
  ".*WATER'S EDGE.*": "Water's Edge",
  '.*ABBEY WAY SERVICES.*': 'Corner Shop',

  # People
  '.*Liliana Cernecca.*': 'Lili',
  '.*Jac Jones.*': 'Jac',
  '.*Anna Ayres.*': 'Anna',
}