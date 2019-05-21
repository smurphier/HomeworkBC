// from data.js
var tableData = data;
var tbody = d3.select("tbody");

tableData.forEach(function(tableData) {
  var row = tbody.append("tr");
  // var row = tbody.append("td", index);
  Object.entries(tableData).forEach(function([key, value]) {
    row.append("td").text(value);
  });
});
// Use bootstrap to style the table with striped rows
// var tableStripe = data.attr("class", "table table-striped");

var inData = {
  datetime: "1/28/1996", 
  city: "dallas",
  state: "tx",
  country: "us",
  shape: "star",
  durationMinutes: "5 mins.",
  comments: "Cowboys win a superbowl, that's alien!."
}
// select the 3rd data row of the HTML table, by it's ID.
// Iterate through datum values and substite the inData values.
// var thirdSight = tableData[2];
// console.log(thirdSight);
// [...parent.children].forEach(function (child) {
//   console.log(child)
// });
// thirdSight.forEach(function([key, value]) {
//   thirdSight.getElementById(td).innerHTML=inData;
// })
//   // "city"==="el cajon"

// // Select the submit button
// var submit = d3.select("#submit");
// submit.on("click", function() {
//   // Prevent the page from refreshing
//   d3.event.preventDefault();

//   // Select the input element and get the raw HTML node
//   var inputElement = d3.select(".form-control");
//   // Get the value property of the input element
//   var inputValue = inputElement.property("value");
//   // console.log(inputValue);
//   // console.log(this);

//   var filteredData = tableData.filter(data => data.datetime === inputValue);
//   d3.select("tbody").push
//   var dateSelect = filteredData.map()

  // // BONUS: how many sightings fit filter criteria?
  // var filterCount = filteredData.length;
  // console.log(filterCount);