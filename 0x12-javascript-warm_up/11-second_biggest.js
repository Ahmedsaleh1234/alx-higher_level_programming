#!/usr/bin/node
function big (a, b) {
  if (a > b) {
    return (a);
  } else if (b > a) {
    return (b);
  } else {
    return (0);
  }
}
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
console.log(big(num1, num2));
