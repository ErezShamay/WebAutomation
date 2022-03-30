import time
import pytest
import allure

from reali_web.pages.loans_page import LoansPage
from reali_web.pages.blend_page import BlendPage
from reali_api.helpers.users import UsersHelper as ApiUsersHelper
from reali_api.services.loans_api import LoansApi
from reali_api.services.salesforce import SF
from reali_api.api_payloads.loans_quotes import refinance_quote_payload


@allure.feature('Loans')
@allure.description(""" Tests to check end-to-end loans->blend->sf flow""")
class TestLoansEndToEnd:

    @pytest.fixture(scope="class")
    def loans_refinance_user_with_requested_quotes(self):
        with allure.step("Prepare loans refinance user with requested quotes"):
            user = ApiUsersHelper("loans").create_loans_user_via_email().verify_user()
            loans_user_data = user.user_data_as_variables()
            LoansApi(token=loans_user_data.token).get_refinance_quote(payload=refinance_quote_payload)
            return loans_user_data

    @allure.title("Refinance flow from loans to blend submission should succeed")
    @pytest.mark.usefixtures('loans_refinance_user_with_requested_quotes')
    def test_loans_to_blend_refinance_flow(self, browser, loans_refinance_user_with_requested_quotes):
        loans_page = LoansPage(browser)
        loans_page.open_main_page()
        loans_page.login_with_email(loans_refinance_user_with_requested_quotes.email, "Qaz123wsx#")
        loans_page.apply_for_rate(0)

        blend = BlendPage(browser)
        blend.check_blend_opened()
        blend.choose_refinance_journey()
        blend.fill_getting_started_page()
        blend.fill_getting_you_know_section_refinance()
        blend.fill_assets()
        blend.fill_income()
        blend.fill_real_estate()
        blend.fill_declaration_refinance()
        blend.enter_demographic_info()
        blend.pass_additional_questions()
        blend.review_and_submit_your_application()

    @allure.title("Salesforce lead creation should succeed")
    @pytest.mark.usefixtures('loans_refinance_user_with_requested_quotes')
    def test_loans_sf_lead_created(self, loans_refinance_user_with_requested_quotes):
        user_name = loans_refinance_user_with_requested_quotes.firstName
        user_email = loans_refinance_user_with_requested_quotes.email

        sf = SF()

        with allure.step(f"Check that user with the name {user_name} existing in SF leads"):
            for attempt in range(10):
                time.sleep(3)
                leads_search_results = sf.find_sf_leads_via_search_query(user_name)
                if leads_search_results:
                    break

            assert len(leads_search_results) == 1

        with allure.step(f"Check that lead details in sf having the next email: {user_email}"):
            lead_url = leads_search_results[0]["attributes"]["url"]
            lead_details = sf.get_lead_details(lead_url)
            assert lead_details['Email'] == user_email

    @pytest.mark.dependency(depends=["test_loans_to_blend_refinance_flow"])
    @allure.title("Salesforce loan creation should succeed")
    @pytest.mark.usefixtures('loans_refinance_user_with_requested_quotes')
    def test_sf_loan_created(self, loans_refinance_user_with_requested_quotes):
        user_name = loans_refinance_user_with_requested_quotes.firstName
        user_email = loans_refinance_user_with_requested_quotes.email

        sf = SF()

        with allure.step(f"Check that user with the name {user_name} having a loan"):
            for attempt in range(10):
                time.sleep(30)  # we need some time for encompass to process requests
                loans_search_results = sf.find_sf_loans_via_search_query(user_name)
                if loans_search_results:
                    break

            assert len(loans_search_results) == 1
            loan_url = loans_search_results[0]["attributes"]["url"]
            loan_details = sf.get_loan_details(loan_url)

        with allure.step(f"Check that loans details in sf having the next email: {user_email}"):
            assert loan_details['Email__c'] == user_email

        with allure.step(f"Check that loans details in sf having correct property value:"
                         f" {BlendPage.default_property_price}"):
            assert int(float(loan_details["Property_Value__c"])) == BlendPage.default_property_price

        with allure.step(f"Check that loans details in sf having encompass id attached"):
            assert loan_details["Unique_LOS_Identifier__c"]

        with allure.step(f"Check that loans details in sf having blend id attached"):
            assert loan_details["Loan_Id__c"]
