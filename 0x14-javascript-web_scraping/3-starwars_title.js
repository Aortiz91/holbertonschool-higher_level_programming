#!/usr/bin/node
// Get the status code
const request = require('request');
let url = 'http://swapi.co/api/films/';
url = url + process.argv[2];
request(url, function (error, response, body) {
	if (error) {
		console.log(error);
	} else {
		console.log(JSON.parse(body).title);
}
});
