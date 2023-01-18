from selenium import webdriver
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import time

from .selenium_service import SeleniumDataProcessor, SeleniumPageProcessor
from constants import BASE_URL, driver_options, driver_path


def thread_process(driver, page_list, num):
    """Функция, выполняющаяся в потоке"""
    print('INFO:   ',f'Поток [{num}] получил {len(page_list)} страниц')
    res_data = []
    with driver as driver:
        page_processor = SeleniumPageProcessor(driver)
        for page in page_list:
            page_processor.get_page(page)
            try:
                page_processor.wait_for_element()
            except:
                print("WARNING:    ",f"Поток [{num}]. Загрузка страницы заняла слишком много времени! ({page})")
                continue
            data_processor = SeleniumDataProcessor(page_processor.get_source())
            table = data_processor.get_table()
            res_data += data_processor.get_table_data(table)
            print('INFO:   ',f'Поток [{num}]. Страница ({page}) выполнена')

    print('INFO:   ',f'Поток [{num}] закончил!')
    return res_data

def run(threads: int, pages: int):
    """Запускает потоки"""
    drivers = [webdriver.Chrome(executable_path=driver_path, options=driver_options) for _ in range(threads)]
    target_urls = [BASE_URL + f'&page={i}' for i in range(2, pages+1)]
    page_list = np.array_split(target_urls, threads)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        bucket = executor.map(thread_process, drivers, page_list, range(1,threads+1))

    res_data = [item for block in bucket for item in block]
    return res_data