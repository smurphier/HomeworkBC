// from data.js
var tableData = data;

var tbody = d3.select("tbody");
tabledata.forEach((sighting, i) => {
    var row = tbody.append("tr");
    var row = tbody.append("td", i)
    Object.entries(tabledata).forEach(([key, value]) => {
      var datum = row.append("td");
      datum.text(value);
    });
  });

  var inData = {
    ID: ,
    datetime: "1/28/1996", 
    city: "dallas",
    state: "tx",
    country: "us",
    shape: "star",
    durationMinutes: "5 mins.",
    comments: "Cowboys win a superbowl, that's alien!."
};
// select the 3rd data row of the HTML table, by it's ID.
var toReplace = tabledata.getElementById("tr").selectedIndex = "3";
// Iterate through datum values and substite the inData values.
toReplace.map(datum => inData.value);
console.log(this)


// Select the submit button
var submit = d3.select("#submit");
submit.on("click", function() {
  // // Prevent the page from refreshing
  // d3.event.preventDefault();
  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#example-form-input");
  // Get the value property of the input element
  var inputValue = inputElement.property("value");
  // console.log(inputValue);
  var filteredData = tabledata.filter(sighting => sighting.datetime === inputValue);
  console.log(filteredData);
  // Set the span tag of h1 element to input text
    d3.select("h1>span").text(filteredData);
});
// BONUS: how many sightings fit filter criteria?
var sumFilter = filteredData.length;

var tableStripe = tableData.attr("class", "table table-striped");