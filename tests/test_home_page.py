from urllib.parse import urljoin

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL
from utils.driver_setup import driver

def test_logo_presence_and_clickable(driver):
    url = BASE_URL
    driver.get(url)

    # Wait for the logo to be visible
    logo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="container-bca776d573"]/div[1]/div[2]/div[1]/div[1]/a/img'))
    )
    assert logo is not None, "Logo is not present on Home Page"

    # Validate logo is clickable
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="container-bca776d573"]/div[1]/div[2]/div[1]/div[1]/a/img'))
        )
    except:
        pytest.fail("Logo is not clickable")

    # Opcional: clickeamos y validamos URL
    logo.click()
    expected_url = urljoin(BASE_URL, "/en/gl.html")
    WebDriverWait(driver, 5).until(EC.url_to_be(expected_url))
    assert driver.current_url == expected_url, "Wrong redirection URL after clicking the logo"