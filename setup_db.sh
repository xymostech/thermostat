#!/usr/bin/env bash

set -e

DATABASE="db.sqlite"
SCHEMA_FILE="curr_schema"

CURR_SCHEMA=2

if [ ! -e "$SCHEMA_FILE" ]; then
    if [ -e "$DATABASE" ]; then
        echo "The schema version was lost but the database ($DATABASE) still"
        echo "exists. Either delete the database, or put the current schema"
        echo "version in $SCHEMA_FILE."
        exit 1
    fi
    SCHEMA=0
else
    SCHEMA=$(cat "$SCHEMA_FILE")
fi

while [ $SCHEMA -lt $CURR_SCHEMA ]; do
    SCHEMA=$(($SCHEMA + 1))

    echo "Upgrading to schema $SCHEMA..."
    sqlite3 "$DATABASE" < "schemas/$SCHEMA.sql"
done

echo $SCHEMA > "$SCHEMA_FILE"
