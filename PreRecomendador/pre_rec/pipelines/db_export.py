from rec_edu_utils.database.neo4j_db import Neo4jDB
from rec_edu_utils.models.material import Material
from rec_edu_utils.models.question import Question


class Neo4jDBExport(object):

    def open_spider(self, spider):
        self.db = Neo4jDB()

    def process_item(self, item, spider):
        if isinstance(item, Question):
            self.db.upsert_question(dict(item))
        elif isinstance(item, Material):
            self.db.upsert_material(dict(item))
            spider.p_bar.update()

        return item
