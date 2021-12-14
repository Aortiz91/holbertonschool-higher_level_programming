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

  // Method
  rotate () {
    const wd = this.width;
    this.width = this.height;
    this.height = wd;
  }

  // Method
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
