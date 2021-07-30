#!/bin/bash

#test loop
testNum=1
for unittestFile in project/tests/*Tests.py; do

    name=${unittestFile%.py}
    printf "TestFile #$testNum - $name:\n"

    python3 -m coverage run -p $unittestFile -b
    printf "\n\n"

    ((testNum++))
done

# One final coverage report
python3 -m coverage combine
python3 -m coverage report -m
