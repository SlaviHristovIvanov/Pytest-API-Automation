import pytest
import requests

@pytest.mark.parametrize('url', [
    "https://www.google.com",
    "https://brave.com",
    "https://www.google.com/chrome/"
])

def test_sites_responding(url):
    response = requests.get(url)
    assert response.status_code == 200