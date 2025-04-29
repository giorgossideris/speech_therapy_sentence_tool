"""Module to run the speech therapy sentence generation tool."""
import argparse
import os
from dotenv import dotenv_values
from openai import OpenAI
from corpus_creation import create_corpus
from sentence_writing import write_sentences
from words_selection import select_words

config = dotenv_values()

def run(to_create_corpus: bool, comb: str, count: int):
    """Main function to run the speech therapy sentence generation tool."""
    if to_create_corpus:
        # Create the corpus from the Wikipedia pages
        create_corpus(config["WIKIPEDIA_FOLDER"], config["CORPUS_PATH"])
    # select the words from the corpus that include the combination
    words = select_words(comb, count, config["CORPUS_PATH"])

    # create the OpenAI client
    client = OpenAI(api_key=config["KEY"])
    
    # write the sentences using the selected words
    sentences = write_sentences(words, client, config["MODEL"])

    # save the sentences to a file
    results_path = os.path.join(config["RESULTS_FOLDER"], f"λέξεις_με_{comb}.txt")
    with open(results_path, 'w', encoding='utf-8') as f:
        f.write(f"Λέξεις με {comb}:\n")
        for word in words:
            f.write(f"{word}\n")
        f.write("\n\n")
        f.write("Προτάσεις:\n")
        for sentence in sentences:
            f.write(f"{sentence}\n")
    print(f"Results saved to {results_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Speech Therapy Sentence Generation Tool")
    parser.add_argument("--create_corpus", action="store_false", help="Create the corpus from Wikipedia pages. Use it only for the first time.")
    parser.add_argument("--comb", type=str, required=True, help="The combination of letters to search for in the words")
    parser.add_argument("--count", type=int, required=True, help="The number of words to select")
    args = parser.parse_args()

    run(not args.create_corpus, args.comb, args.count)



    
