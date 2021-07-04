CALL db.schema.visualization;

MATCH (k: Kanji)-[r]->(t) 
RETURN k,r,t 
LIMIT 100;


// https://neo4j.com/docs/cypher-manual/current/clauses/match/
// https://neo4j.com/docs/cypher-manual/current/clauses/create/
// https://neo4j.com/docs/cypher-manual/current/clauses/merge/
// https://neo4j.com/docs/cypher-manual/current/clauses/return/

// https://neo4j.com/docs/cypher-manual/current/clauses/with/
// https://neo4j.com/docs/cypher-manual/current/clauses/where/

// https://neo4j.com/docs/cypher-manual/current/clauses/delete/

// https://neo4j.com/docs/cypher-manual/current/clauses/call/