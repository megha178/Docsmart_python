import time
import requests
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.common import doct_no
from src.pageObjects.new_signup import test_New_signup


class TestDoctorSignup:

    def test_doctor_signup(self, setup):
        driver = setup
        newsignup = test_New_signup(driver)
        newsignup.test_signup(first_name="naina", last_name="m", password="Admin@123",
                              conf_password="Admin@123")

        expected_url = "https://testapp.docsmart.in/onboard-doctor"
        WebDriverWait(driver, 10).until(EC.url_contains(expected_url))

        # Check if the current URL contains the expected URL
        current_url = driver.current_url
        assert expected_url in current_url
        time.sleep(10)
