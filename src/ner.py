from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('../stanford-ner-2020-11-17/classifiers/english.conll.4class.distsim.crf.ser.gz',
					   '../stanford-ner-2020-11-17/stanford-ner.jar',
					   encoding='utf-8')

text = 'New Delhi is having a lot of cases. Help needed. Please contact Umesh for this'

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

for i in classified_text:
    if i[1] == 'LOCATION':
        print(i[0])