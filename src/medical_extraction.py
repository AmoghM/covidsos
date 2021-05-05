import spacy

med7 = spacy.load("en_core_med7_lg")

# create distinct colours for labels
col_dict = {}
seven_colours = ['#e6194B', '#3cb44b', '#ffe119', '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']
for label, colour in zip(med7.pipe_labels['ner'], seven_colours):
    col_dict[label] = colour

options = {'ents': med7.pipe_labels['ner'], 'colors':col_dict}

text = 'Urgently looking for remdesvir of 400 mg for the next 5 days for a patient in New Delhi. Plasma donor on B+ blood group reach out to us. Blood donation of O- needed.'
doc = med7(text)

spacy.displacy.render(doc, style='ent', jupyter=True, options=options)

res = [(ent.text, ent.label_) for ent in doc.ents]
print(res)
