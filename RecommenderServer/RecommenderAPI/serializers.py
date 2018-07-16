from rec_edu_utils.models.topics import Topics
from rest_framework import serializers

from RecommenderAPI import NUMBER_OF_QUESTIONS, db

TOPIC_CHOICES = [topic.name for topic in Topics]


class QuestionSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    stem = serializers.CharField()
    alternatives = serializers.ListField(child=serializers.CharField())
    topic = serializers.ChoiceField(choices=TOPIC_CHOICES)


class SaveQuestionSerializer(QuestionSerializer):
    correct_alt = serializers.IntegerField()

    def create(self, validated_data):
        return db.insert_question(validated_data)


class QuestionIDListSerizalizer(serializers.Serializer):
    id_list = serializers.ListField(child=serializers.CharField(max_length=20),
                                    max_length=NUMBER_OF_QUESTIONS)


class AnswerSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    correct_alt = serializers.IntegerField(read_only=True)


class MaterialSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    link = serializers.CharField(read_only=True)
    summary = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    topic = serializers.CharField(read_only=True)
    similarity = serializers.FloatField(read_only=True)


class TopicsSerializer(serializers.Serializer):
    code = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)

class SuperTopicsSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    topic_list = TopicsSerializer(many=True, read_only=True)