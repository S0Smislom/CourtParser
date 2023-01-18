from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import (
    BASE_URL,
    BASE_FILTER,
    TARGET_CLASS_NAME,
    driver_options,
    driver_path
)


class SeleniumPageProcessor:
    """Класс взаимодействия драйвером"""

    def __init__(self, driver):
        self.driver = driver

    def get_page(self, url=BASE_URL):
        """Получает страницу"""
        self.driver.get(url)
        
    def wait_for_element(self, delay:int = 5, by:str = By.CLASS_NAME, class_name: str = TARGET_CLASS_NAME):
        """Ждет загрузки элемента на странице"""
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by,  class_name)))

    def get_source(self):
        """Возвращает источник"""
        return self.driver


class SeleniumDataProcessor:
    """Класс для получения данных со страницы"""

    def __init__(self, source):
        self.source = source

    def get_pages(self, id_='paginationFormMaxPages'):
        """Возвращает количество страниц"""
        page = self.source.find_element(By.ID, id_)
        return int(page.get_attribute('value'))
        
    def get_table(self, class_name=TARGET_CLASS_NAME):
        """Возвращает таблицу"""
        return self.source.find_element(By.CLASS_NAME, class_name)

    def get_table_data(self, table, category_filter=BASE_FILTER):
        """Возвращает данные из таблицы"""
        data = []
        for row in table.find_elements(By.TAG_NAME, 'tr'):
            row_data = []
            if not row.find_element('xpath', f"//*[contains(text(), '{category_filter}')]"):
                continue
            for cell in row.find_elements(By.TAG_NAME, 'td'):
                row_data.append(cell.text)
            if row_data:
                data.append(row_data)
        return data
    
    def get_table_head(self, table):
        """Возвращает загаловки таблицы"""
        return [ t.text for t in table.find_elements(By.TAG_NAME, 'th')]


def get_init_data():
    """Возвращает данные с первой страницы"""
    with webdriver.Chrome(executable_path=driver_path, options=driver_options) as driver:
        page_processer = SeleniumPageProcessor(driver)
        page_processer.get_page()
        page_processer.wait_for_element()
        
        data_processor = SeleniumDataProcessor(page_processer.get_source())
        table = data_processor.get_table()
        res_data = data_processor.get_table_data(table)
        res_head = data_processor.get_table_head(table)

        pages = data_processor.get_pages()

    return pages, res_head, res_data