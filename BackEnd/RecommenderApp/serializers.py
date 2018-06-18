from rest_framework import serializers


class QuestionsSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    stem = serializers.CharField()
    alternatives = serializers.ListField(child=serializers.CharField())
    topic = serializers.CharField()
