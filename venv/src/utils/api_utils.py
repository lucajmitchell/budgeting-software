
def getPeriods(db):
  yearsAndMonths = db.fetch('''
    SELECT
      strftime('%Y', Date) AS year,
      GROUP_CONCAT(DISTINCT CAST(strftime('%m', Date) AS INTEGER)) AS months
    FROM Transactions
    GROUP BY year
    ORDER BY year
  ''')

  periods = []

  for year, months in yearsAndMonths:
    yearFormatted = int(year)
    monthsFormatted = [int(month) for month in months.split(',')]
    monthsFormatted.sort()

    periods.append({
      'year': yearFormatted,
      'months': monthsFormatted
    })

  return periods
