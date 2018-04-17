upsert_material_query = (
    'WITH $termos as map '
    'MERGE (mat:%s {id: $id}) '
    'SET mat += $props '
    'SET mat.atualizacao = timestamp()'
    'FOREACH(termo in keys(map) | '
        'merge(ter:Termo {termo:toLower(termo)}) '
        'merge (ter)<-[r:POSSUI]-(mat) '
        'set r.quantidade = map[termo]'
        'set r.atualizacao = timestamp())')

remover_termos_query = (
    'MATCH (mat:%s {id: $id})-[r:POSSUI]->(termo:Termo) '
    'WHERE r.atualizacao < mat.atualizacao '
    'SET termo.ocorrencias = termo.ocorrencias - 1 '
    'DELETE r '
    'WITH termo WHERE termo.ocorrencias = 0 '
    'DELETE termo'
)

inserir_contagem_query = (
    'MATCH (mat:%s {id: $id})-[:POSSUI]->(termo:Termo) '
    'MATCH (termo)<-[:POSSUI]-(item) where item:Material or item:Pergunta '
    'WITH  termo, count(item) as ocorr '
    'SET termo.ocorrencias = ocorr'
)

obter_perguntas_query =(
    'MATCH (perg :Pergunta) '
    'RETURN perg'
)