"""This module selects words for practice that include specific combinations."""
import os

def select_words(comb: str, count: int, corpus_path: str) -> list:
    """Selects words for practice that include specific combinations.
    
    Args:
        comb (str): The combination of letters to search for in the words.
        count (int): The number of words to select.
        corpus_path (str): The path to the corpus file.
        
    Returns:
        list: A list of words that include the specified combination.
    """
    corpus_path = os.path.join(corpus_path)
    words = []
    with open(corpus_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if comb in line:
                words.append(line.strip())
                if len(words) >= count:
                    break
    return words
