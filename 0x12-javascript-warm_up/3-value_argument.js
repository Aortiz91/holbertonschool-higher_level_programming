#!/usr/bin/node
const { argv } = require('process');

if (!argv[2]) {
  console.log('No argument');
} else {
  const arg = argv[2];
  console.log(arg);
}
