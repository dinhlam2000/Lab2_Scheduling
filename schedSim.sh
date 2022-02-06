#!/usr/bin/env bash

while getopts p:q: option
do
case "${option}"
in
p) algorithm=${OPTARG};;
q) quantum=${OPTARG};;
esac
done

python3 ./main.py $1 -p "$algorithm" -q "$quantum"