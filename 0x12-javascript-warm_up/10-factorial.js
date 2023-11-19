#!/usr/bin/node
const num = Number(process.argv[2]);
console.log(func(num));
function func (n) {
  if (n === 0) {
    return (1);
  } else if (n > 0) {
    return (n * func(n - 1));
  } else {
    return (1);
  }
}
