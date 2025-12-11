from pytest_bdd import given, when, then

from pages.home_page import HomePage


@given("As an not logged user navigate to homepage https://www.kiwi.com/en/")
def open_homepage(context,screenshot_helper):
    home_page = HomePage(context['page'])
    home_page.open()
    screenshot_helper.take("Homepage loaded")
    context['home_page'] = home_page

@when("I select one-way trip type")
def search_one_way(context,screenshot_helper):
    context['home_page'].select_one_way()
    screenshot_helper.take("One way option selected")

@when("Set as departure airport RTM")
def select_RTM_departure(context,screenshot_helper):
    context['home_page'].set_airport("Rotterdam The Hague", True)
    screenshot_helper.take("Departure settings")

@when("Set the arrival Airport MAD")
def select_RTM_departure(context,screenshot_helper):
    context['home_page'].set_airport("MAD", False)
    screenshot_helper.take("Arrival settings")

@when("Set the departure time 1 week in the future starting current date")
def select_departure_date(context,screenshot_helper):
    context['home_page'].set_future_date(7)
    screenshot_helper.take("Period selected")

@when("Uncheck the `Check accommodation with booking.com` option")
def uncheck_booking(context,screenshot_helper):
    context['home_page'].click_booking_option()
    screenshot_helper.take("Booking option")

@when("Click the search button")
def search_flights(context,screenshot_helper):
    context['home_page'].submit_search()

@then("I am redirected to search results page")
def verify_redirect(context,screenshot_helper):
    context['home_page'].verify_redirect()
    screenshot_helper.take("Homepage loaded")