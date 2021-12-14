#!/usr/bin/node
const { argv } = require('process');

add(parseInt(argv[2]), parseInt(argv[3]));

function add (a, b) {
  console.log(a + b);
}
