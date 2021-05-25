#!/usr/bin/env bash

set -ef

cli_help() {
  cli_name=${0##*/}
  echo "
$cli_name entrypoint
Usage: $cli_name [command]
Commands:
  migrate   deploy worker
  test      deploy clock
  runserver deploy runserver
  *         Help
"
  exit 1
}

case "$1" in
  migrate)
    python manage.py migrate
    ;;
  test)
    pip install -r requirements_dev.txt --no-cache-dir && pytest -vvs
    ;;
  runserver)
    python manage.py runserver 0.0.0.0:5000
    ;;
  *)
    cli_help
    ;;
esac
