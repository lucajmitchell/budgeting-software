function createSideBarTitle(year) {
  const container = document.querySelector(".side-bar");
  const newSpan = document.createElement("span");
  newSpan.className = "small muted side-bar-subtitle";
  newSpan.textContent = year;
  container.appendChild(newSpan);
}

function createSideBarButton(month, year) {
  const monthNames = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
  };

  const container = document.querySelector(".side-bar");
  const newButton = document.createElement("button");
  newButton.className = "button faint";
  newButton.textContent = `${monthNames[month]} ${year}`;
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

document.addEventListener("DOMContentLoaded", async () => {
  const periods = await getPeriods()
  populateSideBar(periods)
});