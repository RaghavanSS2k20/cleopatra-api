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

# Example usage
generated_output = """CRIMINAL 1: Alright boys, let's do this.
CRIMINAL 2: Yeah, let's get this money.
(The criminals start robbing the bank. They start putting the money in bags.)
CRIMINAL 3: Hurry up, we don't have all day.
(The criminals finish robbing the bank and start to leave.)
CRIMINAL 4: Let's get out of here.
(The criminals start to leave the bank, but then the Joker appears.)
JOKER: Hold it right there.
(The criminals stop and turn around.)
CRIMINAL 1: Who are you?
JOKER: I'm the one who's going to take all your money.
(The criminals start to laugh.)
CRIMINAL 2: You and what army?
JOKER: This army.
(The Joker pulls out a gun and shoots the criminals. The criminals all fall to the ground, dead.)
JOKER: Now, where's the money?
(The Joker starts to search the criminals for the money.)
JOKER: Aha! Here it is.
(The Joker finds the money and starts to put it in his bag.)
JOKER: Thank you, gentlemen. I'll be taking this.
(The Joker leaves the bank with the money.)"""

character_names = ['CRIMINAL 1', 'CRIMINAL 2', 'CRIMINAL 3', 'CRIMINAL 4', 'JOKER']

cleaned_dialogues = clean_dialogues(generated_output, character_names)
for dialogue in cleaned_dialogues:
    print(dialogue)