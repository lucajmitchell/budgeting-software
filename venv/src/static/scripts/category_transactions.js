function createCategoryTransactionsRows(transactions) {
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

function createCategoryTransactionsCard(
  category,
  income,
  spending,
  transactions,
) {
  return `
    <div class="card">
      <div class="card-header">
        <div class="card-header-text">
          <h2 class="title">${category}</h2>
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
          ${createCategoryTransactionsRows(transactions)}
        </table>
      </div>
    </div>
  `;
}

async function fillCategoryTransactions(year, month) {
  // Reset container
  document.getElementById("category-transactions").innerHTML = "";

  // Get category data
  const response = await fetch(
    `/api/category-transactions?year=${year}&month=${month}`,
  );
  const data = await response.json();
  console.log(data);

  // Create cards
  data.forEach((categoryData) => {
    const category = categoryData.category;
    const income = categoryData.income;
    const spending = categoryData.spending;
    const transactions = categoryData.transactions;
    const card = createCategoryTransactionsCard(
      category,
      income,
      spending,
      transactions,
    );
    document.getElementById("category-transactions").innerHTML += card;
  });
}
