import time
from typing import Dict
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import datetime

time_start = time.time()
logging.getLogger().setLevel(logging.INFO)

url = 'https://www.e-disclosure.ru/portal/files.aspx?id=636&type=3'
name_company = ''


class SupLogging:
    @staticmethod
    def log_info(text: str):
        logging.info(f"{datetime.datetime.now()} {text}")

    @staticmethod
    def log_warn(text: str):
        logging.warning(f"{datetime.datetime.now()} {text}")


def options(sm=True):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument("--incognito")
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        f'user-agent={"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}')
    options.headless = sm
    return options


def check_docs(url: str) -> Dict:
    global name_company
    info_data_TRNF = {}
    service = Service(r'C:\Selenium\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options(sm=True))
    driver.get(url)
    time.sleep(1)
    search_tr = driver.find_elements(By.XPATH, "//tbody/tr")[1:]
    name_company = driver.find_element(By.XPATH, "//div/h2").text
    logged = False
    for el in search_tr:
        if not el.text.find('2024') >= 0 and logged == False:
            logged = True
            if el.text[0] == '1':
                name_doc1 = el.find_element(By.XPATH, "//td[2]").text
                name_doc2 = el.find_element(By.XPATH, "//td[3]").text
                fullname_doc = name_doc1 + ' - ' + name_doc2
                href_doc_link = el.find_element(By.XPATH, "//td[6]/a")
                doc_link = href_doc_link.get_attribute('href')
                SupLogging.log_info(
                    f"Документов за 2024 год нет, всего документов: {len(search_tr)}. Последний файл: {fullname_doc} - Обновление {name_company} не требуется.")
                info_data_TRNF = {
                    'company': name_company,
                    'name': fullname_doc,
                    'url': doc_link,
                }
            continue
        elif el.text.find('2024') >= 0 and logged == False:
            i = 10
            while i > 0:
                SupLogging.log_warn(f"Требуется обновление {name_company} ({i})")
                time.sleep(2)
                i -= 1

    # print(info_data_TRNF)


def main():
    check_docs(url)
    time_finish = time.time() - time_start
    SupLogging.log_info(f'Работа выполнена за {round(time_finish, 3)} секунд. По {name_company}')
    SupLogging.log_info(f'---------------------------------------------------------------------')


if __name__ == "__main__":
    main()
