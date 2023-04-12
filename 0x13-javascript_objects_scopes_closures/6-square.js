#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
  charPrint (c) {
    if (typeof c === 'undefined') {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
