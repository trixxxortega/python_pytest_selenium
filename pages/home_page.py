# pages/home_page.py

from selenium.webdriver.common.by import By

class HomePage:
    """
    Page Object Model for the Home Page of the Application Under Test (AUT).
    This class contains locators and methods to interact with the home page.
    """

    # Define locators as class variables
    TITLE_LOCATOR = (By.TAG_NAME, "")  # Example: you rarely get title this way, better driver.title
    WELCOME_MESSAGE = (By.ID, "welcome-msg")  # Example locator by id
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.login")  # Example locator by CSS selector

    def __init__(self, driver):
        """
        Constructor method.
        :param driver: Selenium WebDriver instance
        """
        self.driver = driver

    def get_title(self):
        """
        Return the page title using Selenium driver method.
        """
        return self.driver.title

    def is_welcome_message_displayed(self):
        """
        Check if the welcome message element is visible on the page.
        Returns True if displayed, False otherwise.
        """
        element = self.driver.find_element(*self.WELCOME_MESSAGE)
        return element.is_displayed()

    def click_login(self):
        """
        Click on the login button.
        """
        self.driver.find_element(*self.LOGIN_BUTTON).click()
