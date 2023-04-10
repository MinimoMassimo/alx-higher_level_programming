#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
function add (a, b) {
  return a + b;
}
console.log(add(args[0], args[1]));
