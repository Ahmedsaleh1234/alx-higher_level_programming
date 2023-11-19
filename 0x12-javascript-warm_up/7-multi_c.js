#!/usr/bin/node
const argv = Number(process.argv[2]);
if (argv && Number(process.argv[2])) {
  for (let i = 0; i < argv; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
