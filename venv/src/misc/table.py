def printTable(records):
  print(f'┌{'─'*10}┬{'─'*30}┬{'─'*10}┐')
  print(f'│{'Date':>10}│{'Payee':>30}│{'Amount':>10}│')
  print(f'┝{'━'*10}┿{'━'*30}┿{'━'*10}┥')
  for record in records:
    print(f'│{record['Date']:>10}│{record['Payee']:>30}│{(record['Amount']):>10}│')
    print(f'├{'─'*10}┼{'─'*30}┼{'─'*10}┤')