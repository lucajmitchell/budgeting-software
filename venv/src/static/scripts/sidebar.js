function createSideBarTitle(year) {
  const container = document.querySelector(".side-bar");
  const newSpan = document.createElement("span");
  newSpan.className = "small muted side-bar-subtitle";
  newSpan.textContent = year;
  container.appendChild(newSpan);
}

function createSideBarButton(month, year) {
  const container = document.querySelector(".side-bar");
  const newButton = document.createElement("button");
  newButton.className = "button faint";
  newButton.textContent = `${MONTH_NAMES[month]} ${year}`;
  newButton.onclick = () => loadDataFor(year, month);
  container.appendChild(newButton);
}

function createSideBarDivider() {
  const container = document.querySelector(".side-bar");
  const newDivider = document.createElement("hr");
  container.appendChild(newDivider);
}

function populateSideBar(periods) {
  periods.forEach((period) => {
    year = period.year;
    months = period.months;

    createSideBarTitle(year);
    months.forEach((month) => {
      createSideBarButton(month, year);
    });
    createSideBarDivider();
  });
}

async function getPeriods() {
  const response = await fetch("/api/periods");
  const data = await response.json();
  return data;
}

function getMostRecentMonth(periods) {
  return periods
    .map((group) => ({
      year: group.year,
      month: Math.max(...group.months),
    }))
    .sort((a, b) => {
      if (a.year !== b.year) return b.year - a.year;
      return b.month - a.month;
    })[0];
}

document.addEventListener("DOMContentLoaded", async () => {
  const periods = await getPeriods();
  populateSideBar(periods);

  const mostRecentMonth = getMostRecentMonth(periods);
  loadDataFor(mostRecentMonth.year, mostRecentMonth.month);
});
