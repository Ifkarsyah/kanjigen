from helper import *

import matplotlib.pyplot as plt
import matplotlib_venn as venn

data_kanji_joyo = get_data_joyo()
data_csv_radical = get_data_radical()
data_kanji_concept = get_data_kanji_concept()

print('kanji_joyo', len(data_kanji_joyo))
print('csv_radical', len(data_csv_radical))
print('kanji_concept', len(data_kanji_concept))

venn.venn3_unweighted(
    [data_kanji_joyo, data_csv_radical, data_kanji_concept],
    set_labels=('Kanji Joyo', 'CSV Radical', 'Kanji Concept'),
    set_colors=('blue', 'green', 'yellow')
)
plt.savefig('venn_data.png')
