import time
import pytest
import allure

from reali_api.configs.config import env
from reali_api.api_payloads.lead_source_generate_link import *
from reali_api.helpers.users import UsersHelper as ApiUsersHelper
from reali_api.services.loans_api import LoansApi
from reali_api.services.webhooks import WebHookApi
from reali_api.api_payloads.loans_quotes import refinance_quote_payload
from reali_api.configs.env_setup import admin_token
from reali_web.pages.loans_page import LoansPage
from reali_mobile.core.gmail import GmailAPI
from reali_web.pages.blend_page import BlendPage
from reali_api.services.salesforce import SF


@pytest.mark.flaky(reruns=1, reruns_delay=2)
@allure.feature('Loans')
@allure.description(""" Tests to check webhooks and end-to-end flows according to provider""")
class TestLoansWebHookEndToEnd:
    DEFAULT_NAME = f"sergiip+{env.lower()}"
    DEFAULT_PWD = "Qaz123wsx#"

    @allure.title("Test zillow refinance flow should succeed")
    def test_zillow_refinance_flow(self, browser_def):
        user_email = f"{self.DEFAULT_NAME}{int(time.time())}@reali.com"

        with allure.step("Webhook: Generate a link for zillow provider"):
            payload = zillow_refinance_payload
            payload["sender"]["emailAddress"] = user_email
            response = WebHookApi(token=admin_token).generate_zillow_link(payload=payload)
            generated_link = response.json()["applicationURL"]

        with allure.step(f"Open provided url: {generated_link}"):
            loans_page = LoansPage(browser_def)
            loans_page.open_lead_source_link(link_to_open=generated_link)

        with allure.step("Verify zillow logo shown on loans page"):
            loans_page.verify_logo("zillow")

        with allure.step("Apply for rate"):
            loans_page.apply_for_rate(0)

        with allure.step(f"Signup user from lead source: {user_email}"):
            loans_page.signup_lead_source(password=self.DEFAULT_PWD)
            loans_page.enter_confirmation_code(GmailAPI.get_confirmation_code_simplified(receiver_email=user_email))

        with allure.step("Process blend form"):
            blend = BlendPage(browser_def)
            blend.process_full_refinance_flow()

        with allure.step("Verify MY LOANS btn existing after re sign in"):
            self.check_my_loans_after_re_sign_in(browser_def, user_email, self.DEFAULT_PWD)

        with allure.step("Verify SF loan containing required details"):
            loans = self.get_user_loan_urls(user_email)
            self.verify_loan_details_by_lead_source(user_email=user_email,
                                                    loan_url=loans[0],
                                                    blend=blend,
                                                    loan_source_detail='Zillow Rate Table')

    @allure.title("Test zillow purchase flow should succeed")
    def test_zillow_purchase_flow(self, browser_def):
        user_email = f"{self.DEFAULT_NAME}{int(time.time())}@reali.com"

        with allure.step("Generate a link"):
            payload = zillow_purchase_payload
            payload["sender"]["emailAddress"] = user_email
            response = WebHookApi(token=admin_token).generate_zillow_link(payload=payload)
            generated_link = response.json()["applicationURL"]

        with allure.step(f"Open provided url: {generated_link}"):
            loans_page = LoansPage(browser_def)
            loans_page.open_lead_source_link(link_to_open=generated_link)

        with allure.step("Verify zillow logo shown on loans page"):
            loans_page.verify_logo("zillow")

        with allure.step("Apply for the first rate"):
            loans_page.apply_for_rate(0)

        with allure.step(f"Signup a user from lead source(zillow) {user_email}"):
            loans_page.signup_lead_source(password=self.DEFAULT_PWD)
            loans_page.enter_confirmation_code(GmailAPI.get_confirmation_code_simplified(receiver_email=user_email))

        with allure.step("Process blend form"):
            blend = BlendPage(browser_def)
            blend.process_full_purchase_flow()

        with allure.step("Verify MY LOANS btn existing after re sign in"):
            self.check_my_loans_after_re_sign_in(browser_def, user_email, self.DEFAULT_PWD)

        with allure.step("Verify SF loan containing required details"):
            loans = self.get_user_loan_urls(user_email)
            self.verify_loan_details_by_lead_source(user_email=user_email,
                                                    loan_url=loans[0],
                                                    blend=blend,
                                                    loan_source_detail='Zillow Rate Table')

    @allure.title("Test tqm refinance flow should succeed")
    def test_tqm_refinance_flow(self, browser_def):
        user_email = f"{self.DEFAULT_NAME}{int(time.time())}@reali.com"

        with allure.step("Generate a link"):
            payload = tqm_refinance_payload
            payload["email"] = user_email
            response = WebHookApi(token=admin_token).generate_tqm_link(payload=payload)
            generated_link = response.json()["applicationURL"]

        with allure.step(f"Open provided url: {generated_link}"):
            loans_page = LoansPage(browser_def)
            loans_page.open_lead_source_link(link_to_open=generated_link)

        with allure.step("Verify tqm logo shown on loans page"):
            loans_page.verify_logo("tqm")

        with allure.step("Apply for rate"):
            loans_page.apply_for_rate(0)
        with allure.step(f"Signup user from lead source {user_email}"):
            loans_page.signup_lead_source(password=self.DEFAULT_PWD)
            loans_page.enter_confirmation_code(GmailAPI.get_confirmation_code_simplified(receiver_email=user_email))

        with allure.step("Process blend form"):
            blend = BlendPage(browser_def)
            blend.process_full_refinance_flow()

        with allure.step("Verify MY LOANS btn existing after re sign in"):
            self.check_my_loans_after_re_sign_in(browser_def, user_email, self.DEFAULT_PWD)

        with allure.step("Verify SF loan containing required details"):
            loans = self.get_user_loan_urls(user_email)
            self.verify_loan_details_by_lead_source(user_email=user_email,
                                                    loan_url=loans[0],
                                                    blend=blend,
                                                    loan_source_detail='True Quote Mortgage')

    @allure.title("Test tqm purchase flow should succeed")
    def test_tqm_purchase_flow(self, browser_def):
        user_email = f"{self.DEFAULT_NAME}{int(time.time())}@reali.com"

        with allure.step("Generate a link"):
            payload = tqm_purchase_payload
            payload["email"] = user_email
            response = WebHookApi(token=admin_token).generate_tqm_link(payload=payload)
            generated_link = response.json()["applicationURL"]

        with allure.step(f"Open provided url: {generated_link}"):
            loans_page = LoansPage(browser_def)
            loans_page.open_lead_source_link(link_to_open=generated_link)

        with allure.step("Verify tqm logo shown on loans page"):
            loans_page.verify_logo("tqm")

        with allure.step("Apply for rate"):
            loans_page.apply_for_rate(0)
        with allure.step(f"Signup user from lead source {user_email}"):
            loans_page.signup_lead_source(password=self.DEFAULT_PWD)
            loans_page.enter_confirmation_code(GmailAPI.get_confirmation_code_simplified(receiver_email=user_email))

        with allure.step("Process blend form"):
            blend = BlendPage(browser_def)
            blend.process_full_purchase_flow()

        with allure.step("Verify MY LOANS btn existing after re sign in"):
            self.check_my_loans_after_re_sign_in(browser_def, user_email, self.DEFAULT_PWD)

        with allure.step("Verify SF loan containing required details"):
            loans = self.get_user_loan_urls(user_email)
            self.verify_loan_details_by_lead_source(user_email=user_email,
                                                    loan_url=loans[0],
                                                    blend=blend,
                                                    loan_source_detail='True Quote Mortgage')

    @allure.title("Test aim refinance flow should succeed")
    def test_aim_refinance_flow(self, browser_def):
        user_email = f"{self.DEFAULT_NAME}{int(time.time())}@reali.com"

        with allure.step("Generate a link"):
            payload = aim_refinanse_payload
            payload["email"] = user_email
            response = WebHookApi(token=admin_token).generate_aim_link(payload=payload)
            generated_link = response.json()["applicationURL"]

        with allure.step(f"Open provided url: {generated_link}"):
            loans_page = LoansPage(browser_def)
            loans_page.open_lead_source_link(link_to_open=generated_link)

        with allure.step("Verify aim logo shown on loans page"):
            loans_page.verify_logo("aim")

        with allure.step("Apply for rate"):
            loans_page.apply_for_rate(0)

        with allure.step(f"Signup user from lead source {user_email}"):
            loans_page.signup_lead_source(password=self.DEFAULT_PWD)
            loans_page.enter_confirmation_code(GmailAPI.get_confirmation_code_simplified(receiver_email=user_email))

        with allure.step("Process blend form"):
            blend = BlendPage(browser_def)
            blend.process_full_refinance_flow()

        with allure.step("Verify MY LOANS btn existing after re sign in"):
            self.check_my_loans_after_re_sign_in(browser_def, user_email, self.DEFAULT_PWD)

        with allure.step("Verify SF loan containing required details"):
            loans = self.get_user_loan_urls(user_email)
            self.verify_loan_details_by_lead_source(user_email=user_email,
                                                    loan_url=loans[0],
                                                    blend=blend,
                                                    loan_source_detail='AI Marketing')

    @allure.title("Test aim purchase flow should succeed")
    def test_aim_purchase_flow(self, browser_def):
        user_email = f"{self.DEFAULT_NAME}{int(time.time())}@reali.com"

        with allure.step("Generate a link"):
            payload = aim_purchase_payload
            payload["email"] = user_email
            response = WebHookApi(token=admin_token).generate_aim_link(payload=payload)
            generated_link = response.json()["applicationURL"]

        with allure.step(f"Open provided url: {generated_link}"):
            loans_page = LoansPage(browser_def)
            loans_page.open_lead_source_link(link_to_open=generated_link)

        with allure.step("Verify aim logo shown on loans page"):
            loans_page.verify_logo("aim")

        with allure.step("Apply for rate"):
            loans_page.apply_for_rate(0)

        with allure.step(f"Signup user from lead source {user_email}"):
            loans_page.signup_lead_source(password=self.DEFAULT_PWD)
            loans_page.enter_confirmation_code(GmailAPI.get_confirmation_code_simplified(receiver_email=user_email))

        with allure.step("Process blend form"):
            blend = BlendPage(browser_def)
            blend.process_full_purchase_flow()

        with allure.step("Verify MY LOANS btn existing after re sign in"):
            self.check_my_loans_after_re_sign_in(browser_def, user_email, self.DEFAULT_PWD)

        with allure.step("Verify SF loan containing required details"):
            loans = self.get_user_loan_urls(user_email)
            self.verify_loan_details_by_lead_source(user_email=user_email,
                                                    loan_url=loans[0],
                                                    blend=blend,
                                                    loan_source_detail='AI Marketing')

    @allure.title("Test consistency of loan provider should succeed")
    def test_loan_provider_tracking_consistency(self, browser_def):
        user_email = f"{self.DEFAULT_NAME}{int(time.time())}@reali.com"

        with allure.step("Webhook: Generate a link for zillow provider"):
            payload = zillow_refinance_payload
            payload["sender"]["emailAddress"] = user_email
            response = WebHookApi(token=admin_token).generate_zillow_link(payload=payload)
            generated_link = response.json()["applicationURL"]

        with allure.step(f"Open provided url: {generated_link}"):
            loans_page = LoansPage(browser_def)
            loans_page.open_lead_source_link(link_to_open=generated_link)

        with allure.step("Verify zillow logo shown on loans page"):
            loans_page.verify_logo("zillow")

        with allure.step("Apply for rate"):
            loans_page.apply_for_rate(0)

        with allure.step("Signup user from lead source"):
            loans_page.signup_lead_source(password=self.DEFAULT_PWD)
            loans_page.enter_confirmation_code(GmailAPI.get_confirmation_code_simplified(receiver_email=user_email))

        with allure.step("Process blend form"):
            blend = BlendPage(browser_def)
            blend.process_full_refinance_flow()

        with allure.step("Verify SF loan containing required details"):
            loans = self.get_user_loan_urls(user_email)
            self.verify_loan_details_by_lead_source(user_email=user_email,
                                                    loan_url=loans[0],
                                                    blend=blend,
                                                    loan_source_detail='Zillow Rate Table')
        with allure.step("Generate a link"):
            payload = aim_refinanse_payload
            payload["email"] = user_email
            response = WebHookApi(token=admin_token).generate_aim_link(payload=payload)
            generated_link_2 = response.json()["applicationURL"]

        with allure.step(f"Open provided url: {generated_link_2}"):
            loans_page = LoansPage(browser_def)
            loans_page.open_lead_source_link(link_to_open=generated_link_2)

        with allure.step("Apply for rate"):
            loans_page.apply_for_rate(1)

        with allure.step("Process blend form"):
            blend = BlendPage(browser_def)
            blend.start_new_application()
            blend.choose_refinance_journey_for_2nd_appication()
            blend.fill_getting_started_page()
            blend.fill_getting_you_know_section_refinance()
            blend.fill_assets()
            blend.fill_income()
            blend.fill_real_estate()
            blend.fill_declaration_refinance()
            blend.enter_demographic_info()
            blend.pass_additional_questions()
            blend.review_and_submit_your_application()

        with allure.step("Verify SF parameters for all loans created in SF"):
            time.sleep(10)  # additional wait to give some time for encompass
            loans = self.get_user_loan_urls(user_email)
            for loan in loans:
                self.verify_loan_details_by_lead_source(user_email=user_email,
                                                        loan_url=loan,
                                                        blend=blend,
                                                        loan_source_detail='Zillow Rate Table')

    @allure.title("Test source consistency regular flow + zillow flow")
    def test_regular_flow_then_lead_source(self, browser_def):
        with allure.step("Create regular user via API"):
            user = ApiUsersHelper("loans").create_loans_user_via_email().verify_user()
            loans_user_data = user.user_data_as_variables()
            LoansApi(token=loans_user_data.token).get_refinance_quote(payload=refinance_quote_payload)

        with allure.step(f"Sign in to created user: {loans_user_data.email}"):
            loans_page = LoansPage(browser_def)
            loans_page.open_main_page()
            loans_page.login_with_email(loans_user_data.email, "Qaz123wsx#")

        with allure.step("Apply for rate #1"):
            loans_page.apply_for_rate(0)
        with allure.step("Process blend form"):
            blend = BlendPage(browser_def)
            blend.process_full_refinance_flow()

        with allure.step("Generate a link"):
            payload = aim_refinanse_payload
            payload["email"] = loans_user_data.email
            response = WebHookApi(token=admin_token).generate_aim_link(payload=payload)
            generated_link_2 = response.json()["applicationURL"]

        with allure.step(f"Open provided url: {generated_link_2}"):
            loans_page = LoansPage(browser_def)
            loans_page.open_lead_source_link(link_to_open=generated_link_2)

        with allure.step("Apply for rate"):
            loans_page.apply_for_rate(1)

        with allure.step("Process blend form"):
            blend = BlendPage(browser_def)
            blend.start_new_application()
            blend.choose_refinance_journey_for_2nd_appication()
            blend.fill_getting_started_page()
            blend.fill_getting_you_know_section_refinance()
            blend.fill_assets()
            blend.fill_income()
            blend.fill_real_estate()
            blend.fill_declaration_refinance()
            blend.enter_demographic_info()
            blend.pass_additional_questions()
            blend.review_and_submit_your_application()

        with allure.step("Verify SF parameters for all loans created in SF"):
            time.sleep(10)  # additional wait to give some time for encompass
            loans = self.get_user_loan_urls(loans_user_data.email)
            for loan in loans:
                self.verify_loan_details_by_lead_source(user_email=loans_user_data.email,
                                                        loan_url=loan,
                                                        blend=blend,
                                                        loan_source_detail=None,
                                                        skip_loan_amount=True,
                                                        skip_prop_price=True)

    @allure.title("Test source consistency zillow flow + regular flow ")
    def test_lead_source_then_normal_flow(self, browser_def):
        user_email = f"{self.DEFAULT_NAME}{int(time.time())}@reali.com"

        with allure.step("Webhook: Generate a link for zillow provider"):
            payload = zillow_refinance_payload
            payload["sender"]["emailAddress"] = user_email
            response = WebHookApi(token=admin_token).generate_zillow_link(payload=payload)
            generated_link = response.json()["applicationURL"]

        with allure.step(f"Open provided url: {generated_link}"):
            loans_page = LoansPage(browser_def)
            loans_page.open_lead_source_link(link_to_open=generated_link)

        with allure.step("Verify zillow logo shown on loans page"):
            loans_page.verify_logo("zillow")

        with allure.step("Apply for rate"):
            loans_page.apply_for_rate(0)

        with allure.step("Signup user from lead source"):
            loans_page.signup_lead_source(password=self.DEFAULT_PWD)
            loans_page.enter_confirmation_code(GmailAPI.get_confirmation_code_simplified(receiver_email=user_email))

        with allure.step("Process blend form"):
            blend = BlendPage(browser_def)
            blend.process_full_refinance_flow()

        with allure.step(f"Open  loans app again"):
            loans_page = LoansPage(browser_def)
            loans_page.open_main_page()

        with allure.step("Apply for rate #2"):
            loans_page.apply_for_rate(1)

        with allure.step("Process blend form"):
            blend = BlendPage(browser_def)
            blend.start_new_application()
            blend.choose_refinance_journey_for_2nd_appication()
            blend.fill_getting_started_page()
            blend.fill_getting_you_know_section_refinance()
            blend.fill_assets()
            blend.fill_income()
            blend.fill_real_estate()
            blend.fill_declaration_refinance()
            blend.enter_demographic_info()
            blend.pass_additional_questions()
            blend.review_and_submit_your_application()

        with allure.step("Verify SF parameters for all loans created in SF"):
            time.sleep(10)  # additional wait to give some time for encompass
            loans = self.get_user_loan_urls(user_email)
            for loan in loans:
                self.verify_loan_details_by_lead_source(user_email=user_email,
                                                        loan_url=loan,
                                                        blend=blend,
                                                        loan_source_detail='Zillow Rate Table')

    @staticmethod
    def get_user_loan_urls(user_email):
        time.sleep(30)  # sleep to allow backend fully process all changes in SF
        with allure.step(f"Check that user with the name {user_email} existing in SF leads"):
            sf = SF()
            for attempt in range(10):
                time.sleep(3)
                loans_search_results = sf.find_sf_loans_via_search_query(user_email)
                if loans_search_results:
                    break
            loans = []
            for result in loans_search_results:
                loans.append(result["attributes"]["url"])

            return loans

    """
    Function helper for this test to validate Loan details in SF
    """
    @staticmethod
    def verify_loan_details_by_lead_source(user_email,
                                           loan_url,
                                           blend,
                                           loan_source_detail,
                                           skip_loan_amount=False,
                                           skip_prop_price=False):
        sf = SF()
        loan_details = sf.get_loan_details(loan_url)
        with allure.step(f"Check that loan details in sf having the next email: {user_email}"):
            assert loan_details['Email__c'] == user_email

        with allure.step(f"Check that loans details in sf having encompass id attached"):
            assert loan_details["Unique_LOS_Identifier__c"]

        with allure.step(f"Check that loans details in sf having blend id attached"):
            assert loan_details["Loan_Id__c"]

        if loan_source_detail:
            with allure.step(f"Check that loan details in sf having 'Loan_Source_Detail__c': '{loan_source_detail}'"):
                assert loan_details['Loan_Source_Detail__c'] == loan_source_detail
        elif not loan_source_detail:
            assert not loan_details['Loan_Source_Detail__c']

        if not skip_prop_price:
            with allure.step(f"Check that loan details in sf having property price entered in Blend"):
                assert int(float(loan_details['Property_Value__c'])) == int(blend.loans_config["property_price"])

        if not skip_loan_amount:
            with allure.step(f"Check that loan details in sf having loan amount entered in Blend"):
                assert int(float(loan_details['Loan_Amount__c'])) == int(blend.loans_config["loan_amount"])

    @staticmethod
    def check_my_loans_after_re_sign_in(browser_def, user_email, user_pwd):
        loans_page = LoansPage(browser_def)
        loans_page.open_main_page()
        loans_page.clear_local_storage()
        loans_page.delete_all_cookies()
        loans_page.open_main_page()
        loans_page.login_with_email(user_email, user_pwd)
        loans_page.verify_my_loans_btn()
