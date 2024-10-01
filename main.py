from playwright.sync_api import sync_playwright


def auto_punch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://portal.uwplatt.edu/")

        # page.click('a[aria-label="Launch MyUW"]')
        page.click('"Launch MyUW"')

        page.wait_for_timeout(2000)

        browser.close()


if __name__ == "__main__":
    auto_punch()
