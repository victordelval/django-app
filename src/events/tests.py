from django.test import TestCase
from django.urls import reverse
from django.db import IntegrityError

from events.models import Event, Tag


# Testing views with GET requests

class GetRequestsViewsTests(TestCase):
    """
    Set of tests for each view of the application, consisting of
    launching a GET request from the client to check the status code
    of the response and the rendered template.
    """

    def test_get_event_list_view(self):
        response = self.client.get(reverse('events:event-list-view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_list.html')

    def test_get_event_form_view(self):
        response = self.client.get(reverse('events:event-form-view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_form.html')

    def test_get_tag_form_view(self):
        response = self.client.get(reverse('events:tag-form-view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/tag_form.html')


# Testing views and models with POST requests

class PostRequestsViewsTests(TestCase):
    """
    Set of tests for each creation view of the application, consisting of
    launching a POST request from the client, passing the arguments to create
    the new object, to check the status code of the response and the total
    count of related objects.
    """

    def test_post_event_form_view(self):
        event_count = Event.objects.count()
        tag = Tag.objects.create(name='Foobar')
        response = self.client.post(
            reverse('events:event-form-view'), {
                'title': "Outdoor summer cinema",
                'description': "",
                'price': 5.95,
                'tags': [tag.id]
            })
        self.assertEqual(response.status_code, 302)  # HttpResponseRedirect
        self.assertEqual(Event.objects.count(), event_count + 1)

    def test_post_tag_form_view(self):
        tag_count = Tag.objects.count()
        response = self.client.post(
            reverse('events:tag-form-view'), {
                'name': "cuecuecue",
            })
        self.assertEqual(response.status_code, 302)  # HttpResponseRedirect
        self.assertEqual(Tag.objects.count(), tag_count + 1)


# Testing models


class EventModelTests(TestCase):
    """Set of tests to validate the fields of the Event model."""

    def test_string_representation(self):
        """Checks the string representation of a Event object."""
        event = Event(title="Outdoor summer cinema", price=5.95)
        expected = "Outdoor summer cinema (5.95 €)"
        self.assertEqual(str(event), expected)

    def test_title_field_unique(self):
        """Checks the constraint that the title field should be unique."""
        with self.assertRaises(IntegrityError):
            Event.objects.create(title="Event A", price=0)
            Event.objects.create(title="Event A", price=0)


class TagModelTests(TestCase):

    def test_unique_constraint_fail_creation(self):
        with self.assertRaises(IntegrityError):
            Tag.objects.create(name="foobar")
            Tag.objects.create(name="foobar")

    def test_string_representation(self):
        tag = Tag(name="foobar")
        self.assertEqual(str(tag), tag.name)


# Testing model forms
