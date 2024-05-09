import pytest
from apis.models import WordCount
from unittest.mock import patch
from django.test import Client
from ninja.testing import TestClient
from apis.views import api

api_client = TestClient(api)


@pytest.mark.django_db
class TestWordCount:

    def test_empty_request(self):
        response = api_client.post("/wordcount")

        # Assert 422 validation error
        assert response.status_code == 422

        # Assert that there are no changes in model
        assert not WordCount.objects.count()

    def test_no_word_passed(self):
        response = api_client.post(
            "/wordcount", json={"url": "http://www.example.com/"}
        )

        # Assert 422 validation error
        assert response.status_code == 422

        # Assert that there are no changes in model
        assert not WordCount.objects.count()

    def test_no_url_passed(self):
        response = api_client.post(
            "/wordcount",
            json={
                "word": "domain",
            },
        )

        # Assert 422 validation error
        assert response.status_code == 422

        # Assert that there are no changes in model
        assert not WordCount.objects.count()

    def test_get_word_count_error(self):
        with patch("apis.views.get_word_count", side_effect=Exception("test error")):
            response = api_client.post(
                "/wordcount",
                json={
                    "word": "invalid",
                    "url": "http://www.example.com/",
                },
            )

        # Assert 500 internal server error
        assert response.status_code == 500

        # Assert that there are no changes in model
        assert not WordCount.objects.count()

    def test_success_db_error(self):
        with patch.object(
            WordCount.objects, "create", side_effect=Exception("test error")
        ):
            response = api_client.post(
                "/wordcount",
                json={
                    "word": "invalid",
                    "url": "http://www.example.com/",
                },
            )

        # Assert that the process is still successful
        assert response.status_code == 200

        # Assert that there are no changes in model
        assert not WordCount.objects.count()

    def test_success_no_hits(self):
        response = api_client.post(
            "/wordcount",
            json={
                "word": "invalid",
                "url": "http://www.example.com/",
            },
        )

        # Assert 200 success
        assert response.status_code == 200

        # Assert that there is a new WordCount entry
        assert WordCount.objects.count() == 1

        instance = WordCount.objects.last()

        # Assert that the instance details are correct
        assert instance.word == "invalid"
        assert instance.url == "http://www.example.com/"
        assert instance.count == 0

    def test_success(self):
        response = api_client.post(
            "/wordcount",
            json={
                "word": "domain",
                "url": "http://www.example.com/",
            },
        )

        # Assert 200 success
        assert response.status_code == 200

        # Assert that there is a new WordCount entry
        assert WordCount.objects.count() == 1

        instance = WordCount.objects.last()

        # Assert that the instance details are correct
        assert instance.word == "domain"
        assert instance.url == "http://www.example.com/"
        assert instance.count == 4
