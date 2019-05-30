// from data.js
var tableData = data;
console.log(tableData);

var tbody = d3.select("tbody");

function buildTable(data) {
  console.log("executing buildTable");  
  // First, clear out existing data in "tbody" (for each iteration).
  console.log("executing function buildTable");
  tbody.html("");
  // add comment
  data.forEach((sighting) => {
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
  // Reusable filter, can filter by multiple inputs??
  console.log(filterSoFar);
  if (inputValue) {
    // Apply `filter` to the table data to *only keep the
    // rows where the `datetime` value *matches the filter value:
    filterSoFar = filterSoFar.filter(row => row.datetime === inputValue);
  }

  // filterSoFar = filterSoFar.filter(sighting => sighting.datetime === inputValue);
  // filterSoFar1 = filterSoFar.filter(sighting => sighting.datetime === inputValue);
  console.log(filterSoFar);
  console.log("logging filtered data")
  buildTable(filterSoFar);
}

// Back to baseline. Check data, build table (call fcn):
var submit = d3.select("#filter-btn");
submit.on("click", clickBuild);
buildTable(tableData);

// Use bootstrap to style the table with striped rows
// Done in HTML file index.html


// var inData = {
//   // ID: ,
//   datetime: "1/28/1996", 
//   city: "dallas",
//   state: "tx",
//   country: "us",
//   shape: "star",
//   durationMinutes: "5 mins.",
//   comments: "Cowboys win a superbowl, that's alien!."
// };
// Select the 3rd data row of the HTML table, by it's ID.

// // var toReplace = data.getElementById("tr").item(2);
// var toReplace = d3.select("tr").item(2);
// // // Iterate through datum values and substite the inData values.
// // toReplace.map(datum => inData.value);
// console.log(this);

// var thirdSight = data[2];
// console.log(thirdSight);
// [...parent.children].forEach(function (child) {
//   console.log(child)
// });
// thirdSight.forEach(function([key, value]) {
//   thirdSight.getElementById(td).innerHTML=inData;
// })

// data.forEach(function(each, index) {
//   // The original array is mutated with forEach
//   data[index] = `Stage ${index + 1}: ${each}`;
// });
// for (var i = 0; i < stringArray.length; i++) {
//   var currentWord = stringArray[i];
//   if (currentWord in wordFrequency) {
//     // Add one to the counter
//     wordFrequency[currentWord] += 1;
//   }
//   else {
//     // Set the counter at 1
//     wordFrequency[currentWord] = 1;
//   }
// }
// console.log(wordFrequency);
// return wordFrequency;
// }



// // BONUS: how many sightings fit filter criteria?
// var sumFilter = filteredData.length;
