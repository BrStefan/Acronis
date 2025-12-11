from playwright.sync_api import Page
from .home_locators import HomePageLocators as L

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://www.kiwi.com/en/")
        self.accept_cookies()

    def select_one_way(self):
        self.open_travel_modes()
        self.page.locator(L.TRIP_TYPE_ONEWAY).click()

    def open_travel_modes(self):
        self.page.locator(L.TRIP_TYPE_DROPDOWN).click()

    def set_airport(self, code: str, is_origin: bool):
        chips = self.page.locator(L.TRAVEL_CHIP_CLOSE)
        if chips.count() > 0:
            idx = 0 if is_origin else 1
            if chips.count() > idx:
                chips.nth(idx).click()
        input_locator = L.FROM_INPUT if is_origin else L.TO_INPUT
        self.page.locator(input_locator).fill(code)

        self.page.locator(L.SUGGESTION_FILTER).first.click()

    def set_future_date(self, days: int):
        self.page.locator(L.DATE_INPUT).click()
        self.page.locator(L.FUTURE_DATE).nth(days).click()
        self.page.locator(L.SET_DATES_BUTTON).click()

    def click_booking_option(self):
        self.page.locator(L.BOOKING_CHECKBOX).click()

    def submit_search(self):
        self.page.locator(L.SEARCH_BUTTON).click()

    def accept_cookies(self):
        self.page.locator(L.ACCEPT_COOKIES).click()

    def verify_redirect(self):
        results = self.page.locator(L.SEARCH_RESULTS)
        results.wait_for(timeout=10000)
        assert results.count() > 0, "No results found"

