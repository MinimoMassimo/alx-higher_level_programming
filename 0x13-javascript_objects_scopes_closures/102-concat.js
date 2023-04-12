#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
fs.readFile(args[0], function (err, data) {
  if (err) {
    return console.error(err);
  }
  fs.writeFile(args[2], data, function (err, res) {
    if (err) {
      return console.error(err);
    }
  });
});
fs.readFile(args[1], function (err, data) {
  if (err) {
    return console.error(err);
  }
  fs.appendFile(args[2], data, function (err, res) {
    if (err) {
      return console.error(err);
    }
  });
});
