// from data.js
var tableData = data;
// console.log(tableData);

var tbody = d3.select("tbody");

function buildTable(tableData) {
  console.log("executing buildTable");  
  // First, clear out existing data in "tbody" (for each iteration).
  tbody.html("");
  // add comment
  tableData.forEach((sighting) => {
    var row = tbody.append("tr");
    Object.entries(sighting).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
};

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
  }

  // Reusable filter, can filter by multiple inputs??
  // filterSoFar = filterSoFar.filter(sighting => sighting.datetime === inputValue);
  // filterSoFar1 = filterSoFar.filter(sighting => sighting.datetime === inputValue);
  console.log(filterSoFar);
  // console.log("logging filtered data")
  buildTable(filterSoFar);
}

// Back to baseline. Check data, build table (call fcn):
var submit = d3.select("#filter-btn");
submit.on("click", clickBuild);
buildTable(tableData);

// Use bootstrap to style the table with striped rows
// Done in HTML file index.html

// LASTLY: Replace 3rd row of table with new data:
// Create new data Object; select row to replace; forEach to replace.
var inData = {
  datetime: "1/28/1996", 
  city: "dallas",
  state: "tx",
  country: "us",
  shape: "star",
  durationMinutes: "5 mins.",
  comments: "Cowboys win a superbowl, that's alien!."
};
console.log(inData);

// Select the 3rd data row of the HTML table, by it's ID.
var toReplace = tableData[2];
console.log(toReplace);

// Iterate through datum values and substite the inData values.
Object.values(toReplace).forEach(d => inData.value);

// tableData[2].forEach(function(sighting) {
// });
// Object.values(tableData[2]).forEach(([key, value]) => {
//   var cell = row.text("");
//   cell.text(inData.value);
// });
// tableData[2].function(callback(tableData [, 2]) => {
// tableData.getElementById(td).innerHTML=inData;

console.log(toReplace);
console.log(tableData[2]);


// // BONUS: how many sightings fit filter criteria?
// var sumFilter = filterSoFar.length;
