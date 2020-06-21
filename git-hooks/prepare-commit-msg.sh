#!/bin/bash

PYTHONVERSION=$(python -V)

case $PYTHONVERSION in
  *3.*)
  echo "$(python -V) is installed"
  chmod +x .git/hooks/prepare-commit-msg.py
  python .git/hooks/prepare-commit-msg.py
  result=$?
  ;;
  *2.*)
  echo "$(python -V) is installed"
  chmod +x .git/hooks/prepare-commit-msg.py
  python .git/hooks/prepare-commit-msg.py
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
