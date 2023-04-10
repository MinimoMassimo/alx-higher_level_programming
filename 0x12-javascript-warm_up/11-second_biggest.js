#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  let Max = args[0];
  let sol = Max;
  for (let i = 0; i < args.length; i++) {
    if (args[i] > Max) Max = args[i];
  }
  for (let i = 0; i < args.length; i++) {
    // console.log(i);
    if (args[i] > sol && args[i] < Max) sol = args[i];
  }
  console.log(sol);
}
