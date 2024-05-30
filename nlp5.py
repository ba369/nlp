from collections import Counter 
import numpy as np 
# Define corpus 
corpus = "the quick brown fox jumps over the lazy dog" 
# Create unigrams 
unigrams = Counter(corpus.split()) 
# Define function to compute n-grams 
def get_ngrams(sentence, n): 
    return [tuple(sentence[i:i+n]) for i in range(len(sentence)-n+1)] 
# Create bigrams 
bigrams = Counter(get_ngrams(corpus.split(), 2)) 
# Define smoothing function 
def add_k_smoothing(ngram_counts, k, n_1gram_counts): 
    # Calculate total number of n-grams 
    total_ngrams = sum(ngram_counts.values()) 
    # Calculate vocabulary size 
    vocabulary_size = len(n_1gram_counts) 
    # Calculate denominator for probability calculation 
    denominator = total_ngrams + k*vocabulary_size 
    # Calculate smoothed probabilities 
    probabilities = {} 
    for ngram, count in ngram_counts.items(): 
        probabilities[ngram] = (count + k) / denominator 
    # Handle unseen n-grams 
    for ngram in set(n_1gram_counts.keys()) - set(ngram_counts.keys()): 
        probabilities[ngram] = k / denominator 
    return probabilities 
# Apply smoothing to bigrams 
k = 1 
bigram_probabilities = add_k_smoothing(bigrams, k, unigrams) 
# Print results 
for bigram, probability in bigram_probabilities.items(): 
    print(bigram, probability) 
    