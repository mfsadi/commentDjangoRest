from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from commentManager import models
from rest_framework import serializers

'''
#----------------- Post Serializer ---------------

class PostSerializer(serializers.Serializer):
    class Meta:
        model = models.Post
        fields = ['id']
'''


#----------------- Serializer for listing comments relating to a certain post ---------------

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['id', 'commenter', 'content', 'commenter_email', 'post']


#----------------- Serializer for showing, updating, creating or deleting a coment ----------

class CommentDetailSerializer(serializers.ModelSerializer):
    #Override update method to filter by post id
    def update(self, instance, validated_data):
        instance.commenter = validated_data.get('commenter', instance.commenter)
        instance.content = validated_data.get('content', instance.content)
        instance.commenter_email = validated_data.get('commenter_email', instance.commenter_email)
        post = validated_data.pop('post')
        instance.post = post
        instance.save()
        return instance
    class Meta:
        model = models.Comment
        fields = ['id', 'commenter', 'content', 'commenter_email', 'post']