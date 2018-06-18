from rec_edu_utils.database.neo4j_db import Neo4jDB
from RecommenderApp.serializers import QuestionsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rec_edu_utils.models.topics import Topics
import random

db = Neo4jDB()

NUMBER_OF_QUESTIONS = 15

class QuestionsAll(APIView):

    def get(self, request, format=None):
        questions = db.get_questions()
        serializer = QuestionsSerializer(questions, many=True)
        return Response(serializer.data)

class Questions(APIView):

    def get(self, request, topics_text, format=None):

        if topics_text:
            topic_list = []
            topic_text_list = topics_text.split('-')

            for topic in topic_text_list:
                try:
                    topic_list.append(Topics[topic])
                except KeyError:
                    continue
        else:
            topic_list = list(Topics)

        question_ids_per_topic = db.get_questions_by_topic(topic_list)

        question_id_list = []
        questions_per_topic = int(NUMBER_OF_QUESTIONS/len(topic_list))

        for topic, question_id_list_topic in question_ids_per_topic.items():
            if questions_per_topic > len(question_id_list_topic):
                question_id_list.extend(question_id_list_topic)
                continue

            index_list = random.sample(
                range(0,len(question_id_list_topic)), questions_per_topic)

            question_id_list.extend(
                [question_id_list_topic[index] for index in index_list])

        questions = db.get_questions(question_id_list)

        serializer = QuestionsSerializer(questions, many=True)
        return Response(serializer.data)