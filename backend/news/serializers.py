from django.contrib.auth.models import User
from rest_framework import serializers
from news.models import News


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class NewsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'image', 'created_at', 'author')

    def create(self, validated_data):
        author = self.context['request'].user
        news = News.objects.create(
            author=author,
            title=validated_data['title'],
            image=validated_data['image'],
            content=validated_data['content']
        )
        return news
