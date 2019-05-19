// from data.js
var tableData = data;

var tbody = d3.select("tbody");

tableData.forEach(function(tableData) {
  var row = tbody.append("tr");
  // var row = tbody.append("td", index);
  Object.entries(tableData).forEach(function([key, value]) {
    console.log(key, value);
    row.append("td").text(value);
  });
});



//   var inData = {
//     datetime: "1/28/1996", 
//     city: "dallas",
//     state: "tx",
//     country: "us",
//     shape: "star",
//     durationMinutes: "5 mins.",
//     comments: "Cowboys win a superbowl, that's alien!."
// };
// // select the 3rd data row of the HTML table, by it's ID.
// var toReplace = tabledata.getElementById("tr").selectedIndex = "3";
// // Iterate through datum values and substite the inData values.
// toReplace.map(datum => inData.value);
// console.log(this)

// Select the submit button
var submit = d3.select("#submit");
submit.on("click", function() {
  // Prevent the page from refreshing
  d3.event.preventDefault();
  // Select the input element and get the raw HTML node
  var inputElement = d3.select(".form-control");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");
  // console.log(inputValue);
  // console.log(this);

  var filteredData = tableData.filter(data => data.datetime === inputValue);
  console.log(filteredData);
});

// // // BONUS: how many sightings fit filter criteria?
// // var sumFilter = filteredData.length;

var tableStripe = data.attr("class", "table table-striped");

