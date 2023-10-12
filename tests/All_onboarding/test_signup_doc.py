import time
import requests
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.common import doct_no
from src.pageObjects.new_signup import test_New_signup
from faker import Faker


class TestDoctorSignup:

    def test_doc_signup(self, setup):
        driver = setup
        newsignup = test_New_signup(driver)
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        role = "Doctor"

        newsignup.test_common_signup(first_name=first_name, last_name=last_name, role=role, password="Admin@123",
                              conf_password="Admin@123")
        expected_url = "https://testapp.docsmart.in/onboard-doctor"
        WebDriverWait(driver, 10).until(EC.url_contains(expected_url))

        # Check if the current URL contains the expected URL
        current_url = driver.current_url
        assert expected_url in current_url

    def test_pat_signup(self, setup):
        driver = setup
        newsignup = test_New_signup(driver)
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        role = "Patient"

        newsignup.test_common_signup(first_name=first_name, last_name=last_name, role=role, password="Admin@123",
                                     conf_password="Admin@123")
        expected_url = "https://testapp.docsmart.in/onboard-patient"
        WebDriverWait(driver, 10).until(EC.url_contains(expected_url))

        # Check if the current URL contains the expected URL
        current_url = driver.current_url
        assert expected_url in current_url

