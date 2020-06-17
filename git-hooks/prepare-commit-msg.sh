#!/bin/sh

checkExitCondition() {
  if [[ $VAR != 0 ]]
  then
    echo "1"
  else
    echo "0"
  fi
}

if [[ "$(python3 -V)" =~ "Python 3" ]];
then
  echo "$(python3 -V) is installed"
  python3 prepare-commit-msg.py
  exit "$(checkExitCondition $?)"
  goto
elif [[ "$(python -V)" =~ "Python" ]];
then
  echo "$(python -V) is installed"
else
  exit 1
fi