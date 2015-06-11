# coding: utf-8

from django.conf.urls import url
from drfwebapp.api.views import messages_view
from drfwebapp.api.views import users_view

urlpatterns = [
    url(r'^api/register/$', users_view.CreateUserView.as_view(), name='user-create'),
    url(r'^api/messages/$', messages_view.MessageList.as_view(), name='message-list'),
    url(r'^api/messages/(?P<pk>[0-9]+)/$', messages_view.MessageDetail.as_view(), name='message-detail'),
]