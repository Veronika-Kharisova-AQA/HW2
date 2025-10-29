def test_github_web(browser):
    url = "https://github.com/"
    browser.get(url)

    assert (
        browser.title == "GitHub · Change is constant. GitHub keeps you ahead. · GitHub"
    )
    assert browser.current_url == url


def test_google_web(browser):
    url = "https://www.google.com/"
    browser.get(url)

    assert browser.title == "Google"
    assert browser.current_url == url
