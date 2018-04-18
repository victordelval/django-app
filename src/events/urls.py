from django.urls import path

from . import views


# app namespace
app_name = 'events'

urlpatterns = [
    path('tag', views.TagFormView.as_view(), name='tag-form-view'),
    path('event', views.EventFormView.as_view(), name='event-form-view'),
    path('', views.EventListView.as_view(), name='event-list-view'),
]
