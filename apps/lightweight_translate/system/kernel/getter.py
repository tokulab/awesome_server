import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from ..handler import error_handler as e_handler

class Crawler:

    def __init__(self, chdriver_path):
        import chromedriver_binary
        try:
            self.driver = webdriver.Chrome(executable_path=chdriver_path)
            self.driver.implicitly_wait(3)
        except Exception as e:
            self._occur_err(e)


    def get_text(self, text):
        try:
            self.driver.get('https://miraitranslate.com/trial/')
            self.driver.find_element_by_id("select2-sourceButtonUrlTranslation-container").click()
            self.driver.find_element_by_xpath('//li[position()=1]').click()
            time.sleep(0.2)
            self.driver.find_element_by_id("select2-targetButtonTextTranslation-container").click()
            time.sleep(0.2)
            self.driver.find_element_by_xpath('//li[position()=1]').click()
            time.sleep(0.2)
            box = self.driver.find_element_by_id("translateSourceInput")
            box.send_keys(text)
            time.sleep(0.2)
            self.driver.find_element_by_id("translateButtonTextTranslation").click()
            time.sleep(self._infer_infertime(text))
            try:
                translated = WebDriverWait(self.driver, self._infer_infertime(text)).until(
                    expected_conditions.presence_of_element_located((By.ID, 'translate-text'))
                )
                result = translated.get_attribute("textContent")
            finally:
                self.driver.quit()
                return result



        except Exception as e:
            self._occur_err(e)

    def _infer_infertime(self, text):
        cnt = len(text)
        infertime = int(cnt / 100) + 1
        return infertime

    def _occur_err(self, err_obj):
        message = e_handler.ERROR_OCCURRED_TEMPLATE.format(err=str(err_obj).rstrip('\n'))
        print(message)
        e_handler.force_abort()
