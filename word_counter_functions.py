def get_sentence_input() -> str:
    """
    Prompts the user to enter a sentence.
    
    Returns:
        str: The sentence entered by the user.
    """
    sentence = input("Enter a sentence: ")
    return sentence


def count_words(sentence: str) -> int:
    """
    Counts the number of words in a given sentence.
    
    Parameters:
        sentence (str): The sentence to count words in.
    
    Returns:
        int: The number of words in the sentence.
    """
    words = sentence.split()  
    return len(words)


def main() -> None:
    """
    Main function to execute the word counting program.
    It calls get_sentence_input() to get the sentence and count_words() to count the words.
    """
    sentence = get_sentence_input()  
    word_count = count_words(sentence)  
    print(f"The sentence has {word_count} words.")  


if __name__ == "__main__":
    main()