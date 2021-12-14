#!/usr/bin/node
const { argv } = require('process');

if (parseInt(argv[2])) {
  const x = parseInt(argv[2]);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
