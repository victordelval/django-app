from django.http import HttpResponse


def EventListView(request):
    return HttpResponse("This view is the 'Event List'")


def EventFormView(request):
    return HttpResponse("This view is the 'Event Form'")


def HashtagFormView(request):
    return HttpResponse("This view is the 'Hashtag Form'")
