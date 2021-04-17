from pprint import pprint
import csv

data = dict()

with open('../web-wiki-joyo/kanji_joyo_output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)  # skip the headers
    for row in csv_reader:
        num, kanji, meaning = row
        data[kanji] = {"num": num, "meaning": meaning}

assert len(data) == 2136

with open('../csv-radical/radicals_output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)  # skip the headers
    for row in csv_reader:
        kanji, radical_list = row
        if kanji in data:
            data[kanji]['radicals'] = radical_list

with open('../web-wiki-kanji-concept/kanji_concept_output_step_2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)  # skip the headers
    for row in csv_reader:
        kanji, meaning, concept, subconcept = row
        if kanji in data:
            data[kanji]["kanji_in_concept_meaning"] = meaning
            data[kanji]["concept"] = concept
            data[kanji]["subconcept"] = subconcept


data = sorted(data.items(), key=lambda x: int(x[1]["num"]))

data = [{
    'num': v['num'],
    'kanji': k,
    'meaning': v.get('meaning'),
    'radicals': v.get('radicals'),
    'kanji_in_concept_meaning': v.get('kanji_in_concept_meaning'),
    'h2_concept': v.get('h2_concept'),
    'h3_concept': v.get('h3_concept'),
} for k, v in data]


with open('kanji_total_1_raw.csv', mode='w') as file:
    attribs = ['num', 'meaning', 'radicals',
               'kanji_in_concept_meaning', 'h2_concept', 'h3_concept']
    fieldnames = ['kanji'] + attribs
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
