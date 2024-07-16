def count_words(text):
    """
    Counts the number of words in a given text.
    
    Parameters:
    text (str): The input text to count words from.

    Returns:
    int: The number of words in the input text.
    """
    # Split the text into words based on whitespace and punctuation
    import re
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def get_user_input():
    """
    Prompts the user to enter a sentence or paragraph.

    Returns:
    str: The user input text.
    """
    return input("Enter a sentence or paragraph: ")

def main():
    """
    Main function to run the word counter program.
    """
    while True:
        user_input = get_user_input().strip()
        
        # Error handling for empty input
        if not user_input:
            print("Error: The input cannot be empty. Please enter some text.")
        else:
            # Count the number of words in the input
            word_count = count_words(user_input)
            
            # Display the word count
            print(f"The number of words in the input text is: {word_count}")
            break

# Entry point of the program
if __name__ == "__main__":
    main()