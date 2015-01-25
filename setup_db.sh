#!/usr/bin/env bash

set -e

DATABASE="db.sqlite"

rm -f "$DATABASE"

sqlite3 "$DATABASE" < setup.sql
