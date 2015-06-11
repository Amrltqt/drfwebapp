# coding: utf-8

from django.conf.urls import url
from rest_framework import routers

from app.api.views import messages_view
from app.api.views import users_view


router = routers.DefaultRouter()
router.register(r'accounts', users_view.User)

urlpatterns = [

    url(r'^api/users/$', users_view.UserList.as_view(), name='user-list'),
    url(r'^api/users/(?P<pk>[0-9]+)/$', users_view.UserDetail.as_view(), name='user-detail'),
    url(r'^api/messages/$', messages_view.MessageList.as_view(), name='message-list'),
    url(r'^api/messages/(?P<pk>[0-9]+)/$', messages_view.MessageDetail.as_view(), name='message-detail'),
]