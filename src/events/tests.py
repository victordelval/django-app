from django.test import TestCase


class GetRequestsViewsTests(TestCase):
    """
    Set of tests for each view of the application, consisting of
    launching a GET request from the client to check the status code
    of the response.
    """

    def test_get_event_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_event_form_view(self):
        response = self.client.get('/events')
        self.assertEqual(response.status_code, 200)

    def test_get_hashtag_form_view(self):
        response = self.client.get('hashtag')
        self.assertEqual(response.status_code, 200)
