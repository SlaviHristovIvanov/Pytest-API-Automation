import pytest
import requests

def test_sites_responding(get_user_api):
    response = get_user_api
    assert response.status_code in (200, 202)


def test_response_time(get_user_api):
    response = get_user_api
    assert response.elapsed.total_seconds() < 1    # check how fast the api responds


def test_user_data_structure(get_user_api):
    response = get_user_api
    json_data = response.json()
    user = json_data["data"]
    assert isinstance(user["id"], int)
    assert "email" in user
    assert user["email"].endswith("@reqres.in")

def test_user_data_credentials(get_user_api):
    response = get_user_api
    json_data = response.json()
    user = json_data["data"]
    assert isinstance(user["id"], int)
    assert "first_name" in user
    assert "last_name" in user
    assert "avatar" in user
    assert user["first_name"] == "Janet"
    assert user["last_name"] == "Weaver"
    assert user["avatar"].endswith("image.jpg")

def test_user_data_support(get_user_api):
    response = get_user_api
    json_data = response.json()
    user = json_data["support"]
    assert "url" in user
    assert "text" in user
    assert user["url"] == "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral"
    assert user["text"] == "Tired of writing endless social media content? Let Content Caddy generate it for you."


def test_create_user_missing_fields(get_user_api):
    payload= {}  #empty body
    response = requests.post("https://reqres.in/api/users", json=payload)
    assert response.status_code in (400, 401, 422)


def test_user_authentication():
    headers = {
        # No token header
    }
    response = requests.post("https://reqres.in/api/users", headers=headers, json={"name": "John", "job": "Developer"})
    assert response.status_code == 401