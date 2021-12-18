#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let number = 0;
  list.forEach(function (index) {
    if (index === searchElement) {
      number += 1;
    }
  });
  return (number);
};
