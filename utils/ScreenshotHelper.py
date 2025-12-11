from pytest_html import extras


class ScreenshotHelper:
    def __init__(self, page, request):
        self.page = page
        self.request = request

    def take(self, name="screenshot"):
        screenshot_bytes = self.page.screenshot()
        extra = getattr(self.request.node, 'extra', [])
        extra.append(extras.image(screenshot_bytes, name=name))
        self.request.node.extra = extra