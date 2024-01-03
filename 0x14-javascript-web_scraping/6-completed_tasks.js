#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, _req, body) {
  if (err) {
    console.log(err);
  } else {
    const todo = {};
    body = JSON.parse(body);
    for (let i = 0; i < body.length; i++) {
      const userId = body[i].userId;
      const completed = body[i].completed;
      if (completed && !todo[userId]) {
        todo[userId] = 0;
      }
      if (completed) {
        ++todo[userId];
      }
    }
    console.log(todo);
  }
});
