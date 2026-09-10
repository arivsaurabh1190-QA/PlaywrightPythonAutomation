from pathlib import Path


def take_screenshot(page, test_name):

    screenshot_dir = Path("screenshots")

    screenshot_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    screenshot_path = (
        screenshot_dir / f"{test_name}.png"
    )

    page.screenshot(
        path=str(screenshot_path),
        full_page=True
    )

    return screenshot_path