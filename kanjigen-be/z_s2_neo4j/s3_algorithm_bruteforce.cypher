// https://neo4j.com/docs/cypher-manual/current/clauses/foreach/
// https://neo4j.com/docs/cypher-manual/current/clauses/call-subquery/
// https://neo4j.com/docs/cypher-manual/current/clauses/union/
// https://neo4j.com/docs/cypher-manual/current/clauses/unwind/


// https://neo4j.com/docs/cypher-manual/current/functions/predicate/
// https://neo4j.com/docs/cypher-manual/current/functions/aggregating/
// https://neo4j.com/docs/cypher-manual/current/functions/list/

// https://neo4j.com/docs/cypher-manual/current/functions/list/#functions-nodes

// Step 1: Generate cross-product
WITH 
    [1,2,3] AS input_list, 
    [4,5,6] AS output_list
UNWIND input_list AS in
UNWIND output_list AS out
RETURN in,out;

// Step 2: Shortest Path
// https://khalidabuhakmeh.com/use-neo4j-to-find-the-shortest-path
// https://stackoverflow.com/questions/33185425/cypher-find-shortest-path-between-two-nodes-identified-by-their-ids
MATCH (k1:Kanji { value: '怨' }),(k2:Kanji { value: '浦' }), 
path = shortestPath((k1)-[*..15]-(k2))
RETURN path;

// Step 1 + Step 2 Combined
WITH 
    ['怨','姻','桜'] AS input_list, 
    ['浦','奥','媛'] AS output_list
UNWIND input_list AS kin
UNWIND output_list AS kout
WITH kin,kout
MATCH (k1:Kanji { value: kin }),(k2:Kanji { value: kout }), 
path = shortestPath((k1)-[*..15]-(k2))
RETURN path;
