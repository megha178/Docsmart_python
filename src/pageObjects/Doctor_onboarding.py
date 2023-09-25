from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from tests.common import doct_no
import random
import requests
from selenium.webdriver.common.keys import Keys
from datetime import datetime


class Doctor_onboarding:

    def __init__(self, driver):
        self.driver = driver

    login_button = (By.ID, "loginRegister")
    role = (By.XPATH, ".//div[@class='v-select__selections']")
    select_role = (By.XPATH, "//div[@class='v-list-item v-list-item--link theme--light'][2]")
    num = (By.XPATH, "//label[text()='Enter your mobile number here.']/following-sibling::input")
    pwd = (By.XPATH, "//label[text()='Password']/following-sibling::div//input[@type='password']")
    submit = (By.XPATH, "//span[normalize-space()='Login']")
    age = (By.ID, "age")
    gender = (By.XPATH, "//select[@id='genderdoctor']")
    age_error = (By.XPATH, "//span[normalize-space()='This field must be 18 or more']")
    age_error_150 = (By.XPATH, "//span[normalize-space()='This field must be 150 or less']")
    branch_medicine = (By.NAME, "branchOfMedicinesDoctor")
    specialities = (By.NAME, "Specialities")
    first_name = (By.XPATH, "//input[@placeholder='First Name']")
    last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    Mobile_no = (By.XPATH, "//input[@placeholder='Mobile']")
    calender = (By.XPATH, "//input[@placeholder='DD/MM/YYYY']")
    profile = (By.XPATH, "//div[contains(text(), 'Upload Photo')]")
    date_element_xpath = (By.XPATH, "//span[@aria-label='Thursday, 8 September 2005']")
    div_element = (By.CSS_SELECTOR, "div.col-sm-12.p-0.mid-div")
    date_elements = (By.XPATH, "//span[contains(@class, 'vc-day-content')]")

    age_mandatory = (
        By.XPATH,
        "(//input[@id='age']/following-sibling::span[@class='text-danger' and text()='This field is required'])"
    )
    gender_mandatory = (
        By.XPATH, "//select[@id='genderdoctor']/following-sibling::span[contains(text(), 'This field is required')]"
    )
    branch_mandatory = (
        By.XPATH,
        "//select[@id='branchOfMedicinesDoctor']/following-sibling::span[@class='text-danger' and text()='This field is required']"
    )
    speciality_mandatory = (
        By.XPATH,
        "//select[@id='specialityDoctor']/following-sibling::span[@class='text-danger' and text()='This field is required']"
    )
    state_mandatory = (
        By.XPATH,
        "//select[@id='registering_state']/following-sibling::span[@class='text-danger' and text()='This field is required']"
    )
    co_name_mandatory = (
        By.XPATH,
        "//input[@id='registeringCouncilNameDoctor']/following-sibling::span[@class='text-danger' and text()='This field is required']"
    )
    co_no_mandatory = (
        By.XPATH,
        "//input[@id='registeringCouncilNumberDoctor']/following-sibling::span[@class='text-danger' and text()='This field is required']"
    )
    qual_mandatory = (
        By.XPATH,
        "//span[@class='text-danger required-fields' and contains(text(), 'This field is required') and preceding::input[@name='Qualification']]"
    )
    since_mandatroy = (
        By.XPATH,
        "//select[@id='inPracticeSinceDoctor']/following-sibling::span[@class='text-danger' and normalize-space()='This field is required']"
    )
    sumbit_button = (By.XPATH, "(//button[contains(@type,'button')])[32]")

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.login_button)
        )

    def get_role(self):
        return self.driver.find_element(*Doctor_onboarding.role)

    def get_select_role(self):
        return self.driver.find_element(*Doctor_onboarding.select_role)

    def get_num(self):
        return self.driver.find_element(*Doctor_onboarding.num)

    def get_pwd(self):
        return self.driver.find_element(*Doctor_onboarding.pwd)

    def get_gender(self):
        return self.driver.find_element(*Doctor_onboarding.gender)

    def get_submit(self):
        return self.driver.find_element(*Doctor_onboarding.submit)

    def get_age_error(self):
        return self.driver.find_element(*Doctor_onboarding.age_error)

    def get_age(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.age)
        )

    def get_element(self):
        return self.driver.find_element(*Doctor_onboarding.div_element)

    #  def get_age_error(self):
    #     return WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(Doctor_onboarding.age_error)
    #     )

    # def get_age_error150(self):
    #     return WebDriverWait(self.driver, 10).until(
    #        EC.visibility_of_element_located(Doctor_onboarding.age_error_150)
    #    )

    def get_age_error_150(self):
        # Locate the age error element directly without waiting
        return self.driver.find_element(*Doctor_onboarding.age_error_150)

    def get_calender(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Doctor_onboarding.calender)
        )

    def get_branch(self):
        return self.driver.find_element(*Doctor_onboarding.branch_medicine)

    def get_specialities(self):
        return self.driver.find_element(*Doctor_onboarding.specialities)

    def get_profile(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.profile)
        )

    # def get_date_elements(self):
    #    return WebDriverWait(self.driver, 10).until(
    #       EC.presence_of_all_elements_located(Doctor_onboarding.date_elements)
    #    )
    def get_date_elements(self):
        return self.driver.find_elements(*Doctor_onboarding.date_elements)

    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.first_name)
        )

    def get_last_name(self):
        return self.driver.find_element(*Doctor_onboarding.last_name)

    def get_mobile_no(self):
        return self.driver.find_element(*Doctor_onboarding.Mobile_no)

    def get_day(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.date_element_xpath)
        )

    def get_age_mandatory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.age_mandatory)
        )

    def get_gender_mandatory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.gender_mandatory)
        )

    def get_speciality_mandatory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.speciality_mandatory)
        )

    def get_branch_mandatory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.branch_mandatory)
        )

    def get_state_mandatory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.state_mandatory)
        )

    def get_co_name_mandatory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.co_name_mandatory)
        )

    def get_co_no_mandatory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.co_no_mandatory)
        )

    def get_co_qual_mandatory(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Doctor_onboarding.qual_mandatory)
        )

    def get_since_mandatroy(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.since_mandatroy)
        )

    def get_submit_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.sumbit_button)
        )

    def test_login(self, pwd="Admin@123"):
        self.get_login_button().click()
        self.get_role().click()
        time.sleep(2)
        self.get_select_role().click()
        time.sleep(2)
        self.get_num().send_keys(doct_no)
        self.get_pwd().send_keys(pwd)
        self.get_submit().click()
        time.sleep(5)

    def select_branch(self):
        branch_element = self.get_branch()
        all_options = branch_element.find_elements(By.TAG_NAME, "option")
        all_options.pop[0]
        random.shuffle(all_options)
        select_branch = all_options[0].text
        Select(branch_element).select_by_visible_text(select_branch)
        # time.sleep(5)
        print("random branch is", select_branch)
        return select_branch

    def select_gender(self):
        gender_element = self.get_gender()
        all_gender = gender_element.find_elements(By.TAG_NAME, "option")
        all_gender.pop(0)
        random.shuffle(all_gender)
        select_gender = all_gender[0].text
        # select = Select(gender_element)
        Select(gender_element).select_by_visible_text(select_gender)
        print("random gender is", select_gender)
        return select_gender

    def select_speciality(self):
        sp_element = self.get_specialities()
        all_speciality = sp_element.findelements(By.TAG_NAME, "option")
        all_speciality.pop(0)
        random.shuffle(all_speciality)
        select_sp = all_speciality[0].text
        Select(sp_element).select_by_visible_text(select_sp)

    def test_age_val(self):
        calendar_element = self.get_calender()
        calendar_element.click()

        # Add additional waiting logic here to ensure the calendar is fully loaded

        # Get all date elements in the calendar
        date_elements = self.get_date_elements()

        # Select a random date from the available date elements
        random_date_element = random.choice(date_elements)
        random_date_text = random_date_element.get_attribute("aria-label")

        # Now that you have selected the date, calculate the age
        selected_date_text = random_date_text
        print("selected date is", selected_date_text)
        selected_date = datetime.strptime(selected_date_text, '%A, %d %B %Y')
        current_date = datetime.now()
        age = current_date.year - selected_date.year - (
                (current_date.month, current_date.day) < (selected_date.month, selected_date.day))

        # Set the calculated age into the age input field
        age_input = self.get_age()
        age_input.clear()
        age_input.send_keys(str(age))
        return age

    def age_field_validation(self, age_values):
        error_messages = []

        for age in age_values:
            self.get_age().clear()
            self.get_age().send_keys(age)
            if age == "151":
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[normalize-space()='This field must be 150 or less']"))
                )
                age_error = self.get_age_error_150()
                error_messages.append(age_error.text)
            elif age == "17":
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[normalize-space()='This field must be 18 or more']"))
                )
                age_error = self.get_age_error()
                error_messages.append(age_error.text)
            #  error_messages.append(age_error.text)
            else:

                error_messages.append(None)

        return error_messages

    def checkall_mandatory_fields(self):

        self.get_submit_button().click()
        time.sleep(2)
