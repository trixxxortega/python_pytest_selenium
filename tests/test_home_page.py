import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BASE_URL = "https://www.terumobct.com/"


@pytest.mark.logo
def test_logo_is_visible(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 30)

    # Aceptar cookies si aparece el botón
    try:
        accept_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        accept_btn.click()
        print("✅ Botón de cookies aceptado")
    except TimeoutException:
        pass

    # Esperar a que cargue el logo principal
    try:
        logo = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@id, 'container-')]/div[1]/div[2]/div[1]/div[1]/a/img"))
        )
        assert logo.is_displayed(), "El logo está presente pero no visible"
        print("✅ Logo encontrado y visible")
    except TimeoutException:
        driver.save_screenshot("screenshot_logo_fail.png")
        pytest.fail("❌ No se pudo encontrar el logo dentro del tiempo esperado")
