upsert_material = (
    'WITH $terms as terms_map '
    'MERGE (item:%s {_id: $id}) '
    'SET item += $props '
    'SET item.update = timestamp()'
    'FOREACH(term in keys(terms_map) | '
    'MERGE(ter:Term {term:toLower(term)}) '
    'MERGE (ter)<-[r:HAS]-(item) '
    'SET r.quantity = terms_map[term]'
    'SET r.update = timestamp())')

remove_terms = (
    'MATCH (item:%s {_id: $id})-[r:HAS]->(term:Term) '
    'WHERE r.update < item.update '
    'SET term.occurrences = term.occurrences - 1 '
    'DELETE r '
    'WITH term WHERE term.occurrences = 0 '
    'DELETE term'
)

insert_count = (
    'MATCH (:%s {_id: $id})-[:HAS]->(term:Term) '
    'MATCH (term)<-[:HAS]-(item) where item:Material or item:Question '
    'WITH  term, count(item) as ocorr '
    'SET term.occurrences = ocorr'
)

insert_question = (
    'CREATE (question:Question $props) '
    'SET question._id = "re_question." + toString(id(question))'
)

get_raw_questions = (
    'MATCH (question:Question) '
    'WHERE NOT exists((question)-[:HAS]->(:Term)) '
    'RETURN question '
)

get_questions = (
    'MATCH (question :Question) '
    'WHERE exists((question)-[:HAS]->(:Term)) '
    'RETURN question {.topic, ._id, .alternatives, .stem}'
)

get_questions_by_id = (
    'MATCH (question :Question) '
    'WHERE question._id in $id_list AND exists((question)-[:HAS]->(:Term)) '
    'RETURN question {.topic, ._id, .alternatives, .stem}'
)

get_questions_all_topics = (
    'MATCH (question:Question) '
    'WHERE exists((question)-[:HAS]->(:Term)) '
    'RETURN question.topic as topic, collect(question._id) as id_list'
)

get_questions_topics = (
    'MATCH (question:Question) '
    'WHERE exists((question)-[:HAS]->(:Term)) and question.topic in $topic_list '
    'RETURN question.topic as topic, collect(question._id) as id_list'
)

get_answers = (
    'MATCH(question :Question) '
    'WHERE question._id in $id_list '
    'RETURN question._id as id, question.correct_alt as correct_alt'
)

get_similar_materials = (
    'MATCH (item) '
    'WHERE item:Material or item:Question '
    'WITH count(item) as N '

    'WITH N, $question_id_list as questions_ids '
    'MATCH (question:Question) '
    'WHERE question._id in questions_ids '
    'WITH  N, collect(question) as question_list '

    'UNWIND question_list as question '
    'MATCH (question)-[r1:HAS]->(term:Term) '
    'WITH N, question_list, term, '
    '((log10(sum(r1.quantity))/log10(2))+1.0) as tf1, '
    'log10(N/(term.occurrences*1.0))/log10(2) as idf1 '
    'WITH N, question_list, sum(tf1*idf1) as sum_tf_idf1 '

    'UNWIND question_list as question '
    'MATCH (question)-[r1:HAS]->(term:Term)<-[r2:HAS]-(mat:Material) '
    'WITH N, mat, sum_tf_idf1, term, '
    '((log10(sum(r1.quantity))/log10(2))+1.0) as tf1, '
    '((log10(r2.quantity)/log10(2))+1.0) as tf2,  '
    'log10(N/(term.occurrences*1.0))/log10(2) as idf '
    'WITH N, mat, sum(tf1*tf2*idf*idf) as num, sum_tf_idf1 '

    'MATCH (mat)-[r2:HAS]->(term:Term) '
    'WITH mat, num, sum_tf_idf1, term, '
    '((log10(r2.quantity)/log10(2))+1.0) as tf2, '
    'log10(N/(term.occurrences*1.0))/log10(2) as idf2 '
    'WITH mat, num, sum_tf_idf1, sum(tf2*idf2) as sum_tf_idf2 '

    'WITH mat, num / sqrt(sum_tf_idf1*sum_tf_idf2) as similarity '
    'RETURN mat { .* , similarity} '
    'ORDER by similarity desc '
)
