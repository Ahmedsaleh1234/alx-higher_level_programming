#!/bin/bash
#displays the size of the body of the response
curl -sI "$1" | grep -i Content-length | cut -d " " -f 2 
