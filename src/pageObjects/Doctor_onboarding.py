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
from src.pageObjects.new_signup import test_New_signup


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
    add_speciality = (By.CSS_SELECTOR,
                      ".v-input.ww-100.additional-speciality-select.v-text-field.v-text-field--placeholder.v-select.v-select--chips.v-select--chips--small.v-autocomplete.v-input--hide-details.v-input--is-disabled.theme--light")
    add_sp1 = (By.XPATH, "//input[@placeholder='Select Speciality']")
    list1 = (By.CSS_SELECTOR, "div[role='listitem']")

    first_name = (By.XPATH, "//input[@placeholder='First Name']")
    last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    Mobile_no = (By.XPATH, "//input[@placeholder='Mobile']")
    calender = (By.XPATH, "//input[@placeholder='DD/MM/YYYY']")
    profile = (By.XPATH, "//div[contains(text(), 'Upload Photo')]")
    date_element_xpath = (By.XPATH, "//span[@aria-label='Thursday, 8 September 2005']")
    div_element = (By.CSS_SELECTOR, "div.col-sm-12.p-0.mid-div")
    date_elements = (By.XPATH, "//span[contains(@class, 'vc-day-content')]")
    practice_since = (By.ID, "inPracticeSinceDoctor")
    year = (By.ID, "number_of_years_practicing")
    state = (By.ID, "registering_state")
    council_name = (By.ID, "registeringCouncilNameDoctor")
    council_number = (By.ID, "registeringCouncilNumberDoctor")
    qualification = (By.XPATH,
                     "//div[@class='v-input v-text-field v-text-field--placeholder v-select v-select--chips v-input--hide-details theme--light']//i[@class='v-icon material-icons theme--light'][normalize-space()='arrow_drop_down']")
    list_qailification = (By.XPATH, "//div[contains(text(),'MBBS')]")
    not_haveclinic = (By.XPATH, "//label[normalize-space()='I do not have a Clinic']")
    alert = (By.XPATH, "//div[@role='dialog']")
    Add_clinic = (By.XPATH, "//div[normalize-space()='Add Clinic +']")
    first_fee = (By.ID, "firstFeeDoctor")
    follow_up = (By.ID, "followUpFeesDoctor")

    hovered_followup = (By.XPATH, "//p[contains(@class,'text-success')]")
    i_followup = (By.XPATH, "//div[@data-v-4ac3fb3c and @class='i-hover-tooltip']")
    clinic_no = (By.XPATH, "//input[@placeholder='Clinic Contact Number']")
    clinic_no_val = (By.XPATH, "//span[normalize-space()='This field must be at least 6 characters']")
    clinic_address = (By.XPATH, "//input[@placeholder='Address']")
    appt_slot = (By.XPATH, "//input[@placeholder='Slot']")
    everyday = (By.XPATH,
                "//div[@class='v-radio theme--light accent--text']//input[@aria-label='Everyday' and @aria-checked='true']")
    from_time_parent = (By.XPATH,
                        "//div[@class='v-input active d-block v-text-field v-text-field--single-line v-text-field--solo v-text-field--enclosed v-select v-input--hide-details theme--light']//i[@class='v-icon material-icons theme--light'][normalize-space()='arrow_drop_down']")

    item_list = (By.XPATH, ".//div[@role='listitem']")

    list2 = (By.XPATH,
             "//body/div[@id='app']/div[contains(@class,'v-dialog__content v-dialog__content--active')]/div[contains(@class,'v-dialog v-dialog--active v-dialog--fullscreen v-dialog--scrollable')]/div[contains(@class,'center-add-modal v-card v-sheet theme--light')]/div[contains(@class,'v-card-min-height')]/div[contains(@class,'container pb-6rem')]/div[contains(@class,'row')]/div[contains(@class,'col-sm-12 nopad')]/div[contains(@class,'row martop-2p')]/div[contains(@class,'row')]/div[contains(@class,'col-sm-12')]/div/div[contains(@class,'col-sm-12')]/div[contains(@class,'row')]/div[contains(@class,'row')]/div[contains(@class,'col-sm-12')]/div[contains(@class,'col-sm-4 col-xs-6 select-style')]/div[contains(@role,'combobox')]/div[contains(@class,'v-menu__content theme--light menuable__content__active')]/div[contains(@class,'v-select-list v-card theme--light')]/div[1]/div")

    to_time_validation = (By.XPATH, "//span[normalize-space()='To Time should be greater then from time']")
    to_time_parent = (By.XPATH,
                      "//div[contains(@class,'col-sm-12 nopad')]//div[contains(@class,'col-sm-12')]//div//div[2]//div[1]//div[2]//div[1]//div[1]//div[2]//div[1]//i[1]")

    time_val = (By.XPATH, "//span[normalize-space()='To Time should be greater then from time']")

    MtF = (By.XPATH, "//label[normalize-space()='Everyday']")
    MtS = (By.XPATH, "//label[normalize-space()='Monday to Saturday']")
    customize = (By.XPATH, "//label[normalize-space()='Customize']")
    save_clinic = (By.XPATH, "//button[@id='saveButtonClinic']")
    check_box = (By.CSS_SELECTOR, "label[role='tablist'] span[class='checkmarked']")
    cancel = (By.XPATH,
              "//button[contains(@class,'btn btn-red-outline bg-light-danger text-danger border-0 font-weight-bold mt-0 v-btn theme--light')]//div[contains(@class,'v-btn__content')][normalize-space()='Cancel']")

    ok_button = (
        By.XPATH, "//button[contains(@class, 'swal2-confirm') and contains(@class, 'swal2-styled') and text()='OK']")

    i_icon = (By.XPATH,
              "//div[@class='icon-div']//*[name()='svg']//*[name()='g' and @id='Layer_4']//*[name()='circle' and contains(@class,'st0')]")
    hovered_text_element = (By.XPATH, "//div[@class='icon-div']//div[@class='hover-div w-20rem']/p")

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
    sumbit_button = (By.XPATH, "(//button[@type='button'])[32]")

    file_path = "/Users/megha/PycharmProject/Docsmart_python/tests/All_onboarding/certificate.jpeg"
    upload_certificate = (By.XPATH, "//div[@class='upload-btn-div']//input[@type='file'][@id='upload1Qual']")

    current_address = (By.XPATH,
                       "//input[@type='text' and @name='Address1' and @placeholder='Address' and contains(@class, 'pac-target-input')]")
    curr_add = (By.XPATH, "//div[@id='address_line_2']//img[@class='ab']")
    radio_slot = (By.XPATH,
                  "//div[@class='v-input v-input--selection-controls v-input--radio-group v-input--radio-group--row v-input--is-label-active v-input--is-dirty theme--light']")
    element = (By.XPATH, "//div[@class='v-card__text  v-card-min-height']")

    practice_year_validation = (
        By.XPATH, "//span[@class='text-danger' and text()='Practice experience should not exceed age']")

    def get_list_qualification(self):
        return self.driver.find_element(*Doctor_onboarding.list_qailification)

    def get_practice_year_validation(self):
        return self.driver.find_element(*Doctor_onboarding.practice_year_validation)

    def get_to_time_validation(self):
        return self.driver.find_element(*Doctor_onboarding.to_time_validation)

    def get_element2(self):
        return self.driver.find_element(*Doctor_onboarding.element)

    def get_to_list(self):
        return self.driver.find_elements(*Doctor_onboarding.list2)

    def get_list_from_time(self):
        return self.driver.find_elements(*Doctor_onboarding.item_list)

    def get_time_val(self):
        return self.driver.find_elements(*Doctor_onboarding.time_val)

    def get_from_time(self):
        return self.driver.find_element(*Doctor_onboarding.from_time_parent)

    def get_to_time(self):
        return self.driver.find_element(*Doctor_onboarding.to_time_parent)

    def get_radio_option(self):
        return self.driver.find_elements(*Doctor_onboarding.radio_slot)

    def get_curr_Add(self):
        return self.driver.find_element(*Doctor_onboarding.curr_add)

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
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.gender)
        )

    def get_submit(self):
        return self.driver.find_element(*Doctor_onboarding.submit)

    def get_age_error(self):
        return self.driver.find_element(*Doctor_onboarding.age_error)

    def get_age(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.age)
        )

    def get_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.div_element)
        )

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
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Doctor_onboarding.branch_medicine)
        )

    def get_specialities(self):
        return self.driver.find_element(*Doctor_onboarding.specialities)

    def get_add_specialities(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.add_speciality)
        )

    def get_add1(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.add_sp1)
        )

    def get_list1(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Doctor_onboarding.list1)
        )

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

    def get_practice_since(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.practice_since)
        )

    def get_year(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.year)
        )

    def get_submit_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Doctor_onboarding.sumbit_button)
        )

    def get_i_icon(self):
        return self.driver.find_element(*Doctor_onboarding.i_icon)

    def get_i_icon_text(self):
        return self.driver.find_element(*Doctor_onboarding.hovered_text_element)

    def get_upload_certificate(self):
        return self.driver.find_element(*Doctor_onboarding.upload_certificate)

    def get_state(self):
        return self.driver.find_element(*Doctor_onboarding.state)

    def get_council_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Doctor_onboarding.council_name)
        )

    def get_council_num(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Doctor_onboarding.council_number)
        )

    def get_qualification(self):
        return self.driver.find_element(*Doctor_onboarding.qualification)

    def get_not_haveclinic(self):
        return self.driver.find_element(*Doctor_onboarding.not_haveclinic)

    def get_currentaddress(self):
        return self.driver.find_element(*Doctor_onboarding.current_address)

    def get_alert(self):
        return self.driver.find_element(*Doctor_onboarding.alert)

    def get_alert_ok(self):
        return self.driver.find_element(*Doctor_onboarding.ok_button)

    def get_add_clinic(self):
        return self.driver.find_element(*Doctor_onboarding.Add_clinic)

    def get_first_fee(self):
        return self.driver.find_element(*Doctor_onboarding.first_fee)

    def get_follow_up(self):
        return self.driver.find_element(*Doctor_onboarding.follow_up)

    def get_hovered_followup(self):
        return self.driver.find_element(*Doctor_onboarding.hovered_followup)

    def get_i_followup(self):
        return self.driver.find_element(*Doctor_onboarding.i_followup)

    def get_clinic_no(self):
        return self.driver.find_element(*Doctor_onboarding.clinic_no)

    def get_clinic_address(self):
        return self.driver.find_element(*Doctor_onboarding.clinic_address)

    def get_appt_slot(self):
        return self.driver.find_element(*Doctor_onboarding.appt_slot)

    def get_everyday(self):
        return self.driver.find_element(*Doctor_onboarding.everyday)

    def get_MtF(self):
        return self.driver.find_element(*Doctor_onboarding.MtF)

    def get_MtS(self):
        return self.driver.find_element(*Doctor_onboarding.MtS)

    def get_customize(self):
        return self.driver.find_element(*Doctor_onboarding.customize)

    def get_save_clinic(self):
        return self.driver.find_element(*Doctor_onboarding.save_clinic)

    def get_check_box(self):
        return self.driver.find_element(*Doctor_onboarding.check_box)

    def get_cancel(self):
        return self.driver.find_element(*Doctor_onboarding.check_box)

    def get_clinic_contact_val(self):
        return self.driver.find_element(*Doctor_onboarding.clinic_no_val)

    def test_login(self, pwd="Admin@123"):

        self.get_login_button().click()
        self.get_role().click()
        time.sleep(2)
        self.get_select_role().click()
        time.sleep(1)


        self.get_num().send_keys(doct_no)
        self.get_pwd().send_keys(pwd)
        self.get_submit().click()
        time.sleep(2)

    def select_state(self):
        state_element = self.get_state()
        all_options = state_element.find_elements(By.TAG_NAME, "option")
        all_options.pop(0)
        random.shuffle(all_options)
        select_state = all_options[0].text
        Select(state_element).select_by_visible_text(select_state)
        print("state is", select_state)
        return select_state

    def select_branch(self):
        branch_element = self.get_branch()
        all_options = branch_element.find_elements(By.TAG_NAME, "option")
        all_options.pop(0)
        random.shuffle(all_options)
        select_branch = all_options[0]
        Select(branch_element).select_by_visible_text(select_branch.text)
        # time.sleep(5)
        print("random branch is", select_branch.text)
        return select_branch

    def select_speciality(self):
        speciality_element = self.get_specialities()
        all_options = speciality_element.find_elements(By.TAG_NAME, "option")
        all_options.pop(0)
        random.shuffle(all_options)
        select_speciality = all_options[0]
        Select(speciality_element).select_by_visible_text(select_speciality.text)
        # time.sleep(5)
        print("random branch is", select_speciality)
        return select_speciality

    def select_gender(self):
        gender_element = self.get_gender()
        all_gender = gender_element.find_elements(By.TAG_NAME, "option")
        all_gender.pop(0)
        random.shuffle(all_gender)
        select_gender = all_gender[0]
        # select = Select(gender_element)
        Select(gender_element).select_by_visible_text(select_gender.text)
        print("random gender is", select_gender.text)
        return select_gender

    def select_year(self):
        year_element = self.get_practice_since()
        all_year = year_element.find_elements(By.TAG_NAME, "option")
        all_year.pop(0)
        random.shuffle(all_year)
        select_year = all_year[0].text
        # select = Select(year_element)
        Select(year_element).select_by_visible_text(select_year)
        print("random Year is", select_year)
        return select_year

    def invalid_year(self):
        year_element = self.get_practice_since()
        all_year = year_element.find_elements(By.TAG_NAME, "option")

        select_year = all_year[1].text
        # select = Select(year_element)
        Select(year_element).select_by_visible_text(select_year)
        print("random Year is", select_year)
        return select_year

    def select_additional_speciality(self):
        # self.get_add1()
        list_1 = self.get_add1()
        list_1.click()

        list_item1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@class="v-list__tile__title"][contains(text(), "Adult Intensivist")]')))

        list_item1.click()

        list_item2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@class="v-list__tile__title"][contains(text(), "Allergy Specialist")]')))
        list_item2.click()
        time.sleep(5)

    def check_third_speciality(self):

        list_item3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@class="v-list__tile__title"][contains(text(), "Anesthesia")]')))

        list_item3.click()
        time.sleep(2)

        # Locate the parent div element for the checkbox
        parent_div = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@class="v-input--selection-controls__input"]')
            )
        )

        # Find the nested input element within the parent div
        checkbox_input = parent_div.find_element(By.XPATH, './input')

        # Get the aria-checked attribute of the checkbox

        aria_checked = checkbox_input.get_attribute("aria-checked")

        # Assert that aria-checked is "false"
        if aria_checked == "false":
            print("user can not select 3rd speciality")
        else:
            print("user can able to select the 3rd speciality")

    def test_age_val(self):
        calendar_element = self.get_calender()
        calendar_element.click()

        # Add additional waiting logic here to ensure the calendar is fully loaded

        # Get all date elements in the calendar
        date_elements = self.get_date_elements()

        # Select a random date from the available date elements
        random_date_element = random.choice(date_elements)
        random_date_element.click()
        time.sleep(10)

        random_date_text = random_date_element.get_attribute("aria-label")

        # Now that you have selected the date, calculate the age
        selected_date_text = random_date_text
        print("selected date is", selected_date_text)
        time.sleep(10)
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
