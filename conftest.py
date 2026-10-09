import pytest

from utils.screenshots import take_screenshot


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )


@pytest.fixture(scope="function")
def browser_page(page, request):
    """
    Provides a configured Playwright page for each test.
    """

    # Standard desktop viewport
    page.set_viewport_size({
        "width": 1920,
        "height": 1080
    })

    yield page

    # Capture screenshot when test fails
    if (
        hasattr(request.node, "rep_call")
        and request.node.rep_call.failed
    ):
        take_screenshot(
            page,
            request.node.name
        )