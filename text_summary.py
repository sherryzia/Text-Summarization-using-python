import nltk
# nltk.download('stopwords')
nltk.download('punkt')
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize  # Import sentence tokenizer

def read_article(file_name):
    file = open(file_name, "r")
    text = file.read()
    sentences = sent_tokenize(text)
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
    sent1 = [w.lower() for w in sent1 if w.lower() not in stopwords]
    sent2 = [w.lower() for w in sent2 if w.lower() not in stopwords]
    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for w in sent1:
        vector1[all_words.index(w)] += 1
    
    for w in sent2:
        vector2[all_words.index(w)] += 1
    return 1 - cosine_distance(vector1, vector2)

def gen_sim_matrix(sentences,stop_words):
    similarity_matrix=np.zeros((len(sentences),len(sentences)))
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1==idx2:
                continue
            similarity_matrix[idx1][idx2]=sentence_similarity(sentences[idx1],sentences[idx2],stop_words)
    return similarity_matrix
        
def generate_summary(file_name, top_n=5):
    stop_words = stopwords.words('english')
    summarize_text = []
    sentences = read_article(file_name)
    sentence_similarity_matrix = gen_sim_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    # Check if ranked_sentences is not empty
    if ranked_sentences:
        for i in range(min(top_n, len(ranked_sentences))):
            summarize_text.append("".join(ranked_sentences[i][1]))
        print("Summary:\n", ". ".join(summarize_text))
    else:
        print("No sentences to summarize.")

generate_summary('text.txt',3)