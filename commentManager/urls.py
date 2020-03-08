from django.urls import path, include,URLPattern
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from commentManager.models import Comment
from commentManager import views


#---------- Insert Comment id for <int:pk>, list gets post argument as GET method---------

urlpatterns = [
    path('comment-list/', views.CommentList.as_view(),name="CommentList"),
    path('comment-create/', views.CommentCreate.as_view(),name="CommentCreate"),
    path('comment-detail/<int:pk>', views.CommentDetail.as_view(),name="CommentDetail"),
    path('comment-update/<int:pk>', views.CommentUpdate.as_view(),name="CommentUpdate"),
    path('comment-delete/<int:pk>', views.CommentDelete.as_view(),name="CommentDelete")]