import csv

import matplotlib.pyplot as plt
import matplotlib_venn as venn

data_kanji_joyo = set()
with open('../web-wiki-joyo/kanji_joyo_output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)  # skip the headers
    for row in csv_reader:
        num, kanji, meaning = row
        data_kanji_joyo.add(kanji)

data_csv_radical = set()
with open('../csv-radical/radicals_output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)  # skip the headers
    for row in csv_reader:
        kanji, radical_list = row
        data_csv_radical.add(kanji)

data_kanji_concept = set()
with open('../web-wiki-kanji-concept/kanji_concept_output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)  # skip the headers
    for row in csv_reader:
        kanji,meaning,h2,h3,h4 = row
        data_kanji_concept.add(kanji)

print('kanji_joyo', len(data_kanji_joyo))
print('csv_radical', len(data_csv_radical))
print('kanji_concept', len(data_kanji_concept))


venn.venn3_unweighted(
    [data_kanji_joyo,data_csv_radical, data_kanji_concept],
    set_labels=('Kanji Joyo','CSV Radical', 'Kanji Concept'),
    set_colors=('blue', 'green', 'yellow')
)
plt.savefig('venn_data.png')