from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
from textblob import TextBlob

plurals = ['caresses', 'flies', 'dies', 'mules', 'denied','died', 'agreed', 'owned', 'humbled', 'sized','meeting', 'stating', 'siezing', 'itemization',
 'sensational', 'traditional', 'reference', 'colonizer',
'plotted', 'generously', 'running','pictures']

stemmer1 = SnowballStemmer("english")
stemmer = SnowballStemmer("porter")
stemmer2= TextBlob('flies dies died meeting pictures')

for word in stemmer2.words:
 word.sin

singles = [stemmer.stem(plural) for plural in plurals]
print(' '.join(singles))  # doctest: +NORMALIZE_WHITESPACE

singles = [stemmer1.stem(plural) for plural in plurals]
print(' '.join(singles))  # doctest: +NORMALIZE_WHITESPACE