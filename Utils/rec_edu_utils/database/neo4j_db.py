import logging

from neo4j.v1 import GraphDatabase

import rec_edu_utils.database.queries as queries
from rec_edu_utils.database import (neo4j_uri, neo4j_user, neo4j_password)


class Neo4jDB(object):

    def __init__(self):
        self._driver = GraphDatabase.driver(neo4j_uri,
                                            auth=(neo4j_user, neo4j_password))
        self.logger = logging.getLogger(self.__class__.__name__)

    ## Insert raw questions ##

    def insert_question(self, dict_question):
        with self._driver.session() as session:
            session.write_transaction(self._insert_question_tx, dict_question)

    @staticmethod
    def _insert_question_tx(tx, props):
        tx.run(queries.insert_question, props=props)

    ## Upsert questions and materials ##

    def upsert_material(self, dict_material):
        label = 'Material'
        self._upsert_item(dict_material, label)

    def upsert_question(self, dict_question):
        label = 'Question'
        self._upsert_item(dict_question, label)

    def _upsert_item(self, dict_item, label):
        id_ = dict_item['_id']
        terms = dict_item['terms']
        props = {k: v for k, v in dict_item.items() if
                 k not in ['_id', 'terms']}

        with self._driver.session() as session:
            self.logger.info('Inserting item: {}'.format(id_))
            session.write_transaction(self._upsert_item_tx,
                                      label, id_, props, terms)

            self.logger.info('Removing terms: {}'.format(id_))
            session.write_transaction(self._remove_terms_tx, label, id_)

            self.logger.info('Inserting count in terms: {}'.format(id_))
            session.write_transaction(self._insert_count_tx, label, id_)

    @staticmethod
    def _upsert_item_tx(tx, label, id_, props, terms):
        tx.run(queries.upsert_material % label,
               id=id_,
               props=props,
               terms=terms)

    @staticmethod
    def _remove_terms_tx(tx, label, id_):
        tx.run(queries.remove_terms % label,
               id=id_)

    @staticmethod
    def _insert_count_tx(tx, label, id_):
        tx.run(queries.insert_count % label,
               id=id_)

    ## Get raw questions ##

    def get_raw_questions(self):
        with self._driver.session() as session:
            result = session.read_transaction(self._get_raw_questions_tx)
            return [dict(record['question']) for record in result]

    @staticmethod
    def _get_raw_questions_tx(tx):
        return tx.run(queries.get_raw_questions)

    ## Get questions ##

    def get_questions(self, id_list=None):
        with self._driver.session() as session:
            if not id_list:
                result = session.read_transaction(self._get_questions_tx)
            else:
                result = session.read_transaction(
                    self._get_questions_by_ids_tx, id_list)

            return [dict(record['question']) for record in result]

    @staticmethod
    def _get_questions_tx(tx):
        return tx.run(queries.get_questions)

    @staticmethod
    def _get_questions_by_ids_tx(tx, id_list):
        return tx.run(queries.get_questions_by_id, id_list=id_list)

    ## Get ids of questions by topic ##

    def get_questions_by_topic(self, topic_list=None):
        with self._driver.session() as session:
            if not topic_list:
                result = session.read_transaction(
                    self._get_questions_all_topics_tx)
            else:
                topic_list_text = [topic.name for topic in topic_list]
                result = session.read_transaction(
                    self._get_questions_by_topic_tx, topic_list_text)

            return {record['topic']: record['id_list'] for record in result}

    @staticmethod
    def _get_questions_all_topics_tx(tx):
        return tx.run(queries.get_questions_all_topics)

    @staticmethod
    def _get_questions_by_topic_tx(tx, topic_list_text):
        return tx.run(queries.get_questions_topics, lista_temas=topic_list_text)

    ## Get answers ##

    def get_answers(self, id_list):
        with self._driver.session() as session:
            result = session.read_transaction(self._get_answers_tx, id_list)
            return {record['id']: record['correct_alt'] for record in result}

    @staticmethod
    def _get_answers_tx(tx, id_list):
        return tx.run(queries.get_answers, id_list=id_list)

    ## similarity ##

    def get_similar_materials(self, question_id_list):
        with self._driver.session() as session:
            result = session.read_transaction(
                self._get_similar_materials_tx, question_id_list)
            return [dict(record['mat']) for record in result]

    @staticmethod
    def _get_similar_materials_tx(tx, question_id_list):
        return tx.run(queries.get_similar_materials,
                      question_id_list=question_id_list)

    def close(self):
        self._driver.close()
