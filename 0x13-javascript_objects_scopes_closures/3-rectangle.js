#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method
  print () {
    let printer = '';
    let i = 0;
    let j = 0;
    while (i < this.width) {
      printer = printer + 'X';
      i++;
    }
    while (j < this.height) {
      console.log(printer);
      j++;
    }
  }
};
