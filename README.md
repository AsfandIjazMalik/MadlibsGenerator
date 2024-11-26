# Madlibs Generator
Python Programming 

# Madlibs Story Generator 
Welcome to the **Madlibs Story Generator**! This interactive Python game allows users to create fun and unique stories by filling in placeholders with different types of words. The game asks the player for specific types of words (like nouns, adjectives, and names) and then generates a personalized story based on those inputs. <br>
## Game Overview
- The game starts by displaying a greeting message and providing the user with a main menu. <br>
- Players can choose to: <br>
  1. Generate a new Madlibs story by filling in placeholders. <br>
  2. Read the game rules to understand how to play. <br>
  3. Exit the game. <br>

### Game Flow

1. **Greeting Message**: The game welcomes the user to the "Madlibs Story Generator." <br>
2. **User Choices**: Users can choose one of the following options: <br>
   - **G** or **1**: Generate a new story. <br>
   - **R** or **2**: Read the game rules. <br>
   - **E** or **3**: Exit the game. <br>
3. **Story Generation**: If the user selects to generate a story: <br>
   - The program reads a story template from a file and identifies placeholders in the format `<placeholder>`.<br>
   - It then prompts the user to provide words that fit each placeholder (e.g., nouns, adjectives, names, places). <br>
   - After collecting the user input, the program generates a unique story with the provided words and displays the final output. <br>

## Python Concepts Used<br>
This project demonstrates several key concepts and techniques in Python: <br>
### 1. **File Handling**
   - The program reads a story template from a text file (`story.txt`) using Python’s built-in `open()` function. <br>
   - The file contents are read using `read()` and processed for placeholders. <br>
### 2. **Loops**
   - A `while True` loop is used for the main menu, allowing the user to repeatedly choose actions until they decide to exit the game. <br>
   - The game will keep asking for user input until a valid option is provided. <br>
### 3. **Conditionals**
   - Conditional statements (`if-elif-else`) are used to handle the user's choice from the main menu and direct them to the appropriate action (either generating a story, displaying rules, or exiting the game). <br>
### 4. **String Manipulation**
   - The story template contains placeholders in the form of `<placeholder>`. These are identified and replaced with user inputs using Python string methods like `replace()`.<br>
   - The program splits the story into individual words, identifies placeholders, and replaces them accordingly. <br>
### 5. **Dictionaries**
   - A dictionary (`user_inputs`) is used to store the user inputs corresponding to each placeholder, making it easy to replace the placeholders with the correct words. <br>
### 6. **User Input**
   - The program uses the `input()` function to ask the user for specific words to replace the placeholders in the story. <br>
********************************************<br>
    WELCOME TO THE STORY GENERATOR<br>
********************************************<br><br>

1. Press G to Generate Story (or press 1) <br>
2. Press R to Read Game Rules (or press 2) <br>
3. Press E to Exit the Game (or press 3) <br><br>

Enter your choice (G/R/E or 1/2/3): 1<br><br>

Enter the word for <adjective>: funny<br>
Enter the word for <noun>: dog<br>
Enter the word for <name>: Alice<br>
Enter the word for <place>: beach<br><br>

