for unittestFile in *Tests.py; do

    name=${unittestFile%.py}
    printf "$name:\n"

    python3 -m coverage run $unittestFile
    python3 -m coverage report -m

done