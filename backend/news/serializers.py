from django.contrib.auth.models import User
from rest_framework import serializers
from .models import News


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class NewsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'created_at', 'author')

    def create(self, validated_data):
        news = News.objects.create(
            author=self.context['request'].user,
            title=validated_data['title'],
            content=validated_data['content']
            )
        return news
