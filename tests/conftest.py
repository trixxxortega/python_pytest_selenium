import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Crear la carpeta screenshots si no existe
SCREENSHOTS_DIR = "screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless=new")  # Descomenta si querés modo headless
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--disable-gpu")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(20)
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook que se ejecuta después de cada test para obtener el reporte.
    Si el test falla, toma un screenshot del driver si está disponible.
    """
    # Ejecutar el resto de hooks para obtener el reporte
    outcome = yield
    rep = outcome.get_result()

    # Solo nos interesan fallos en la fase "call" (cuando corre el test)
    if rep.when == "call" and rep.failed:
        # Buscar el fixture driver en los argumentos del test
        driver = item.funcargs.get("driver", None)
        if driver is not None:
            # Construir nombre de archivo para el screenshot
            test_name = item.name
            screenshot_path = os.path.join(SCREENSHOTS_DIR, f"{test_name}.png")

            # Tomar screenshot y guardarlo
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot guardado en {screenshot_path}")
