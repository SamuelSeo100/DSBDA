from nltk.stem import PorterStemmer
#from nltk.stem.snowball import SnowballStemmer
from nltk.stem import LancasterStemmer

ps = PorterStemmer()
ls = LancasterStemmer()
#ss = SnowballStemmer()

word = 'Streaming'

print(ps.stem(word))
print(ls.stem(word))
#print(ss.stem(word))
