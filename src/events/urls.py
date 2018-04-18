from django.urls import path

from . import views


# app namespace
app_name = 'events'

urlpatterns = [
    path('hashtag', views.HashtagFormView, name='hashtag-form-view'),
    path('event', views.EventFormView, name='event-form-view'),
    path('', views.EventListView, name='event-list-view'),
]
