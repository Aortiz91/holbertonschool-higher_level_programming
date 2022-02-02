#!/usr/bin/node
// Get the status code
const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const reqResults = JSON.parse(body).results;
    let total = 0;
    for (let x = 0; x < reqResults.length; x++) {
      const reqCharacters = reqResults[x].characters;
      const stringChar = JSON.stringify(reqCharacters);
      if (stringChar.includes('/18/') === true) {
        total += 1;
      }
    }
    console.log(total);
  }
});
