This code provides a simple text summarization technique using sentence similarity based on cosine distance. Given a text file as input, it generates a summary by extracting the most important sentences from the text.
Setup

To run the code, you will need to have Python and the required packages installed. You can install the necessary packages by using the following commands in your Python environment:

import nltk
nltk.download('stopwords')

**Code Description**

    Importing Libraries: The code starts by importing the required libraries:
        nltk is used for natural language processing tasks.
        numpy is used for numerical computations.
        networkx is used for creating a graph to represent sentence similarity.
        stopwords from nltk.corpus contains common words that can be ignored in the summarization process.

    Function Definitions:
        read_article(file_name): This function reads the input file containing the text and tokenizes the sentences.
        sentence_similarity(sent1, sent2, stopwords=None): This function computes the sentence similarity using cosine distance. It takes two sentences and an optional list of stopwords as input and returns the similarity score.
        gen_sim_matrix(sentences, stop_words): This function generates a similarity matrix for all sentences in the text based on sentence similarity scores.
        generate_summary(file_name, top_n=5): This is the main function that generates the summary. It reads the input file, calculates sentence similarity scores, and then ranks the sentences based on their importance. The top n sentences with the highest scores are selected as the summary.

    Example Usage: The code provides an example usage for generating a summary from a text file. Replace "your_file.txt" with the path to your input text file and set top_n to the desired number of sentences in the summary.

**How to Use**
    Ensure that you have Python and the required libraries installed (as mentioned in the setup section).
    Save the code into a Python script (e.g., text_summarization.py).
    Prepare your input text file (e.g., input.txt) that contains the text you want to summarize.
    Update the generate_summary() function call in the code with your input file path and the desired number of sentences in the summary (top_n).
    Run the script using the following command:
          python text_summarization.py
    The summary will be printed on the console.
