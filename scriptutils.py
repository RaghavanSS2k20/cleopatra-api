def getCharectersForBeat(beat, charecterNames, asList):
    keys = charecterNames.keys()
    beatList = beat.split(" ")
    for name in keys:
        print(name.lower())
    presentCharecters = [name.lower() for name in keys if name.lower() in beat.lower().split(' ')]
    print("Hekkekke ",charecterNames, "beat", beat)
    charDesc = ""
    for character in charecterNames:
        charDesc = charDesc + charecterNames[character]
    if(not asList):
        return  charDesc
    else:
        presentCharecters

import re

def clean_dialogues(generated_output, character_names):
    cleaned_dialogues = []
    
    # Define pattern for identifying character names
    character_pattern = '|'.join(map(re.escape, character_names))
    
    # Split the generated output into lines
    lines = generated_output.split('\n')
    
    # Initialize variables to store character name and dialogue
    current_character = None
    current_dialogue = ''
    
    # Process each line
    for line in lines:
        # Check if the line contains a character name
        char_match = re.match(r'^({}): (.*)$'.format(character_pattern), line)
        if char_match:
            # If a new character name is found, save the previous dialogue
            if current_character is not None:
                cleaned_dialogues.append({'charname': current_character, 'dialogue': current_dialogue.strip()})
            # Update current character and dialogue
            current_character = char_match.group(1)
            current_dialogue = char_match.group(2)
        else:
            # If the line doesn't contain a character name, append it to the current dialogue
            current_dialogue += ' ' + line.strip()
    
    # Add the last dialogue
    if current_character is not None:
        cleaned_dialogues.append({'charname': current_character, 'dialogue': current_dialogue.strip()})
    
    return cleaned_dialogues

