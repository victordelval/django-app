from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic import ListView, View

from events.models import Event, Tag


class EventListView(ListView):
    template_name = 'events/event_list.html'

    def get_queryset(self):
        return None


class EventFormView(View):
    template_name = 'events/event_form.html'

    def get(self, request, *args, **kwargs):
        template = self.template_name
        return render(request, template, {})

    def post(self, request, *args, **kwargs):
        data = request.POST
        event = Event.objects.create(
            title=data['title'],
            description=data['description'],
            price=data['price']
        )
        event.tags.set(data['tags'])
        return HttpResponseRedirect(
            reverse('events:event-list-view'))


class TagFormView(View):
    template_name = 'events/tag_form.html'

    def get(self, request, *args, **kwargs):
        template = self.template_name
        return render(request, template, {})

    def post(self, request, *args, **kwargs):
        data = request.POST
        Tag.objects.create(name=data['name'])
        return HttpResponseRedirect(
            reverse('events:event-list-view'))
