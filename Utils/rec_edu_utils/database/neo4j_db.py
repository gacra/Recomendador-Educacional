from neo4j.v1 import GraphDatabase
import logging

from rec_edu_utils.database import (neo4j_uri, neo4j_user, neo4j_password)
import rec_edu_utils.database.queries as queries


class Neo4jDB(object):
    def __init__(self):
        self._driver = GraphDatabase.driver(neo4j_uri,
                                            auth=(neo4j_user, neo4j_password))
        self.logger = logging.getLogger(self.__class__.__name__)

    def upsert_material(self, dict_material):
        id_ = dict_material['_id']
        termos = dict_material['termos']
        props = {k: v for k, v in dict_material.items() if
                 k not in ['id', 'termos']}

        label = 'Material'

        with self._driver.session() as session:
            self.logger.info('Inserindo material: {}'.format(id_))
            session.write_transaction(self.upsert_item_tx,
                                      label, id_, props, termos)

            self.logger.info('Removendo termos: {}'.format(id_))
            session.write_transaction(self.remover_termos_tx, label, id_)

            self.logger.info('Inserindo contagem nos termos: {}'.format(id_))
            session.write_transaction(self.inserir_contagem, label,  id_)

    @staticmethod
    def upsert_item_tx(tx, label, id_, props, termos):
        tx.run(queries.upsert_material_query %label,
               id=id_,
               props=props,
               termos=termos)

    @staticmethod
    def remover_termos_tx(tx, label, id_):
        tx.run(queries.remover_termos_query %label,
               id=id_)

    @staticmethod
    def inserir_contagem(tx, label, id_):
        tx.run(queries.inserir_contagem_query %label,
               id=id_)

    def obter_perguntas(self):
        with self._driver.session() as session:
            return session.read_transaction(self.obter_perguntas_tx)

    @staticmethod
    def obter_perguntas_tx(tx):
        resultado = tx.run(queries.obter_perguntas_query)
        return [dict(registro['perg']) for registro in resultado]

    def close(self):
        self._driver.close()
