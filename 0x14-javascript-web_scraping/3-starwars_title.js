#!/usr/bin/node
// Get the status code
const request = require('request');

let url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
	if (error) {
		console.log(err)
	} else {
		console.log(JSON.parse(body).title);
	}
});
