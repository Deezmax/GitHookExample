#!/bin/bash

PYTHONVERSION=$(python -V)

case $PYTHONVERSION in
  Python*3.*)
  echo "$(python -V) is installed"
  chmod +x Python/prepare-commit-msg.py
  python .git/hooks/PythonScripts/prepare-commit-msg.py "$1" "$2" "$3"
  result=$?
  ;;
  *)
  echo "NO PYTHON DETECTED"
  ;;
esac

echo "$result"
#echo "Press something to exit"
#read -r junk

case $result in
  0)
    exit 0
    ;;
  1)
    exit 1
    ;;
  *)
    exit 2
    ;;
esac
