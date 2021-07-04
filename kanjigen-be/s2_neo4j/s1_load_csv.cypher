LOAD CSV WITH HEADERS FROM "file:///s7_kanji_total_clean.csv" AS row
MERGE (k:Kanji {value: row["kanji"]})


WITH row, k
UNWIND split(row["meaning"], ":") AS meaning
MERGE (m:Meaning {value: meaning})
WITH row, k, m
MERGE (k)-[:HAS_MEANING]->(m)


WITH row, k
UNWIND split(row["radicals"], ":") AS radical
MERGE (r:Radical {value: radical})
WITH row, k, r
MERGE (k)-[:HAS_RADICAL]->(r)


WITH row, k
WHERE row["theme"] IS NOT NULL
MERGE (t:Theme {value: row["theme"]})
WITH row, k, t
MERGE (k)-[:HAS_THEME]->(t)


WITH row, k
WHERE row["subtheme"] IS NOT NULL
MERGE (s:Subtheme {value: row["subtheme"]})
WITH row, k, s
MERGE (k)-[:HAS_SUBTHEME]->(s)

RETURN count(row);
