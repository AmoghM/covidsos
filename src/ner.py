from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('../stanford-ner-2020-11-17/classifiers/english.conll.4class.distsim.crf.ser.gz',
					   '../stanford-ner-2020-11-17/stanford-ner.jar',
					   encoding='utf-8')

def get_ner(text):
    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)
    return classified_text