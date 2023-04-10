#!/usr/bin/node
const args = process.argv.slice(2);
if (Number.isNaN(Number(args[0])) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[0]; i++) {
    console.log('X'.repeat(args[0]));
  }
}
