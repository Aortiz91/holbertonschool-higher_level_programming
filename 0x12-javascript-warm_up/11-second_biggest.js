#!/usr/bin/node
const { argv } = require('process');
let a = 2;
let biggest = Number(argv[2]);
let secondbiggest = Number(argv[3]);

if (!argv[2] || (argv[2] && !argv[3])) {
  console.log('0');
} else {
  while (a < argv.length) {
    if (Number(argv[a]) > biggest) {
      secondbiggest = biggest;
      biggest = Number(argv[a]);
    } else if (Number(argv[a]) > secondbiggest && Number(argv[a]) < biggest) {
      secondbiggest = Number(argv[a]);
    }
    a++;
  }
  console.log(secondbiggest);
}
