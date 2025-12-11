import base64
import os

import pytest
from playwright.sync_api import sync_playwright
from pytest_html import extras


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        headless = os.getenv('HEADLESS', 'false').lower() == 'true'

        browser = p.chromium.launch(
            headless=headless,
            args=[
                '--no-sandbox',
                '--disable-dev-shm-usage',
                '--disable-blink-features=AutomationControlled',
                '--disable-web-security',
                '--disable-features=IsolateOrigins,site-per-process',
            ]
        )

        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            locale='en-US',
            timezone_id='Europe/Bucharest',
            permissions=['geolocation'],
            geolocation={'latitude': 44.4268, 'longitude': 26.1025},
            extra_http_headers={
                'Accept-Language': 'en-US,en;q=0.9',
            }
        )

        page = context.new_page()

        page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)

        yield page
        context.close()
        browser.close()

@pytest.fixture
def context(page):
    return {"page": page}


screenshot_storage = {}


@pytest.fixture
def screenshot_helper(request, page):
    test_name = request.node.nodeid
    screenshot_storage[test_name] = []

    class ScreenshotHelper:
        def take(self, name="screenshot"):
            screenshot_bytes = page.screenshot()
            screenshot_b64 = base64.b64encode(screenshot_bytes).decode('utf-8')
            screenshot_storage[test_name].append((name, screenshot_b64))
            print(f"Screenshot '{name}' captured and stored")

    return ScreenshotHelper()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        test_name = item.nodeid
        if test_name in screenshot_storage:
            extra = getattr(report, 'extra', [])
            for name, screenshot_b64 in screenshot_storage[test_name]:
                extra.append(extras.image(screenshot_b64, name=name))
            report.extra = extra
            print(f"Attached {len(screenshot_storage[test_name])} screenshots to report")