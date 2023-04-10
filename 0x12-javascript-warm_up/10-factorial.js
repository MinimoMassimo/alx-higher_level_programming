#!/usr/bin/node
const arg = Number(process.argv[2]);
function factorial (x) {
  if (Number.isNaN(arg) === true) return 1;
  if (x === 1 || x === 0) return 1;
  return x * factorial(x - 1);
}
console.log(factorial(arg));
