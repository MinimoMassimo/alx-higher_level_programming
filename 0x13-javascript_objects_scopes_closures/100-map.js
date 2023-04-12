#!/usr/bin/node
const arr = require('./100-data').list;
console.log(arr);
let arr2 = [];
let i = 0;
arr2 = arr.map(elem => {
  i++;
  return elem * (i - 1);
});
console.log(arr2);
