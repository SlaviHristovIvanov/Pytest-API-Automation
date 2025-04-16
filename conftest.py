import requests
import pytest

@pytest.fixture
def get_harry_potter_books():
    url = 'https://www.googleapis.com/books/v1/volumes?q=harry+potter'
    response = requests.get(url, timeout=5)
    return response
