#!/usr/bin/node
exports.converter = function (base) {
  return function transform (x) {
    return x.toString(base);
  };
};
