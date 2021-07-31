from s6_1_helper import *

import matplotlib.pyplot as plt
import matplotlib_venn as venn

data_kanji_joyo = get_data_joyo()
data_csv_radical = get_data_radical()
data_kanji_theme = get_data_kanji_theme()

print("kanji_joyo", len(data_kanji_joyo))
print("csv_radical", len(data_csv_radical))
print("kanji_theme", len(data_kanji_theme))

venn.venn3_unweighted(
    [data_kanji_joyo, data_csv_radical, data_kanji_theme],
    set_labels=("Kanji Joyo", "CSV Radical", "Kanji Theme"),
    set_colors=("blue", "green", "yellow"),
)
plt.savefig("s6_3_venn_data.png")
