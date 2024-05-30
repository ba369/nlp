import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
text=nltk.word_tokenize("And now for Everything completely Same")
print(nltk.pos_tag(text))
print("Rakesh-211211101037")