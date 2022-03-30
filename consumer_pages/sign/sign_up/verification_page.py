import logging
import time
from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from reali_web.wait import wait_options
import imaplib 
import email
from reali_web.consumer_pages.sign.sign_up import verification_page_locators

w = wait_options.wait_functions
vpl = verification_page_locators.VerificationPageLocators

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "erez.reali" + ORG_EMAIL
FROM_PWD = "Es@170186"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993


class VerificationPage:
    @staticmethod
    def validate_in_verification_page(driver: webdriver):
        try:
            w.wait_for_element(driver, vpl.VERIFICATION_CODE)
            driver.find_element(*vpl.VERIFICATION_CODE)
            logging.info('in verification_page')
            print('in verification_page')
            return True
        except NoSuchElementException as err:
            logging.error('not in verification_page')
            print('not in verification_page')
            raise err

    @staticmethod
    def get_verification_code():
        time.sleep(20)
        verification_code = ''
        valid = 'Your confirmation code is'
        flag = False
        try:
            mail = imaplib.IMAP4_SSL(SMTP_SERVER)
            mail.login(FROM_EMAIL, FROM_PWD)
            mail.select('inbox')

            data = mail.search(None, 'ALL')
            mail_ids = data[1]
            id_list = mail_ids[0].split()
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])

            for i in range(latest_email_id, first_email_id, -1):
                data = mail.fetch(str(i), '(RFC822)')
                for response_part in data:
                    arr = response_part[0]
                    if isinstance(arr, tuple):
                        msg = email.message_from_string(str(arr[1], 'utf-8'))
                        email_subject = msg['subject']
                        if valid in email_subject:
                            verification_code = VerificationPage.cut_confirmation_code(email_subject)
                            flag = True
                            break
                if flag:
                    break
            logging.info('got verification code')
            print('got verification code')
        except():
            logging.info('did not get the verification code')
            print('did not get the verification code')
        return verification_code

    @staticmethod
    def enter_verification_code(driver: webdriver):
        counter = 0
        try:
            verification_code = VerificationPage.get_verification_code()
            list_verification_code = VerificationPage.split_str_to_list(verification_code)
            element = driver.find_element(*vpl.FIRST_DIGIT)
            VerificationPage.send_keys_to_element(driver, element, list_verification_code[0])
            element = driver.find_element(*vpl.SECOND_DIGIT)
            VerificationPage.send_keys_to_element(driver, element, list_verification_code[1])
            element = driver.find_element(*vpl.THIRD_DIGIT)
            VerificationPage.send_keys_to_element(driver, element, list_verification_code[2])
            element = driver.find_element(*vpl.FOURTH_DIGIT)
            VerificationPage.send_keys_to_element(driver, element, list_verification_code[3])
            element = driver.find_element(*vpl.FIFTH_DIGIT)
            VerificationPage.send_keys_to_element(driver, element, list_verification_code[4])
            element = driver.find_element(*vpl.SIXTH_DIGIT)
            VerificationPage.send_keys_to_element(driver, element, list_verification_code[5])
            if counter == 3:
                if VerificationPage.validate_incorrect_code_toaster_error_message_is_shown(driver):
                    VerificationPage.enter_verification_code(driver)
                    counter += 1
                    VerificationPage.validate_incorrect_code_toaster_error_message_is_shown(driver)
            logging.info('verification code was entered correctly')
            w.wait_for_element(driver, vpl.WAIT)
            return True
        except (NoSuchElementException, WebDriverException) as err:
            logging.error('error in entering verification code')
            print('error in entering verification code')
            raise err

    @staticmethod
    def send_keys_to_element(driver: webdriver, element, value: str):
        try:
            action = ActionChains(driver)
            action.click(on_element=element)
            action.send_keys(value)
            action.perform()
            logging.info('send keys to element')
            print('send keys to element')
        except(NoSuchElementException, ElementClickInterceptedException) as err:
            logging.error('issue in send keys')
            print('issue in send keys')
            raise err

    @staticmethod
    def split_str_to_list(verification_code):
        list_verification_code = list(verification_code)
        return list_verification_code

    @staticmethod
    def cut_confirmation_code(email_subject: str):
        for word in email_subject.split():
            if word.isdigit():
                return word

    @staticmethod
    def validate_incorrect_code_toaster_error_message_is_shown(driver: webdriver):
        try:
            time.sleep(2)
            driver.find_element(*vpl.TOASTER_ERROR_MESSAGE)
            logging.error('found toaster error message')
            print('found toaster error message')
            return True
        except NoSuchElementException:
            logging.info('did not find toaster error message')
            print('did not find toaster error message')
            return False
