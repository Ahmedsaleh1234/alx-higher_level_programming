#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (_err, req) {
  console.log('code: ', req.statusCode);
});
