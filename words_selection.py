"""This module selects words for practice that include specific combinations."""
import os
import snowballstemmer

stemmer = snowballstemmer.stemmer('greek')

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
    stems_set = set()
    with open(corpus_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for word in lines:
        if comb in word:
            stem = stemmer.stemWord(word[0])
            if stem in stems_set: # avoid adding words with the same stem to have more variety
                continue
            words.append(word.strip())
            stems_set.add(stem)
            if len(words) >= count:
                break
    print(f"Selected {len(words)} words with the combination '{comb}'")
    return words
