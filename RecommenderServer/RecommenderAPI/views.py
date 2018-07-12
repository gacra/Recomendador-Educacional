import random

from rec_edu_utils.models.topics import Topics
from rest_framework import status, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication

from RecommenderAPI import NUMBER_OF_QUESTIONS, PAGE_SIZE
from RecommenderAPI import db
from RecommenderAPI.serializers import (QuestionSerializer,
                                        SaveQuestionSerializer,
                                        QuestionIDListSerizalizer,
                                        AnswerSerializer,
                                        MaterialSerializer,
                                        TopicsSerializer)


class Questions(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        questions = db.get_questions()

        paginator = PageNumberPagination()
        paginator.page_size = PAGE_SIZE
        questions_page = paginator.paginate_queryset(questions, request)

        question_serializer = QuestionSerializer(questions_page, many=True)
        return paginator.get_paginated_response(question_serializer.data)

    def post(self, request, format=None):
        serializer = SaveQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionsByTopics(APIView):

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
        questions_per_topic = int(NUMBER_OF_QUESTIONS / len(topic_list))

        for topic, question_id_list_topic in question_ids_per_topic.items():
            if questions_per_topic > len(question_id_list_topic):
                question_id_list.extend(question_id_list_topic)
                continue

            index_list = random.sample(
                range(0, len(question_id_list_topic)), questions_per_topic)

            question_id_list.extend(
                [question_id_list_topic[index] for index in index_list])

        questions = db.get_questions(question_id_list)

        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class Answers(APIView):

    def post(self, request, format=None):
        question_id_list = get_question_id_list(request)

        if isinstance(question_id_list, ReturnDict):
            return Response(question_id_list,
                            status=status.HTTP_400_BAD_REQUEST)

        answers = db.get_answers(question_id_list)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)


class Materials(APIView):

    def post(self, request, format=None):
        question_id_list = get_question_id_list(request)

        if isinstance(question_id_list, ReturnDict):
            return Response(question_id_list,
                            status=status.HTTP_400_BAD_REQUEST)

        materials = db.get_similar_materials(question_id_list)

        paginator = PageNumberPagination()
        paginator.page_size = PAGE_SIZE
        materials_page = paginator.paginate_queryset(materials, request)

        material_serializer = MaterialSerializer(materials_page, many=True)
        return paginator.get_paginated_response(material_serializer.data)


class TopicsReference(APIView):

    def get(self, request, format=None):
        topics_reference = [{"code": topic.name, "description": topic.value} for
                            topic in Topics]
        serializer = TopicsSerializer(topics_reference, many=True)
        return Response(serializer.data)


def get_question_id_list(request):
    question_id_list_serializer = QuestionIDListSerizalizer(
        data=request.data)
    if not question_id_list_serializer.is_valid():
        return question_id_list_serializer.errors

    return question_id_list_serializer.validated_data['id_list']
