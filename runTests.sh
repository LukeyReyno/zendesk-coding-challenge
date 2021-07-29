#!/bin/bash

#test loop
testNum=1
for unittestFile in *Tests.py; do

    name=${unittestFile%.py}
    printf "TestFile #$testNum - $name:\n"

    python3 -m coverage run $unittestFile
    python3 -m coverage report -m

    ((testNum++))
    printf "\n\n\n"
done