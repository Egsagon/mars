#! /bin/bash
# read -s -n 1 key

while :; do
    read -s -n 1 key
    echo $key
done

# if [[ "$key" == "your key" ]]; then
#     #your script here
# fi
