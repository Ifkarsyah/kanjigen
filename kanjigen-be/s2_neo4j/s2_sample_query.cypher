CALL db.schema.visualization;

MATCH (k: Kanji)-[r]->(t) 
RETURN k,r,t 
LIMIT 100;
