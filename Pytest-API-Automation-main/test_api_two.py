import pytest
import requests

@pytest.mark.parametrize('url', [
    "https://www.google.com",
    "https://brave.com",
    "https://www.google.com/chrome/"
])

def test_sites_responding(url):
    response = requests.get(url)
    assert response.status_code in (200, 202)


def test_response_time():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.elapsed.total_seconds() < 1    # check how fast the api responds

def test_user_data_structure():
    response = requests.get("https://reqres.in/api/users/2")
    json_data = response.json()
    user = json_data["data"]
    assert isinstance(user["id"], int)
    assert "email" in user
    assert user["email"].endswith("@reqres.in")



def test_create_user_missing_fields():
    payload= {}  #empty body
    response = requests.post("https://reqres.in/api/users", json=payload)
    assert response.status_code in (400, 401, 422)
