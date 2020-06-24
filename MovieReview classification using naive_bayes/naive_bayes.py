sample_review="""I loved this movie since I was 7 and I saw it on the opening day. It was so touching and beautiful. I strongly recommend seeing for all. It's a movie to watch with your family by far.<br /><br />My MPAA rating: PG-13 for thematic elements, prolonged scenes of disastor, nudity/sexuality and some language."""

import sys
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords       # by default it provides us with the english language

tokenizer=RegexpTokenizer(r'\w+')
en_stopwords=set(stopwords.words("english"))
ps=PorterStemmer()

def cleanedreviews(review):
    review=review.lower()
    review=review.replace("<br /><br />"," ")
# tokenize
    tokens=tokenizer.tokenize(review)
# filterout stopwords
    new_tokens=[token for token in tokens if token not in en_stopwords]
    stemmed_tokens=[ ps.stem(token) for token in new_tokens]
    cleaned_review=" ".join(stemmed_tokens)
    return cleaned_review

cleanedreviews(sample_review)

def cleaneddoc(inputfile,outputfile):
    out=open(outputfile,'w',encoding="utf8")
    
    with open(inputfile,encoding="utf8") as f:
        reviews=f.readlines()
    for review in reviews:
        cleaned_review=cleanedreviews(review)
        print((cleaned_review),file=out)
    out.close()     

# Read commandline arguments
#inputfile=sys.argv[1]
#outputfile=sys.argv[2]
#cleaneddoc(inputfile,outputfile)