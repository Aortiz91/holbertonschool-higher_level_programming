#!/usr/bin/node

const ParentSquare = require('./5-square.js');
module.exports = class Square extends ParentSquare {
  // Method
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let a = '';
      let i = 0;
      let j = 0;
      while (i < this.width) {
        a = a + c;
        i++;
      }
      while (j < this.width) {
        console.log(a);
        j++;
      }
    }
  }
};
