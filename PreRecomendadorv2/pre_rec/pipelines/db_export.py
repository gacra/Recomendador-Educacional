from rec_edu_utils.database.neo4j_db import Neo4jDB
from rec_edu_utils.models.material import Material
from rec_edu_utils.models.question import Question

class Neo4jDBExport(object):

    def open_spider(self, spider):
        if spider:
            spider.crawler.stats.set_value('re_material_saved_in_db', 0)
        self.db = Neo4jDB()

    def process_item(self, item, spider):
        if isinstance(item, Question):
            self.db.upsert_question(dict(item))
        elif isinstance(item, Material):
            spider.p_bar.update()