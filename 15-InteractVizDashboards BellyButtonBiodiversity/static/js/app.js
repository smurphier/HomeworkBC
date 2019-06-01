function buildMetadata(sample) {   // Build the metadata panel
  // Use `d3.json` to fetch the metadata for a sample
  console.log("doing buildMetadata");
  d3.json(`/metadata/${sample}`).then(function(data) {
    // Use d3 to select the panel with id of `#sample-metadata`
    var metaSample = d3.select("#sample-metadata");
    // Use `.html("") to clear any existing metadata
    metaSample.html("");
    console.log("About to add keyValues to Metadata Panel");

    // Use `Object.entries` to add each key and value pair to the panel
    Object.entries(data).forEach(function([key, value]) {
      // Construct HTML line of indexed data for appended row:
      var rowMeta = (`${key}: ${value}`); 
      // Append a cell to the row for each value pair; check if empty data.
        var cell = metaSample.append("h5");
        // Inside loop, use d3 to append new tag for each key-value in metadata.
        cell.text(rowMeta);
    });
    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
  });
}
//***************************************
//***************************************
//***************************************
console.log("About to build charts");
function buildCharts(sample) {
  console.log("doing buildCharts");
  // Fetch the sample data for the plots...
  d3.json(`/metadata/${sample}`).then(function(data) {
    // Build a Bubble Chart using the sample data
    console.log("Building BUBBLE");
    var trace1 = {
      x: data.otu_ids,
      y: data.sample_values,
      mode: "markers",
      marker: {
        size: data.sample_values, 
        color: data.otu_ids,
        symbol: "star"
      },
      type: "scatter"
    };
    console.log(trace1);
    var data = [trace1];
    var layout = {
      // showlegend: true,
      // height: 600,
      // width: 600,
      title: 'BellyButtonWashers'
    };
    console.log(data[otu_ids]);
    console.log("plotting BUBBLE");
    Plotly.newPlot("bubble", data, layout);
    });
    // @TODO: Build a Pie Chart

    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
}    

function init() {
  console.log("doing init");
    // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
 d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}


function optionChanged(newSample) {
  console.log("doing optionChanged");
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
