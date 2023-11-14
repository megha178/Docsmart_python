import datetime
import time
import requests
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.common import doct_no
from src.pageObjects.Doctor_onboarding import Doctor_onboarding
from src.pageObjects.new_signup import test_New_signup
# from .test_signup_doc import TestDoctorSignup
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from tests.All_onboarding.conftest import setup, doct_login
from selenium.webdriver.support.ui import Select
import random


class TestDoctoronboading:
    @pytest.mark.description("This test case verifies all the mandatory fields on the page ,when click on submit")
    def test_all_mandatory_fields(self, doct_login):
        driver = doct_login
        doct_onboarding = Doctor_onboarding(driver)
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

    @pytest.mark.description(
        "This test case verifies first name ,last name and mobile no coorectly fetch from signup and it should be disabled")
    def test_first_last_mobile_no(self, doct_login):
        driver = doct_login
        doct_onboarding = Doctor_onboarding(driver)
        div_element = doct_onboarding.get_element()
        scroll_script = "arguments[0].scrollTop -= 400;"
        driver.execute_script(scroll_script, div_element)

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

    @pytest.mark.description(
        "This test case verifies gender drop down is visisble and select random values in the srop down")
    def test_gender_field(self, doct_login):
        driver = doct_login
        doct_onboarding = Doctor_onboarding(driver)
        gender = doct_onboarding.select_gender()
        assert gender.is_displayed() and gender.is_enabled(), "gender is not disaplyed or enabaled"

    @pytest.mark.description(
        "This test case verifies age field validation correctly , it checks for boundry value and after that randmly select the age")
    def test_age_field_validation(self, doct_login):
        driver = doct_login
        doct_onboarding = Doctor_onboarding(driver)

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

        random_age = random.randint(18, 150)
        age_input = str(random_age)
        doct_onboarding.get_age().clear()
        doct_onboarding.get_age().send_keys(age_input)

        div_element = doct_onboarding.get_element()
        scroll_script = "arguments[0].scrollTop += 400;"
        driver.execute_script(scroll_script, div_element)

        # Assuming the selected year is in the format "1934" (as a string)

        # Keep selecting a new year until it's less than the expected year
        while True:

            selected_year_str = doct_onboarding.select_year()

            # Convert the selected year to an integer
            selected_year = int(selected_year_str)
            current_year = datetime.now().year

            expected_year_difference = current_year - selected_year

            if expected_year_difference < random_age:
                break
            else:
                validation = doct_onboarding.get_practice_year_validation().text
                expected = "Practice experience should not exceed age"
                if validation == expected:
                    print(
                        f"Validation message '{validation}' matched the expected message '{expected}'. Retrying year selection.")
                else:
                    # If the validation message is unexpected, break the loop to handle the issue
                    print(f"Unexpected validation message: '{validation}'. Breaking the loop.")
                    break

    @pytest.mark.my_marker
    @pytest.mark.description(
        "This test case verifies drop down such as, branch of medicine, speciality, state, qualification feilds are enabled and select randomly values amongs them")
    def test_branch_state_qaulification(self, doct_login):
        driver = doct_login
        doct_onboarding = Doctor_onboarding(driver)

        branch_of_medicine = doct_onboarding.select_branch()
        assert branch_of_medicine.is_displayed() and branch_of_medicine.is_enabled(), "branch_of_medicine is not disaplyed or enabaled"
        time.sleep(2)
        div_element = doct_onboarding.get_element()
        scroll_script = "arguments[0].scrollTop += 400;"
        driver.execute_script(scroll_script, div_element)

        qualification = doct_onboarding.get_Highest_Qualification()
        qualification.click()
        qualification1 = doct_onboarding.get_main_qualification()
        qualification1.click()
        doct_onboarding.get_other_qualificationdropdown().click()
        doct_onboarding.get_otherqualification1().click()
        doct_onboarding.get_alert().is_displayed()
        alert_text = doct_onboarding.get_alert()
        actual_text = alert_text.text
        expected_text = "You cannot choose the qualification already selected in Higher qualifications."
        assert expected_text in actual_text, f"Expected alert text: '{expected_text}', Actual alert text: '{actual_text}'"
        doct_onboarding.get_alert_ok().click()
        doct_onboarding.get_otherqualification2().click()
        doct_onboarding.select_state()

    def test_council_name_no(self, doct_login):
        driver = doct_login
        doct_onboarding = Doctor_onboarding(driver)
        council_name = doct_onboarding.get_council_name()
        assert council_name.is_displayed(), "council name field is not availible"
        council_name.send_keys("ABCcouncil")
        council_no = doct_onboarding.get_council_num()
        assert council_no.is_displayed(), "council num is not availible"
        council_no.send_keys("1544")

    @pytest.mark.description(
        "This test case verifies that additional speciality is disabled initialy when user select primary speciality then only it gets enabled also user can select only 2 additioanl specaility")
    def test_speciality_additional_speciality(self, doct_login):
        driver = doct_login
        doct_onboarding = Doctor_onboarding(driver)

        add_sp = doct_onboarding.get_add_specialities()
        if "disabled" in add_sp.get_attribute("class"):
            print("Additional Speciality dropdown is disabled initially")
        else:
            print("Additional Speciality dropdown is still enabled.")

        time.sleep(2)
        speciality = doct_onboarding.select_speciality()
        assert speciality.is_displayed() and speciality.is_enabled(), "speciality is not disaplyed or enabaled"
        time.sleep(5)
        doct_onboarding.select_additional_speciality()
        doct_onboarding.check_third_speciality()

        # Assert that aria-checked is "false"

    #  if aria_checked == "false":
    #      print("User can only select the 2 additional specialities")
    #  else:
    #      print("User can select the 3rd speciality")

    def test_certifciate_upload(self, doct_login):
        driver = doct_login
        doct_onboarding = Doctor_onboarding(driver)
        div_element = doct_onboarding.get_element()
        scroll_script = "arguments[0].scrollTop += 400;"
        driver.execute_script(scroll_script, div_element)
        time.sleep(2)

        certificate_upload = doct_onboarding.get_upload_certificate()
        time.sleep(5)
        assert certificate_upload.is_enabled()
        certificate_upload.send_keys(doct_onboarding.file_path)

        #   icon_elemnet = doct_onboarding.get_i_icon()
        #   action = ActionChains(driver)
        #  action.move_to_element(icon_elemnet).perform()
        #   time.sleep(5)
        #  hovered_text_element = doct_onboarding.get_i_icon_text()
        #  time.sleep(5)
        #   hovered_text = hovered_text_element.text
        #   expected_text = "This certificate will not be shared.This authenticates you as a doctor.This will help patient search for you."
        #   assert hovered_text == expected_text, f"Hovered text is not as expected. Actual text: {hovered_text}"
        # scroll_script = "arguments[0].scrollTop + 400;"
        # driver.execute_script(scroll_script, div_element)

        #   assert certificate_upload.is_displayed() and certificate_upload.is_enabled()

    # time.sleep(5)

    def test_do_nothave_clinic(self, doct_login):
        driver = doct_login
        doct_onboarding = Doctor_onboarding(driver)

        time.sleep(2)
        div_element = doct_onboarding.get_element()
        scroll_script = "arguments[0].scrollTop += 300;"
        time.sleep(2)
        driver.execute_script(scroll_script, div_element)
        doct_onboarding.get_not_haveclinic().click()

        try:
            # Verify if the address input field is displayed
            address_input = doct_onboarding.get_currentaddress()
            assert address_input.is_displayed()
            # Enter address detail
            address_input.send_keys("waghbil thane")
            time.sleep(2)
            ActionChains(driver).send_keys(Keys.DOWN).perform()
            time.sleep(2)
            address_input.send_keys(Keys.RETURN)
            selected_address = address_input.get_attribute("value")
            expected_substring = "Waghbil,"
            assert expected_substring in selected_address, f"Expected substring '{expected_substring}' not found in selected address '{selected_address}'."
            address_input.send_keys(Keys.ESCAPE)
            time.sleep(2)
        except TimeoutException:
            # If no alert appears, handle it accordingly (e.g., raise an exception or print a message)
            print("No address field is found.")

        doct_onboarding.get_not_haveclinic().click()
        time.sleep(5)
        try:
            dialog = doct_onboarding.get_alert()
            dialog_text = dialog.text
            print("text is", dialog_text)
            expected_text = "Kindly Add a clinic or tick on do not have clinic option to proceed."

            if expected_text in dialog_text:
                print(f"Dialog text '{expected_text}' is present in the dialog.")
            else:
                print(f"Dialog text '{expected_text}' is not present in the dialog.")
        except TimeoutException:
            # If no alert appears, handle it accordingly (e.g., raise an exception or print a message)
            print("No alert found.")

        doct_onboarding.get_alert_ok().click()

    def test_add_clinic(self, doct_login):
        driver = doct_login
        doct_onboarding = Doctor_onboarding(driver)
        div_element = doct_onboarding.get_element()
        scroll_script = "arguments[0].scrollTop += 500;"
        driver.execute_script(scroll_script, div_element)
        doct_onboarding.get_add_clinic().click()
        time.sleep(5)
        prescription_no = doct_onboarding.get_check_box()
        is_checked = "checkmarked" in prescription_no.get_attribute("class")

        if is_checked:
            print("Prescription no Checkbox is checked by default.")
        else:
            print("Checkbox is not checked by default.")

        icon_element = doct_onboarding.get_i_followup()
        action = ActionChains(driver)
        action.move_to_element(icon_element).perform()
        hovered_text_followup = doct_onboarding.get_hovered_followup()
        hovered_text = hovered_text_followup.text
        expected_text = "Follow up fees will be charged after 90 days of the last appointment date."
        assert hovered_text == expected_text, f"Hovered text is not as expected. Actual text: {hovered_text}"

        doct_onboarding.get_clinic_no().send_keys("124")
        doct_onboarding.get_clinic_contact_val()
        doct_onboarding.get_clinic_no().send_keys("125255")
        doct_onboarding.get_first_fee().send_keys("500")
        doct_onboarding.get_follow_up().send_keys("250")

        current_Address = doct_onboarding.get_curr_Add()
        if current_Address.is_displayed() and current_Address.is_enabled():
            current_Address.click()
            time.sleep(10)

        else:
            print("current address field is not disabled")

        time.sleep(5)

        radio_option = doct_onboarding.get_everyday()
        print("1st radio_option is ", radio_option.text)

        if radio_option.get_attribute("aria-checked") == "true":
            print("Everyday time slot has selected by default.")
        else:
            print("Everyday is not selected by default.")
        element = doct_onboarding.get_element2()

        scroll_script = "arguments[0].scrollTop += 600;"
        driver.execute_script(scroll_script, element)

        from_time_list_items = doct_onboarding.get_from_time()
        from_time_list_items.click()
        list_1 = doct_onboarding.get_list_from_time()
        list_1[2].click()
        time.sleep(2)

        to_time_list_items = doct_onboarding.get_to_time()
        to_time_list_items.click()
        time.sleep(2)

        list_2 = doct_onboarding.get_to_list()
        list_2[1].click()
        time.sleep(5)
        validation = doct_onboarding.get_to_time_validation().text
        expected_message = "To Time should be greater then from time"
        print("Actual validation message:", validation)
        assert validation == expected_message, f"Validation message '{validation}' did not match the expected message '{expected_message}'"
        to_time_list_items.click()
        list_2[4].click()

        doct_onboarding.get_save_clinic().click()
        time.sleep(2)
        doct_onboarding.get_submit_button().click()
        expected_url = 'https://testapp.docsmart.in/doctor-dashboard'
        WebDriverWait(driver, 10).until(EC.url_contains(expected_url))
        current_url = driver.current_url
        assert expected_url in current_url
        time.sleep(2)
