#!/usr/bin/node
const request = require('request');
let count = 0;
request.get(process.argv[2], function (err, req, body) {
  if (!err) {
    body = JSON.parse(body).results;
    for (let i = 0; i < body.length; i++) {
      const cs = body[i].characters;
      for (let j = 0; j < cs.length; j++) {
        const c = cs[j];
        const cid = c.split('/')[5];
        if (cid === '18') {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
