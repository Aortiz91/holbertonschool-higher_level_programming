#!/usr/bin/node
const { argv } = require('process');

if (parseInt(argv[2])) {
  const x = parseInt(argv[2]);
  let height = 0;

  while (height < x) {
    console.log('X'.repeat(x));
    height++;
  }
} else {
  console.log('Missing size');
}
