#!/usr/bin/node
// script that writes the content of a file.
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) { console.log(err); } else {
  }
});
