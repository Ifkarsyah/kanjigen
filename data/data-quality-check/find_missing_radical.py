from helper import *

joyo = get_data_joyo()
concept = get_data_kanji_concept()
radical = get_data_radical()

res = (joyo & concept) - (joyo & concept & radical)

print(res)