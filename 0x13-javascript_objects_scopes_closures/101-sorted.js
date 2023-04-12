#!/usr/bin/node
const dict = require('./101-data').dict;
const newD = {};
for (const key in dict) {
  if (newD[dict[key]] === undefined) newD[dict[key]] = [key];
  else newD[dict[key]].push(key);
}
console.log(newD);
