function createDailyTransactionsRows(transactions) {
  rows = "";
  transactions.forEach((transaction) => {
    rows += `
      <tr>
        <td>${transaction.counterparty}</td>
        <td>${formatMoney(transaction.income)}</td>
        <td>${formatMoney(transaction.spending)}</td>
      </tr>  
    `;
  });
  return rows;
}

function createDailyTransactionsCard(date, income, spending, transactions) {
  return `
    <div class="card">
      <div class="card-header">
        <div class="card-header-text">
          <h2 class="title">${new Intl.DateTimeFormat("en-GB").format(date)}</h2>
        </div>
        <div class="card-header-badges">
          <span class="badge good">${formatMoney(income)}</span>
          <span class="badge bad">${formatMoney(spending)}</span>
        </div>
      </div>
      <div class="table-wrapper">
        <table>
          <tr>
            <th>Counterparty</th>
            <th>In</th>
            <th>Out</th>
          </tr>
          ${createDailyTransactionsRows(transactions)}
        </table>
      </div>
    </div>
  `;
}

async function fillDailyTransactions(year, month) {
  // Reset container
  document.getElementById("daily-transactions").innerHTML = "";

  // Get daily data
  const response = await fetch(
    `/api/daily-transactions?year=${year}&month=${month}`,
  );
  const data = await response.json();

  // Create cards
  data.forEach((dailyData) => {
    const date = new Date(dailyData.date);
    const income = dailyData.income;
    const spending = dailyData.spending;
    const transactions = dailyData.transactions;
    const card = createDailyTransactionsCard(
      date,
      income,
      spending,
      transactions,
    );
    document.getElementById("daily-transactions").innerHTML += card;
  });
}
