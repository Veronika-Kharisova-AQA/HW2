import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless=new")  # Запуск без GUI (новый режим)
    options.add_argument("--window-size=1280,900")

    driver = webdriver.Chrome(options=options)
    yield driver

    driver.quit()  # Закрываем браузер после теста


def test_github_web(browser):
    url = "https://github.com/"
    browser.get(url)

    assert (
        browser.title
        == "GitHub · Build and ship software on a single, collaborative platform · GitHub"
    )
    assert browser.current_url == url


def test_google_web(browser):
    url = "https://www.google.com/"
    browser.get(url)

    assert browser.title == "Google"
    assert browser.current_url == url
