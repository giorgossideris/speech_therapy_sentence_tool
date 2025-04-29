"""This module creates sentences for practice using specific words."""
from openai import OpenAI

SYSTEM_MESSAGE = """Είσαι ένας δάσκαλος ελληνικών. 
Η δουλειά σου είναι να φτιάχνεις προτάσεις με τις λέξεις που σου δίνω. 
Οι προτάσεις πρέπει να είναι απλές και σύντομες και θα χρησιμοποιηθούν για να βοηθήσουν μικρά παιδιά στην ανάγνωση. 
Να χρησιμοποιείς τη λέξη ακριβώς στη μορφή και την κλίση που σου τη δίνω. Πρόσεξε ειδικά αν η λέξη είναι στη γενική, να φτιάξεις σωστή πρόταση."""

def call_gpt(
    client: OpenAI,
    model: str,
    system_message: str,
    query: str,
    temperature: int=0.5, 
) -> str:
    """Calls the GPT model to generate a response.

    Args:
        client (OpenAI): The GPT client
        model (str): The name of the GPT model
        system_message (str): The system message to provide context to the model
        query (str): The query to send to the model
        temperature (int): The temperature for the model response

    Returns:
        The response of the GPT model
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": query}
            ],
        temperature=temperature
    )
    return response.choices[0].message.content

def write_sentences(words: list, client: OpenAI, model: str) -> list:
    """Writes sentences using the words provided.

    Args:
        words (list): The list of words to use in the sentences.
        client (OpenAI): The GPT client
        model (str): The name of the GPT model
    
    Returns:
        list: A list of sentences generated using the words provided.
    """
    sentences = []
    for word in words:
        query = f"λέξη: {word}."
        response = call_gpt(client, model, SYSTEM_MESSAGE, query, 0.8)
        sentences.append(response.strip())
    print(f"Generated {len(sentences)} sentences.")
    return sentences
