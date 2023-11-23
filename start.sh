#!/bin/sh
python3 ./motion_photo/dog_detector.py &
python3 ./motion_photo_trigger/main.py &
cd ./photo_server
npm start &

