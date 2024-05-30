import re
from nltk.util import ngrams
s ="Machine learning is an important part of AI""and AI is going to become inmporant for daily functionong"
tokens=[token for token in s.split(" ")]
output =list(ngrams(tokens,2))
print(output)
print("Rakesh-211211101037")
