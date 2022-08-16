import datetime
import json
import random

from django.test import TestCase
from django.test.utils import setup_test_environment
from django.urls import reverse

from .models import Redirect




class RedirectModelTests(TestCase):

    #### POST /shortcode ####
    def test_correct_redirect(self):
        post_body = {
                'url': 'https://www.google.com',
                'shortcode': 'abcdef',
        }

        response = self.client.post(
            '/shorten',
            post_body,
            content_type='application/json',
        )

        correct_response_json = {'shortcode': 'abcdef'}
        actual_response_json = response.json()


        self.assertEqual(response.status_code, 201)

        self.assertEqual(actual_response_json, correct_response_json)

    def test_missing_shortcode(self):
        post_body = {
                'url': 'https://www.google.com',
        }

        response = self.client.post(
            '/shorten',
            post_body,
            content_type='application/json',
        )

        actual_response_json = response.json()

        self.assertEqual(response.status_code, 201)

        self.assertIn('shortcode', actual_response_json)

    def test_missing_url(self):
        post_body = {}

        response = self.client.post(
            '/shorten',
            post_body,
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)

        self.assertEqual(response.content.decode(), 'Url not present')

    
    #### GET /<shortcode> ####
    def test_existing_shortcode(self):
        redirect = Redirect(
            url='https://www.google.com',
            shortcode='abcdef',
        )
        redirect.save()

        response = self.client.get('/abcdef')

        self.assertEqual(response.status_code, 302)
    

    def test_missing_shortcode(self):
        response = self.client.get('/abcdef')

        self.assertEqual(response.status_code, 404)


    #### GET /<shortcode>/stats
    def test_existing_shortcode_stats(self):
        redirect = Redirect(
            url='https://www.google.com',
            shortcode='abcdef',
            created_date=datetime.datetime(2022, 1, 1, 0, 0, 0),
            last_accessed_date=datetime.datetime(2022, 1, 1, 0, 0, 0),
        )
        redirect.save()
        
        random_amount = random.randint(1,1000)


        for _ in range(random_amount):
            self.client.get('/abcdef')

        response = self.client.get('/abcdef/stats')
        
        actual_response_json = response.json()
        redirect_count = actual_response_json.get('redirectCount')
        created_date = actual_response_json.get('created')
        last_accessed_date = actual_response_json.get('lastRedirect')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(redirect_count, random_amount)
        self.assertEqual('2022-01-01T00:00:00.000Z', created_date)
        self.assertNotEqual('2022-01-01T00:00:00.000Z', last_accessed_date)

    def test_missing_shortcode_stats(self):
        response = self.client.get('/abcdef/stats')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content.decode(), 'Shortcode not found')
