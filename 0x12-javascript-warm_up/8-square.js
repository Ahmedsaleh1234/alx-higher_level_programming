#!/usr/bin/node
const argv = Number(process.argv[2]);
if (argv && Number(argv)) {
  for (let i = 0; i < argv; i++) {
    console.log('X'.repeat(argv));
  }
} else {
  console.log('Missing size');
}
