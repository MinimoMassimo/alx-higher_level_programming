#!/usr/bin/node
const args = process.argv.slice(2);
if (Number.isNaN(Number(args[0])) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args[0]; i++) {
    console.log('C is fun');
  }
}
