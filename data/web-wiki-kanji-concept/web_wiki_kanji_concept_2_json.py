import json
import csv

kanji_header = 'kanji_list'

results = []  # (kanji, meaning) -> (h2_concept, h3_concept)

with open('kanji_concept_output_step_1.json') as file:
    data = json.load(file)

    for h2 in data:

        if len(data[h2]) == 0:
            continue

        for h3 in data[h2]:
            # only h2
            if h3 == kanji_header:
                kanji_list = data[h2][kanji_header]
                results += [{'kanji': k['kanji'], 'meaning': k['meaning'],
                             'concept': h2, 'subconcept': None} for k in kanji_list]
                continue

            for h4 in data[h2][h3]:
                # only h2,h3
                if h4 == kanji_header:
                    kanji_list = data[h2][h3][kanji_header]
                    results += [{'kanji': k['kanji'], 'meaning': k['meaning'],
                                 'concept': h2, 'subconcept': h3} for k in kanji_list]
                    continue


with open('kanji_concept_output_step_2.csv', mode='w') as file:
    fieldnames = ['kanji', 'meaning', 'concept', 'subconcept']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)
