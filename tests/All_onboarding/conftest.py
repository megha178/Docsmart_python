import pytest
from selenium import webdriver

from src.pageObjects.Doctor_onboarding import Doctor_onboarding


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://testfe.docsmart.in/")
    driver.maximize_window()

    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def doct_login(request):
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.get("https://testfe.docsmart.in/")
    driver.maximize_window()
    request.cls.driver = driver

    # You can choose the appropriate WebDriver here

    # Perform the login
    doct_onboarding = Doctor_onboarding(driver)
    doct_onboarding.test_login()

    yield driver  # This is where the actual test functions will run
    # Teardown: Close the WebDriver after all tests have run
    driver.quit()


""""@pytest.fixture(scope="function")
def setup_logged_in(request):
    driver = webdriver.Chrome()
    driver.get("https://testfe.docsmart.in/")
    driver.maximize_window()

    # Perform login here
    request.cls.driver = driver
    doct_onboarding = Doctor_onboarding(driver)
    doct_onboarding.login()
    yield driver
    driver.quit()"""
