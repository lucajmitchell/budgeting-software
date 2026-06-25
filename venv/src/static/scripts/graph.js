let monthlySpendGraph;

async function fillGraph(year, month) {
  // Reset graph
  if (monthlySpendGraph) {
    monthlySpendGraph.destroy();
  }

  // Get data
  const graphDataResponse = await fetch(
    `/api/graph?year=${year}&month=${month}`,
  );
  const graphData = await graphDataResponse.json();

  // Graph setup
  const ctx = document.getElementById("monthly-spend-graph");
  const lineColor = window
    .getComputedStyle(document.body)
    .getPropertyValue("--fg");
  const bgColor = window
    .getComputedStyle(document.body)
    .getPropertyValue("--trans");

  // Create graph
  monthlySpendGraph = new Chart(ctx, {
    type: "line",
    data: {
      labels: graphData.dates,
      datasets: [
        {
          data: graphData.spending,
          borderColor: lineColor,
          backgroundColor: "rgba(0, 0, 0, 0)",
        },
        {
          data: graphData.budget,
          borderColor: "rgba(0, 0, 0, 0)",
          backgroundColor: bgColor,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
      borderWidth: 1,
      radius: 0,
      fill: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false,
        },
      },
    },
  });
}
