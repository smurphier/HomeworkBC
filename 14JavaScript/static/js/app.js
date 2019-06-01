// Set data reference, select HTML tag to insert data as a table
var tableData = data;

// Replace 3rd row of table with new data:
console.log(data[2]);
data[2] = {
  datetime: "1/28/1996",
  city: "dallas",
  state: "tx",
  country: "us",
  shape: "star",
  durationMinutes: "5 mins.",
  comments: "Cowboys win a superbowl, that's alien!."
};
console.log(data[2]);

var tbody = d3.select("tbody");

function buildTable(tableData) {
  console.log("executing buildTable");  
  // First, clear out existing data in "tbody" (for each iteration)
  tbody.html("");
  // Insert key & value of Each sighting as TData tag in a TableRow
  tableData.forEach((sighting) => {
    var row = tbody.append("tr");
    Object.entries(sighting).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
};

// Use bootstrap to style the table with striped rows
// Done in HTML file index.html

function clickBuild() {
  console.log("executing clickBuild");
  // Prevent the page from refreshing
  d3.event.preventDefault();
  // Create a variable that holds filtered data.
  var filterSoFar = tableData;
  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");
  // Get the value property of the input element
  var inputValue = inputElement.property("value");
  console.log(inputValue);
  // console.log(filterSoFar);
  if (inputValue) {
    // Apply `filter` to the table data to *only keep the
    // rows where the `datetime` value *matches the filter value:
    filterSoFar = filterSoFar.filter(sighting => sighting.datetime === inputValue);
    // BONUS: Display # of sightings fitting filter criteria
    var sumFilter = filterSoFar.length;
    var inLength = d3.select("textarea")
    inLength.text(sumFilter);
    // document.getElementbyId("h4").innerHTML = sumFilter;
  }

  // Reusable filter, can filter by multiple inputs??
  // filterSoFar = filterSoFar.filter(sighting => sighting.datetime === inputValue);
  // filterSoFar1 = filterSoFar.filter(sighting => sighting.datetime === inputValue);
  // console.log(filterSoFar);
  buildTable(filterSoFar);
}

// Back to baseline. Check data, build table (call fcn):
var submit = d3.select("#filter-btn");
submit.on("click", clickBuild);
buildTable(tableData);
