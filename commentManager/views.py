from rest_framework import viewsets, permissions
from commentManager.serializers import CommentListSerializer, CommentDetailSerializer
from commentManager import models
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


#----------------- List view for showing all of the comments for a post ---------------

class CommentList (ListAPIView):
    serializer_class = CommentListSerializer
    def get_queryset(self):
        ids = self.request.query_params.get('post', None)
        if ids is not None:
            queryset = models.Comment.objects.filter(post=ids)
            return queryset

#-------------------------- Generic views for CRUD Operations -------------------------

class CommentDetail (RetrieveAPIView):
    queryset=models.Comment.objects.all()
    serializer_class = CommentDetailSerializer


class CommentCreate (CreateAPIView):
    queryset=models.Comment.objects.all()
    serializer_class = CommentDetailSerializer


class CommentUpdate (UpdateAPIView):
    queryset=models.Comment.objects.all()
    serializer_class = CommentDetailSerializer


class CommentDelete (DestroyAPIView):
    queryset=models.Comment.objects.all()
    serializer_class = CommentDetailSerializer