def count_words(text):
    """
    Counts the number of words in a given text.
    
    Parameters:
    text (str): The input text to count words from.

    Returns:
    int: The number of words in the input text.
    """
    # Split the text into words based on whitespace
    words = text.split()
    return len(words)

def main():
    """
    Main function to run the word counter program.
    """
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: The input cannot be empty. Please enter some text.")
    else:
        # Count the number of words in the input
        word_count = count_words(user_input)
        
        # Display the word count
        print(f"The number of words in the input text is: {word_count}")

# Entry point of the program
if __name__ == "__main__":
    main()