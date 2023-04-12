#!/usr/bin/node
let glob;
exports.logMe = function (item) {
  if (typeof glob === 'undefined') {
    glob = 0;
  }
  console.log(glob + `: ${item}`);
  glob += 1;
};
