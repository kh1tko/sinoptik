Automated Testing for Sinoptik Website

This project is a set of automated tests to check the functionality of the Sinoptik website. Python, Selenium WebDriver, and Chrome browser are used as tools.

Installing Dependencies

Install Python 3.x (if not already installed).
Install the required libraries by running the command: pip install -r requirements.txt

Running Tests

Before running the tests, specify the path to the Chrome browser driver in the conftest.py file.
Run the tests by executing the command: pytest

Project Structure

- conftest.py: pytest configuration file with a fixture to initialize the browser.
- pages/: Directory containing classes for interacting with elements on pages.
- tests.py: File with a set of test scenarios.

Test Descriptions

City Search Test and Result Verification:
- Fills the city search field, clicks the search button, and verifies the search result.
Weather Forecast Change Tests:
- Navigates to the weather forecast for different days and verifies the displayed information.
Display Weather Links Block Test:
- Scrolls down the page and checks the display of the weather links block.

Adding New Tests
- To add new tests for the web application, create new methods in the tests.py file.
- Use methods from the MainPage class in pages/MainPage.py to interact with page elements.

Help and Support

If you have any questions or issues using this project, please contact me.
