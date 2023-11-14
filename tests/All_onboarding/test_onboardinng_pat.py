import datetime
import random
import time
import requests
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from tests.common import doct_no
#from src.pageObjects.Doctor_onboarding import Doctor_onboarding
# from .test_signup_doc import TestDoctorSignup
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from tests.All_onboarding.conftest import setup
from src.pageObjects.new_signup import test_New_signup
from faker import Faker


class TestPatientonboading:

    @pytest.mark.pat_onboarding
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
