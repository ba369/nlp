import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def morphology_demo(word):
    print('Rakesh-211211101037');
    print(f"Original Word: {word}")

    # Tokenize the word into individual tokens
    tokens = word_tokenize(word)

    # Apply different stemmers
    porter_stemmer = PorterStemmer()
    lancaster_stemmer = LancasterStemmer()
    snowball_stemmer = SnowballStemmer('english')

    porter_stemmed = [porter_stemmer.stem(token) for token in tokens]
    lancaster_stemmed = [lancaster_stemmer.stem(token) for token in tokens]
    snowball_stemmed = [snowball_stemmer.stem(token) for token in tokens]

    print(f"Porter Stemming: {porter_stemmed}")
    print(f"Lancaster Stemming: {lancaster_stemmed}")
    print(f"Snowball Stemming: {snowball_stemmed}")

if __name__ == "__main__":
    word_to_process = "running"
    morphology_demo(word_to_process)
    

