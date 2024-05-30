import nltk
from nltk.corpus import brown
import nltk
nltk.download('brown')

print("Rakesh-211211101037")

# Training data
sentences = brown.tagged_sents()[:5000]

# Create tag frequency distribution and transition probability matrix
tag_freq = nltk.FreqDist(tag for sentence in sentences for word, tag in sentence)
transition_prob = nltk.ConditionalFreqDist(
    (tag1, tag2) for sentence in sentences for (_, tag1), (_, tag2) in nltk.bigrams(sentence))

# Define Viterbi function
def viterbi(sentence, tag_freq, transition_prob):
    # Initialize first word probabilities
    v = [{}]
    for tag in tag_freq:
        v[0][tag] = {"prob": tag_freq[tag] / len(sentences), "prev": None}

    # Recursion step
    for i in range(1, len(sentence)):
        v.append({})
        for tag in tag_freq:
            max_prob = max(v[i - 1][prev_tag]["prob"] * transition_prob[prev_tag][tag] * tag_freq[tag] / len(sentences)
                           for prev_tag in tag_freq)
            for prev_tag in tag_freq:
                if v[i - 1][prev_tag]["prob"] * transition_prob[prev_tag][tag] * tag_freq[tag] / len(sentences) == max_prob:
                    v[i][tag] = {"prob": max_prob, "prev": prev_tag}
                    break

    # Termination step
    max_prob = max(v[-1][tag]["prob"] for tag in tag_freq)
    current_tag = None
    for tag, data in v[-1].items():
        if data["prob"] == max_prob:
            current_tag = tag
            break

    # Backtracking
    tags = [current_tag]
    for i in range(len(v) - 1, 0, -1):
        current_tag = v[i][current_tag]["prev"]
        tags.append(current_tag)
    tags.reverse()
    return list(zip(sentence, tags))

# Example usage
sentence = "The quick brown fox jumps over the lazy dog".split()
pos_tags = viterbi(sentence, tag_freq, transition_prob)
print(pos_tags)





