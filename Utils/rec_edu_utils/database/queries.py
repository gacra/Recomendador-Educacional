upsert_material = (
    'WITH $termos as map_termos '
    'MERGE (item:%s {_id: $id}) '
    'SET item += $props '
    'SET item.atualizacao = timestamp()'
    'FOREACH(termo in keys(map_termos) | '
        'MERGE(ter:Termo {termo:toLower(termo)}) '
        'MERGE (ter)<-[r:POSSUI]-(item) '
        'SET r.quantidade = map_termos[termo]'
        'SET r.atualizacao = timestamp())')

remover_termos = (
    'MATCH (item:%s {_id: $id})-[r:POSSUI]->(termo:Termo) '
    'WHERE r.atualizacao < item.atualizacao '
    'SET termo.ocorrencias = termo.ocorrencias - 1 '
    'DELETE r '
    'WITH termo WHERE termo.ocorrencias = 0 '
    'DELETE termo'
)

inserir_contagem = (
    'MATCH (:%s {_id: $id})-[:POSSUI]->(termo:Termo) '
    'MATCH (termo)<-[:POSSUI]-(item) where item:Material or item:Pergunta '
    'WITH  termo, count(item) as ocorr '
    'SET termo.ocorrencias = ocorr'
)

inserir_pergunta = (
    'CREATE (perg:Pergunta $props) '
    'SET perg._id = "re_pergunta." + toString(id(perg))'
)

obter_perguntas_cruas = (
    'MATCH (perg:Pergunta) '
    'WHERE NOT exists((perg)-[:POSSUI]->(:Termo)) '
    'RETURN perg '
)

obter_perguntas = (
    'MATCH (perg :Pergunta) '
    'where exists((perg)-[:POSSUI]->(:Termo)) '
    'RETURN perg {.tema, ._id, .alternativas, .enunciado}'
)

obter_perguntas_por_ids = (
    'MATCH (perg :Pergunta) '
    'WHERE perg._id in $lista_ids AND exists((perg)-[:POSSUI]->(:Termo)) '
    'RETURN perg {.tema, ._id, .alternativas, .enunciado}'
)

obter_perguntas_todos_temas = (
    'MATCH (perg:Pergunta) '
    'WHERE exists((perg)-[:POSSUI]->(:Termo)) '
    'RETURN perg.tema as tema, collect(perg._id) as lista_ids'
)

obter_perguntas_temas = (
    'MATCH (perg:Pergunta) '
    'WHERE exists((perg)-[:POSSUI]->(:Termo)) and perg.tema in $lista_temas '
    'RETURN perg.tema as tema, collect(perg._id) as lista_ids'
)

obter_respostas = (
    'MATCH(perg :Pergunta) '
    'WHERE perg._id in $lista_ids '
    'RETURN perg._id as id, perg.alt_correta as alt_correta'
)

obter_materiais_similares = (
    'MATCH (item) '
    'WHERE item:Material or item:Pergunta '
    'WITH count(item) as N '
    
    'WITH N, $lista_ids_pergs as pergs_ids '
    'MATCH (perg:Pergunta) '
    'WHERE perg._id in pergs_ids '
    'WITH  N, collect(perg) as lista_pergs '
    
    'UNWIND lista_pergs as perg '
    'MATCH (perg)-[r1:POSSUI]->(termo:Termo) '
    'WITH N, lista_pergs, termo, '
    '((log10(sum(r1.quantidade))/log10(2))+1.0) as tf1, '
    'log10(N/(termo.ocorrencias*1.0))/log10(2) as idf1 '
    'WITH N, lista_pergs, sum(tf1*idf1) as soma_tf_idf1 '
    
    'UNWIND lista_pergs as perg '
    'MATCH (perg)-[r1:POSSUI]->(termo:Termo)<-[r2:POSSUI]-(mat:Material) '
    'WITH N, mat, soma_tf_idf1, termo, '
    '((log10(sum(r1.quantidade))/log10(2))+1.0) as tf1, '
    '((log10(r2.quantidade)/log10(2))+1.0) as tf2,  '
    'log10(N/(termo.ocorrencias*1.0))/log10(2) as idf '
    'WITH N, mat, sum(tf1*tf2*idf*idf) as num, soma_tf_idf1 '
    
    'MATCH (mat)-[r2:POSSUI]->(termo:Termo) '
    'WITH mat, num, soma_tf_idf1, termo, '
    '((log10(r2.quantidade)/log10(2))+1.0) as tf2, '
    'log10(N/(termo.ocorrencias*1.0))/log10(2) as idf2 '
    'WITH mat, num, soma_tf_idf1, sum(tf2*idf2) as soma_tf_idf2 '
    
    'WITH mat, num / sqrt(soma_tf_idf1*soma_tf_idf2) as similaridade '
    'RETURN mat { .* , similaridade}'
    'ORDER by similaridade desc '
)