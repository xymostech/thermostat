#!/usr/bin/env bash

set -e

function clean_up() {
    set +e
    kill -SIGINT 0
    exit
}

# Kill all child processes on script abort
trap clean_up SIGTERM SIGINT ERR

if [ "$1" == "--debug" ]; then
    ./node_modules/.bin/watchify \
        -v \
        -t reactify \
        js/main.jsx \
        -o static/build/bundle.js &
fi

python app.py
