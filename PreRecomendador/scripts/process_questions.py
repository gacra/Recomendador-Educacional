import sys

from rec_edu_utils.database.neo4j_db import Neo4jDB
from rec_edu_utils.models.question import Question

sys.path.append('.')

from pre_rec.pipelines.requirements import CheckRequirements
from pre_rec.pipelines.freq_calc import FreqCalc
from pre_rec.pipelines.json_export import JsonExport
from pre_rec.pipelines.db_export import Neo4jDBExport

db = Neo4jDB()

check_req_pipe = CheckRequirements()
freq_calc_pipe = FreqCalc()
json_export_pipe = JsonExport()
json_export_pipe.open_spider(None)
db_export_pipe = Neo4jDBExport()
db_export_pipe.open_spider(None)

raw_question_db_list = db.get_raw_questions()

print('Number of raw questions processed: {}'.format(len(raw_question_db_list)))

for raw_question_db in raw_question_db_list:
    terms = raw_question_db['stem']
    terms += ' '.join(raw_question_db['alternatives'])
    question = Question(raw_question_db, terms=terms)

    question = check_req_pipe.process_item(question, None)
    question = freq_calc_pipe.process_item(question, None)
    question = json_export_pipe.process_item(question, None)
    question = db_export_pipe.process_item(question, None)

json_export_pipe.close_spider(None)
