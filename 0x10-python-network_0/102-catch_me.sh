#!/bin/bash
#  a Bash script that makes a request to 0.0.0.0:5000/catch_me thatcauses the server to respond with a message containing You got me!, in the body of the response.
curl -s -X PUT -L -H "Origin:School" 0.0.0.0:5000/catch_me_3
