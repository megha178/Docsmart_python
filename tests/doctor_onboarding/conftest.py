import pytest
from selenium import webdriver

#from src.pageObjects.Doctor_onboarding import Doctor_onboarding


@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://testfe.docsmart.in/")
    driver.maximize_window()

    request.cls.driver = driver
    yield driver
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
