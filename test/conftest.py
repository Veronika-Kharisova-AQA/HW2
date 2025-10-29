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
