#!/usr/bin/node
// Get the status code
const request = require('request');

let url = process.argv[2];
url = url.replace('films', 'people');
url = url + '18/';
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).films.length);
  }
});
