#!/usr/bin/node
/* script that prints a message depending
of the number of arguments passed */
const num = process.argv.length;
if (num < 3) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
