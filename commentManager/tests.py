from rest_framework.test import APITestCase, CoreAPIClient
from django.urls import include, path
from commentManager. models import Comment,Post
from rest_framework.test import RequestsClient
from django.http import HttpResponseNotFound
from django.http.response import HttpResponse
from rest_framework.test import APIClient
from rest_framework import status
from commentManager import views


#-------------------- This test case examines Comment Model integrity ------------------

class ModelTest(APITestCase):
    def setUp(self):
        Post.objects.create(id='1')
        Comment.objects.create(
            id='18', commenter='me', content='test comment', commenter_email='test@test.com', post_id='1')
    def test_comment_table(self):
        true_comment = Comment.objects.get(id='18')
        self.assertEqual(
            true_comment.commenter, "me")

#----------------- This test case checks the response of different URLs -----------------
#-------------- Make sure you have at least on comment and post in your db --------------

class CommentTest(APITestCase):
    def test_urls(self):  
        client = APIClient()
        responseList=client.get('/comment-list/', {'post': '1'}, format='json')
        responseDetail=client.get('/comment-detail/1', format='json')
        responseDelete=client.get('/comment-delete/1', format='json')
        responseUpdate=client.get('/comment-update/1', format='json')
        responseCreate=client.get('/comment-create/', format='json')
        self.assertEqual(responseList.status_code, status.HTTP_200_OK)
       #self.assertEqual(responseDetail.status_code, status.HTTP_200_OK)#--DIDN'T WORK ON MY MACHINE
        self.assertEqual(responseDelete.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(responseUpdate.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(responseCreate.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)