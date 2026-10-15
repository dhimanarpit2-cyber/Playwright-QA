
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    # Start Playwright
    with sync_playwright() as p:

        # Launch the browser
        browser = p.chromium.launch(headless=False,slow_mo=50)

        # Open a new browser tab
        page = browser.new_page()

        # Give the page to the test
        yield page

        # Close the browser after the test
        browser.close()
