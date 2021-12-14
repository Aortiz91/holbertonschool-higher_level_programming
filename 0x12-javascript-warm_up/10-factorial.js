#!/usr/bin/node
const { argv } = require('process');

function factorial (a) {
  if (a < 0) {
    return;
  }
  if (a === 0 || isNaN(a)) {
    return (1);
  }
  return (a * factorial(a - 1));
}

console.log(factorial(argv[2]));
