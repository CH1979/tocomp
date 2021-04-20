from rest_framework import serializers
from .models import Exam, ExamCard, Question, LabelForChoice


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class ExamCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamCard
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelForChoice
        fields = '__all__'
