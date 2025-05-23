from urllib.parse import urljoin
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.config import BASE_URL
from utils.driver_setup import driver

def test_logo_presence_and_clickable(driver):
    url = BASE_URL
    driver.get(url)

    try:
        # Wait for the logo to be visible
        logo = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="container-bca776d573"]/div[1]/div[2]/div[1]/div[1]/a/img'))
        )
    except TimeoutException:
        driver.save_screenshot("error_logo_not_visible.png")
        pytest.fail("Logo is not present on Home Page")

    try:
        # Validate logo is clickable
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="container-bca776d573"]/div[1]/div[2]/div[1]/div[1]/a/img'))
        )
    except TimeoutException:
        driver.save_screenshot("error_logo_not_clickable.png")
        pytest.fail("Logo is not clickable")

    # Opcional: clickeamos y validamos URL
    logo.click()
    expected_url = urljoin(BASE_URL, "/en/gl.html")
    try:
        WebDriverWait(driver, 20).until(EC.url_to_be(expected_url))
    except TimeoutException:
        driver.save_screenshot("error_wrong_redirect_url.png")
        pytest.fail("Wrong redirection URL after clicking the logo")

    assert driver.current_url == expected_url
