#!/usr/bin/node
// Get the cotent of a webpage

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(process.argv[3], body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
