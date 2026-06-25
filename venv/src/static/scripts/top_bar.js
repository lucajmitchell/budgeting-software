function fillTopBar(year, month) {
  const pageTitle = document.getElementById("page-title");
  pageTitle.innerText = `${MONTH_NAMES[month]} ${year}`;
}