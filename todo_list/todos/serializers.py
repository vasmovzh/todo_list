from rest_framework import serializers
from .models import Todo, Company
from django.contrib.auth.models import User

"""
class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=20)
    content = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        \"""
        Create and return a new `Snippet` instance, given the validated data.
        \"""
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        \"""
        Update and return an existing `Snippet` instance, given the validated data.
        \"""
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.code)
        instance.save()
        return instance
"""


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user_owner = serializers.ReadOnlyField(source='owner.username')
    company_owner = serializers.ReadOnlyField(source='owner.company_name')

    class Meta:
        model = Todo
        fields = ('url', 'id', 'title', 'content', 'completed', 'user_owner', 'company_owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', read_only=True)
    #companies = serializers.HyperlinkedRelatedField(many=True, view_name='company-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'todos')

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    #todos = serializers.HyperlinkedRelatedField(many=True, view_name='company-detail', read_only=True)

    class Meta:
        model = Company
        fields = ('url', 'id', 'company_name')
