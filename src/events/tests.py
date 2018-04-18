from django.test import TestCase
from django.urls import reverse


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
