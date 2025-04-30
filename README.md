# speech_therapy_sentence_tool
This project is a specialized tool designed to support speech therapy by helping individuals improve their **reading** and **pronunciation** skills. It allows users to input specific letter combinations and automatically generates words containing those combinations, along with example sentences that incorporate them naturally. This focused approach helps individuals practice challenging phonemes in a meaningful and contextual way, making it especially useful for people with speech or reading difficulties, such as those with dyslexia or articulation disorders.

**Notes:**
- *The sentence creation is done with an OpenAI model, so an OpenAI subscription key is required to execute the code.*
- *The project is designed for the Greek language. To use it with a different language, you must create a new corpus (see instructions below) and update the context and file names used in `run.py` accordingly.*

## Process
The process is structured around 3 componenets:
1. **Corpus Creation**
    - *Goal*: Create a corpus of commonly used words in a given language.
    - *Methodology*: Wikipedia[https://www.wikipedia.org/] articles are collected, and the words are extracted and sorted in descending order of frequency.
2. **Words Selection**
    - *Goal*: Select words that include a specific combination of letters.
    - *Methodology*: A user-defined number of the most frequent words containing the specified letter combination is selected from the corpus. Stemming is used to promote variety.
3. **Sentence Writing**
    - *Goal*: Create simple sentences using the selected words to support reading practice.
    - *Methodology*: A large language model (LLM) is used to generate sentences that naturally incorporate the selected words.

## How to run

### Corpus creation
Before using the tool, a word frequency corpus must be available. You have two options:
1) **Use the provided Greek corpus:**
A pre-built corpus based on [Wikipedia's Greek dump (2025-04-20)](https://dumps.wikimedia.org/elwiki/20250420/) is available at: `Data/corpus/corpus.txt`
2) **Create a new corpus manually:**
To generate a new corpus from a Wikipedia dump:
- Use [WikiExtractor](https://github.com/attardi/wikiextractor/tree/master) to extract text from a Wikipedia dump (follow the instructions in their README).
- Update the `WIKIPEDIA_FOLDER` variable in the `.env` file (see below).
- Run the script with the `--create_corpus` flag as described in the next section.

### Environment Setup (`.env` File)
The script requires several environment variables, which should be defined in a `.env` file. You can create it based on the provided `.env.template`. The required variables are:

- `WIKIPEDIA_FOLDER`: Path to the folder containing the extracted Wikipedia files (AA, AB, etc.). Only needed if creating a new corpus.
- `CORPUS_PATH`: Path to the text file where the word frequency corpus is stored or will be saved.
- `RESULTS_FOLDER`: Folder where the output text file (with the generated words and sentences) will be saved.
- `KEY`: Your OpenAI API key.
- `MODEL`: The name of the language model to use for sentence generation.

### Code execution
Make sure all dependencies listed in `requirements.txt` are installed:
```
pip install -r requirements.txt.
```
You can run the script from the command line with the following syntax:
```
python run.py --comb <letter_combination> --count <number_of_words> [--create_corpus]
```

#### Arguments
- `--comb` (required): The combination of letters to search for in the words .
- `--count` (required): The number of words to select that contain the given letter combination.
- `--create_corpus` (optional): Include this flag only if you want to regenerate the word frequency corpus from Wikipedia data. This process may take some time.

**Example**
```
python run.py --comb στ --count 10 --create_corpus
```
This command will:
- Create the word frequency corpus,
- Select 10 of the most common words that contain the letter combination στ,
- Generate simple sentences using those words.

If there is no need to create the corpus, skip `--create_corpus` to use the existing corpus:
```
python run.py --comb στ --count 10
```