function loadDataFor(year, month) {
  fillTopBar(year, month);

  fillBudgetPanel(year, month)
  fillSpendingPanel(year, month)
  fillMoneyRemainingPanel(year, month)
  fillIncomePanel(year, month)

  fillGraph(year, month)

  fillBudget(year, month)

  fillDailyTransactions(year, month)

  fillCategoryTransactions(year, month)
}
