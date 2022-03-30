import logging
import pytest
import allure
import sys
import os
from selenium import webdriver
from datetime import datetime
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager




def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default="0", help="Headless mode for chrome")
    parser.addoption("--env", action="store", default="dev", help="dev, qa, staging, prod")
    parser.addoption("--email", action="store", default="erez@reali.com", help="user for echo login")
    parser.addoption("--pswd", action="store", default="Es@12345", help="password for echo login")


@pytest.fixture(scope="class")
def browser(request):
    chrome_options = Options()
    headless = request.config.getoption("--headless")
    if headless == "1":
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--window-size=1280,1024')
    driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
    yield driver
    if driver:
        driver.quit()

"""This fixture is duplicating browser() with one difference. It is not having scope equal to class.
 Default scope is function."""
@pytest.fixture()
def browser_def(request):
    chrome_options = Options()
    headless = request.config.getoption("--headless")
    if headless == "1":
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--window-size=1280,1024')
    driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
    yield driver
    if driver:
        driver.quit()


# hook which will try to attach screenshot to allure report on test failure
def pytest_exception_interact(node, call, report):
    try:
        try:
            browser = node.funcargs.get("browser")
        except:
            browser = node.funcargs.get("browser_def")
        name = f'{datetime.now().strftime("%H%M%S")}.png'
        allure.attach(browser.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
    except Exception as ex:
        logging.critical(ex)


@pytest.fixture(scope="class")
def echo_user_email(request):
    email = request.config.getoption("--email")
    return email


@pytest.fixture(scope="class")
def echo_password(request):
    password = request.config.getoption("--pswd")
    return password


@pytest.fixture(scope="class")
def environment(request):
    env = request.config.getoption("--env")
    return env


class Product:

    @staticmethod
    def consumer(env: str):
        if env == 'prod':
            entry_point = 'https://app.reali.com/buy/homes'
        else:
            entry_point = f'https://webapp.{env}-reali.com/buy/homes'
        return entry_point

    @staticmethod
    def echo(env: str):
        if env == 'prod':
            entry_point = 'https://echo.reali.com/main/chats'
            token = 'e85cb085-f1af-4636-81d7-aec384b4855b'
        elif env == 'staging':
            entry_point = f'https://echo.{env}-reali.com/main/chats'
            token = '262e91b7-9ce6-4b59-93dd-a9e073e9527f'
        else:
            entry_point = f'https://{env}.echo.{env}-reali.com/main/chats'
            token = 'e29a9bed-80e0-4408-a484-65eb721b5782'
        return entry_point, token

    @staticmethod
    def loans(env: str):
        if env == 'prod':
            entry_point = 'https://loans.reali.com/'
        else:
            entry_point = f'https://loans.{env}-reali.com/'
        return entry_point


def take_screenshot(driver, method_name):
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    name = f'{method_name}-{current_time}.png'
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)


def check_browser_console(driver, title):
    browser_logs = driver.get_log('browser')
    if browser_logs:
        logging.warning('\n')
        logging.critical(f'----- {title} CONSOLE LOGS START -----')
        for logs in browser_logs:
            logging.warning(logs.get('message', logging))
        logging.critical(f'----- {title} CONSOLE LOGS END -----')
    logging.warning('\n')


@pytest.fixture(scope="session", autouse=True)
def generate_env_properties_for_allure(pytestconfig):
    markers_arg = pytestconfig.getoption('-m')

    # Lets find passed via command line allure dir folder
    for argument in sys.argv:
        if "--alluredir=" in argument:
            allure_folder = argument.replace("--alluredir=", '')

            # Lets try to remove old environment.txt / properties
            if os.path.exists(f"{allure_folder}/environment.txt"):
                os.remove(f"{allure_folder}/environment.txt")
            if os.path.exists(f"{allure_folder}/environment.properties"):
                os.remove(f"{allure_folder}/environment.properties")

            # Lets create a new allure properties file
            f = open(f"{allure_folder}/environment.txt", "w+")
            f.write(f"UsedMarkers={str(markers_arg)}\r\n")

            cmd_env = None
            for argument in sys.argv:
                if "--env=" in argument:
                    cmd_env = argument.replace("--env=", '')
                    break

            f.write(f"Env={str(cmd_env)}\r\n")

            f.close()
            os.rename(f"{allure_folder}/environment.txt", f"{allure_folder}/environment.properties")
            break


