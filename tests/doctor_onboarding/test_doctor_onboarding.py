import datetime
import time
import requests
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.common import doct_no
from src.pageObjects.Doctor_onboarding import Doctor_onboarding
from .test_doctor_signup import TestDoctorSignup
from datetime import datetime, timedelta


class TestDoctoronboading:

    def test_first_last_mobile_no(self, setup):
        driver = setup
        doct_onboarding = Doctor_onboarding(driver)
        doct_onboarding.test_login()

        # verify Last name should not be empty and it is disabeld
        first_name_input = doct_onboarding.get_first_name()
        first_name = first_name_input.get_attribute("value")
        assert first_name.strip() != ""
        print("first_name content is", first_name)
        readonly_first_name = first_name_input.get_attribute('readonly')
        # Check if the "readonly" attribute is set to "readonly"
        assert readonly_first_name == "true", "The 'First Name' input field is disabled."

        # verify Last name should not be empty and it is disabeld

        last_name_input = doct_onboarding.get_last_name()
        last_name = last_name_input.get_attribute("value")
        assert last_name.strip() != ""
        readonly_last_name = last_name_input.get_attribute('readonly')
        readonly_last_name == "true", "The 'Last Name input field is disabled ."

        # verify mobile no should not be empty and it is also disabled
        mobile_no_input = doct_onboarding.get_mobile_no()
        mobile_no = mobile_no_input.get_attribute("value")
        assert mobile_no.strip() != ""
        readonly_mobile_no = last_name_input.get_attribute('readonly')
        readonly_mobile_no == "true", "The 'mobile_no input field is disabled ."
        # doct_onboarding.test_age_val()

    def test_calender(self, setup):
        driver = setup
        doct_onboarding = Doctor_onboarding(driver)
        doct_onboarding.test_login()

        # Call the test_age_val method to get the calculated age
        age = doct_onboarding.test_age_val()

        # Perform assertions on the age here
        # For example:
        if age < 18:
            # Trigger the error message
            age_error = doct_onboarding.get_age_error()
            assert age_error.text == "This field must be 18 or more", "Age validation is correct"

        elif age > 150:
            age_error_150 = doct_onboarding.age_error_150()
            assert age_error_150.text == "This field must be 150 or less", "Age validation is correct"
        else:
            "age validation is correct"

    def test_age_field_validation(self, setup):
        driver = setup
        doct_onboarding = Doctor_onboarding(driver)
        doct_onboarding.test_login()

        age_values = ["17", "151", "18", "150"]  # List of age inputs

        error_messages = doct_onboarding.age_field_validation(age_values)

        for age, error_message in zip(age_values, error_messages):
            age = int(age)
            if age < 18:
                expected_error = "This field must be 18 or more"
                assert error_message == expected_error, f"Age validation for {age} is correct"

            elif age > 150:
                expected_error = "This field must be 150 or less"
                assert error_message == expected_error, f"Age validation for {age} is correct"

    def test_all_mandatory_fields(self, setup):
        driver = setup
        doct_onboarding = Doctor_onboarding(driver)
        doct_onboarding.test_login()
        doct_onboarding.checkall_mandatory_fields()
        age_mandatory = doct_onboarding.get_age_mandatory()
        assert age_mandatory.text == "This field is required"
        gender_mandatory = doct_onboarding.get_gender_mandatory()
        assert gender_mandatory.text == "This field is required"
        # Scroll the div element down using JavaScript
        div_element = doct_onboarding.get_element()
        scroll_script = "arguments[0].scrollTop += 400;"
        driver.execute_script(scroll_script, div_element)
        time.sleep(5)
        branch_mandatory = doct_onboarding.get_age_mandatory()
        assert branch_mandatory.text == "This field is required"
        speciality_mandatory = doct_onboarding.get_speciality_mandatory()
        assert speciality_mandatory.text == "This field is required"
        state_mandatory = doct_onboarding.get_state_mandatory()
        assert state_mandatory.text == "This field is required"
        co_name_mandatory = doct_onboarding.get_co_name_mandatory()
        assert co_name_mandatory.text == "This field is required"
        co_no_mandatory = doct_onboarding.get_co_no_mandatory()
        assert co_no_mandatory.text == "This field is required"
        qual_mandatory = doct_onboarding.get_co_qual_mandatory()
        assert qual_mandatory.text == "This field is required"
        since_mandatroy = doct_onboarding.get_since_mandatroy()
        assert since_mandatroy.text == "This field is required"

    def test_select_branch(self, setup):
        driver = setup
        doct_onboarding = Doctor_onboarding(driver)
        doct_onboarding.test_login()
        doct_onboarding.select_gender()
