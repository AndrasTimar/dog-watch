#!/bin/sh
python3 ./dog_watch_server/server.py &
npm start --prefix ./photo_server &

