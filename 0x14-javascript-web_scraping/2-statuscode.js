#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, req) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + req.statusCode);
  }
});
