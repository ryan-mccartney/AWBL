#!/bin/sh
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
REM cd "C:/Users/Public/Documents/Git Projects/Orion Trail"
while true; do clear; git log -2 | cat; sleep 5 | git log -1 --format=medium > log.txt; exit; done

exit
