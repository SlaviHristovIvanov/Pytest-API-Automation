import pytest

@pytest.mark.harry_potter
def test_harry_potter_api(get_harry_potter_books):
    response = get_harry_potter_books
    assert response.status_code in (200, 202)
    assert 'totalItems' in response.json()

@pytest.mark.harry_potter
def test_harry_potter_api_two(get_harry_potter_books):
    response = get_harry_potter_books
    assert response.status_code in (200, 202)
    assert 'kind' in response.json()

@pytest.mark.harry_potter
def test_harry_potter_api_three(get_harry_potter_books):
    response = get_harry_potter_books
    assert response.status_code in (200, 202)
    assert 'items' in response.json()
