from .models import Answer, Question
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "title", "question_id")


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ("id", "description", "test_id", "answers")
