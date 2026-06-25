const MONTH_NAMES = {
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

function formatMoney(amount) {
  return new Intl.NumberFormat("en-GB", {
    style: "currency",
    currency: "GBP",
  }).format(amount);
}

function daysInMonth(year, month) {
  return new Date(year, month, 0).getDate();
}

function drawCircleMeters() {
  const meters = document.querySelectorAll(".circle-meter");
  meters.forEach((meter) => {
    const value = Number(meter.getAttribute("value"));
    const max = Number(meter.getAttribute("max"));
    const progress = value / max;
    meter.style.setProperty("--progress", progress);
  });
}
