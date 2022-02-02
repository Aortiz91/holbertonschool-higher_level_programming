#!/usr/bin/node
// Get the info from API
const request = require('request');
const taskCompleted = {};
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const reqResults = JSON.parse(body);
    for (const items in reqResults) {
      if (reqResults[items].completed === true) {
        if (taskCompleted[reqResults[items].userId] == null) {
          taskCompleted[reqResults[items].userId] = 1;
        } else {
          taskCompleted[reqResults[items].userId] += 1;
        }
      }
    }
  }
  console.log(taskCompleted);
});
