#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const reqResults= JSON.parse(body);
  for (const items in reqResults.characters) {
    request(reqResults.characters[items], function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const charReq = JSON.parse(body);
      console.log(charReq.name);
    });
  }
});
