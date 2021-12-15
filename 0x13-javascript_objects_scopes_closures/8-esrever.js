#!/usr/bin/node
// Function that returns the reversed version of a list
exports.esrever = function (list) {
  const reverted = [];
  const len = list.length;
  let a = len - 1;
  let b = 0;
  while (a >= 0) {
    reverted[b] = list[a];
    a--;
    b++;
  }
  return (reverted);
};
