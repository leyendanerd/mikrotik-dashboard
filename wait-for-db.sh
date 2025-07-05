#!/bin/sh
# wait-for-db.sh
set -e
host="$1"
shift
until pg_isready -h "$host" -U "$POSTGRES_USER" >/dev/null 2>&1; do
  echo "Waiting for Postgres at $host..."
  sleep 1
done
exec "$@"
