# Unit 14 | Assignment - JavaScript and DOM Manipulation
 create a table dynamically based upon a [dataset we provide](StarterCode/static/js/data.js). 
 filter the table data for specific values.
 only use pure JavaScript, HTML, and CSS, and D3.js 

### Level 1: Automatic Table and Date Search

* Create a basic HTML web page or use the [index.html](StarterCode/index.html) file provided (we recommend building your own custom page!).

* Using the UFO dataset provided in the form of an array of JavaScript objects, write code that appends a table to your web page and then adds new rows of data for each UFO sighting.

  * Make sure you have a column for `date/time`, `city`, `state`, `country`, `shape`, and `comment` at the very least.

* Add the following datum as the third entry of the data.js file:

```js
    {
    datetime: "1/28/1996",
    city: "dallas",
    state: "tx",
    country: "us",
    shape: "star",
    durationMinutes: "5 mins.",
    comments: "Cowboys win a superbowl, that's alien!."
    }
```

* Use a date form in your HTML document and write JavaScript code that will listen for events and search through the `date/time` column to find rows that match user input.

* Use bootstrap to style the table with striped rows



### Level 2: Multiple Search Categories (Optional)

* Complete all of Level 1 criteria.

* Using multiple `input` tags and/or select dropdowns, write JavaScript code so the user can to set multiple filters and search for UFO sightings using the following criteria based on the table columns:

  1. `date/time`
  2. `city`
  3. `state`
  4. `country`
  5. `shape`

- - -

### Dataset

* [UFO Sightings Data](StarterCode/static/js/data.js)

- - -

**Good luck!**

- - -

### Copyright

Data Boot Camp © 2018. All Rights Reserved.
