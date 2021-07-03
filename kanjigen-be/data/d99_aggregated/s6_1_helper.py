import csv


def get_data_joyo():
    data_kanji_joyo = set()
    with open("s1_input_d1_kanji_joyo.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)  # skip the headers
        for row in csv_reader:
            num, kanji, meanings, grade, jlpt, readings, unicode = row
            data_kanji_joyo.add(kanji)
    return data_kanji_joyo


def get_data_radical():
    data_csv_radical = set()
    with open("s1_input_d2_radicals.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)  # skip the headers
        for row in csv_reader:
            kanji, radical_list = row
            data_csv_radical.add(kanji)
    return data_csv_radical


def get_data_kanji_theme():
    data_kanji_theme = set()
    with open("s1_input_d3_theme.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader, None)  # skip the headers
        for row in csv_reader:
            kanji, _, _, _ = row
            data_kanji_theme.add(kanji)
    return data_kanji_theme
