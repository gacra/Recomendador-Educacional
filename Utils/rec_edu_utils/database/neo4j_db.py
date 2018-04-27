from neo4j.v1 import GraphDatabase
import logging

from rec_edu_utils.database import (neo4j_uri, neo4j_user, neo4j_password)
import rec_edu_utils.database.queries as queries


class Neo4jDB(object):
    def __init__(self):
        self._driver = GraphDatabase.driver(neo4j_uri,
                                            auth=(neo4j_user, neo4j_password))
        self.logger = logging.getLogger(self.__class__.__name__)

    ## Inserir Pergunta Crua ##

    def inserir_pergunta(self, dict_pergunta):
        with self._driver.session() as session:
            session.write_transaction(self._inserir_pergunta_tx, dict_pergunta)

    @staticmethod
    def _inserir_pergunta_tx(tx, props):
        tx.run(queries.inserir_pergunta, props=props)

    ## Upsert de Perguntas e Materiais ##

    def upsert_material(self, dict_material):
        label = 'Material'
        self._upsert_item(dict_material, label)

    def upsert_pergunta(self, dict_pergunta):
        label = 'Pergunta'
        self._upsert_item(dict_pergunta, label)

    def _upsert_item(self, dict_item, label):
        id_ = dict_item['_id']
        termos = dict_item['termos']
        props = {k: v for k, v in dict_item.items() if
                 k not in ['_id', 'termos']}

        with self._driver.session() as session:
            self.logger.info('Inserindo item: {}'.format(id_))
            session.write_transaction(self._upsert_item_tx,
                                      label, id_, props, termos)

            self.logger.info('Removendo termos: {}'.format(id_))
            session.write_transaction(self._remover_termos_tx, label, id_)

            self.logger.info('Inserindo contagem nos termos: {}'.format(id_))
            session.write_transaction(self._inserir_contagem, label, id_)

    @staticmethod
    def _upsert_item_tx(tx, label, id_, props, termos):
        tx.run(queries.upsert_material % label,
               id=id_,
               props=props,
               termos=termos)

    @staticmethod
    def _remover_termos_tx(tx, label, id_):
        tx.run(queries.remover_termos % label,
               id=id_)

    @staticmethod
    def _inserir_contagem(tx, label, id_):
        tx.run(queries.inserir_contagem % label,
               id=id_)

    ## Obter Perguntas Cruas ##

    def obter_perguntas_cruas(self):
        with self._driver.session() as session:
            resultado = session.read_transaction(self._obter_perguntas_cruas_tx)
            return [dict(registro['perg']) for registro in resultado]

    @staticmethod
    def _obter_perguntas_cruas_tx(tx):
        return tx.run(queries.obter_perguntas_cruas)

    ## Obter Conteúdo das Perguntas ##

    def obter_perguntas(self, lista_ids=None):
        with self._driver.session() as session:
            if not lista_ids:
                resultado = session.read_transaction(self._obter_perguntas_tx)
            else:
                resultado = session.read_transaction(
                    self._obter_perguntas_por_ids_tx, lista_ids)

            return [dict(registro['perg']) for registro in resultado]

    @staticmethod
    def _obter_perguntas_tx(tx):
        return tx.run(queries.obter_perguntas)

    @staticmethod
    def _obter_perguntas_por_ids_tx(tx, lista_ids):
        return tx.run(queries.obter_perguntas_por_ids, lista_ids=lista_ids)

    ## Obter IDs das Perguntas por Temas ##

    def obter_perguntas_temas(self, lista_temas=None):
        with self._driver.session() as session:
            if not lista_temas:
                resultado = session.read_transaction(
                    self._obter_perguntas_todos_temas_tx)
            else:
                lista_temas_texto = [tema.name for tema in lista_temas]
                resultado = session.read_transaction(
                    self._obter_perguntas_temas_tx, lista_temas_texto)

            return {registro['tema']: registro['lista_ids'] for registro in
                    resultado}

    @staticmethod
    def _obter_perguntas_todos_temas_tx(tx):
        return tx.run(queries.obter_perguntas_todos_temas)

    @staticmethod
    def _obter_perguntas_temas_tx(tx, lista_temas_texto):
        return tx.run(queries.obter_perguntas_temas,
                      lista_temas=lista_temas_texto)

    ## Obter Respostas ##

    def obter_respostas(self, lista_ids):
        with self._driver.session() as session:
            resultado = session.read_transaction(self._obter_respostas_tx,
                                                 lista_ids)
            return {registro['id']: registro['alt_correta'] for registro in
                    resultado}

    @staticmethod
    def _obter_respostas_tx(tx, lista_ids):
        return tx.run(queries.obter_respostas, lista_ids=lista_ids)

    def close(self):
        self._driver.close()

    ## Similaridade ##

    def obter_materiais_similares(self, lista_ids_perguntas):
        with self._driver.session() as session:
            resultado = session.read_transaction(
                self.obter_materiais_similares_tx, lista_ids_perguntas)
            return [dict(registro['mat']) for registro in resultado]

    @staticmethod
    def obter_materiais_similares_tx(tx, lista_ids_perguntas):
        return tx.run(queries.obter_materiais_similares,
                      lista_ids_pergs=lista_ids_perguntas)
