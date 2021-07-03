import csv


def get_data_joyo():
    data_kanji_joyo = set()
    with open('../web-wiki-joyo/kanji_joyo_output.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)  # skip the headers
        for row in csv_reader:
            num, kanji, meaning = row
            data_kanji_joyo.add(kanji)
    return data_kanji_joyo


def get_data_radical():
    data_csv_radical = set()
    with open('../csv-radical/radicals_output.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)  # skip the headers
        for row in csv_reader:
            kanji, radical_list = row
            data_csv_radical.add(kanji)
    return data_csv_radical


def get_data_kanji_concept():
    data_kanji_concept = set()
    with open('../web-wiki-kanji-concept/kanji_concept_output_step_2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)  # skip the headers
        for row in csv_reader:
            kanji, _, _, _ = row
            data_kanji_concept.add(kanji)
    return data_kanji_concept
