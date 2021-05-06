from rest_framework import serializers
from .models import Exam, ExamCard, Question, LabelForChoice


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelForChoice
        fields = ('label',)


class QuestionSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'examcard',
            'id',
            'title',
            'content',
            'answer_type',
            'labels'
        )

    def create(self, validated_data):
        labels_data = validated_data.pop('labels')
        question = Question.objects.create(**validated_data)
        for label_data in labels_data:
            LabelForChoice.objects.create(question=question, **label_data)
        return question


class ExamCardSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = ExamCard
        fields = ('id', 'exam', 'number', 'questions')


class ExamDetailSerializer(serializers.ModelSerializer):
    examcards = ExamCardSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ('theme', 'examcards', )
