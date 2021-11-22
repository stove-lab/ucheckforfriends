import os
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from ucheck import UCheck

if __name__ == "__main__":
    # E.g., Save UTORid login and password as environment variables.
    utorid_login = os.environ.get('UTORID_USER')
    utorid_pass = os.environ.get('UTORID_PASS')
    with UCheck(Chrome, Service,
                driver_path="/opt/WebDriver/bin/chromedriver") as ucheck:
        ucheck.complete_ucheck(utorid_login, utorid_pass)
        # Briefly keep browser window open before closing.
        time.sleep(5)
