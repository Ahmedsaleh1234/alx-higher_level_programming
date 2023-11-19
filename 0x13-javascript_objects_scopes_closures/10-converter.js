#!/usr/bin/node
exports.converter = function (base) {
  function con (n) {
    return n.toString(base);
  }
  return con;
};
