#!/usr/bin/node
const args = process.argv.slice(2);
if (Number.isNaN(Number(args[0])) === false) {
  console.log(`My number: ${args[0]}`);
} else {
  console.log('Not a number');
}
