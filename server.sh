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
    ./node_modules/.bin/beefy \
        js/main.jsx:bundle.js \
        9876 \
        -- \
        -t [ reactify --es6 ] &
fi

python app.py --debug
