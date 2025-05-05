This project provides a robust and scalable API automation testing framework designed to ensure the quality and reliability of backend services. Built with Python, Pytest, and Requests, it is capable of testing REST APIs, handling authentication, and performing multiple validations, with clear test reports generated using pytest-html.

Technologies Used

Python 3.10+ – The primary language for the framework.
Pytest – A popular testing framework for writing and organizing unit and integration tests.
Requests – A simple HTTP library for making REST API calls.
pytest-html – Plugin for generating clean, detailed, and customizable HTML reports.
pytest-mock – For mocking objects and functions to isolate tests.
CI/CD Integration – Easily integrates with continuous integration tools for automated testing.
Features

Automated API Testing – Validates RESTful APIs to ensure they return correct and expected responses.
Reusable Fixtures – Simplifies common setup and teardown processes across tests, improving maintainability.
Parameterized Tests – Run the same test logic with multiple sets of data, increasing test coverage.
Custom Markers – Organize and execute tests by category (e.g., smoke tests, regression tests) with custom markers.
HTML Test Reports – Automatically generates detailed and easy-to-read test reports, viewable in a web browser.
Authentication & Authorization Tests – Test API endpoints with and without authentication tokens, validating proper authorization checks.
Error Handling – Ensures that APIs return the correct error codes for scenarios like missing data, invalid IDs, or unauthorized access.
Response Time Validation – Measures and ensures that APIs respond within acceptable time limits.
Edge Case Testing – Validate API behavior for unusual or boundary input scenarios.
##  Test Report

After running tests, you can view the HTML report locally at: file:///Users/slavi/Downloads/Pytest-API-Automation-main/response.html?sort=result

