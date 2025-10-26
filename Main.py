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

    assert browser.title == "GitHub · Build and ship software on a single, collaborative platform · GitHub"
    assert browser.current_url == url


print("Привет, README!")

text = "Lorem Ipsum — это текст-«рыба», часто используемый в печати и веб-дизайне. Lorem Ipsum"

def add(a, b):
    return a + b

def greet(name):
    print("Привет, " + name)

numbers = [1, 2, 3, 4, 5]

greet("мир")        # вызов функции greet
print(add(2, 2))    # вызов функции add и вывод результата