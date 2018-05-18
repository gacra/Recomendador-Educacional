from rec_edu_utils.database.neo4j_db import Neo4jDB
from rec_edu_utils.models.question import Question

class AddRawQuestions(object):

    def __init__(self):
        self.db = Neo4jDB()
        self.first_time = True

    def process_spider_output(self, response, result, spider):

        if self.first_time:
            raw_question_list = self.db.get_raw_questions()

            for raw_question in raw_question_list:
                terms = raw_question['stem']
                terms += ' '.join(raw_question['alternatives'])
                yield Question(raw_question, terms=terms)

            self.first_time = False

        for r in result:
            yield r
