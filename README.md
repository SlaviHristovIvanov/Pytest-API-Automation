# Pytest-API-Automation

This project is a simple but complete API automation testing framework built with **Python**, **Pytest**, and **Requests**.  
It includes reusable fixtures, parametrized tests, custom markers, and generates **HTML reports** using `pytest-html`.

- **Python 3.10+**
- **Pytest** – Test framework
- **Requests** – HTTP client for REST APIs
- **Pytest-HTML** – To generate beautiful test reports

Run all tests with verbose output and HTML report:
pytest -v --html=response.html --self-contained-html


Run only specific test group using markers:
pytest -m harry_potter
