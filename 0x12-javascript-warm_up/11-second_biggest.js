#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  args.sort(function (a, b) { return a - b; });
  console.log(args[args.length - 2]);
}
