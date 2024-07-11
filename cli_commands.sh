#!/bin/bash

while true; do
cd CLI
CHOOSE=$(gum choose "cli table" "cli logging" "cli viewers json ./data/test.json -n 25" "exit")
if [[ $CHOOSE == "exit" ]];
then
    break
fi
$CHOOSE
# SCOPE=$(gum input --placeholder "W8 for once" )
done

exec cli hello