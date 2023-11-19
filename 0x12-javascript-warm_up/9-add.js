#!/usr/bin/node
const x = Number(process.argv[2]);
const y = Number(process.argv[3]);
add(x, y);
function add (a, b) {
  console.log(a + b);
}
