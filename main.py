# Greeting message
print('********************************************\n'
      '\tWELCOME TO THE STORY GENERATOR\n'
      '********************************************\n')

# Function to display the game rules
def display_game_rules():
    """
    This function displays the rules of the Madlibs game.
    It explains how the user should provide words to fill in placeholders 
    in the Madlibs story.
    """
    print("\nGAME RULES:\n"
          "1. The Madlibs story contains placeholders that need to be filled with specific types of words.\n"
          "2. The placeholders are wrapped in '<>' symbols (e.g., <adjective>, <noun>, <name>, <place>).\n"
          "3. You will be prompted to enter a word for each placeholder.\n"
          "4. Enter the word according to the category requested:\n"
          "   - For '<adjective>', provide a word that describes something (e.g., beautiful, tall).\n"
          "   - For '<noun>', provide a person, place, or thing (e.g., dog, city, apple).\n"
          "   - For '<name>', provide a proper name (e.g., John, Alice).\n"
          "   - For '<place>', provide a location (e.g., park, beach).\n"
          "5. Once all the placeholders are filled, the program will replace them with your words.\n"
          "6. The result will be a funny and unique story with the words you've provided.\n"
          "7. Have fun and enjoy the creative story you've made!\n")

# Function to generate the Madlibs story
def generate_madlibs_story():
    """
    This function reads the story from a file, identifies the placeholders (words inside '<>'),
    prompts the user to fill them, and then generates a story by replacing the placeholders 
    with the user's input.
    """
    # Reading the story from the file
    with open('story.txt', 'r') as story_file:
        story_content = story_file.read()

    # Splitting the story into individual words
    words_in_story = story_content.split()  # Read story by words
    placeholder_words = set()  # Set to store words with placeholders

    # Identifying words that start with '<' and end with '>'
    for word in words_in_story:
        if word.startswith('<') and word.endswith('>'):
            placeholder_words.add(word)

    # Dictionary to store user input for the placeholders
    user_inputs = {}

    # Asking the user for words to replace placeholders
    for placeholder in placeholder_words:
        user_input = input(f'Enter the word for {placeholder}: ')
        user_inputs[placeholder] = user_input

    # Replacing the placeholders in the story with user input
    for placeholder in placeholder_words:
        story_content = story_content.replace(placeholder, user_inputs[placeholder])

    # Displaying the final modified story
    print(f'\n{story_content}')

# Main menu loop
while True:
    """
    The main loop of the game. It asks the user for their choice to generate a story, 
    read the game rules, or exit the game.
    """
    user_choice = input('1. Press G to Generate Story (or press 1)\n'
                        '2. Press R to Read Game Rules (or press 2)\n'
                        '3. Press E to Exit the Game (or press 3)\n\n'
                        'Enter your choice (G/R/E or 1/2/3): ').lower()
    
    # Calling the corresponding function based on the user's input
    if user_choice in ['r', '2']:
        display_game_rules()  # Display the game rules
    elif user_choice in ['g', '1']:
        generate_madlibs_story()  # Generate and display the Madlibs story
    elif user_choice in ['e', '3']:
        print('You have exited the game. See you next time!\nTHANK YOU :)')
        break  # Exit the game
    else:
        print('Invalid input. Please enter a valid option.\n')  # Invalid input handling