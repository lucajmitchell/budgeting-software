function createDoughnutChart(container, dataset) {
  const ctx = document.getElementById(container);
  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: dataset.categories,
      datasets: [
        {
          label: dataset.label,
          data: dataset.values,
        },
      ],
    },
    options: {
      plugins: {
        legend: {
          position: "bottom",
        },
      },
    },
  });
}

async function fillBudget(year, month) {
  // Reset table
  document.getElementById("budget-table").innerHTML = "";

  // Get budget data
  const response = await fetch(`/api/budget?year=${year}&month=${month}`);
  const budget = await response.json();

  // Create HTML
  let rows = `       
    <tr>
      <th>Category</th>
      <th>Spent</th>
      <th>Budget</th>
    </tr>
  `;
  for (let i = 0; i < budget.length; i++) {
    const budgetRow = budget[i];
    const budgetRowHtml = `
      <tr>
        <td>
          <div class="circle-meter-label-wrapper">
            <meter
              value="${budgetRow.spending}"
              max="${budgetRow.budget}"
              class="circle-meter"
              id="category-meter-${i}"
            ></meter>
            <label for="category-meter-${i}">${budgetRow.category}</label>
          </div>
        </td>
        <td><span class="badge ${budgetRow.spending > budgetRow.budget ? "bad" : "good"}">${formatMoney(budgetRow.spending)}</span></td>
        <td>${formatMoney(budgetRow.budget)}</td>
      </tr>
    `;
    rows += budgetRowHtml;
  }

  // Add HTML to table
  document.getElementById("budget-table").innerHTML += rows;
  drawCircleMeters();

  // Create donut charts
  let categories = [];
  let budgetedValues = [];
  let actualValues = [];
  budget.forEach((category) => {
    categories.push(category.category);
    budgetedValues.push(category.budget);
    actualValues.push(category.spending);
  });

  const budgetedDistribution = {
    label: "Budget",
    categories: categories,
    values: budgetedValues,
  };
  createDoughnutChart("budgeted-distribution", budgetedDistribution);

  const actualDistribution = {
    label: "Spending",
    categories: categories,
    values: actualValues,
  };
  createDoughnutChart("actual-distribution", actualDistribution);
}
