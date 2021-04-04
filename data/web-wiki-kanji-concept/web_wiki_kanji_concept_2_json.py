import json
import csv

kanji_header = 'kanji_list'

results = [] # (kanji, meaning) -> (h2_concept, h3_concept, h4_concept)

with open('kanji_concept_intermediate.json') as file:
    data = json.load(file)
    
    for h2 in data:

        if len(data[h2]) == 0:
            continue

        for h3 in data[h2]:
            # only h2
            if h3 == kanji_header:
                kanji_list = data[h2][kanji_header]
                results += [{'kanji': k['kanji'], 'meaning': k['meaning'],'h2': h2, 'h3': None, 'h4': None} for k in kanji_list]
                continue

            for h4 in data[h2][h3]:
                # only h2,h3
                if h4 == kanji_header:
                    kanji_list = data[h2][h3][kanji_header]
                    results += [{'kanji': k['kanji'], 'meaning': k['meaning'],'h2': h2, 'h3': h3, 'h4': None} for k in kanji_list]
                    continue
                
                kanji_list = data[h2][h3][h4].get(kanji_header)
                if not kanji_list: continue
                results += [{'kanji': k['kanji'], 'meaning': k['meaning'],'h2': h2, 'h3': h3, 'h4': h4} for k in kanji_list]



with open('kanji_concept_output.csv', mode='w') as file:
    fieldnames = ['kanji', 'meaning', 'h2', 'h3', 'h4']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

    