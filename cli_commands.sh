#!/bin/bash

git_color_text(){
    text=$1
    gum style --foreground "#f14e32" "$text"
}

gum style --border double --margin "1" --padding "1" --border-foreground "#f14e32" "CLI $(git_color_text "COMMAND" ) INTERFACE" 
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