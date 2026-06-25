async function fillBudgetPanel(year, month) {
  const response = await fetch("/api/budget-total");
  const data = await response.json();

  const amount = data.amount;
  const dailyAmount = amount / daysInMonth(year, month);

  document.getElementById("quick-info-budget").innerText = formatMoney(amount);
  document.getElementById("quick-info-budget-daily").innerText =
    formatMoney(dailyAmount) + "/day";
}

async function fillSpendingPanel(year, month) {
  const response = await fetch(
    `/api/total-spending?year=${year}&month=${month}`,
  );
  const data = await response.json();

  const amount = data.amount;
  const dailyAmount = amount / daysInMonth(year, month);

  document.getElementById("quick-info-spending").innerText =
    formatMoney(amount);
  document.getElementById("quick-info-spending-daily").innerText =
    formatMoney(dailyAmount) + "/day";
}

async function fillMoneyRemainingPanel(year, month) {
  const budgetResponse = await fetch("/api/budget-total");
  const budgetData = await budgetResponse.json();
  const budget = budgetData.amount;

  const spendingResponse = await fetch(
    `/api/total-spending?year=${year}&month=${month}`,
  );
  const spendingData = await spendingResponse.json();
  const spending = spendingData.amount;

  const remaining = budget - spending;
  const dailyRemaining = remaining / daysInMonth(year, month);

  document.getElementById("quick-info-remaining").innerText =
    formatMoney(remaining);
  document.getElementById("quick-info-remaining-daily").innerText =
    formatMoney(dailyRemaining) + "/day";
}

async function fillIncomePanel(year, month) {
  const response = await fetch(`/api/total-income?year=${year}&month=${month}`);
  const data = await response.json();

  document.getElementById("quick-info-income").innerText = formatMoney(
    data.amount,
  );
}
