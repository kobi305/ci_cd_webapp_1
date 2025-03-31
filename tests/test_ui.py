from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_ui_title():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get("http://localhost:5000/")
    assert "Deployed via CI/CD!" in driver.title
    driver.quit()
