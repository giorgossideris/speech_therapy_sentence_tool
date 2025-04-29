"""This module creates the corpus by collecting and counting th words from the wikipedia pages."""
import os
import re
from collections import defaultdict

def count_words(wikipedia_folder: str) -> dict:
    """Counts how many times a word appears in the wikipedia pages.
    
    Args:
        wikipedia_folder (str): The folder where the parsed wikipedia pages are stored. 
            The wikipedia folder contains a list of folders, each folder contains a list of files.
            As extracted by: https://github.com/attardi/wikiextractor/tree/master
    Returns:
        dict: A dictionary with the words as keys and the number of times they appear as values.
    """
    word_counter = defaultdict(int)
    for nested_folder in os.listdir(wikipedia_folder):
        print(f"Counting words from: {nested_folder}")
        files = os.listdir(os.path.join(wikipedia_folder, nested_folder))
        for filename in files:
            with open(os.path.join(wikipedia_folder, nested_folder, filename), 'r', encoding='utf-8') as f:
                lines = f.readlines()
            for line in lines:
                # skip the lines that start with '<' (these are the metadata lines)
                if line.startswith('<'):
                    continue
                # find the words in the line and remove the punctuation
                words = re.findall(r'\b\w+\b', line)
                for word in words:
                    word_counter[word] += 1
    
    print("Counting words finished.")
    return word_counter

def clean_corpus(word_counter: dict) -> dict:
    """Cleans the words by removing the words that are too short or too rare and handling case sensitivity.

    To handle case sensitivity, for words that start with a capital letter, compares how often the word appears
    with both a capital and a lowercase first letter, then keeps the version that appears more frequently.
    
    Args:
        word_counter (dict): A dictionary with the words as keys and the number of times they appear as values.
        
    Returns:
        dict: A dictionary with the words as keys and the number of times they appear as values after the cleaning.
    """
    # remove words that are too short or too rare
    words_to_remove = []
    for word in word_counter:
        if len(word) < 5:
            words_to_remove.append(word)
            continue
        if word_counter[word] < 10:
            words_to_remove.append(word)
            continue

    for word in words_to_remove:
        del word_counter[word]
    
    # handle case sensitivity
    words_to_remove = []

    for word in word_counter:
        if word[0].isupper():
            # lower the first letter of the word
            lower_word = word[0].lower() + word[1:]
            if lower_word in word_counter:
                # keep the version that appears more frequently
                if word_counter[word] < word_counter[lower_word]:
                    words_to_remove.append(word)
                    word_counter[lower_word] += word_counter[word]
                else:
                    words_to_remove.append(lower_word)
                    word_counter[word] += word_counter[lower_word]
    
    for word in words_to_remove:
        del word_counter[word]

    print("Cleaning corpus finished.")
    return word_counter

def extract_corpus(word_counter: dict, corpus_path: str) -> None:
    """Creates the corpus by writing the words to a file, in a descending order of frequency.

    Args:
        word_counter (dict): A dictionary with the words as keys and the number of times they appear as values.
        corpus_path (str): The path to the text file where the corpus will be saved.
    """
    # sort the words by frequency
    sorted_words = sorted(word_counter, key=word_counter.get, reverse=True)

    with open(corpus_path, 'w', encoding='utf-8') as f:
        for word in sorted_words:
            f.write(f"{word} {word_counter[word]}\n")
    print("Extracting corpus finished.")

def create_corpus(wikipedia_folder: str, output_folder: str) -> None:
    """Creates the corpus by collecting and counting the words from the wikipedia pages.
    
    Args:
        wikipedia_folder (str): The folder where the parsed wikipedia pages are stored. 
            The wikipedia folder contains a list of folders, each folder contains a list of files.
            As extracted by: https://github.com/attardi/wikiextractor/tree/master
    """
    word_counter = count_words(wikipedia_folder)
    word_counter_cleaned = clean_corpus(word_counter)
    extract_corpus(word_counter_cleaned, output_folder)
