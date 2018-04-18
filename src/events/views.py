from django.shortcuts import render

from django.views.generic import ListView, View


class EventListView(ListView):
    template_name = 'events/event_list.html'

    def get_queryset(self):
        return None


class EventFormView(View):
    template_name = 'events/event_form.html'

    def get(self, request, *args, **kwargs):
        template = self.template_name
        return render(request, template, {})


class TagFormView(View):
    template_name = 'events/tag_form.html'

    def get(self, request, *args, **kwargs):
        template = self.template_name
        return render(request, template, {})
