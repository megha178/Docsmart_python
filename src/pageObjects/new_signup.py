from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests
from faker import Faker
import random
from selenium.common.exceptions import NoSuchElementException


# from tests.common import doct_no


class test_New_signup:

    def __init__(self, driver):
        self.driver = driver
        self.mobile_no = None

    signup_button = (By.XPATH, "//li[@id='newUser']")
    select_role = (By.XPATH, "//div[@role='button']")
    doctor_role = (By.XPATH, "//div[@class='v-list-item v-list-item--link theme--light'][2]")
    patient_role = (By.XPATH, "//div[@class='v-list-item v-list-item--link theme--light'][1]")

    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    number = (By.XPATH, "//label[text()='Enter your mobile number here.']/following-sibling::input")
    check_1 = (By.XPATH, "//label[normalize-space()='I confirm I am over 18 years old.']")
    check_2 = (By.XPATH, "//label[normalize-space()='I agree to the']")
    send_otp = (By.XPATH, "//span[normalize-space()='SEND OTP']")
    Enter_otp = (By.XPATH, "//label[text()='Enter OTP']/following-sibling::input[@type='text']")
    verify_otp = (By.XPATH, "//button[contains(., 'Verify OTP')]")
    yes_option = (By.XPATH, "//span[contains(., 'Yes')]")
    password = (By.XPATH, "//div[label[text()='Password']]/input[@type='password']")
    conf_passowrd = (
        By.XPATH, "//label[contains(text(), 'Confirm Password')]/following-sibling::input[@type='password']")
    set_password = (By.XPATH, "//span[normalize-space()='set password']")
    go_to_dashboard = (By.XPATH, "//span[normalize-space()='Proceed']")
    user_already_exists_xpath = (
        By.XPATH, "//div[@class='v-snack__content' and contains(text(), 'USER ALREADY EXISTS')]")

    def get_user_already_exisit(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(test_New_signup.user_already_exists_xpath)
        )

    def get_signup_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(test_New_signup.signup_button)
        )

    def get_select_role(self):
        return self.driver.find_element(*test_New_signup.select_role)

    def get_doctor_role(self):
        return self.driver.find_element(*test_New_signup.doctor_role)
    def get_patient_role(self):
        return self.driver.find_element(*test_New_signup.patient_role)

    def get_first_name(self):
        return self.driver.find_element(*test_New_signup.first_name)

    def get_last_name(self):
        return self.driver.find_element(*test_New_signup.last_name)

    def get_number(self):
        return self.driver.find_element(*test_New_signup.number)

    def get_check_1(self):
        return self.driver.find_element(*test_New_signup.check_1)

    def get_check_2(self):
        return self.driver.find_element(*test_New_signup.check_2)

    def get_send_otp(self):
        return self.driver.find_element(*test_New_signup.send_otp)

    def get_role_option(self, role):
        if role == "Doctor":
            return self.get_doctor_role()
        elif role == "Patient":
            return self.get_patient_role()
        else:
            raise ValueError("invalid role provided")

    def generate_random_mobile_number(self):
        if self.mobile_no is None:
            fake = Faker()
            while True:
                # Generate a random number that starts from 1 to 5 (avoiding 0 and 6-9)
                first_digit = str(random.randint(1, 5))
                # Generate the rest of the digits
                rest_of_digits = fake.random_int(min=100000000, max=999999999)
                mobile_number = first_digit + str(rest_of_digits)
                if len(mobile_number) == 10:
                    print("no is", mobile_number)
                    self.mobile_no = mobile_number  # Store the generated mobile_no
                    break  # Exit the loop when a valid mobile number is generated
            return self.mobile_no

    def save_mobile_no(self):
        self.generate_random_mobile_number()

    def call_api_to_fetch_otp(self, mobile_number):

        # random_mobile_number = self.generate_random_mobile_number()
        # self.get_send_otp().click()

        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYwMzYyMmEyOGRmN2JkNjg5OTFjOGQ4OSIsImlhdCI6MTY2NzE0NDAwMX0.QbTTz4KFzo00b0FXKb8DbODY3RpWy5ggFd5SlIa75hs"
        url = "https://testapi.docsmart.in/api/v2/admin/users/details"

        # Headers with the Authorization token
        headers = {
            "Authorization": f"Bearer {token}"
        }

        # JSON data to send in the POST request (if needed)
        payload = {
            "mobile": mobile_number
        }

        response = requests.post(url, headers=headers, json=payload)

        # Perform assertions or verifications on the response
        assert response.status_code == 200

        OTP = response.json()["data"]["userDetails"]["otp"]
        print("OTP:", OTP)
        return OTP

    def get_Enter_otp(self):
        return self.driver.find_element(*test_New_signup.Enter_otp)

    def get_verify_otp(self):
        return self.driver.find_element(*test_New_signup.verify_otp)

    def get_yes_option(self):
        return self.driver.find_element(*test_New_signup.yes_option)

    def get_password(self):
        return self.driver.find_element(*test_New_signup.password)

    def get_conf_passowrd(self):
        return self.driver.find_element(*test_New_signup.conf_passowrd)

    def get_set_password(self):
        return self.driver.find_element(*test_New_signup.set_password)

    def get_go_to_dashboard(self):

        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(test_New_signup.go_to_dashboard)
        )

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def test_common_signup(self, first_name, last_name, role, password, conf_password):
        self.get_signup_button().click()
        self.get_select_role().click()
        self.get_role_option(role).click()
        #  self.get_doctor_role().click()
        self.get_first_name().send_keys(first_name)
        self.get_last_name().send_keys(last_name)
        while True:
            mobile_no = self.generate_random_mobile_number()
            self.get_number().send_keys(mobile_no)
            time.sleep(2)

            self.get_check_1().click()
            self.get_check_2().click()

            time.sleep(5)
            self.get_send_otp().click()
            try:
                # user_exists_element = self.get_user_already_exisit()
                if self.is_element_present(test_New_signup.user_already_exists_xpath):
                    # Element is present, generate a new number
                    continue
                else:
                    # Element is not present, break out of the loop
                    break
            except NoSuchElementException:
                # Element not found, continue execution
                pass
        time.sleep(2)
        otp = self.call_api_to_fetch_otp(mobile_no)
        self.get_Enter_otp().send_keys(otp)
        time.sleep(5)
        self.get_verify_otp().click()
        time.sleep(2)
        self.get_yes_option().click()
        time.sleep(2)
        self.get_password().send_keys(password)
        self.get_conf_passowrd().send_keys(conf_password)
        self.get_set_password().click()
        time.sleep(2)
        self.get_go_to_dashboard().click()
